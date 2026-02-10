# MEMORY.md — Trade Agent 長期記憶

## 項目狀態
- tty_dexter: TypeScript + Bun，投資個人助理 Telegram bot
- qlib_market_scanner: Python，Qlib 美股量化掃描器
- dexter_trading_agents: Python，多智能體交易分析框架

## 每日早報 Cron Job
- Job ID: `1bb10ad3-037b-4658-9a42-fbb555ea0806`
- 每日 08:00 HKT → Telegram 群組 `-5036824968`
- Agent: trade-agent, isolated session, timeout 600s
- 內容：1) 大市宏觀 + 3) Paper Digest（詳細版）
- 注意：與 daily learning（內部記錄）功能不重疊

## 已知資料源限制
- export.arxiv.org API: 不穩定（timeout/503/429），不應作為每日準時產出依賴
- arxiv RSS (`arxiv.org/rss/<cat>`): 穩定可用，推薦作為論文 fallback
- Finnhub `/calendar/economic`: 403（權限不足）
- Finnhub `/quote`, `/news`, `/calendar/earnings`: 正常
- agentic-paper-digest skill: kept=0 問題，需調整 topic/filter

## 學習來源
- Moltbook Agent: `/Users/admin/.openclaw/workspace/moltbook-agent/memory/`

---

*初始化日期: 2026-02-10*
