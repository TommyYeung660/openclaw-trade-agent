# 每日早報（詳細版）— 2026-02-12 08:00 HKT

## (1) 美股大市 + 主要宏觀事件
- 指數：SPY: 691.96 (-0.02%)； QQQ: 613.11 (0.27%)； DIA: 501.33 (-0.11%)； IWM: 264.95 (-0.45%)
- 宏觀 proxy：SHY: 82.85 (-0.10%)； IEF: 96.24 (-0.28%)； TLT: 88.06 (-0.53%)； UUP: 26.83 (0.11%)； USO: 78.89 (1.10%)； BNO: 32.90 (0.95%)； GLD: 467.63 (1.13%)
- 重要宏觀事件/政策/風險（新聞抽取）：
  - This iconic American brand’s debt may be on the verge of junk status（MarketWatch）
  - Cisco’s stock falls as investors pan a seemingly upbeat earnings report（MarketWatch）
  - McDonald’s says value meals are bringing back customers, as results lift stock（MarketWatch）
  - 9 years in college football? This Montana linebacker is the latest Division I student athlete sticking around.（MarketWatch）
  - Why Amazon’s AI spending triggered the stock’s worst slide in over a year（MarketWatch）
- 行業輪動：
  - XLK: 0.29%； XLF: -1.51%； XLE: 2.61%； XLI: 0.53%； XLY: -0.48%； XLP: 1.43%； XLV: 0.59%； XLU: 0.88%； XLB: 1.34%； XLRE: -0.09%； XLC: -0.71%
- 財報日曆：未來 7 天重點
  - 2026-02-19 BABA（bmo）— EPS預估 12.7081；營收預估 296807232201
  - 2026-02-19 WMT（amc）— EPS預估 0.731；營收預估 192249729013
  - 2026-02-19 ETSY（amc）— EPS預估 0.8664；營收預估 902600193
  - 2026-02-19 DE（bmo）— EPS預估 2.1097；營收預估 7916755100
  - 2026-02-18 OXY（amc）— EPS預估 0.2099；營收預估 5672236962
  - 2026-02-18 BKNG（amc）— EPS預估 49.0829；營收預估 6243334595
  - 2026-02-18 ADI（bmo）— EPS預估 2.3259；營收預估 3140835612
  - 2026-02-18 CVNA（amc）— EPS預估 1.1144；營收預估 5357771442
  - 2026-02-17 DVN（amc）— EPS預估 0.8252；營收預估 3892648322
  - 2026-02-17 PANW（amc）— EPS預估 0.9606；營收預估 2633646028

## (3) Paper Digest（量化交易/風控/因子/LLM in finance）
- **Revisiting the Excess Volatility Puzzle Through the Lens of the Chiarella Model** — https://arxiv.org/abs/2505.07820
  - 研究問題：We amend and extend the Chiarella model of financial markets to deal with arbitrary long-term value drifts in a consistent way
  - 方法：基於摘要推斷，主要採用模型/估計/理論推導與模擬或實證。
  - 數據/實驗設定：以摘要描述為主，若為實證則含多資產或多市場樣本。
  - 主要結論： This allows us to improve upon existing calibration schemes, opening the possibility of calibrating individual monthly time series instead of classes of time series
  - 可落地啟示：可用於風險度量/定價/信號穩健性評估。
  - 限制/風險：依賴模型假設與樣本設定，外推需謹慎。
- **Stationary Distributions of the Mode-switching Chiarella Model** — https://arxiv.org/abs/2511.13277
  - 研究問題：We derive the stationary distribution in various regimes of the extended Chiarella model of financial markets
  - 方法：基於摘要推斷，主要採用模型/估計/理論推導與模擬或實證。
  - 數據/實驗設定：以摘要描述為主，若為實證則含多資產或多市場樣本。
  - 主要結論： This model is a stochastic nonlinear dynamical system that encompasses dynamical competition between a (saturating) trending and a mean-reverting component
  - 可落地啟示：可用於風險度量/定價/信號穩健性評估。
  - 限制/風險：依賴模型假設與樣本設定，外推需謹慎。
- **Incentive Pareto Efficiency in Monopoly Insurance Markets with Adverse Selection** — https://arxiv.org/abs/2602.09967
  - 研究問題：We study a monopolistic insurance market with hidden information, where the agent's type $\theta$ is private information that is unobservable to the insurer, and it is drawn from a continuum of types
  - 方法：基於摘要推斷，主要採用模型/估計/理論推導與模擬或實證。
  - 數據/實驗設定：以摘要描述為主，若為實證則含多資產或多市場樣本。
  - 主要結論： The hidden type affects both the loss distribution and the risk attitude of the agent
  - 可落地啟示：可用於風險度量/定價/信號穩健性評估。
  - 限制/風險：依賴模型假設與樣本設定，外推需謹慎。
- **Holistic Multi-Scale Inference of the Leverage Effect: Efficiency under Dependent Microstructure Noise** — https://arxiv.org/abs/2505.08654
  - 研究問題：This paper addresses the long-standing challenge of estimating the leverage effect from high-frequency data contaminated by dependent, non-Gaussian microstructure noise
  - 方法：基於摘要推斷，主要採用模型/估計/理論推導與模擬或實證。
  - 數據/實驗設定：以摘要描述為主，若為實證則含多資產或多市場樣本。
  - 主要結論： We depart from the conventional reliance on pre-averaging or volatility "plug-in" methods by introducing a holistic multi-scale framework that operates directly on the leverage effect
  - 可落地啟示：可用於風險度量/定價/信號穩健性評估。
  - 限制/風險：依賴模型假設與樣本設定，外推需謹慎。
- **Enhanced Graph Transformer with Serialized Graph Tokens** — https://arxiv.org/abs/2602.09065
  - 研究問題：Transformers have demonstrated success in graph learning, particularly for node-level tasks
  - 方法：基於摘要推斷，主要採用模型/估計/理論推導與模擬或實證。
  - 數據/實驗設定：以摘要描述為主，若為實證則含多資產或多市場樣本。
  - 主要結論： However, existing methods encounter an information bottleneck when generating graph-level representations
  - 可落地啟示：可用於風險度量/定價/信號穩健性評估。
  - 限制/風險：依賴模型假設與樣本設定，外推需謹慎。
- **Spectral Disentanglement and Enhancement: A Dual-domain Contrastive Framework for Representation Learning** — https://arxiv.org/abs/2602.09066
  - 研究問題：Large-scale multimodal contrastive learning has recently achieved impressive success in learning rich and transferable representations, yet it remains fundamentally limited by the uniform treatment of feature dimensions and the neglect of the intrinsic spectral structure of the learned features
  - 方法：基於摘要推斷，主要採用模型/估計/理論推導與模擬或實證。
  - 數據/實驗設定：以摘要描述為主，若為實證則含多資產或多市場樣本。
  - 主要結論： Empirical evidence indicates that high-dimensional embeddings tend to collapse into narrow cones, concentrating task-relevant semantics in a small subspace, while the majority of dimensions remain occupied by noise and spurious correlations
  - 可落地啟示：可用於風險度量/定價/信號穩健性評估。
  - 限制/風險：依賴模型假設與樣本設定，外推需謹慎。

### 研究想法（僅研究建議）
1. 以微結構噪音下的槓桿效應估計作為因子穩健性檢驗基準，衡量高頻訊號失真。
2. 以趨勢/均值回歸競爭模型校準長期估值漂移，檢驗不同資產類別的“超額波動”幅度。
3. 探討多 token 表徵在多資產關聯圖上的聚合能力，與傳統圖因子比較穩定度。
4. 以譜分解增強對多模態財經訊息表徵，測試在事件驅動預測的泛化提升。
5. 在保險/信用風險的逆向選擇框架中，研究激勵相容的定價區間對風控資本的影響。
