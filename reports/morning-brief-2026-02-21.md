# 每日早報（詳細版）— 2026-02-21 08:00 HKT

## (1) 美股大市 + 主要宏觀事件

### 指數表現
- **SPY (S&P 500)**: [資料暫時不可用]
- **QQQ (NASDAQ 100)**: [資料暫時不可用]
- **DIA (道瓊工業平均)**: [資料暫時不可用]
- **IWM (羅素 2000)**: [資料暫時不可用]

### 宏觀 Proxy
- **利率 ETFs**:
  - SHY (1-3 年期美國國債): [資料暫時不可用]
  - IEF (7-10 年期美國國債): [資料暫時不可用]
  - TLT (20 年以上美國國債): [資料暫時不可用]
- **美元指數** U (US Dollar Index): [資料暫時不可用]
- **大宗商品**:
  - USO/BNO (原油): [資料暫時不可用]
  - GLD (黃金): [資料暫時不可用]

### 重要宏觀事件/政策/風險
[資料暫時不可用]

### 行業輪動
- XLK (科技): [資料暫時不可用]
- XLF (金融): [資料暫時不可用]
- XLE (能源): [資料暫時不可用]
- XLI (工業): [資料暫時不可用]
- XLY (非必需消費): [資料暫時不可用]
- XLP (必需消費): [資料暫時不可用]
- XLV (醫療保健): [資料暫時不可用]
- XLU (公用事業): [資料暫時不可用]
- XLB (原材料): [資料暫時不可用]
- XLRE (房地產): [資料暫時不可用]
- XLC (通信服務): [資料暫時不可用]

### 財報日曆（未來 7 天重點）
[資料暫時不可用]

---

## (3) Paper Digest（量化交易/風控/因子/LLM in finance）

### 1. Trading in CEXs and DEXs with Priority Fees and Stochastic Delays
**鏈接**: https://arxiv.org/abs/2602.10798
**類別**: q-fin.TR (交易與市場微結構)
**作者**: Philippe Bergault, Yadh Hafsi, Leandro Sánchez-Betancourt

#### 研究問題
在中心化交易所（CEX）和去中心化交易所（DEX）之間的最優交易執行，考慮優先費（priority fees）和隨機執行延遲的影響。

#### 方法
- 開發混合控制框架，結合絕對連續控制與脈衝干預
- 允許控制器選擇脈衝的隨機延遲均值
- 支持多個待訂單，使多個脈衝可異步提交和執行

#### 數據/實驗設定
理論分析框架，推導動態規劃原理和擬變分不等式的黏性性質。

#### 主要結論
- 在 DEX 中，交易者通過優先費控制執行延遲分布
- 引入延遲、不確定性和成本之間的基本權衡
- 採用最優優先費顯著優於非策略性費選擇

#### 可落地啟示
對於跨 CEX/DEX 套利或執行，可建立延遲感知的優先費策略，優化管理延遲風險。

#### 限制/風險
- 模型假設延遲分布可參數化控制
- 實際 DEX 流動性和滑點可能比理論更複雜
- 未考慮 gas 費用波動的動態影響

---

### 2. Optimalistic Portfolio Choice with Cross-Impact Propagators
**鏈接**: https://arxiv.org/abs/2403.10273
**類別**: q-fin.TR, q-fin.PM (投資組合與市場微結構)
**作者**: Eduardo Abi Jaber, Eyal Neuman, Sturmius Tuschmann

#### 研究問題
考慮交易者交易對多資產價格產生交叉影響（cross-impact）情況下的最優投資組合選擇。

#### 方法
- 矩陣值 Volterra 推進器建模暫時性交叉影響
- 最大化收益-風險泛函
- 利用價格預測信號
- 將一階條件簡化為耦合隨機 Fredholm 方程組

#### 數據/實驗設定
理論框架，提供最優投資組合和最優執行問題的實現。

#### 主要結論
- 交叉影響顯著影響最優策略
- 提供了操作符解析子（resolvents）形式的顯式解
- 給出了不允許價格操縱的充分條件

#### 可落地啟示
對多資產執行，可建模資產間交叉影響矩陣，優化批量交易時機和分配。

#### 限制/風險
- 需要估計交叉影響矩陣，實際估計難度高
- 假設暫時性影響模型，永久性影響未建模
- 理論解假設市場參數已知

---

### 3. A Few-Shot LLM Framework for Extreme Day Classification in Electricity Markets
**鏈接**: https://arxiv.org/abs/2602.16735
**類別**: cs.LG (機器學習)
**作者**: Saud Alghumayjan, Ming Yi, Bolun Xu

#### 研究問題
使用大語言模型（LLM）在少量數據場景下預測電力市場價格尖峰日。

#### 方法
- 將系統狀態信息（需求、可再生能源、天氣、歷史價格）聚合為統計特徵
- 將特徵格式化為自然語言提示，輸入 LLM
- LLM 輸出尖峰日發生概率和置信度

#### 數據/實驗設定
德州電力市場（ERCOT）歷史數據，與 SVM、XGBoost 等監督學習模型比較。

#### 主要結論
- Few-shot LLM 性能與 SVM、XGBoost 相當
- 在歷史數據稀缺時優於 XGBoost
- LLM 作為數據高效的分類工具具備潛力

#### 可落地啟示
對資源受限市場（如加密貨幣、新興商品），可用 LLM 進行少樣本事件分類。

#### 限制/風險
- 依賴 LLM 提示設計，不穩定性較高
- 推理成本相對傳統模型更高
- LLM 可能產生幻覺，需後處理驗證

---

### 4. Poisson-MNL Bandit: Nearly Optimal Dynamic Joint Assortment and Pricing
**鏈接**: https://arxiv.org/abs/2602.16923
**類別**: stat.ML (統計機器學習)
**作者**: Junhui Cai, Ran Chen, Qitao Huang, Linda Zhao, Wu Zhu

#### 研究問題
動態聯合產品選擇和定價，其中客戶到達率依賴於提供的產品組合和價格。

#### 方法
- Poisson-MNL 模型：MNL 選擇模型 + 依賴產品組合/價格的 Poisson 到達率
- PMNL 算法：基於上置信界（UCB）思想
- 建立 O(√(T log T)) 後悔界和匹配下界

#### 數據/實驗設定
模擬研究，證明考慮到達率依賴性的重要性。

#### 主要結論
- 忽略到達率對組合和定價的依賴性導致次優決策
- PMNL 有效學習客戶選擇和到達模型
- 在有限數據下優於假設固定到達率的方法

#### 可落地啟示
對電子商務或加密貨幣流動性提供，可建模到達率對流動性深度的依賴性，優化掛單策略。

#### 限制/風險
- 假設 MNL 選擇模型，實際行為可能更複雜
- 需要參數估計，冷啟動風險
- 未考慮競爭對手行為

---

### 5. Moment Guided Diffusion for Maximum Entropy Generation (MGD)
**鏈接**: https://arxiv.org/abs/2602.17211
**類別**: stat.ML (統計機器學習)
**作者**: Etienne Lempereur, Nathanaël Cuvelle-Magar, Florentin Coeurdoux, Stéphane Mallat, Eric Vanden-Eijnden

#### 研究問題
從矩約束生成最大熵分布樣本，結合擴散模型的高效性和最大熵方法的理論保證。

#### 方法
- 基於隨機插值框架（stochastic interpolant framework）
- 求解隨機微分方程，在有限時間內將矩推向目標值
- 避免 MCMC 在高維的緩慢混合
- 從動態學中直接估計熵

#### 數據/實驗設定
應用於金融時間序列、湍流、宇宙場的小波散射矩。

#### 主要結論
- 大波動極限下，MGD 收斂到最大熵分布
- 提供可直接計算的熵估計器
- 生成金融時間序列的高維多尺度過程的負熵

#### 可落地啟示
對風險模型壓力測試或生成對抗樣本，可用 MGD 生成符合矩約束的場景，保留尾部特性。

#### 限制/風險
- 依賴矩估計，高維矩估計不穩定
- 擴散模型訓練成本
- 生成樣本可能不完全符合所有矩約束

---

### 6. Beyond Procedure: (Label-Clustered) Conformal Prediction for Substantive Fairness
**鏈接**: https://arxiv.org/abs/2602.16794
**類別**: stat.ML (統計機器學習)
**作者**: Pengqi Liu, Zijun Yu, Mouloud Belbahri, Arthur Charpentier, Masoud Asgharian, Jesse C. Cresswell

#### 研究問題
保形預測（CP）與下遊決策公平性的交互，超越 CP 作為單獨操作的「程序公平性」，分析決策結果的「實質公平性」。

#### 方法
- 推導預測集大小差異的解析上界
- 分解為可解釋組件，說明 label-clustered CP 如何控制方法驅動的不公平性
- 引入 LLM-in-the-loop 評估器近似人類實質公平性評估

#### 數據/實驗設定
實驗顯示 label-clustered CP 變體持續提供優越的實質公平性。

#### 主要結論
- 相等集大小（而非覆蓋率）與實質公平性強相關
- 設計更公平的 CP 系統應優化集大小平等

#### 可落地啟示
對算法交易風險模型或不確定量化，可採用 label-clustered CP 減少不同群體的預測集大小差異，提升公平性。

#### 限制/風險
- 依賴 LLM 評估公平性，存在主觀性
- 標籤聚類策略影響結果
- 實質公平性定義依賴具體應用場景

---

### 7. Anti-causal domain generalization: Leveraging unlabeled data
**鏈接**: https://arxiv.org/abs/2602.17187
**類別**: stat.ML (統計機器學習)
**作者**: Sorawit Saengkyongam, Juan L. Gamella, Andrew C. Miller, Jonas Peters, Nicolai Meinshausen, Christina Heinze-Deml

#### 研究問題
在反因果設定下進行域泛化，利用無標籤數據處理分布轉移。

#### 方法
- 在反因果設定下，結果導致觀測協變量
- 環境對協變量的擾動不傳播到結果
- 正則化模型對協變量均值和協方差變化的敏感性
- 無標籤數據即可估計擾動方向

#### 數據/實驗設定
物理系統和生理信號數據集，證明最優性理論保證。

#### 主要結論
- 反因果結構下，協變量擾動不影響結果，提供泛化優勢
- 正則化敏感性可利用無標籤數據
- 提供最壞情況最優性保證

#### 可落地啟示
對跨市場策略遷移（如美股→港股），若目標變量（如報酬）驅動特徵（如成交量），可利用無標籤目標市場數據提升泛化性。

#### 限制/風險
- 依賴因果結構假設，實際難驗證
- 需要無標籤數據，某些市場難獲得
- 反因果設定不總是成立

---

## 研究想法總結

### 1. 延遲感知的跨交易所執行框架
**靈感來源**: Trading in CEXs and DEXs with Priority Fees
**研究思路**: 量化 CEX（高頻交易所）與 DEX（鏈上 DEX）之間的套利機會時，建模執行延遲分布和優先費的權衡。可建立動態規劃或強化學習框架，優化跨交易所訂單路由和費用分配。

### 2. 交叉影響感知的批量交易優化
**靈感來源**: Optimal Portfolio Choice with Cross-Impact Propagators
**研究思路**: 對多資產投資組合再平衡，估計資產間交叉影響矩陣（如資金流動性共用、新聞傳導），優化批量交易時序和規模，減少滑點。

### 3. LLM 驅動的極端事件預測（少樣本場景）
**靈感來源**: A Few-Shot LLM Framework for Extreme Day Classification
**研究思路**: 對加密貨幣或新興市場，歷史數據稀缺但極端事件重要時，用 LLM 將市場狀態（流動性、波動率、情緒）轉化為自然語言提示，預測極端波動或黑天鵝事件。

### 4. 矩約束生成的風險場景壓力測試
**靈感來源**: Moment Guided Diffusion for Maximum Entropy Generation
**研究思路**: 用 MGD 生成符合特定矩約束（如偏度、峰度、相關矩陣）的金融時間序列場景，用於投資組合壓力測試或生成對抗訓練樣本。

### 5. 公平保形預測用於風險模型
**靈感來源**: Beyond Procedure: Conformal Prediction for Substantive Fairness
**研究思路**: 在算法交易風險管理中，採用 label-clustered CP 減少不同資產類別或市場環境的預測區間大小差異，確保風險覆蓋的公平性。

---

*生成時間: 2026-02-21 08:00 HKT*
*數據來源: arXiv RSS (q-fin.TR, q-fin.RM, q-fin.ST, cs.LG, stat.ML)*
*Finhhub API: [不可用 - 需配置 API key 或 finnhub CLI]*
*Brave Search: [不可用 - 需配置 BRAVE_API_KEY]*
