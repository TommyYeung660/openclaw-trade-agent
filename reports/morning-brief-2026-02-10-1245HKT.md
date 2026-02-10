# 每日早報（詳細版）— 2026-02-10（二）08:00 HKT

資料來源：
- 市場報價/新聞：Finnhub
- 論文：arXiv RSS（q-fin.TR/RM/ST/PM + cs.LG/stat.ML）

---

## (1) 美股大市 + 主要宏觀事件

### A) 美股大市（以 ETF proxy）
- **SPY**：693.95（+0.48%）
- **QQQ**：614.32（+0.77%）
- **DIA**：501.22（+0.04%）
- **IWM**：266.88（+0.70%）

**收市概況（因果拆解）**
- 風格：以 QQQ、IWM 相對強，顯示風險偏好較好；DIA 幾乎持平，偏大盤/傳統價值相對落後。
- 內部結構：科技（XLK）走強而醫療（XLV）偏弱，屬「成長/科技回溫」而非全面風險資產上漲。

### B) 宏觀 proxy（利率/美元/商品）
**利率（以債券 ETF 價格反推方向）**
- SHY：82.88（+0.02%）短端：幾乎無變化
- IEF：96.09（+0.02%）中端：幾乎無變化
- TLT：87.52（-0.02%）長端：近乎持平偏弱（長端利率壓力未完全解除）

**美元/商品**
- 美元：UUP 26.79（-0.81%）美元明顯轉弱
- 原油：USO 78.02（+1.34%）；BNO 32.52（+1.56%）油價走高
- 黃金：GLD 467.03（+2.54%）避險/通脹對沖需求上升（與美元走弱同向）

### C) 行業輪動（11 大板塊；按日變動強弱排序）
1) XLK 科技 +1.57%
2) XLB 原材料 +1.30%
3) XLC 通訊 +0.97%
4) XLE 能源 +0.73%
5) XLRE 地產 +0.62%
6) XLI 工業 +0.30%
7) XLU 公用 +0.30%
8) XLY 可選 -0.37%
9) XLP 必需 -0.58%
10) XLF 金融 -0.59%
11) XLV 醫療 -0.88%

**解讀重點**
- 「科技+原材料+能源」同時偏強：一邊係 risk-on（科技/通訊），一邊係通脹/供應風險定價（油、原材料）。
- 金融偏弱而長端債不強：反映市場未完全押注快速降息；利率路徑仍偏分歧。

### D) 重要宏觀事件 / 政策 / 風險（Finnhub general news 抽取；按潛在影響排序）
1) 美國就業與通脹數據周（市場關注「有冇新增就業」「通脹是否真係放緩」）
   - 影響：決定 Fed 今年減息預期是否再延後；同時影響長端利率與成長股估值。
2) AI 投資敘事降溫：市場開始質疑 hyperscalers 的巨額 AI 資本開支對估值支撐
   - 影響：科技板塊內部分化（軟件/AI 受壓 vs. 受益供應鏈）。
3) 美元走弱 /「Sell America」主題再現（美元向低位移動）
   - 影響：有利金/油等商品價格；同時改變跨資產對沖需求與資金流向。
4) 中東地緣風險推升油價波動（市場評估美國對伊朗軍事風險）
   - 影響：能源價格上行→通脹黏性↑→減息路徑更難。
5) 美國政府停擺風險（預算/撥款不確定性）
   - 影響：短期風險溢價上升；對消費/公共服務相關行業造成情緒拖累。

### E) 財報日曆（未來 7 天重點；Finnhub earnings calendar）
- 02/10（今日）：KO、F、SPGI、MAR、GILD、DDOG、SPOT、HOOD、INMD、WCC、DGX、IPG、DUK、AIG 等
- 02/11：MCD、CSCO、SHOP、TMUS、EQIX、PAYC、NTES、HUM、BWA、HLT 等
- 02/12：ABNB、AMAT、COIN、DKNG、NET、PINS、ZTS、VRTX、WYNN、ANET、IRM、PCG、EXPE 等
- 02/13：ROKU、MRNA、CCJ、WEN、AAP 等
- 02/17：PANW、CDNS、MDT、DVN（能源）、AU（黃金股）、DTE 等

**觀察位（只作分析）**
- 若「就業/通脹」偏熱：長端利率再上行風險→成長股估值壓力回來；油價上行會放大呢個方向。
- 若數據偏冷且油價回落：科技/小盤可能延續相對強勢，金融/必需或有修復空間。

---

## (3) Paper Digest（量化交易/風控/因子/LLM in finance）

### 1) Fill Probabilities in a Limit Order Book with State-Dependent Stochastic Order Flows
- 連結：https://arxiv.org/abs/2403.02572
- 問題：限價單放喺唔同價位，實際成交概率點估？（execution 成本 vs. 未成交風險）
- 方法：LOB 建模為「狀態依賴」嘅隨機訂單流 + 互動排隊系統；推導半解析成交概率與 mid-price 變動概率。
- 數據/驗證：真實 FX 現貨市場數據；大量數值實驗。
- 結論：在可計算性下仍能捕捉關鍵 order book 動態；對 best quotes 成交概率估計表現良好。
- 可落地啟示：execution optimizer 的「成交概率子模型」，支持不同掛單深度/市場狀態下 fill-risk 定價。
- 限制/風險：深價位成交率低；狀態定義與參數估計影響穩健性。

### 2) Insider Purchase Signals in Microcap Equities: Gradient Boosting Detection of Abnormal Returns
- 連結：https://arxiv.org/abs/2602.06198
- 問題：內部人買入披露（Form 4）對 microcap 是否有可交易異常回報？
- 方法：Gradient Boosting classifier；特徵含 insider 身份、交易歷史、披露時市場狀態。
- 數據：2018–2024；17,237 宗 open-market insider purchases；市值 30M–500M。
- 結果：AUC 0.70（2024 OOS）；threshold=0.20 時 precision 0.38、recall 0.69；最重要特徵「距離 52-week high」。
- 啟示：microcap 可能存在較慢信息反映；披露時若股價已上漲>10% 平均 CAR 更高（6.3%），偏「趨勢確認」。
- 限制：流動性/交易成本、可賣空限制、披露延遲；需以可交易性嚴格回測。

### 3) Wishart conditional tail risk measures: An analytic approach
- 連結：https://arxiv.org/abs/2602.06401
- 問題：多變量條件尾部風險度量如何解析計算並做資本分配？
- 方法：Wishart process 推導 conditional tail risk；多數只需 1–2 維積分即可計。
- 結論：可嵌入 intertemporal 視角；同時服務 risk measure 與 capital allocation。
- 可落地：多資產/多因子 covariance 動態下的尾部風險引擎。
- 限制：跳躍/厚尾等現象可能令 Wishart 假設失配；需做壓力測試。

### 4) Single- and Multi-Level Fourier-RQMC Methods for Multivariate Shortfall Risk
- 連結：https://arxiv.org/abs/2602.06424
- 問題：多變量 shortfall risk 計算昂貴，MC 收斂慢。
- 方法：Fourier inversion + Randomized Quasi-Monte Carlo；頻域 integrand 更平滑；加 multilevel 降成本。
- 結論：精度/成本優於 sample-average 與 stochastic optimization 基準。
- 啟示：高精度尾部風險（stress、資本分配）可考慮「頻域 + RQMC」。
- 限制：需可做 Fourier 表達；高維仍有實作複雜度。

### 5) Credit Risk Estimation with Non-Financial Features: Evidence from a Synthetic Istanbul Dataset
- 連結：https://arxiv.org/abs/2512.12783
- 問題：underbanked 人群無 bureau file 時，能否用非金融行為特徵估信貸風險？
- 方法：合成數據（公開統計 + RAG 生成檔案）；CatBoost/LightGBM/XGBoost；對比 demographic-only vs. 加入替代特徵。
- 數據：10 萬名合成 Istanbul 居民；7 個人口特徵 + 9 個替代特徵。
- 結論：替代特徵令 AUC 約 +1.3pct；balanced F1 由 ~0.84 → ~0.95。
- 啟示：替代數據有潛力，但監管/偏差/可解釋性與真實外推需嚴格驗證。

---

## 可轉化為研究假設/特徵/風控流程（只作研究建議）
1) Execution：用「狀態依賴 fill probability」作為限價單策略核心風險項，統一預期滑點與未成交風險。
2) Alpha：insider signal 或更像「趨勢確認」；可測試 披露前短期動量 × 距離 52W high 交互特徵。
3) Risk：用 Wishart / Fourier-RQMC 類解析框架提升尾部風險計算穩定性，用於每日風險監控。
4) 系統性風險：shortfall risk 的資本分配可作風險預算 benchmark（對比 VaR/ES 分配差異）。
5) 信貸/替代數據：若用非金融特徵，需配套 fairness + drift 監控（分層、時間漂移、缺失機制）。
