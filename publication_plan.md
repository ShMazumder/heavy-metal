# Publication-Ready Research Roadmap: Heavy Metal Contamination in Bangladesh Rivers

**Working Title (Paper 1):**  
*Spatial Modeling and Ecological Risk Assessment of Heavy Metal Contamination in River Sediments across Bangladesh Using River-Network Machine Learning and Geostatistics*

**Working Title (Paper 2):**  
*Dissolved Heavy Metals in Bangladesh River Waters: Multi-Study Synthesis, Health Hazard Indices, and Geospatial Monitoring Gap Analysis*

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
│ • Sample size: N = 264 (Pb/Cr)│   │ • Sample size: N = 140–160    │
│ • Key Targets: Cr, Pb, Cd,    │   │ • Key Targets: As, Cr, Cd, Pb │
│   Cu, Ni, As                  │   │ • Methods: Hydrological stage │
│ • Methods: Spatial-block ML,  │   │   correlation, seasonal gaps, │
│   Regression Kriging, SHAP,   │   │   WHO/BD drinking & aquatic   │
│   Igeo, PLI, RI               │   │   criteria exceedance rates   │
│ • Venue: STOTEN, Env Pollut,  │   │ • Venue: Chemosphere, Env Mon │
│   J. Hydrology (Q1)           │   │   Assess, Ecotox & Env Safety │
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

| Parameter | Minimum Requirement (Per Model) | Target in Dataset | Status |
|---|---|---|---|
| Independent Sample Sites ($N$) | $\ge 80$ spatial sites | Sediment: 120–180 unique sites | **GO** |
| Unique River Systems | $\ge 6$ distinct hydrological basins | 12 rivers listed | **GO (post-audit)** |
| Distinct Studies | $\ge 5$ peer-reviewed studies | 28 studies available | **GO** |
| Non-detect Rate | $< 35\%$ | Most major metals < 20% | **GO** |
| Target Selection (Sediment) | Cr, Pb, Cd, Cu, Ni, As | Non-null count $\ge 210$ | **CONFIRMED** |
| Target Selection (Water) | As, Cr, Cd, Pb | Non-null count: 124–160 | **CONFIRMED** |
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

## 9. Deliverable Manuscripts Blueprint

### Paper 1: Sediment Spatial Modeling (Core Paper)
- **Target Journal:** *Science of The Total Environment* (Elsevier, IF ~9.8) or *Journal of Hazardous Materials* (IF ~13.6).
- **Core Narrative:** High-resolution river-network prediction of 6 heavy metals across Bangladesh rivers; proof that upstream topological indicators outperform Euclidean distance; identification of critical regional sediment sinks and ecological risk hotpots.
- **Figures:**
  - Fig 1: Hydrological map of Bangladesh, sampling stations, study quality distribution, and data density.
  - Fig 2: Validation scatter plots: Random CV vs. Spatial Block CV vs. LORO-CV.
  - Fig 3: Four-panel reach-level continuous maps for Pb and Cr: (a) Predicted median, (b) Uncertainty width, (c) AOA mask, (d) $I_{geo}$ class.
  - Fig 4: SHAP summary beeswarm and ALE response functions for top 5 hydrological/anthropogenic features.
  - Fig 5: National Multi-metal Ecological Risk ($RI$) reach classification highlighting priority remediation reaches.

### Paper 2: Surface Water Synthesis & Monitoring Prioritization
- **Target Journal:** *Chemosphere* or *Environmental Monitoring and Assessment*.
- **Core Narrative:** Meta-analysis of surface water metal concentrations across Bangladesh; seasonal comparison (monsoon vs dry-flow dilution effects); compliance assessment against Bangladesh ECR 2023 and WHO guidelines; spatial gap analysis designating optimal future government monitoring stations.

---

## 10. Execution Timeline & Role Distribution (18 Weeks)

```
WEEKS 1–4: DATA HARMONIZATION & AUDIT SPRINT
├── Re-read 28 source papers
├── Resolve 149 missing river records & georeference coordinates
├── Standardize units to mg/kg dw (sediment) and µg/L (water)
└── Establish SQLite database and LOD registry
    Deliverable: Audited Master Dataset v1.0 + Audit Report

WEEKS 5–8: GEOSPATIAL EXTRACTION & NETWORK ACCUMULATION
├── Extract HydroSHEDS river reach network
├── Calculate upstream accumulated covariates via PySheds
├── Match sample stations to nearest river reaches
└── Build feature matrix X
    Deliverable: Feature Engine Matrix + Covariate Multicollinearity Report

WEEKS 9–13: MACHINE LEARNING & SPATIAL VALIDATION BENCHMARK
├── Implement SBCV, LORO-CV, LOSO-CV pipelines
├── Train baselines, tree ensembles, and Regression Kriging
├── Hyperparameter optimization via Optuna
└── Compute QRF uncertainty intervals and AOA masks
    Deliverable: Model Benchmark Tables + Spatial Error Maps

WEEKS 14–16: XAI & ECOLOGICAL RISK INTEGRATION
├── Run TreeSHAP and ALE interpretation
├── Calculate reach-level Igeo, PLI, and RI
└── Generate publication cartography in QGIS/Python
    Deliverable: Final Publication Figures (300 DPI)

WEEKS 17–18: MANUSCRIPT DRAFTING & SUBMISSION
├── Draft Manuscript Sections (Paper 1)
├── Package code & reproducible workflow on GitHub/Zenodo
└── Complete journal formatting & peer review submission
    Deliverable: Submitted Paper 1 Manuscript
```

### Team Responsibilities (3 Researchers)

- **Researcher 1 (Data Lead & Geochemist):**
  - Primary ownership: Weeks 1–4.
  - Task: Literature extraction audit, analytical quality scoring, digestion method harmonization, LOD table, background value validation, geochemical interpretation.
- **Researcher 2 (GIS & Spatial Analyst):**
  - Primary ownership: Weeks 5–8.
  - Task: HydroSHEDS topology, upstream catchment flow routing, land use/population extraction, coordinate snapping, QGIS cartography and vector reach preparation.
- **Researcher 3 (ML Engineer & Statistician):**
  - Primary ownership: Weeks 9–14.
  - Task: Spatial Block CV pipeline, ML training/tuning, Regression Kriging, SHAP/ALE scripts, QRF prediction intervals, reproducible codebase.
- **Joint Effort:**
  - Manuscript writing, review response, and data curation.

