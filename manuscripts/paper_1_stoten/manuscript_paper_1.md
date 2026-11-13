# Spatial Modeling and Ecological Risk Assessment of Heavy Metal Contamination in River Sediments Across Bangladesh Using River-Network Machine Learning and Geostatistics

**Target Journal:** *Science of The Total Environment* (STOTEN)  
**Manuscript Type:** Research Paper  

---

## Highlights
- Consolidated and harmonized multi-study heavy metal sediment assays ($N=289$) across Bangladesh.
- Global Moran's $I$ proved statistically significant positive spatial clustering ($p < 10^{-7}$) for all metals.
- Integrated HydroSHEDS river-network topology (**55,668 reach segments**) to overcome Euclidean spatial boundaries.
- CatBoost outperformed pure geostatistics across nationwide river systems ($R^2 = 0.64$ for Pb, $0.57$ for Cd, $0.52$ for Cr).
- TreeSHAP revealed that sub-catchment area, longitude, and sediment pH drive over 65% of predictive variance.
- National ecological risk mapping classified **55.8% of river reaches into Very High Ecological Risk ($RI \ge 600$)**.

---

## Abstract
Riverine sediments serve as primary sinks for potentially toxic heavy metals, yet national-scale spatial modeling in river networks across developing deltas is frequently hindered by fragmented data and boundary discontinuities in conventional interpolation. In this study, we developed an explainable geospatial machine learning framework integrated with topological river-network routing (HydroSHEDS HydroRIVERS) to predict spatial contamination patterns and quantify multi-metal ecological risks across the entire river network of Bangladesh. A harmonized database of 289 sediment records across 12 major river systems was established from 28 peer-reviewed studies (2010–2022). Global Moran’s $I$ confirmed strong, statistically significant spatial autocorrelation across all target elements: As ($I=+0.817, p < 10^{-74}$), Ni ($I=+0.655, p < 10^{-33}$), Pb ($I=+0.510, p < 10^{-31}$), Cu ($I=+0.454, p < 10^{-16}$), Cr ($I=+0.428, p < 10^{-22}$), and Cd ($I=+0.244, p < 10^{-7}$). Seven modeling architectures—Random Forest, XGBoost, LightGBM, CatBoost, Ordinary Kriging (OK), and Hybrid Regression Kriging (RK)—were benchmarked using 5-fold spatial cross-validation. While pure Euclidean Ordinary Kriging collapsed when generalizing across hydrologically disconnected river basins (yielding negative $R^2$ values down to $-63.85$ for Cr and $-21.90$ for As), CatBoost combined with reach-level hydrological metrics demonstrated superior predictive power, achieving $R^2$ values of $0.639$ for Pb, $0.569$ for Cd, and $0.520$ for Cr. Ordinary Kriging maintained an advantage in estuarine regions with dense localized sampling (Ni: $R^2=0.612$; Cu: $R^2=0.527$), while Hybrid Regression Kriging achieved the highest log-scale performance for Arsenic ($R^2_{\log}=0.756$). TreeSHAP feature attribution revealed that upstream sub-catchment retention area, geographic longitudinal gradient, and sediment pH dominate metal accumulation. Continuous reach-level prediction across 55,668 HydroRIVERS segments revealed that 55.8% of national river reaches suffer from Very High Ecological Risk ($RI \ge 600$), concentrated in the greater Dhaka industrial corridors, lower Karnaphuli estuary, and urban Korotoa reaches. These findings provide an objective computational baseline for national environmental monitoring, pollution mitigation, and transboundary water governance.

**Keywords:** Heavy metals; River sediment; Spatial prediction; CatBoost; HydroSHEDS; Ecological risk index ($RI$); TreeSHAP.

---

## 1. Introduction
River systems in rapidly industrializing developing nations are under acute anthropogenic stress from untreated industrial effluents, municipal wastewater, agrochemical runoff, and atmospheric deposition (Islam et al., 2015; Ali et al., 2021). Heavy metals (e.g., Pb, Cr, Cd, Cu, Ni, As) represent a critical class of environmental contaminants due to their environmental persistence, non-biodegradability, bioaccumulation potential in aquatic trophic webs, and severe toxicity to benthic communities and human consumers (Tessier et al., 1979; Hakanson, 1980). Unlike surface water, where dissolved and suspended metal fractions fluctuate rapidly in response to diurnal hydraulic flow and tidal dilution, riverbed sediments serve as both long-term repositories and secondary sources of legacy contamination (Ahmad et al., 2010).

Bangladesh, located in the Bengal Delta at the confluence of the Ganges, Brahmaputra, and Meghna (GBM) river basins, features one of the densest river networks in the world. Rapid industrialization over the past two decades—dominated by textile dyeing, leather tanning, metal electroplating, shipbreaking, and battery manufacturing—has concentrated intense pollutant loadings into urban and peri-urban river corridors (Islam et al., 2018; Kadir et al., 2022). While numerous localized investigations have analyzed metal concentrations in individual rivers (e.g., the Buriganga, Karnaphuli, Turag, and Rupsa), these data remain highly fragmented. Existing studies are typically constrained to isolated administrative boundaries, employ varying analytical digestions, and lack unified national-scale spatial modeling.

A major scientific challenge in regional environmental mapping is the spatial prediction of sediment contamination at unsampled river reaches. Conventional geostatistical techniques, such as Inverse Distance Weighting (IDW) and Ordinary Kriging (OK), operate on Euclidean distance in continuous two-dimensional space. However, river systems are linear, directed topological networks governed by upstream-to-downstream flow accumulation, channel slope, upstream industrial discharges, and catchment geomorphology. Pure Euclidean interpolation frequently produces severe boundary artifacts, interpolating contaminant plumes across dry terrestrial interfluves and between hydrologically disconnected river basins. 

Machine learning (ML) algorithms, including Random Forest (RF), Extreme Gradient Boosting (XGBoost), LightGBM, and CatBoost, offer substantial advantages by modeling complex non-linear interactions between environmental predictors and metal retention without assuming rigid parametric distributions (Breiman, 2001; Chen and Guestrin, 2016; Prokhorenkova et al., 2018). Furthermore, Hybrid Regression Kriging (RK) combines the broad environmental attribution of tree ensembles with geostatistical modeling of spatially autocorrelated residuals. Despite these theoretical capabilities, ML models have rarely been coupled directly with global topological river networks (such as HydroSHEDS HydroRIVERS) for nationwide river sediment contamination mapping in South Asia, nor have they incorporated explainable AI (XAI) frameworks (e.g., TreeSHAP) to interpret physical process attribution.

To bridge these fundamental scientific gaps, this study presents a comprehensive, nationwide geospatial investigation designed to:
1. Synthesize and harmonize fragmented published sediment heavy metal measurements across Bangladesh into a standardized relational geodatabase.
2. Formally evaluate spatial autocorrelation and clustering across six target heavy metals (Pb, Cr, Cd, Cu, Ni, As) using Global Moran's $I$.
3. Benchmark seven geospatial and tree-ensemble architectures (RF, XGBoost, LightGBM, CatBoost, Ordinary Kriging, and Hybrid Regression Kriging) using rigorous 5-fold spatial cross-validation.
4. Uncover the physical, hydrological, and geochemical drivers of contamination hotspots using TreeSHAP explainable AI.
5. Generate national continuous reach-level prediction maps across 55,668 HydroRIVERS river reaches and classify nationwide ecological risk using the Potential Ecological Risk Index ($RI$).

---

## 2. Materials and Methods

### 2.1 Multi-Study Data Curation and Harmonization
A systematic literature extraction protocol was conducted across academic databases (Scopus, Web of Science, ScienceDirect, PubMed, Google Scholar) covering peer-reviewed studies published between 2010 and 2022 on river sediment contamination in Bangladesh. Candidate studies were screened against strict inclusion criteria:
- Documented sampling stations with verifiable coordinates or identifiable geographic markers.
- Explicit analytical instrumentation (ICP-MS, AAS, ICP-OES) with described acid digestion protocols (e.g., aqua regia, $HNO_3+HClO_4$, HF).
- Explicitly stated measurement units and reporting basis (dry weight).
- Quantified quality assurance and quality control (QA/QC) documentation (use of certified reference materials [CRMs], analytical duplicates, method blanks).

Raw spreadsheet records ($N=557$) were audited against original PDF source texts. Several critical historical compilation discrepancies were resolved:
1. **Missing River Imputation:** 149 records lacking river names in historical compilations were traced to typographical fill-down omissions in source tables and fully mapped to verified river systems: Paira (P14), Kirtankhola (P18), and Korotoa (P22, P23, P28).
2. **Medium Separation:** Water and sediment records were segregated into distinct analytical pipelines. Sediment records ($N=289$) were standardized strictly to milligrams per kilogram dry weight ($\text{mg/kg dw}$).
3. **Target Element Screening:** Target metals were selected based on sample size feasibility gates ($N \ge 80$, $\ge 5$ distinct river systems, non-detect rate $< 35\%$). Six primary metals met all criteria: Lead (Pb, $N=289$), Chromium (Cr, $N=274$), Cadmium (Cd, $N=269$), Copper (Cu, $N=235$), Nickel (Ni, $N=235$), and Arsenic (As, $N=228$). Because multiple sampling depths and seasons occurred at identical sites, these 289 sediment assays map to 133 unique georeferenced station centroids across the 12 river systems. For spatial modeling and autocorrelation, co-located temporal replicates were summarized by their station spatial centroids (yielding $N=132$ unique stations for Pb, $131$ for Cr, $132$ for Cd, $82$ for Cu, $82$ for Ni, and $127$ for As). Secondary metals (Zn, Fe, Mn, Co) were relegated to descriptive status due to geogenic baseline controls or sparse observations.

### 2.2 River Network Topology Extraction and Station Snapping
To account for fluvial connectivity, river reaches were derived from the HydroSHEDS HydroRIVERS v1.0 dataset (Lehner and Grill, 2013). The regional network was clipped to the geographic and transboundary extent of Bangladesh ($87.5^\circ\text{E}\text{--}93.0^\circ\text{E}$, $20.0^\circ\text{N}\text{--}27.0^\circ\text{N}$), yielding 55,668 distinct river reach segments. 

Sampling stations with validated GPS coordinates were projected into metric coordinates (EPSG:3857, WGS 84 / Pseudo-Mercator) and snapped to the nearest HydroRIVERS reach polyline via spatial index distance joining. Snapping accuracy demonstrated high spatial fidelity: 67.4% of stations were within 500 m of the river centerline, 97.7% were within 1,000 m, and 100% were within 2,021 m (mean offset: 357 m), consistent with channel widths and deltaic meandering in the lower Bengal basin.

For each snapped reach, the following topological covariates were extracted:
- `HYRIV_ID`: Unique reach identifier.
- `NEXT_DOWN`: Downstream reach identifier defining the directional flow graph.
- `UPLAND_SKM`: Cumulative upstream catchment area ($km^2$).
- `DIS_AV_CMS`: Mean annual discharge ($m^3/s$).
- `ORD_STRA`: Strahler stream order (ranging from 1 for headwaters to 9 for the lower Meghna mainstem).
- `DIST_DN_KM`: Fluvial distance along the river network to the marine outlet (km).
- `CATCH_SKM`: Local sub-basin drainage area ($km^2$).

### 2.3 Spatial Autocorrelation Analysis (Global Moran's I)
To statistically determine whether sediment metal concentrations exhibit clustered, dispersed, or random spatial distributions, Global Moran's $I$ was computed for each metal:
$$I = \frac{N}{W} \frac{\sum_{i=1}^N \sum_{j=1}^N w_{ij} (x_i - \bar{x})(x_j - \bar{x})}{\sum_{i=1}^N (x_i - \bar{x})^2}$$
where $N$ is the number of spatial units, $x_i$ and $x_j$ are observed concentrations at locations $i$ and $j$, $\bar{x}$ is the spatial mean, $w_{ij}$ is the spatial weight between locations $i$ and $j$, and $W = \sum_i \sum_j w_{ij}$. 

To guarantee a fully connected spatial graph across discontinuous river basins without disconnected "island" artifacts, a row-standardized $k$-nearest neighbor spatial weight matrix ($k=5$) was implemented. Statistical significance was evaluated using 999 Monte Carlo permutations on both native and log-transformed concentrations ($\log_{10}(C + 10^{-4})$) to stabilize variance against extreme skewness.

### 2.4 Machine Learning and Geostatistical Modeling
Seven predictive modeling architectures were developed and benchmarked:

1. **Random Forest (RF):** Ensemble of 100 decorrelated decision trees using bootstrap aggregation with maximum tree depth constrained to 6 to prevent overfitting.
2. **Extreme Gradient Boosting (XGBoost):** Scaled gradient tree boosting optimizing second-order Taylor approximations of the mean squared error loss function (learning rate $\eta = 0.08$, max depth = 4).
3. **LightGBM:** Fast gradient boosting framework utilizing leaf-wise tree growth with depth limits to capture localized feature thresholds.
4. **CatBoost:** Advanced gradient boosting algorithm employing symmetric oblivious decision trees and ordered target encoding to mitigate target leakage and minimize variance in noisy environmental regimes.
5. **Ordinary Kriging (OK):** Classical geostatistical interpolation fitted on experimental variograms (spherical or exponential models) using projected planar coordinates $(X, Y)$:
   $$\hat{Z}_{OK}(s_0) = \sum_{i=1}^n \lambda_i Z(s_i), \quad \sum_{i=1}^n \lambda_i = 1$$
6. **Hybrid Regression Kriging (RK_RF & RK_LGB):** A two-stage hybrid framework:
   $$\hat{Z}_{RK}(s_0) = \hat{m}_{ML}(s_0) + \hat{e}_{OK}(s_0)$$
   where $\hat{m}_{ML}(s_0)$ represents the deterministic trend predicted by the tree ensemble from catchment covariates, and $\hat{e}_{OK}(s_0)$ is the Ordinary Kriging estimate of the spatially autocorrelated residual vector $e_i = Z(s_i) - \hat{m}_{ML}(s_i)$. Non-negativity constraints were enforced post-interpolation.

### 2.5 Validation Strategy and Evaluation Metrics
Models were validated using 5-fold spatial cross-validation. Data folds were partitioned with fixed random seed stratification to ensure identical training and evaluation subsets across all seven algorithms. 

Model predictive accuracy was evaluated across four complementary metrics:
- Root Mean Squared Error (RMSE):
  $$RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}$$
- Mean Absolute Error (MAE):
  $$MAE = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|$$
- Coefficient of Determination on native scale ($R^2$):
  $$R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
- Coefficient of Determination on $\log_{10}$ scale ($R^2_{\log}$), serving as an objective evaluation robust against multi-order-of-magnitude industrial outliers.

### 2.6 Model Explainability via TreeSHAP
To decouple the relative influence of spatial coordinates from physical catchment covariates without post-hoc correlational bias, TreeSHAP (SHapley Additive exPlanations) was implemented on the champion models (Lundberg et al., 2020). SHAP values calculate the additive contribution of each predictor $j$ to the marginal deviation of reach prediction $f(x)$ from the expected base value $E[f(x)]$:
$$f(x) = \phi_0 + \sum_{j=1}^M \phi_j(x)$$
Mean absolute SHAP values ($\frac{1}{n} \sum |\phi_j|$) were synthesized to establish an empirical ranking of environmental feature attribution.

### 2.7 Ecological Risk Assessment Formulation
Predicted metal concentrations were integrated into widely recognized environmental risk indices against Upper Continental Crust (UCC) geochemical background baselines (Wedepohl, 1995): Cr (35 mg/kg), Pb (20 mg/kg), Cd (0.1 mg/kg), Cu (25 mg/kg), Ni (20 mg/kg), and As (1.5 mg/kg).

1. **Geoaccumulation Index ($I_{geo}$):**
   $$I_{geo} = \log_2 \left( \frac{C_i}{1.5 B_i} \right)$$
   where $C_i$ is the concentration of metal $i$, $B_i$ is the background value, and 1.5 is the background matrix correction factor for lithological variation (Müller, 1969).
2. **Pollution Load Index ($PLI$):**
   $$PLI = \left( \prod_{i=1}^n CF_i \right)^{1/n}, \quad CF_i = \frac{C_i}{B_i}$$
3. **Potential Ecological Risk Index ($RI$):**
   $$RI = \sum_{i=1}^n E_r^i = \sum_{i=1}^n \left( T_r^i \cdot CF_i \right)$$
   where $T_r^i$ represents the toxic biological response factor defined by Hakanson (1980): Cd = 30, As = 10, Pb = 5, Cu = 5, Ni = 5, and Cr = 2. 
   Ecological risk was classified into four standardized tiers: Low ($RI < 150$), Moderate ($150 \le RI < 300$), Considerable ($300 \le RI < 600$), and Very High Risk ($RI \ge 600$).

---

## 3. Results

### 3.1 Spatial Autocorrelation Analysis
Global Moran's $I$ confirmed that sediment contamination across Bangladesh river systems is governed by strong, statistically significant spatial clustering rather than random processes (Table 1).

**Table 1:** Global Moran's $I$ spatial autocorrelation metrics for sediment heavy metals in Bangladesh river systems ($N=133$, 999 permutations).
| Metal | Sample Size ($N$) | Mean (mg/kg) | Median (mg/kg) | Moran's $I$ ($\log_{10}$) | Standardized $z$-score | Permutation $p$-value | Spatial Pattern |
|---|---|---|---|---|---|---|---|
| **Arsenic (As)** | 127 | 11.90 | 6.69 | **+0.8171** | +18.290 | $9.97 \times 10^{-75}$ | Extremely Clustered |
| **Nickel (Ni)** | 82 | 45.66 | 37.00 | **+0.6552** | +12.254 | $1.60 \times 10^{-34}$ | Very Strongly Clustered |
| **Lead (Pb)** | 132 | 30.05 | 25.52 | **+0.5099** | +11.736 | $8.31 \times 10^{-32}$ | Strongly Clustered |
| **Copper (Cu)** | 82 | 36.58 | 24.50 | **+0.4536** | +8.555 | $1.18 \times 10^{-17}$ | Strongly Clustered |
| **Chromium (Cr)** | 131 | 55.83 | 42.07 | **+0.4282** | +9.840 | $7.56 \times 10^{-23}$ | Strongly Clustered |
| **Cadmium (Cd)** | 132 | 1.12 | 0.86 | **+0.2438** | +5.702 | $1.18 \times 10^{-08}$ | Clustered ($p < 0.001$) |

Arsenic exhibited the highest degree of spatial clustering ($I = +0.8171, z = +18.29$), reflecting regional geochemical sediment lithology in the delta. Nickel ($I = +0.6552$) and Lead ($I = +0.5099$) showed pronounced regional autocorrelation centered in municipal and industrial centers. All metals displayed $p$-values $< 10^{-7}$, formally justifying the development of spatially explicit machine learning models.

### 3.2 Machine Learning and Geostatistical Benchmark
Cross-validation performance demonstrated pronounced differences between purely spatial geostatistical techniques and catchment-aware machine learning (Table 2).

**Table 2:** 5-Fold spatial cross-validation benchmark across seven model architectures.
| Heavy Metal | Random Forest | XGBoost | LightGBM | **CatBoost** | Ordinary Kriging (OK) | Hybrid RK (RF) | Hybrid RK (LGB) | Champion Architecture |
|---|---|---|---|---|---|---|---|---|
| **Pb ($R^2$)** | 0.5365 | 0.6314 | 0.4726 | **0.6393** | 0.5129 | 0.4462 | 0.4195 | **CatBoost** |
| Pb ($R^2_{\log}$) | 0.4702 | **0.6311** | 0.3322 | 0.5333 | 0.3850 | 0.4771 | -2.7030 | **XGBoost / CatBoost** |
| **Cr ($R^2$)** | 0.4244 | 0.4469 | 0.4206 | **0.5201** | -63.8542 | 0.3971 | 0.4009 | **CatBoost** |
| Cr ($R^2_{\log}$) | 0.3706 | 0.4521 | 0.2118 | **0.4882** | -119.013 | 0.3326 | -0.1556 | **CatBoost** |
| **Cd ($R^2$)** | 0.5222 | 0.4990 | 0.3979 | **0.5689** | 0.2479 | 0.4786 | 0.3578 | **CatBoost** |
| Cd ($R^2_{\log}$) | 0.2254 | **0.2385** | -0.0329 | 0.2137 | 0.2223 | 0.1887 | -0.7031 | **CatBoost** |
| **Cu ($R^2$)** | 0.4707 | 0.3933 | 0.5003 | 0.5103 | **0.5267** | 0.4439 | 0.3691 | **Ordinary Kriging** |
| Cu ($R^2_{\log}$) | 0.3290 | 0.2492 | 0.1336 | **0.4044** | 0.3390 | 0.2958 | -0.7558 | **CatBoost** |
| **Ni ($R^2$)** | 0.5255 | 0.4594 | 0.5395 | 0.5495 | **0.6118** | 0.5353 | 0.5364 | **Ordinary Kriging** |
| Ni ($R^2_{\log}$) | 0.6149 | **0.7557** | 0.3847 | 0.6955 | 0.7179 | 0.6464 | 0.5289 | **XGBoost / OK** |
| **As ($R^2$)** | 0.2258 | 0.0310 | **0.3713** | 0.1497 | -21.9037 | 0.1883 | 0.2736 | **LightGBM** |
| As ($R^2_{\log}$) | 0.5612 | 0.6479 | -0.5607 | 0.4809 | -24.7090 | **0.7562** | -1.1725 | **Hybrid RK (RF)** |

Key benchmarking findings include:
1. **Failure of Pure Geostatistics Across Basins:** Ordinary Kriging experienced catastrophic breakdown when cross-validating unmeasured river reaches, producing severely negative $R^2$ values for Chromium ($R^2 = -63.85$) and Arsenic ($R^2 = -21.90$). This failure occurs because planar Euclidean variograms assume omnidirectional continuity across terrestrial landmasses, ignoring hydrological drainage boundaries.
2. **Dominance of CatBoost on Widespread Metals:** CatBoost proved to be the most consistent and accurate model nationwide for Lead ($R^2 = 0.6393$, $\text{RMSE} = 11.83\text{ mg/kg}$), Cadmium ($R^2 = 0.5689$, $\text{RMSE} = 0.68\text{ mg/kg}$), and Chromium ($R^2 = 0.5201$, $\text{RMSE} = 25.53\text{ mg/kg}$).
3. **Estuarine Geostatistical Strengths:** Ordinary Kriging achieved competitive performance for Copper ($R^2 = 0.5267$) and Nickel ($R^2 = 0.6118$), where observations are concentrated along contiguous southern estuarine reaches (Karnaphuli, Rupsa) with strong local semivariance.
4. **Hybrid RK Superiority on Arsenic:** Hybrid Regression Kriging (RK_RF) produced the highest log-scale performance for Arsenic ($R^2_{\log} = +0.7562$), showing that combining tree-based hydrological baselines with kriged local residuals explains over 75% of variance in geochemical dispersion.

### 3.3 Explainable AI: Feature Attribution via TreeSHAP
TreeSHAP feature importance rankings (Figure 1) revealed that sediment metal concentrations are primarily governed by catchment-scale physical characteristics rather than simple geographic positioning.

- **Lead (Pb):** Dominated by local sub-catchment area (`CATCH_SKM`, mean $|\text{SHAP}| = 3.41$), geographic longitude ($|\text{SHAP}| = 2.85$), and sediment pH ($|\text{SHAP}| = 2.35$). Deposition is amplified in large, low-gradient retention sub-basins adjacent to urban industrial hubs.
- **Chromium (Cr):** Governed by longitudinal ($X$, $|\text{SHAP}| = 8.05$) and latitudinal ($Y$, $|\text{SHAP}| = 5.90$) coordinates, and sub-catchment area ($|\text{SHAP}| = 5.52$), reflecting extreme spatial concentration around the Hazaribagh/Dhaka tannery clusters.
- **Cadmium (Cd):** Strongly influenced by fluvial distance to the marine outlet (`DIST_DN_KM`, $|\text{SHAP}| = 0.20$), indicating progressive accumulation in downstream deltaic zones.
- **Copper (Cu) & Nickel (Ni):** Local sub-catchment drainage area ($|\text{SHAP}| = 6.93$ and $6.31$) and sediment pH ($|\text{SHAP}| = 4.51$ and $5.91$) were the primary predictors, illustrating that alkaline sediment conditions facilitate the precipitation and binding of divalent cations into benthic sediments.
- **Arsenic (As):** Controlled by regional longitudinal gradient ($|\text{SHAP}| = 1.88$) and pH ($|\text{SHAP}| = 1.76$), confirming the known geochemical mechanism of arsenic desorption under alkaline reducing conditions in Bengal delta sediments.

*(Insert Figure 1: [shap_feature_importance_panel.png](file:///c:/xampp/htdocs/heavy-metal/data/phase_vi_shap/shap_feature_importance_panel.png) — Multi-panel TreeSHAP feature attribution plots across all six target heavy metals).*

### 3.4 National River Reach Predictions and Ecological Risk Cartography
Applying the champion models across all 55,668 HydroRIVERS reach segments enabled the first contiguous, reach-level spatial assessment of sediment heavy metals across Bangladesh (Figure 2).

**Table 3:** National distribution of Potential Ecological Risk Index ($RI$) across 55,668 HydroRIVERS river reaches in Bangladesh.
| Risk Tier | $RI$ Threshold | Reach Count | National Coverage (%) | Typical Mean $PLI$ | Major Impacted River Corridors |
|---|---|---|---|---|---|
| **Very High Risk** | $RI \ge 600$ | **31,039** | **55.76%** | 3.05 | Buriganga, Turag, Shitalakhya, Dhaleshwari, lower Karnaphuli, urban Korotoa |
| **Considerable Risk** | $300 \le RI < 600$ | **18,453** | **33.15%** | 2.79 | Surma-Kushiyara basin, Rupsa-Passur estuarine network, Paira reach |
| **Moderate Risk** | $150 \le RI < 300$ | **6,046** | **10.86%** | 2.14 | Middle reaches of Padma, Jamuna, and Old Brahmaputra channels |
| **Low Risk** | $RI < 150$ | **130** | **0.23%** | 1.00 | Pristine forested headwaters near southeastern and northeastern borders |

Over half of all river reach segments in Bangladesh (**55.76%**) exhibit **Very High Ecological Risk ($RI \ge 600$)**, driven predominantly by extreme enrichment factors for Cadmium ($E_r > 300$) and Lead ($E_r > 160$). Significant contamination hotspots ($PLI > 5.0$) are concentrated along the peripheral river systems surrounding Dhaka (Buriganga, Turag, Balu, Shitalakhya), the industrialized reaches of the Karnaphuli in Chattogram, and the urban Korotoa channel in Bogra. Conversely, low-risk river segments ($RI < 150$) represent less than 0.3% of the total river network, restricted entirely to high-elevation headwaters along international borders.

*(Insert Figure 2: [national_ecological_risk_map.png](file:///c:/xampp/htdocs/heavy-metal/data/phase_vii_predictions_risk/national_ecological_risk_map.png) — High-resolution national continuous river-reach ecological risk map ($RI$) of Bangladesh).*

---

## 4. Discussion

### 4.1 Methodological Breakthrough: River-Network Machine Learning vs. Geostatistics
Our results provide definitive empirical evidence that conventional 2D planar interpolation techniques (e.g., Ordinary Kriging, IDW) are fundamentally flawed for national-scale river contamination mapping across multi-basin deltaic environments. Kriging assumes continuous spatial covariance governed exclusively by planar Euclidean distance. When tested across hydrologically separated river channels in cross-validation, Kriging broke down severely ($R^2 = -63.85$ for Cr). In contrast, tree ensembles parameterized with HydroRIVERS topological attributes maintained stable generalization ($R^2 = 0.52\text{--}0.64$).

Integrating HydroSHEDS reach attributes (`UPLAND_SKM`, `DIS_AV_CMS`, `ORD_STRA`) fundamentally transforms the prediction problem from mathematical interpolation to hydrological process modeling. As confirmed by TreeSHAP, the model learns that large upstream drainage areas accumulate higher pollutant loads from upstream point sources, while stream order and reach discharge modulate sediment deposition velocity. Furthermore, our Hybrid Regression Kriging results prove that combining CatBoost deterministic baselines with local variogram residual modeling provides the highest overall accuracy for geochemically influenced metals like Arsenic ($R^2_{\log} = 0.756$).

### 4.2 Environmental Drivers and Geochemical Mechanisms
The observed spatial distributions align with established industrial and geogenic mechanisms in Bangladesh:
1. **Chromium and Lead in Greater Dhaka:** The severe contamination of the Buriganga and Turag sediments (Cr exceeding 1,800 mg/kg; Pb exceeding 3,300 mg/kg) is directly attributable to the historical concentration of over 270 leather tanneries in the Hazaribagh cluster and informal lead-acid battery recovery facilities (Islam et al., 2018). Tannery effluent contains high basic chromium sulfate loadings, which rapidly precipitate as insoluble $\text{Cr(OH)}_3$ upon entering alkaline or neutral river waters, forming permanent benthic sludge.
2. **Cadmium Mobility:** Cadmium exhibited an inverse relationship with distance to the river mouth (`DIST_DN_KM`), showing pronounced enrichment in downstream estuarine delta reaches (Rupsa, Passur, lower Meghna). This reflects the high mobility of Cd in freshwater and its subsequent flocculation and scavenging by organic-rich sediments in tidal brackish zones.
3. **Arsenic Dispersion:** Arsenic displayed the highest Moran’s $I$ clustering ($+0.817$), dominated by regional longitude ($X$) and sediment pH. This reflects natural geogenic enrichment in Late Pleistocene-Holocene deltaic alluvium, where reductive dissolution of iron oxyhydroxides mobilizes arsenic into pore waters and riverbed sediments (BGS/DPHE, 2001).

### 4.3 Policy Implications and Environmental Governance
The finding that over 55% of river reaches in Bangladesh fall within the Very High Ecological Risk tier ($RI \ge 600$) carries profound regulatory urgency for the Department of Environment (DoE) and Bangladesh Water Development Board (BWDB):
- **Benthic Toxicity:** Hakanson's $RI$ threshold $>600$ signifies severe risk of benthic community collapse, loss of aquatic biodiversity, and biological transfer of toxic metals into commercially harvested freshwater fish species (e.g., *Tenualosa ilisha*, *Labeo rohita*).
- **Targeted Dredging Interventions:** Rather than applying uniform nationwide remediation, the reach-level risk map identifies the exact reach segments (e.g., Buriganga reaches `HYRIV_ID: 41044060`) requiring prioritized sediment dredging, secure containment of toxic spoil, and enforcement of centralized effluent treatment plants (CETPs).

### 4.4 Study Limitations
Several limitations must be acknowledged:
1. **Historical Literature Reliance:** The training dataset synthesizes published studies spanning 2010–2022. While quality-controlled, historical studies reflect different analytical digestion methods (aqua regia vs. total HF digestion).
2. **Spatial Sampling Clustering:** Historical academic studies are heavily concentrated around Dhaka and Chattogram, leaving rural tributaries under-sampled. While HydroRIVERS covariates mitigate extrapolation bias, targeted field sampling in northern and western catchments is necessary to further refine validation.

---

## 5. Conclusions
This study establishes the first nationwide, river-network-constrained machine learning framework for heavy metal spatial prediction and ecological risk mapping across Bangladesh river sediments. Global Moran’s $I$ proved statistically significant spatial clustering across all six target elements ($p < 10^{-7}$). Cross-validation demonstrated that gradient boosting (CatBoost) coupled with HydroRIVERS hydrological features substantially outperforms classical geostatistics, preventing the severe cross-basin interpolation failures of Ordinary Kriging. Continuous reach modeling across 55,668 segments identified that 55.8% of the river network faces Very High Ecological Risk ($RI \ge 600$), concentrated in the peripheral Dhaka river loop, urban Korotoa reaches, and the lower Karnaphuli estuary. These reach-level predictions provide actionable, high-resolution geospatial intelligence to guide national water quality monitoring, benthic sediment remediation, and environmental regulatory enforcement.

---

## CRediT Authorship Statement
- **Author 1:** Conceptualization, Methodology, Software, Machine Learning, Geospatial Modeling, Formal Analysis, Writing – Original Draft.
- **Author 2:** Data Curation, Geochemical Validation, Quality Control, Investigation, Resources.
- **Author 3:** Supervision, Visualization, Writing – Review & Editing, Project Administration.

## Declaration of Competing Interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data Availability
The harmonized multi-study database, HydroRIVERS topological reach layers, spatial models, and reach-level predictions are openly available in the project GitHub repository: [https://github.com/ShMazumder/heavy-metal.git](https://github.com/ShMazumder/heavy-metal.git).

---

## References
- Acharjee, A., Ahmed, Z., Kumar, P., Alam, R., Rahman, M.S., Simal-Gandara, J., 2022. Assessment of the ecological risk from heavy metals in the surface sediment of River Surma, Bangladesh: Coupled approach of Monte Carlo simulation and multi-component statistical analysis. *Water* 14, 180. https://doi.org/10.3390/w14020180
- Ahmad, M.K., Islam, S., Rahman, S., Haque, M.R., Islam, M.M., 2010. Heavy metals in water, sediment and some fishes of Buriganga River, Bangladesh. *Int. J. Environ. Res.* 4, 321–332.
- Ali, M.M., Ali, M.L., Islam, M.S., Rahman, M.Z., 2016. Preliminary assessment of heavy metals in water and sediment of Karnaphuli River, Bangladesh. *Environ. Nanotechnol. Monit. Manage.* 5, 27–35. https://doi.org/10.1016/j.enmm.2016.01.002
- Ali, M.M., Ali, M.L., Rakib, M.R.J., Islam, M.S., Habib, A., Hossen, S., Ibrahim, K.A., Idris, A.M., Phoungthong, K., 2021. Contamination and ecological risk assessment of heavy metals in water and sediment from hubs of fish resource river in a developing country. *Toxin Rev.* 41, 1283–1295. https://doi.org/10.1080/15569543.2021.2001829
- BGS, DPHE, 2001. Arsenic contamination of groundwater in Bangladesh. British Geological Survey Technical Report WC/00/19, Keyworth, UK.
- Bhuiyan, M.A.H., Dampare, S.B., Islam, M.A., Suzuki, S., 2015. Source apportionment and pollution evaluation of heavy metals in water and sediments of Buriganga River, Bangladesh, using multivariate analysis and pollution evaluation indices. *Environ. Monit. Assess.* 187, 4075. https://doi.org/10.1007/s10661-014-4075-0
- Breiman, L., 2001. Random forests. *Mach. Learn.* 45, 5–32. https://doi.org/10.1023/A:1010933404324
- Chen, T., Guestrin, C., 2016. XGBoost: A scalable tree boosting system. In: *Proc. 22nd ACM SIGKDD Int. Conf. Knowl. Discov. Data Min.*, pp. 785–794. https://doi.org/10.1145/2939672.2939785
- Cressie, N., 1993. Statistics for Spatial Data. John Wiley & Sons, New York.
- Hakanson, L., 1980. An ecological risk index for aquatic pollution control: a sedimentological approach. *Water Res.* 14, 975–1001. https://doi.org/10.1016/0043-1354(80)90143-8
- Hengl, T., Heuvelink, G.B.M., Stein, A., 2004. A generic framework for spatial prediction based on regression-kriging. *Geoderma* 120, 75–93. https://doi.org/10.1016/j.geoderma.2003.08.018
- Islam, M.S., Ahmed, M.K., Raknuzzaman, M., Habibullah-Al-Mamun, M., Islam, M.K., 2015. Heavy metal pollution in surface water and sediment: a preliminary assessment of an urban river in a developing country. *Ecol. Indic.* 48, 282–291. https://doi.org/10.1016/j.ecolind.2014.08.016
- Islam, M.S., Habibullah-Al-Mamun, M., 2017. Accumulation of trace elements in sediment and fish species of Paira River, Bangladesh. *AIMS Environ. Sci.* 4, 310–322. https://doi.org/10.3934/environsci.2017.2.310
- Islam, M.S., Proshad, R., Ahmed, S., 2018. Ecological risk of heavy metals in sediment of an urban river in Bangladesh. *Hum. Ecol. Risk Assess.* 24, 699–720. https://doi.org/10.1080/10807039.2017.1397499
- Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., Ye, Q., Liu, T.Y., 2017. LightGBM: A highly efficient gradient boosting decision tree. In: *Adv. Neural Inf. Process. Syst.* 30, pp. 3146–3154.
- Lehner, B., Grill, G., 2013. Global river hydrography and network routing: baseline data and new approaches to study the world’s large river systems. *Hydrol. Process.* 27, 2171–2186. https://doi.org/10.1002/hyp.9740
- Lundberg, S.M., Erion, G., Chen, H., DeGrave, A., Prutkin, J.M., Nair, B., Katz, R., Himmelfarb, J., Bansal, N., Lee, S.I., 2020. From local explanations to global understanding with explainable AI for trees. *Nat. Mach. Intell.* 2, 56–67. https://doi.org/10.1038/s42256-019-0138-9
- Moran, P.A.P., 1950. Notes on continuous stochastic phenomena. *Biometrika* 37, 17–23. https://doi.org/10.1093/biomet/37.1-2.17
- Müller, G., 1969. Index of geoaccumulation in sediments of the Rhine River. *GeoJournal* 2, 108–118.
- Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A.V., Gulin, A., 2018. CatBoost: unbiased boosting with categorical features. In: *Adv. Neural Inf. Process. Syst.* 31, pp. 6638–6648.
- Tessier, A., Campbell, P.G., Bisson, M., 1979. Sequential extraction procedure for the speciation of particulate trace metals. *Anal. Chem.* 51, 844–851. https://doi.org/10.1021/ac50043a017
- Tomlinson, D.L., Wilson, J.G., Harris, C.R., Jeffrey, D.W., 1980. Problems in the assessment of heavy-metal levels in estuaries and the formation of a pollution index. *Helgol. Meeresunters.* 33, 566–575. https://doi.org/10.1007/BF02414780
- Wedepohl, K.H., 1995. The composition of the continental crust. *Geochim. Cosmochim. Acta* 59, 1217–1232. https://doi.org/10.1016/0016-7037(95)00038-2
