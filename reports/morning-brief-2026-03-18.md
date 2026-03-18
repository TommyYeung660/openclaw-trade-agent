# 每日早報（詳細版）— 2026-03-18 08:00 HKT

---

## (1) 美股大市 + 主要宏觀事件

### 指數表現
| 代號 | 現價 | 漲跌 | 漲跌幅(%) | 最高 | 最低 | 開盤 | 昨收 |
|------|------|------|-----------|------|------|------|------|
| SPY | 670.79 | +1.76 | +0.263% | 674.44 | 669.70 | 672.39 | 669.03 |
| QQQ | 603.31 | +2.93 | +0.488% | 605.90 | 601.87 | 603.14 | 600.38 |
| DIA | 470.90 | +0.60 | +0.128% | 475.13 | 470.62 | 473.38 | 470.30 |
| IWM | 250.05 | +1.13 | +0.454% | 251.71 | 248.96 | 249.87 | 248.92 |

### 宏觀 Proxy（利率/美元/大宗商品）
| 代號 | 描述 | 現價 | 漲跌 | 漲跌幅(%) |
|------|------|------|:----:|:---------:|
| SHY | 1-3 年美債 | 82.66 | +0.01 | +0.012% |
| IEF | 7-10 年美債 | 96.19 | +0.17 | +0.177% |
| TLT | 20+ 年美債 | 87.45 | +0.24 | +0.275% |
| UUP | 美元指數 | 27.68 | -0.05 | -0.180% |
| USO | WTI 原油 | 118.84 | +3.81 | +3.312% |
| BNO | 布倫特原油 | 49.40 | +1.74 | +3.651% |
| GLD | 黃金 | 459.27 | -1.16 | -0.252% |

### 行業輪動表現
| 代號 | 行業 | 現價 | 漲跌 | 漲跌幅(%) |
|------|------|------|:----:|:---------:|
| XLE | 能源 | 58.51 | +0.61 | +1.054% |
| XLY | 消費非必需 | 113.18 | +0.98 | +0.873% |
| XLK | 科技 | 139.54 | +0.76 | +0.548% |
| XLF | 金融 | 49.56 | +0.26 | +0.527% |
| XLRE | 地產 | 42.72 | +0.14 | +0.329% |
| XLI | 工業 | 166.50 | +0.44 | +0.265% |
| XLB | 原材料 | 49.52 | +0.12 | +0.243% |
| XLC | 通訊服務 | 115.37 | +0.04 | +0.035% |
| XLU | 公用事業 | 47.13 | -0.13 | -0.275% |
| XLP | 消費必需 | 84.70 | -0.28 | -0.330% |
| XLV | 醫療 | 149.64 | -1.37 | -0.907% |

### 重要市場新聞

- **Ali Larijani, Iran's ultimate backroom powerbroker, killed in Israeli airstrike - Reuters** (Reuters, 2026-03-18 05:20)
- **US carrier Ford, deployed in war with Iran, to go to port temporarily after fire - Reuters** (Reuters, 2026-03-18 05:06)
- **Nvidia’s big GTC showcase barely budged the stock. Is that a problem?** (CNBC, 2026-03-18 05:05)
- **Iran confirms security chief Ali Larijani killed, Iranian media reports - Reuters** (Reuters, 2026-03-18 04:58)
- **Russia is sharing satellite imagery and drone technology with Iran, WSJ reports - Reuters** (Reuters, 2026-03-18 03:59)
- **Here are the ways 3 of our industrial stocks can weather Iran-fueled volatility** (CNBC, 2026-03-18 03:51)
- **Arizona charges Kalshi with criminal misdemeanors, alleging it's an illegal gambling operation** (CNBC, 2026-03-18 03:09)
- **The Fed issues its latest interest rate decision Wednesday. Here's what to expect** (CNBC, 2026-03-18 02:58)

### 未來 7 天重點財報

**2026-03-25**: FAT, JBS, CBDY, CULL, ALMS, FUL, VINC, WDRP, EQ, CNTX, COEP, PIII, VSTD, KULR, BPTH, STLY, PGEN, RECT, PMVCD, NSYS, IZEA, WHLM, KRMN, MLKN, CTSO, LFT, JFIN, PGAC, TVGN, BYSD, NDLS, CLSD, SRXH, KC, NNDM, SKYH, DLPN, BKYI, EMYB, GPFT, NRSN, FTLF, BZUN, WYY, CRT, WGO, ORMP, CWD, VERF, BNAI

---

## (3) Paper Digest（量化交易/風控/因子/LLM in finance）

### 今日精選論文摘要

#### 1. E-TRENDS: Enhanced LSTM Trend Forecasting for Equities
**分類**: q-fin.TR (交易策略) | [arXiv](https://arxiv.org/abs/2603.14453)

**研究問題**: 提出基於 LSTM 的框架預測標普 500 指數前 30 名成分股的隔日趨勢差異 (Δt)，在 2005-2025 跨市場週期驗證。主要貢獻：(i) 差分法偏差-方差降低的形式化證明，(ii) 對 OLS、Ridge、Lasso 的詳盡基準比較，(iii) 投資組合模擬證實相較其他模型有經濟收益。

**方法**: LSTM 趨勢差異預測，使用差分處理非平穩性

**數據/實驗設定**: S&P 500 top 30 equities, 2005-2025

**主要結論**: 相比 OLS/Ridge/Lasso/LightGBM，LSTM 在 PNL 上有顯著優勢

**可落地啟示**: 趨勢跟蹤策略的改進方向，差分處理可處理非平穩市場

---

#### 2. Robust Optimal Strategies for Early Liquidation in Financial Systems
**分類**: q-fin.RM (風險管理) | [arXiv](https://arxiv.org/abs/2603.14546)

**研究問題**: 研究金融系統中的資產清算問題。在金融危機期間，資產清算不可避免，但大量流動性差的資產同時以壓抑價格出售會導致巨大損失（價格衝擊）。考慮兩期清算模型，允許結算前的早期清算以緩解結算時的價格衝擊，發展最壞情況方法解決早期清算規模的最優決策問題。

**方法**: 兩期清算模型，最壞情況優化

**數據/實驗設定**: 理論模型，含永久價格衝擊和銀行間暴露場景

**主要結論**: 推導出在永久價格衝擊情況下的半封閉解，以及在銀行間暴露情況下的封閉解

**可落地啟示**: 為流動性風險管理提供健壯的清算策略框架，特別適用於壓力場景

---

#### 3. A stochastic SIR model for cyber contagion: application to granular growth of firms and to insurance portfolio
**分類**: q-fin.RM (風險管理) | [arXiv](https://arxiv.org/abs/2603.15369)

**研究問題**: 評估傳染性網絡安全事件在有限時間範圍內對公司財務健康和網絡保險投資組合的影響。基於經濟學和網絡安全的關鍵經驗發現：公司規模和增長率分布非高斯且具有厚尾；傳染動態強烈依賴公司規模和環境條件。提出隨機多組 SIR 模型耦合公司增長的顆粒模型。

**方法**: 隨機多組 SIR 模型 + 顆粒公司增長模型

**數據/實驗設定**: LockBit 勒索軟體攻擊（2024年5-7月），法國巴黎地區 2,929 家公司

**主要結論**: 模型預測在 100 天網絡事件中，50% 概率下保險公司需賠償相當於多達 2 天收入的損失

**可落地啟示**: 為網絡保險定價和公司級風險管理提供量化工具，特別是網絡傳染效應建模

---

#### 4. What's the Price of Monotonicity? A Multi-Dataset Benchmark of Monotone-Constrained Gradient Boosting for Credit PD
**分類**: q-fin.RM (風險管理) | [arXiv](https://arxiv.org/abs/2512.17945)

**研究問題**: 金融機構在部署信用風險機器學習模型時面臨預測準確性和可解釋性的權衡。單調性約束使模型行為與領域知識對齊，但其性能成本尚未量化。本文在五個公開數據集和三個庫上基準測試單調約束與無約束梯度提升模型。

**方法**: 單調約束梯度提升 vs 無約束，跨數據集基準

**數據/實驗設定**: 5 個公開信用風險數據集，3 個機器學習庫

**主要結論**: 單調性代價在 AUC 上從接近 0 到約 2.9%；大數據集約束幾乎無成本（<0.2%），小數據集約束覆蓋廣時成本較高（2-3%）

**可落地啟示**: 大規模信用投資組合可使用單調性約束提升可解釋性而無顯著準確性損失

---

#### 5. Beyond Prompting: An Autonomous Framework for Systematic Factor Investing via Agentic AI
**分類**: q-fin.PM (投資組合管理) | [arXiv](https://arxiv.org/abs/2603.14288)

**研究問題**: 開發通過 Agentic AI 進行系統性因子投資的自主框架。不是依賴順序手動提示，而是將模型操作為自導向引擎，內在地制定可解釋的交易信號。閉環系統通過樣外驗證和經濟理性要求嚴格實證紀律，以緩解數據窺探偏差。

**方法**: Agentic AI 因子投資框架，自導向信號生成 + 樣外驗證

**數據/實驗設定**: 美國股市

**主要結論**: 長短投資組合基於信號的簡單線性組合，年化 Sharpe ratio 3.11，收益率 59.53%

**可落地啟示**: 自演化 AI 為系統性投資提供可擴展、可解釋的範式，減少人工干預

---

#### 6. When Alpha Breaks: Two-Level Uncertainty for Safe Deployment of Cross-Sectional Stock Rankers
**分類**: q-fin.PM (投資組合管理) | [arXiv](https://arxiv.org/abs/2603.13252)

**研究問題**: 橫截面排序模型通常部署為點預測足夠：模型輸出分數，投資組合跟隨誘導排序。在非平穩性下，排序器在制度轉換時可能失敗。2024 holdout 與 AI 主題行情和行業輪動重疊，在長時間範圍上打破信號並削弱 20d 信號。

**方法**: DEUP for ranking，策略級制度信賴門檻 G(t) + 位置級認知尾部風險上限

**數據/實驗設定**: AI Stock Forecaster, LightGBM ranker, 20-day horizon

**主要結論**: G(t) AUROC 約 0.72（FINAL 中 0.75）；操作策略（G(t)>=0.2 時交易，波動率 sizing，認知尾部上限）改進風險調整績效

**可落地啟示**: 非平穩市場中部署 ranking 模型的兩級決策框架：是否交易 + 如何控制風險

---

#### 7. Continuous-time Risk-sensitive Reinforcement Learning via Quadratic Variation Penalty
**分類**: q-fin.PM (投資組合管理) | [arXiv](https://arxiv.org/abs/2404.12598)

**研究問題**: 研究連續時間風險敏感強化學習（RL），在正則化探索擴散過程公式下使用指數形式目標。風險敏感目標來自代理的風險態度或分佈魯棒方法。基於 Jia 和 Zhou（2023）的鞅視角，風險敏感 RL 等價於確保值函數和 q 函數過程的鞅性質，增加懲罰項：值過程的二次變異。

**方法**: 二次變異懲罰的連續時間風險敏感 RL

**數據/實驗設定**: Merton 投資問題，線性二次控制問題

**主要結論**: 證明 Merton 投資問題的收斂性，量化溫度參數對學習行為的影響；風險敏感 RL 改進有限樣本性能

**可落地啟示**: 為風險敏感連續時間決策問題提供 RL 框架，特別是金融應用中的尾部風險控制

---

#### 8. Betting Around the Clock: Time Change and Long Term Model Risk
**分類**: q-fin.ST (統計交易) | [arXiv](https://arxiv.org/abs/2603.13632)

**研究問題**: 研究在收益動力由時間變換過程表示的設置中 Kelly rule 的性能。發現在一般半鞅設置中，Kelly rule 不最大化平均增長率，除非對數收盤是常態分佈。Kelly rule 提議的投資頭寸過大，投資者可通過較不激進投資實現更高平均增長率。

**方法**: 時間變換半鞅模型，Kelly rule 分析

**數據/實驗設定**: 理論分析，含隨機時鐘變異估計

**主要結論**: 在非常態收盤時 Kelly rule 過度投資；Thorp (1969) 破產閾值更接近，但 Kelly rule 仍處於無破產區域

**可落地啟示**: 非高斯市場或隨機交易時間設置中 Kelly rule 的長期模型風險，需考慮更保守的仓位

---

### 研究想法總結

基於今日論文摘要，以下潛在研究方向值得深入探討：

1. **制度轉換感知的因子投資框架** - 結合 'When Alpha Breaks' 的兩級不確定性和 'Agentic AI for Factor Investing' 的自主框架，構建在制度轉換時自動調整或暫停信號的因子投資系統。

2. **LSTM 趨勢差異擴展到因子模型** - 'E-TRENDS' 證明差分處理 + LSTM 可改進趨勢預測，可擴展到多因子動量/反轉信號構建，特別是處理因子輪動的非平穩性。

3. **網絡傳染風險的投資組合層面建模** - 'Cyber SIR model' 提供了傳染動態的量化框架，可應用於信用風險傳染、流動性擠壓等金融系統性風險場景，為壓力測試提供新工具。

4. **單調性約束在風險模型中的應用** - 'Price of Monotonicity' 證明在大數據集上約束幾乎無成本，可在信用 PD、VaR 模型、操縦檢測等領域探索約束約束與可解釋性的權衡。

5. **風險敏感 RL 在投資組合再平衡中的應用** - 'Risk-sensitive RL via Quadratic Variation Penalty' 的二次變異懲罰機制可直接應用於投資組合再平衡，在最大化收益同時控制路徑波動（尾部風險）。

---

*生成時間: 2026-03-18 08:09:20 HKT*