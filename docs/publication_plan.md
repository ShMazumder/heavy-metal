# Publication-Ready Research Roadmap: Heavy Metal Contamination in Bangladesh Rivers

**Working Title (Paper 1):**  
*Spatial Modeling and Ecological Risk Assessment of Heavy Metal Contamination in River Sediments across Bangladesh Using River-Network Machine Learning and Geostatistics*

**Working Title (Paper 2):**  
*Heavy Metals in Monitored River Corridors of Bangladesh: A Critical Synthesis of Published Records (2010--2024), Regulatory Benchmark Discordance, and Hydrographic Surveillance Deficits*

---

## 1. Publication Strategy & Decoupling Architecture

Attempting to merge water, sediment, spatial mapping, temporal forecasting, and industrial source attribution into a single manuscript creates severe methodological vulnerabilities. Reviewers will reject based on:
1. Conflating water (short-term hydraulic transit) with sediment (long-term sink).
2. Spatiotemporal confounding (year included as predictor without longitudinal repeated sampling).
3. Over-claiming causal industrial attribution purely from Euclidean proximity.

### Two-Paper Publication Architecture

```
                       [Master Literature Database]
                    (557 raw records -> Audited Master)
                                    │
            ┌───────────────────────┴───────────────────────┐
            ▼                                               ▼
┌───────────────────────────────┐   ┌───────────────────────────────┐
│            PAPER 1            │   │            PAPER 2            │
│  Sediment Geospatial Modeling │   │    Surface Water Synthesis    │
│    & Ecological Risk Sink     │   │      & Monitoring Gaps        │
├───────────────────────────────┤   ├───────────────────────────────┤
│ • Focus: Long-term sink       │   │ • Focus: Acute exposure       │
│ • Unit: mg/kg dw              │   │ • Unit: µg/L / mg/L           │
│ • Sample size: N = 289 assays │   │ • Sample size: N = 268 assays │
│   (133 unique station points) │   │   (162 heavy metal records,   │
│ • Key Targets: Cr, Pb, Cd,    │   │    112 Core-4 multi-metal)    │
│   Cu, Ni, As                  │   │ • Key Targets: As, Cr, Cd, Pb │
│ • Methods: Spatial-block ML,  │   │ • Methods: Regulatory screening│
│   Regression Kriging, SHAP,   │   │   (ECR 2023 vs WHO), HKSJ     │
│   Igeo, PLI, RI               │   │   seasonal meta-analysis, HPI │
│ • Venue: STOTEN (Elsevier Q1) │   │ • Venue: Chemosphere (Elsevier)│
└───────────────────────────────┘   └───────────────────────────────┘
```

---

## 2. Harmonized Data Schema & Ingestion Protocol

Transform the unnormalized spreadsheet into a 4-table relational relational structure (SQLite or Parquet via Pandas/Polars):

### Table Schema

1. **`studies` (Study Metadata)**
   - `study_id` (PK): Standardized identifier (e.g., `STU_01`).
   - `doi`: Digital Object Identifier.
   - `first_author`, `pub_year`, `journal`.
   - `analytical_method`: AAS, ICP-OES, ICP-MS.
   - `digestion_protocol`: $HNO_3+HClO_4$, Aqua Regia, HF total digestion.
   - `qa_qc_reported`: Boolean (CRM/SRM used, recovery %, replicate blanks).
   - `study_quality_score`: 0–14 rubric scale.

2. **`stations` (Georeferenced Sampling Points)**
   - `station_id` (PK): Globally unique (`STU_01_S01`).
   - `river_name`: Standardized official gazetteer spelling.
   - `raw_coordinates`: Original string from paper.
   - `lat_wgs84`, `lon_wgs84`: Validated EPSG:4326 decimal degrees.
   - `coord_precision_flag`: A (exact GPS), B (published decimal), C (georeferenced map), D (district centroid/approximate — exclude from ML).
   - `hydro_reach_id`: Snapped reach identifier from HydroSHEDS river network.

3. **`assays` (Chemical Concentrations)**
   - `assay_id` (PK).
   - `station_id` (FK).
   - `medium`: `sediment` or `water`.
   - `fraction`: Total, dissolved, bioavailable/acid-extractable.
   - `element`: As, Cd, Cr, Cu, Fe, Mn, Ni, Pb, Zn.
   - `raw_value`: Numeric or string (e.g., `< 0.01`).
   - `raw_unit`: Original unit reported.
   - `harmonized_value`: Standardized value (sediment: mg/kg dry weight; water: µg/L).
   - `censored_flag`: 0 = detected, 1 = left-censored (< LOD).
   - `lod_value`: Method Detection Limit.

4. **`catchment_covariates` (Environmental Predictors per Reach)**
   - Linked to `hydro_reach_id`.
   - Topographic, land cover, hydrological, and anthropogenic features.

### Censored Data (< LOD) Treatment Protocol
- **Prohibited:** Indiscriminate substitution with $0$, $LOD$, or $LOD/2$ (distorts spatial variance and biases variance estimates).
- **Required:**
  - If censoring rate < 15%: Robust Regression on Order Statistics (ROS) or Kaplan-Meier estimation.
  - If censoring rate 15–50%: Non-parametric Tobit regression or imputation drawn from fitted log-normal conditional distribution.
  - If censoring rate > 50%: Binarize target into classification task (Elevated vs. Below Detection).

---

## 3. Minimum Feasibility Gates (Go / No-Go Rules)

To prevent training unstable models on sparse observations:

| Parameter | Minimum Requirement (Per Model) | Actual Audited Dataset | Status |
|---|---|---|---|
| Independent Sample Sites ($N$) | $\ge 80$ spatial sites | Sediment: 133 unique station centroids (289 assays) | **ACHIEVED** |
| Unique River Systems | $\ge 6$ distinct hydrological basins | 12 major river systems | **ACHIEVED** |
| Distinct Studies | $\ge 5$ peer-reviewed studies | 28 peer-reviewed studies (P01–P28) | **ACHIEVED** |
| Non-detect Rate | $< 35\%$ | All target metals $< 15\%$ | **ACHIEVED** |
| Target Selection (Sediment) | Cr, Pb, Cd, Cu, Ni, As | $N = 289$ (Pb: 132, Cr: 131, Cd: 132, As: 127, Cu: 82, Ni: 82) | **CONFIRMED** |
| Target Selection (Water) | As, Cr, Cd, Pb, Ni, Cu, Zn | $N = 268$ total assays ($N=162$ heavy metal records, $N=112$ Core-4) | **CONFIRMED** |
| Dropped from Primary ML | Co, Fe, Mn | Co $N=15$; Fe/Mn geogenic controls | **RELEGATED** |

---

## 4. Geospatial Covariate Engineering Pipeline

Pure Euclidean coordinates ($X, Y$) learn boundary artifacts. Physical environmental features predict true process distribution.

```
       [Raw Spatial Data]
 ├── HydroSHEDS (DEM, Streams) ────► Flow Direction, Catchment Delineation
 ├── ESA WorldCover (10m) ─────────► % Urban, % Agriculture, % Water
 ├── Global Power / OpenStreetMap ─► Industrial Clusters, Ports, Shipyards
 ├── ERA5-Land Reanalysis ─────────► Monsoon/Dry Precipitation, Runoff
 └── WorldPop (100m) ──────────────► Upstream Cumulative Population
                                     │
                                     ▼
                    [Hydrological Routing Engine]
                    Accumulate upstream via PySheds
                                     │
                                     ▼
           Reach-Level Predictor Vector (X_reach) for every river
```

### Feature Dictionary

1. **Hydrological & Geomorphological:**
   - Upstream drainage area ($km^2$).
   - Flow accumulation (log scale).
   - Reach stream order (Strahler order 1–7).
   - Channel slope (m/km).
   - Distance from river mouth / coastal estuary (salinity/tidal intrusion proxy).

2. **Upstream Anthropogenic Drivers (Accumulated along Flow Direction):**
   - Upstream industrial count within basin ($N_{ind}$).
   - Upstream industrial facility density ($N/km^2$ catchment).
   - Flow-weighted distance to nearest upstream industrial point source.
   - Upstream built-up / urban land fraction ($\%_{urban}$).
   - Upstream agricultural land fraction ($\%_{agri}$).
   - Upstream cumulative human population.

3. **Hydroclimatic Covariates:**
   - Mean annual precipitation (mm/yr, ERA5-Land).
   - Wet-season (Monsoon: Jun–Sep) accumulated runoff.
   - Dry-season (Nov–Feb) mean discharge estimate.

4. **Physicochemical / Soil Background:**
   - Catchment soil organic carbon (SoilGrids 250m).
   - Catchment clay/silt/sand fraction.

---

## 5. Machine Learning & Geostatistical Modeling Architecture

### Model Spectrum
1. **Baselines:**
   - Spatial Median Predictor.
   - Ordinary Kriging (OK) on variograms.
   - Generalized Additive Model (GAM) with bivariate spline $s(lon, lat)$.
2. **Machine Learning Ensembles:**
   - Random Forest Regressor (RFR).
   - Extreme Gradient Boosting (XGBoost).
   - LightGBM Regressor.
   - CatBoost Regressor.
3. **Hybrid Geostatistical ML:**
   - Regression Kriging (RK):
     $$\hat{Z}(s) = \hat{m}_{ML}(s) + \hat{e}_{Krig}(s)$$
     Where $\hat{m}_{ML}(s)$ is tree-ensemble prediction and $\hat{e}_{Krig}(s)$ is Ordinary Kriging of spatial residuals.
4. **Mixed-Effects Machine Learning (Lab/Study Effect):**
   - MixedLM or MERF (Mixed Effects Random Forest) specifying `study_id` as random intercept to remove lab extraction bias.

### Strict Validation Strategy (Zero Data Leakage)
- **Prohibited:** Random K-Fold Cross-Validation (inflates $R^2$ due to spatial autocorrelation between adjacent stations).
- **Protocol 1: Spatial Block CV (SBCV):**
  - Partition Bangladesh into $50 \times 50\text{ km}$ spatial blocks.
  - Assign blocks randomly to 5 folds.
  - Ensures minimum spatial buffer between training and test sets.
- **Protocol 2: Leave-One-River-Out (LORO-CV):**
  - Train on $R-1$ rivers, test on the held-out river (e.g., hold out Buriganga or Karnaphuli).
  - Tests model geographical transferability to unmonitored river basins.
- **Protocol 3: Leave-One-Study-Out (LOSO-CV):**
  - Iteratively hold out all records from a given paper. Tests inter-laboratory invariance.

### Metrics Suite
- Primary: Spatial Root Mean Squared Error (RMSE) on native and $\log_{10}$ scale.
- Mean Absolute Error (MAE).
- Nash-Sutcliffe Efficiency (NSE) / Spatial $R^2_{spatial}$.
- Prediction Interval Coverage Probability (PICP) for 90% confidence bands.

---

## 6. Uncertainty Quantification & Applicability Domain

A map without uncertainty is scientifically invalid.

1. **Prediction Confidence Intervals:**
   - Implement Quantile Regression Forests (QRF) or LightGBM Quantile Loss ($\alpha = 0.05, 0.50, 0.95$).
   - Compute reach-level 90% prediction interval width ($W_{90} = \hat{y}_{95} - \hat{y}_{05}$).
2. **Area of Applicability (AOA):**
   - Calculate Meyer & Pebesma (2021) Dissimilarity Index ($DI$) in feature space:
     $$DI_{k} = \frac{\min_{i} d(x_k, x_i)}{\bar{d}_{train}}$$
   - Any river reach where $DI > DI_{threshold}$ is masked as "Extrapolation / Insufficient Data".

---

## 7. Explainability & Causal Guardrails

1. **Model Interpretation via SHAP & ALE:**
   - TreeSHAP for global feature importance and interaction values.
   - Accumulated Local Effects (ALE) plots to determine non-linear response curves (preferred over Partial Dependence Plots when upstream urban and industrial metrics covary).
2. **Attribution Guardrail:**
   - Restrict narrative to: *"Statistical spatial association between upstream industrial intensity and elevated downstream sediment metal accumulation."*
   - Avoid asserting legal liability or direct causality without isotopic/chemical fingerprinting.

---

## 8. Environmental Risk & Indices Mapping

Transform raw predictions ($\hat{C}_i$) into environmental decision indices using established baselines:

1. **Background Reference ($B_i$):**
   - Use Upper Continental Crust (UCC, Wedepohl 1995) or local baseline:
     Cr: 35 mg/kg, Pb: 20 mg/kg, Cd: 0.1 mg/kg, Cu: 25 mg/kg, Ni: 20 mg/kg, As: 1.5 mg/kg.
2. **Indices Computed per Reach:**
   - Geoaccumulation Index:
     $$I_{geo} = \log_2\left(\frac{C_i}{1.5 B_i}\right)$$
   - Pollution Load Index:
     $$PLI = \left(\prod_{i=1}^n \frac{C_i}{B_i}\right)^{1/n}$$
   - Potential Ecological Risk Index ($RI$):
     $$RI = \sum_{i=1}^n E_r^i = \sum_{i=1}^n T_r^i \cdot \frac{C_i}{B_i}$$
     (Toxic response factors: Cd=30, As=10, Cu=Pb=Ni=5, Cr=2).

---

## 9. Deliverable Manuscripts Blueprint (100% Prepared & Compiled)

### Paper 1: Sediment Spatial Modeling (Core Journal Paper)
- **Target Journal:** *Science of The Total Environment* (STOTEN, Elsevier, IF 9.8).
- **Title:** *Spatial Modeling and Ecological Risk Assessment of Heavy Metal Contamination in River Sediments Across Bangladesh Using River-Network Machine Learning and Geostatistics*
- **Status:** **Compiled & Ready** (16 pages, Elsevier standard format).
- **Core Narrative:** High-resolution river-network prediction of 6 heavy metals across 55,668 HydroRIVERS reach segments; proof that upstream topological indicators outperform Euclidean distance; proof of spatial collapse of Ordinary Kriging across disconnected basins; TreeSHAP physical feature attribution; national Hakanson $RI$ ecological risk mapping.
- **Key Figures:**
  - Fig 1: Multi-panel TreeSHAP feature importance and interaction plots ([fig1_shap.png](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/paper_1_stoten/fig1_shap.png)).
  - Fig 2: High-resolution national continuous river-reach ecological risk map ($RI$) ([fig2_risk_map.png](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/paper_1_stoten/fig2_risk_map.png)).
- **Submission Package:** `manuscripts/paper_1_stoten/` (`main.tex`, `main.pdf`, `cover_letter_stoten.md`, `references.bib`).

### Paper 2: Surface Water Synthesis & Surveillance Deficits (Core Journal Paper)
- **Target Journal:** *Environmental Pollution* (Elsevier, IF 8.9, Q1, SCIE Indexed).
- **Title:** *Heavy Metals in Monitored River Corridors of Bangladesh: A Critical Synthesis of Published Records (2010--2024), Regulatory Benchmark Discordance, and Hydrographic Surveillance Deficits*
- **Status:** **Compiled & Ready** (26 pages, Elsevier single-column review format; post-Round 6 peer-review synchronized).
- **Core Narrative:** Critical synthesis of 162 water metal records ($N=112$ Core-4 panel); ECR 2023 Schedule 2 potable screening (85.6% Pb non-compliance) vs ECR 1997 raw intake; confirmation of 0.45 $\mu$m true dissolved medians (Pb: 0.0250 mg/L) and high-sensitivity GF-AAS/ICP-MS exceedances (79.2%); mathematical decoupling of HPI linear weights vs realized score shares; HKSJ random-effects meta-analysis of seasonal contrasts; Monte Carlo spatial surveillance gap analysis.
- **Key Figures & Supplementary:**
  - Graphical Abstract: 4-panel visual summary ([graphical_abstract.png](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/paper_2_environmental_pollution/graphical_abstract.png)).
  - Fig 1: Regulatory benchmark exceedance rates and multi-metal indices ([fig1_exceedance.png](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/paper_2_environmental_pollution/fig1_exceedance.png)).
  - Fig 2: Hydrological stage and seasonal contrast boxplots ([fig2_dilution.png](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/paper_2_environmental_pollution/fig2_dilution.png)).
  - Fig 3: National hydrographic network coverage and surveillance blind spots ([fig3_spatial_coverage_map.png](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/paper_2_environmental_pollution/fig3_spatial_coverage_map.png)).
  - Table S1: Master catalog of 28 audited primary studies with Crossref DOIs ([supplementary_table_s1_audited_studies.md](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/supplementary_table_s1_audited_studies.md)).
- **Submission Package:** `manuscripts/paper_2_environmental_pollution/` (`main.tex`, `main.pdf`, `cover_letter_env_poll.md`, `results_macros.tex`, `references.bib`).

### Conference 1: Explainable AI & Topological Stream Routing
- **Target Venue:** IEEE IGARSS / ACM SIGSPATIAL.
- **Status:** **Compiled & Ready** (3 pages, IEEE double-column format).
- **Submission Package:** `manuscripts/conference_1_igarss/` (`main.tex`, `main.pdf`).

### Conference 2: Fluvial Dilution Dynamics & Surveillance Gaps
- **Target Venue:** IWA World Water Congress & Exhibition / EWRI Congress.
- **Status:** **Compiled & Ready** (3 pages, IEEE double-column format).
- **Submission Package:** `manuscripts/conference_2_water/` (`main.tex`, `main.pdf`).

---

## 10. Execution Timeline & Milestones (100% Completed)

All phases outlined in the initial roadmap have been executed, validated, audited, and compiled:

1. **Phase 1 (Harmonization & Audit):** 28 studies audited (P01–P28); units standardized; 149 missing river coordinates resolved; SQLite database `heavy_metal.db` engineered.
2. **Phase 2 (HydroSHEDS Routing):** 55,668 reaches extracted; stations snapped (mean offset: 357 m); topological covariates accumulated.
3. **Phase 3 (Spatial Benchmarking):** 7 ML architectures tested under 5-fold spatial block CV; CatBoost established as champion; Ordinary Kriging spatial failure confirmed.
4. **Phase 4 (XAI & Risk Mapping):** TreeSHAP attribution and Hakanson $RI$ cartography executed across all 55,668 reaches (55.76% Very High Risk).
5. **Phase 5 (Water Synthesis & Gap Optimization):** Potable benchmark screening, HKSJ seasonal meta-analysis, HPI algebraic decoupling, and top 15 monitoring gap coordinates prioritized.
6. **Phase 6 (Manuscript Packages):** 4 complete, publication-ready packages compiled to clean PDFs with zero LaTeX errors.

