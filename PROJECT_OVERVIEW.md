# PROJECT_OVERVIEW.md — Trade Agent 管理項目總覽

---

## 1. tty_dexter — 投資個人助理 AI Agent

**路徑**: `./tty_dexter/`
**語言/Runtime**: TypeScript + Bun
**主要功能**: 串流式財務報告分析 agent，整合 Telegram bot
**關鍵依賴**: grammy（Telegram bot）、yahoo-finance2（市場數據）、dropbox（檔案存取）、openai（LLM）
**啟動方式**:
```bash
cd tty_dexter && bun run start
```
**設定檔**: `.env`（API keys 等）
**文件**: `docs/` 目錄下有 AGENT_DESIGN.md、DATA_DESIGN.md、SYSTEM_ARCHITECTURE.md 等

---

## 2. qlib_market_scanner — 日量化分析

**路徑**: `./qlib_market_scanner/`
**語言/Runtime**: Python + uv
**主要功能**: 基於微軟 Qlib 的美股市場掃描器，自動從 S&P 500 篩選投資標的
**核心流程**:
1. Universe Selection（S&P 500 → 前 200 檔）
2. Data Fetch（Alpha Vantage API → DuckDB 快取）
3. Model Training（Alpha158 特徵 + LightGBM 分類）
4. Backtest（TopkDropout 策略 + 動態交易成本）
5. Signal Output（每日 Top-K 候選 CSV/JSON）
**啟動方式**:
```bash
cd qlib_market_scanner && uv run ./run.sh
```
**設定檔**: `.env`、`pyproject.toml`
**輸出**: `data/`（數據）、`outputs/`（報告）、`mlruns/`（MLflow 實驗追蹤）

---

## 3. dexter_trading_agents — 股票分析報告生成 AI Agent Team

**路徑**: `./dexter_trading_agents/`
**語言/Runtime**: Python + uv
**主要功能**: 基於 TauricResearch/TradingAgents 的多智能體交易框架
**核心架構**: 多個專門 LLM agent 協作：
- 基本面分析師
- 情緒分析專家
- 技術分析師
- 交易員
- 風險管理團隊
**啟動方式**:
```bash
cd dexter_trading_agents && uv run python main.py
```
**設定檔**: `.env`、`pyproject.toml`
**輸出**: `eval_results/`（評估結果）、`state/`（狀態）

---

## 跨項目關係

- `qlib_market_scanner` 產出嘅每日候選名單（signals.csv）可以上傳 Dropbox，俾 `dexter_trading_agents` 消費
- `tty_dexter` 作為前端介面，可以整合以上兩個系統嘅分析結果
- 三者形成一個完整嘅「數據 → 分析 → 報告 → 用戶介面」pipeline

---

## 學習資源（跨 Agent）

- **Moltbook Agent 知識庫**: `/Users/admin/.openclaw/workspace/moltbook-agent/memory/`
  - 包含量化分析相關的持續學習紀錄
  - 每日有新的學習筆記

---

*最後更新: 2026-02-10*
