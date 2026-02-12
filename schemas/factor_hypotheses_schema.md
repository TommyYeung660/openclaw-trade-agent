# Factor Hypotheses YAML Schema

> 用於 trade-agent daily learning 生成因子假說，上傳到 Dropbox 供 qlib_rd_agent 消費。

## 檔案路徑

- 每日輸出：`outputs/factor_hypotheses/YYYY-MM-DD.yaml`
- 聚合輸出：`outputs/factor_hypotheses/aggregated_hypotheses.yaml`（由同步腳本生成）
- Dropbox 目標：`/qlib_shared/rdagent_inputs/hypotheses/aggregated_hypotheses.yaml`

## YAML 格式

```yaml
version: "1.0"
generated_at: "2026-02-12T09:00:00+08:00"   # ISO 8601，Asia/Hong_Kong
source_agent: "trade-agent"

hypotheses:
  - id: "hyp-YYYYMMDD-NNN"                   # 唯一 ID，日期 + 序號
    source_type: "moltbook"                   # moltbook | arxiv | web_search | paper_digest
    source_ref: "moltbook post UUID / arxiv ID / URL"
    name: "Volume_Weighted_Momentum"          # 英文，snake_case，簡潔
    hypothesis: "成交量加權動量在低波動期表現更好"  # 一句話描述假說
    expression: "($close - Ref($close, 20)) / Ref($close, 20) * ($volume / Mean($volume, 20))"
    rationale: "來源與推理過程"                   # 為什麼這個因子可能有效
    category: "momentum"                      # 見下方分類
    priority: "medium"                        # high | medium | low
    tags: ["momentum", "volume"]              # 自由標籤
    confidence: 0.6                           # 0.0-1.0，agent 自評信心
    limitations: "僅在美股測試，未考慮交易成本"     # 已知限制
    market: "us_equity"                       # us_equity | cn_equity | crypto | multi
```

## 分類（category）

| category | 說明 |
|----------|------|
| momentum | 動量類因子 |
| mean_reversion | 均值回歸 |
| volatility | 波動率相關 |
| volume | 成交量相關 |
| fundamental | 基本面 |
| technical | 技術指標組合 |
| sentiment | 情緒/另類數據 |
| ml_signal | 機器學習衍生信號 |
| cross_sectional | 截面因子 |
| macro | 宏觀因子 |

## Expression 語法

使用 Qlib Expression 語法（兼容 RD-Agent）：
- 價格欄位：`$open`, `$high`, `$low`, `$close`, `$volume`, `$vwap`
- 時間偏移：`Ref($close, N)` — N 日前的值
- 統計函數：`Mean($close, N)`, `Std($close, N)`, `Max($high, N)`, `Min($low, N)`
- 運算：`+`, `-`, `*`, `/`, `>`, `<`
- 滾動：`Rolling($close, N, func)`
- 排名：`Rank($close)`, `CSRank($close)`

如果無法寫出精確 expression，可留空並在 hypothesis 欄位詳細描述邏輯，讓 RD-Agent 自行實現。

## 篩選標準

trade-agent 生成假說時必須滿足：
1. **有明確的數學邏輯**或可轉化為 Qlib expression 的概念
2. **有數據支撐**（來自論文、回測結果、社群實證）
3. **與現有 discovered_factors 不重複**（檢查 name 和 expression）
4. 如果今日沒有符合條件的假說，**不生成檔案**
