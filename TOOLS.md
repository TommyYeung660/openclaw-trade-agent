# TOOLS.md — Trade Agent

## Python 項目管理規則（全局）
- **所有 Python 項目一律用 uv 管理同執行**
- 依賴安裝：`uv sync`
- 執行腳本：`uv run python <script>`
- 禁止直接用 `python` 或 `pip`

## 項目執行指令

### tty_dexter（TypeScript/Bun）
```bash
cd /Users/admin/.openclaw/workspace/trade-agent/tty_dexter && bun run start
```

### qlib_market_scanner（Python/uv）
```bash
cd /Users/admin/.openclaw/workspace/trade-agent/qlib_market_scanner && uv run ./run.sh
```
或直接：
```bash
cd /Users/admin/.openclaw/workspace/trade-agent/qlib_market_scanner && uv run python -m src.main
```

### dexter_trading_agents（Python/uv）
```bash
cd /Users/admin/.openclaw/workspace/trade-agent/dexter_trading_agents && uv run python main.py
```

## 跨 Agent 資源路徑
- Moltbook Agent memory: `/Users/admin/.openclaw/workspace/moltbook-agent/memory/`
