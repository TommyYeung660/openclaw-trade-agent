# 每日早報（詳細版）— 2026-02-15 08:00 HKT

## (1) 美股大市 + 主要宏觀事件

### 市場指數
- **SPY**: [資料暫時不可用 - Finnhub API key 未配置]
- **QQQ**: [資料暫時不可用]
- **DIA**: [資料暫時不可用]
- **IWM**: [資料暫時不可用]

### 宏觀 Proxy
- **利率相關 (SHY/IEF/TLT)**: [資料暫時不可用]
- **美元指數 (UUP)**: [資料暫時不可用]
- **原油 (USO/BNO)**: [資料暫時不可用]
- **黃金 (GLD)**: [資料暫時不可用]

### 行業輪動
- XLK (科技): [資料暫時不可用]
- XLF (金融): [資料暫時不可用]
- XLE (能源): [資料暫時不可用]
- XLI (工業): [資料暫時不可用]
- XLY (消費非必需): [資料暫時不可用]
- XLP (消費必需): [資料暫時不可用]
- XLV (醫療): [資料暫時不可用]
- XLU (公用事業): [資料暫時不可用]
- XLB (原材料): [資料暫時不可用]
- XLRE (房地產): [資料暫時不可用]
- XLC (通信服務): [資料暫時不可用]

### 重要宏觀事件/政策/風險
[資料暫時不可用 - Finnhub API key 未配置]

### 財報日曆（未來 7 天）
[資料暫時不可用]

---

## (3) Paper Digest（量化交易/風控/因子/LLM in finance）

### 數據來源狀態
- **arxiv RSS (q-fin.TR, q-fin.RM, q-fin.ST, q-fin.PM, cs.LG, stat.ML)**:
  - 嘗試調取，但週末無新論文發布（arXiv RSS 週末 skipDays: Saturday/Sunday）
  - 透過 web_search 查詢需要 Brave API key，當前未配置
- **agentic-paper-digest skill**:
  - 嘗試執行但腳本路徑不存在（需要 bootstrap）
  - 當前未安裝

### 論文摘要
[本日暫無新論文可摘要 - 原因：週末無新論文 + 資料源配置不完整]

### 研究想法（暫無）
因無新論文數據，今日無法生成研究想法建議。

---

### 資料源配置建議
為確保每日早報能正常運作，建議完成以下配置：

1. **Finnhub API Key**:
   - 註冊 Finnhub (https://finnhub.io/)
   - 將 API key 配置到環境變數或配置檔案
   - 所需 endpoint: `/quote`, `/news`, `/calendar/earnings`

2. **Brave Search API Key**:
   - 執行 `openclaw configure --section web` 進行配置
   - 或設定環境變數 `BRAVE_API_KEY`

3. **Agentic Paper Digest**:
   - 執行 bootstrap 安裝: `bash "$HOME/.openclaw/skills/agentic-paper-digest/scripts/bootstrap.sh"`
   - 確保 LLM API key 已配置 (OPENAI_API_KEY 或 LITELLM_API_KEY)

---
*生成時間: 2026-02-15 08:02 HKT*
