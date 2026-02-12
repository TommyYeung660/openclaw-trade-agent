# qlib_rd_agent 整合設計文檔：Factor Hypothesis Pipeline（Step 5）

> 目標：讓 qlib_rd_agent 在 sync 階段從 Dropbox 拉取 trade-agent 生成的因子假說，注入 RD-Agent 作為 seed prompts，引導因子挖掘方向。

---

## 1. 數據流概覽

```
trade-agent daily learning (09:00 HKT)
    → outputs/factor_hypotheses/YYYY-MM-DD.yaml
    
trade-agent hypothesis sync (09:30 HKT)
    → Dropbox: /qlib_shared/rdagent_inputs/hypotheses/aggregated_hypotheses.yaml
    
qlib_rd_agent sync (本文檔要改的部分)
    ← Dropbox: /qlib_shared/rdagent_inputs/hypotheses/aggregated_hypotheses.yaml
    → data/hypotheses/aggregated_hypotheses.yaml (local)
    
qlib_rd_agent run
    ← data/hypotheses/ → 注入 RD-Agent seed prompts
```

---

## 2. Config 改動

### `src/config.py` — DropboxConfig 新增欄位

```python
@dataclass
class DropboxConfig:
    # ... 現有欄位 ...
    remote_hypotheses_folder: str = "/qlib_shared/rdagent_inputs/hypotheses"
    local_hypotheses_dir: str = "data/hypotheses"  # 下載假說的本地路徑
```

環境變數映射（在 `load_config()` 中加入）：

```python
# Build DropboxConfig — 新增行
remote_hypotheses_folder=os.getenv(
    "DROPBOX_REMOTE_HYPOTHESES_FOLDER", "/qlib_shared/rdagent_inputs/hypotheses"
),
local_hypotheses_dir=os.getenv("DROPBOX_LOCAL_HYPOTHESES_DIR", "data/hypotheses"),
```

---

## 3. Bridge 改動

### `src/bridge/dropbox_sync.py` — 新增 `download_hypotheses()`

```python
def download_hypotheses(config: AppConfig) -> Optional[Path]:
    """Download factor hypotheses from Dropbox.

    Downloads aggregated_hypotheses.yaml from the remote hypotheses folder.
    Returns the local path if successful, None if no hypotheses file exists.

    Args:
        config: Application configuration.

    Returns:
        Path to local aggregated_hypotheses.yaml, or None if not found.
    """
    client = _create_dropbox_client(config)

    local_dir = Path(config.dropbox.local_hypotheses_dir)
    local_dir.mkdir(parents=True, exist_ok=True)

    remote_path = f"{config.dropbox.remote_hypotheses_folder}/aggregated_hypotheses.yaml"
    local_path = local_dir / "aggregated_hypotheses.yaml"

    logger.info("Checking for factor hypotheses at Dropbox: {}", remote_path)

    try:
        metadata, response = client.dbx.files_download(remote_path)
        content = response.content
        local_path.write_bytes(content)
        logger.info(
            "Downloaded hypotheses ({} bytes, modified: {})",
            len(content),
            metadata.server_modified,
        )
        return local_path
    except dropbox.exceptions.ApiError as e:
        if e.error.is_path() and e.error.get_path().is_not_found():
            logger.info("No hypotheses file found on Dropbox (normal for first run)")
            return None
        raise
```

注意：需要在文件頂部加入 `import dropbox`（如果還沒有的話）。

### 在 `download_shared_data()` 末尾調用

在 `download_shared_data()` 函式的 `return local_dir` 之前加入：

```python
    # ------------------------------------------------------------------
    # Download factor hypotheses (optional — from trade-agent)
    # ------------------------------------------------------------------
    try:
        hypotheses_path = download_hypotheses(config)
        if hypotheses_path:
            logger.info("Factor hypotheses available at: {}", hypotheses_path)
    except Exception as e:
        logger.warning("Failed to download hypotheses (non-fatal): {}", e)
```

這樣 `sync` 命令自動包含假說下載，不需要改 CLI。

---

## 4. Runner 改動

### `src/runner/qlib_runner.py` — 新增 `load_hypotheses()` 和 `build_hypothesis_prompt()`

```python
def load_hypotheses(config: AppConfig) -> List[Dict[str, Any]]:
    """Load factor hypotheses from local cache.

    Reads the aggregated_hypotheses.yaml downloaded by sync step.

    Args:
        config: Application configuration.

    Returns:
        List of hypothesis dicts, empty list if file doesn't exist.
    """
    hypotheses_path = Path(config.dropbox.local_hypotheses_dir) / "aggregated_hypotheses.yaml"
    
    if not hypotheses_path.exists():
        logger.info("No hypotheses file found at {}", hypotheses_path)
        return []

    try:
        data = yaml.safe_load(hypotheses_path.read_text(encoding="utf-8"))
        hypotheses = data.get("hypotheses", [])
        logger.info("Loaded {} factor hypotheses", len(hypotheses))
        return hypotheses
    except Exception as e:
        logger.warning("Failed to load hypotheses: {}", e)
        return []


def build_hypothesis_prompt(hypotheses: List[Dict[str, Any]], max_items: int = 10) -> str:
    """Build a seed prompt string from hypotheses for RD-Agent injection.

    Formats hypotheses into a structured prompt that RD-Agent can use
    as initial factor ideas to explore.

    Args:
        hypotheses: List of hypothesis dicts from YAML.
        max_items: Maximum number of hypotheses to include (avoid prompt bloat).

    Returns:
        Formatted prompt string, empty string if no hypotheses.
    """
    if not hypotheses:
        return ""

    # Sort by priority (high > medium > low) and confidence (descending)
    priority_order = {"high": 0, "medium": 1, "low": 2}
    sorted_h = sorted(
        hypotheses,
        key=lambda h: (
            priority_order.get(h.get("priority", "low"), 3),
            -h.get("confidence", 0),
        ),
    )[:max_items]

    lines = [
        "=== Factor Hypotheses from Trade Agent (seed ideas) ===",
        "The following factor hypotheses were generated from market research,",
        "academic papers, and community insights. Use them as starting points",
        "for factor mining. You may modify, combine, or discard them.",
        "",
    ]

    for i, h in enumerate(sorted_h, 1):
        lines.append(f"--- Hypothesis {i}: {h.get('name', 'unnamed')} ---")
        lines.append(f"Category: {h.get('category', 'unknown')}")
        lines.append(f"Hypothesis: {h.get('hypothesis', 'N/A')}")
        
        expr = h.get("expression", "")
        if expr:
            lines.append(f"Suggested Expression: {expr}")
        
        lines.append(f"Rationale: {h.get('rationale', 'N/A')}")
        lines.append(f"Confidence: {h.get('confidence', 'N/A')}")
        
        limitations = h.get("limitations", "")
        if limitations:
            lines.append(f"Limitations: {limitations}")
        
        lines.append("")

    lines.append("=== End of Hypotheses ===")
    return "\n".join(lines)
```

### 在 `run_rdagent()` 中注入假說

在 `run_rdagent()` 裡，啟動 RD-Agent subprocess 之前，加入假說注入邏輯。

RD-Agent 支持通過環境變數 `FACTOR_HYPOTHESIS_PROMPT` 或 workspace 檔案注入 seed prompts。最穩妥的方式是**寫入 workspace 的 prompt 檔案**讓 RD-Agent 讀取：

```python
def run_rdagent(config: AppConfig) -> Path:
    # ... 現有代碼 ...

    # ── Inject factor hypotheses as seed prompts ──
    hypotheses = load_hypotheses(config)
    if hypotheses:
        hypothesis_prompt = build_hypothesis_prompt(hypotheses)
        
        # 寫入 workspace，RD-Agent 可在 evolve 過程讀取
        workspace_dir = _resolve_path(config.rdagent.workspace_dir)
        workspace_dir.mkdir(parents=True, exist_ok=True)
        
        seed_file = workspace_dir / "seed_hypotheses.txt"
        seed_file.write_text(hypothesis_prompt, encoding="utf-8")
        logger.info(
            "Injected {} seed hypotheses into workspace: {}",
            len(hypotheses),
            seed_file,
        )
        
        # 同時通過環境變數傳遞（RD-Agent 部分版本支持）
        env["FACTOR_SEED_PROMPT"] = hypothesis_prompt[:4000]  # 截斷防止過長
    
    # ... 繼續現有的 subprocess 啟動邏輯 ...
```

**注意：** RD-Agent 的具體注入機制取決於你使用的版本。有兩種方式：

1. **環境變數**（上面的 `FACTOR_SEED_PROMPT`）：如果 RD-Agent 支持
2. **Workspace 檔案**（`seed_hypotheses.txt`）：更通用，RD-Agent 的 `QlibFactorScenario` 可以配置讀取 workspace 中的額外 prompt 檔案

建議先用方式 2（寫檔案），再根據 RD-Agent 版本決定是否加環境變數。

---

## 5. CLI 改動（可選）

如果想單獨觸發假說下載，可以在 `src/main.py` 加一個子命令：

```python
@cli.command()
@click.pass_context
def fetch_hypotheses(ctx: click.Context) -> None:
    """Download factor hypotheses from Dropbox."""
    from src.bridge.dropbox_sync import download_hypotheses

    config = ctx.obj["config"]
    path = download_hypotheses(config)
    if path:
        logger.info("Hypotheses saved to: {}", path)
    else:
        logger.info("No hypotheses available")
```

但這不是必須的，因為 `sync` 命令已經會自動下載。

---

## 6. 檔案結構變化

```
qlib_rd_agent/
├── data/
│   ├── hypotheses/                    # 新增
│   │   └── aggregated_hypotheses.yaml # sync 下載的假說
│   ├── qlib/                          # 現有
│   └── shared_import/                 # 現有
├── src/
│   ├── bridge/
│   │   └── dropbox_sync.py            # 改動：新增 download_hypotheses()
│   ├── config.py                      # 改動：DropboxConfig 新增 2 欄位
│   ├── runner/
│   │   └── qlib_runner.py             # 改動：新增 load_hypotheses() + build_hypothesis_prompt()
│   └── main.py                        # 可選改動：新增 fetch_hypotheses 子命令
└── workspace/
    └── seed_hypotheses.txt            # run 時自動生成
```

---

## 7. YAML 格式參考

trade-agent 上傳的 `aggregated_hypotheses.yaml` 格式：

```yaml
version: "1.0"
generated_at: "2026-02-12T09:30:00+08:00"
source_agent: "trade-agent"
total_count: 3

hypotheses:
  - id: "hyp-20260212-001"
    source_type: "moltbook"
    source_ref: "0df56245-af4c-4445-98f8-64dd24acf5bc"
    name: "Volume_Weighted_Momentum"
    hypothesis: "成交量加權動量在低波動期表現更好"
    expression: "($close - Ref($close, 20)) / Ref($close, 20) * ($volume / Mean($volume, 20))"
    rationale: "ClawQuant 系統實測 Sharpe 0.537，優化後勝率提升"
    category: "momentum"
    priority: "medium"
    tags: ["momentum", "volume"]
    confidence: 0.6
    limitations: "僅在 A 股 2014-2024 測試"
    market: "us_equity"

  - id: "hyp-20260212-002"
    source_type: "arxiv"
    source_ref: "arxiv:2026.xxxxx"
    name: "Volatility_Adjusted_RSI"
    hypothesis: "用波動率調整 RSI 閾值，低波動期放寬、高波動期收緊"
    expression: ""
    rationale: "論文 xxx 提出，在 S&P500 回測 IC 0.05"
    category: "technical"
    priority: "high"
    tags: ["rsi", "volatility", "adaptive"]
    confidence: 0.7
    limitations: "需要更多 out-of-sample 驗證"
    market: "us_equity"
```

---

## 8. 測試驗證步驟

1. 手動建一個測試假說檔案上傳到 Dropbox：
   ```bash
   python -m src.main sync
   ```
   確認 `data/hypotheses/aggregated_hypotheses.yaml` 被下載

2. 跑 `full` pipeline：
   ```bash
   python -m src.main full --max-iterations 1
   ```
   確認 `workspace/seed_hypotheses.txt` 被生成，內容正確

3. 檢查 RD-Agent 日誌，確認是否讀取了 seed prompts

---

## 9. 注意事項

- **不影響現有流程**：如果 Dropbox 上沒有假說檔案，所有現有邏輯完全不受影響（`download_hypotheses` 返回 None，不注入任何 seed）
- **容錯**：假說下載失敗只 warning，不中斷 sync/run pipeline
- **大小控制**：`build_hypothesis_prompt` 預設最多取 10 條，避免 prompt 過長
- **不改動 RD-Agent 核心**：只在外層注入 prompt，不修改 `rdagent` 包本身
