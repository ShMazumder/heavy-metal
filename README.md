# Heavy Metal Contamination and Fluvial Risk in Bangladesh River Systems

A multi-publication research repository consolidating, modeling, and synthesizing heavy metal contamination across river corridors of Bangladesh from published peer-reviewed investigations (2010–2025).

---

## 📚 Publications & Deliverables

| Package | Venue / Target | Description | Status | Build |
|---|---|---|:---:|:---:|
| **Paper 1** | *Science of The Total Environment* (STOTEN) | Spatial modeling & ecological risk assessment of river sediments using CatBoost, HydroSHEDS reach topology, and LORO validation penalty ($N=289$) | **Ready** (17 pp) | `cd manuscripts/paper_1_stoten && ./build.sh` |
| **Paper 2** | *Environmental Pollution* | Surface water synthesis, ECR 2023 statutory screening, HPI mathematical critique, and hydrographic surveillance gaps ($N=162$ metal assays, $N=268$ total) | **Ready** (26 pp) | `cd manuscripts/paper_2_environmental_pollution && ./build.sh` |
| **Paper 3** | *Environmental Research* | Critical systematic review & evidence map: 5 RQs, 8-domain CEE quality appraisal, analytical comparability, and surveillance deficits ($N=557$) | **Ready** (18 pp) | `cd manuscripts/paper_3_systematic_review && ./build.sh` |
| **Paper 4** | Nature *Scientific Data* | A curated and snapped geospatial database of heavy metal concentrations in Bangladesh rivers (222 physical sites, metric UTM 45N snapping) | **Ready** (8 pp) | `cd manuscripts/paper_4_data_descriptor && ./build.sh` |
| **Conference 1** | IEEE IGARSS | River-network ML vs. geostatistical collapse across disconnected basins | **Ready** (3 pp) | `cd manuscripts/conference_1_igarss && ./build.sh` |
| **Conference 2** | IWA World Water Congress | Potable benchmark discordance and surveillance coverage deficits | **Ready** (3 pp) | `cd manuscripts/conference_2_water && ./build.sh` |

---

## 🗂 Repository Structure

```
heavy-metal/
├── README.md                          # Project overview and reproduction guide
├── requirements.txt                   # Pip dependency manifest
├── environment.yml                    # Conda virtual environment specification
│
├── data/
│   ├── raw/                           # Immutable primary source data
│   │   ├── Final_Data_Table.xlsx      # Original unnormalized literature extraction
│   │   ├── hydrorivers_bangladesh.gpkg# HydroSHEDS HydroRIVERS v1.0 clipped reaches
│   │   ├── bangladesh_boundary.geojson# National boundary polygon
│   │   └── source_pdfs/               # P01–P28 primary research articles
│   ├── processed/                     # Harmonized and relational datasets
│   │   ├── heavy_metal.db             # Master relational SQLite database (8 tables, 2 views)
│   │   ├── water_data.csv             # Surface water chemical assays (N=268)
│   │   ├── sediment_data.csv          # River sediment assays (N=289)
│   │   ├── stations.csv               # Normalized physical stations (N=222; 85 georeferenced)
│   │   ├── station_hydrorivers_matched.csv # Metric UTM 45N reach join table (N=85)
│   │   ├── studies.csv                # Study metadata and analytical instrumentation
│   │   ├── study_extraction_evidence.csv   # 8-domain CEE appraisal extraction matrix
│   │   └── prisma_screening_records.csv    # Full PRISMA 2020 screening trail (N=1,420)
│   └── derived/                       # Generated analysis outputs
│       ├── paper_1/                   # Spatial CV benchmarks, SHAP values, risk maps
│       ├── paper_2/                   # Exceedance tables, HPI panels, figures, macros
│       └── paper_3/                   # PRISMA flow chart, meta-regression forest plots, tables
│
├── scripts/
│   ├── common/
│   │   └── benchmarks.py              # Single source of truth (WHO / ECR / FAO / UCC)
│   ├── paper_1/                       # Sediment geospatial & ML modeling pipelines
│   ├── paper_2/
│   │   └── reproduce_paper_2_results.py # Master reproducibility pipeline for Paper 2
│   └── paper_3/
│       └── run_systematic_review_meta_regression.py # 2,000-bootstrap meta-regression
│
├── manuscripts/
│   ├── shared/
│   │   ├── supplementary_table_s1_audited_studies.md  # Master 28-study catalog
│   │   └── submission_and_venue_guide.md              # Editorial & portal roadmap
│   ├── submissions/                   # Self-contained submission ZIP archives
│   │   ├── stoten_paper_1_submission.zip
│   │   ├── env_poll_paper_2_submission.zip
│   │   ├── chemosphere_paper_2_submission.zip
│   │   ├── env_intl_paper_3_submission.zip
│   │   └── scientific_data_paper_4_submission.zip
│   ├── paper_1_stoten/                # STOTEN LaTeX package (17 pp PDF, build.sh)
│   ├── paper_2_environmental_pollution/# Environmental Pollution package (26 pp PDF, build.sh)
│   ├── paper_3_systematic_review/     # Environment International package (16 pp PDF, build.sh)
│   ├── paper_4_data_descriptor/       # Scientific Data package (8 pp PDF, build.sh)
│   ├── conference_1_igarss/           # IEEE IGARSS package (3 pp PDF, build.sh)
│   └── conference_2_water/            # IEEE Water Conference package (3 pp PDF, build.sh)
│
├── review/
│   └── paper_2/                       # Chronological peer review history
│       ├── round_1/                   # Initial submission reviews
│       ├── round_2/                   # Round 2 comments & responses
│       ├── round_3/                   # Round 3 comments & responses
│       ├── round_5/                   # Round 5 comments & responses
│       └── round_6/                   # Round 6 critical review & point-by-point response
│
└── docs/
    ├── plan.md                        # Foundational 1,700-line research roadmap
    ├── publication_plan.md            # Decoupled two-paper publication architecture
    ├── review_and_data_paper_proposals.md # Systematic review & data descriptor specifications
    ├── mindmaps/                      # Conceptual workflow diagrams
    └── reports/                       # Data consistency & reference audit reports
```

---

## ⚡ Quick Start & Environment Setup

### 1. Python Environment

Using **Conda**:
```bash
conda env create -f environment.yml
conda activate heavy-metal
```

Or using **Pip**:
```bash
pip install -r requirements.txt
```

### 2. Reproduce Paper 2 Results

Run the single-master deterministic pipeline (`np.random.seed(42)`):
```bash
python3 scripts/paper_2/reproduce_paper_2_results.py
```
This recomputes:
- WHO / ECR 1997 / ECR 2023 / FAO benchmark exceedances with 5,000 cluster bootstraps.
- Standardized Core-4 HPI, HEI, and mathematical weighting decomposition.
- Seasonal contrast meta-analyses with Hartung-Knapp-Sidik-Jonkman (HKSJ) adjustments.
- HydroSHEDS topological stream distance and 1,000-run Monte Carlo spatial coverage null model.
- 300 DPI publication figures (`fig1_exceedance.png`, `fig2_dilution.png`, `fig3_spatial_coverage_map.png`, `graphical_abstract.png`).
- Updates `results_macros.tex` for automatic LaTeX synchronization.

### 3. Compile Manuscripts to PDF

Each manuscript contains a standalone `build.sh` script:
```bash
# Paper 1 (STOTEN, 17 pages)
cd manuscripts/paper_1_stoten && ./build.sh

# Paper 2 (Environmental Pollution, 26 pages)
cd manuscripts/paper_2_environmental_pollution && ./build.sh

# Conference 1 (IGARSS, 3 pages)
cd manuscripts/conference_1_igarss && ./build.sh

# Conference 2 (Water, 3 pages)
cd manuscripts/conference_2_water && ./build.sh
```

---

## 🔍 Key Findings

1. **Sediment Machine Learning (Paper 1):** CatBoost integrated with HydroSHEDS topological stream network features outperformed conventional 2D Ordinary Kriging ($R^2 = 0.64$ for Pb, $0.57$ for Cd, $0.52$ for Cr), which suffered catastrophic breakdown across disconnected deltaic basins (Cr $R^2 = -63.85$). National risk modeling classifies **55.8% of river reaches** into Hakanson Very High Ecological Risk ($RI \ge 600$).
2. **Regulatory Benchmark Discordance (Paper 2):** Under the updated Bangladesh Environmental Conservation Rules (ECR 2023 Schedule 2), Lead potable benchmark exceedance jumped from **34.9%** (under repealed ECR 1997) to **85.6%**, formally harmonizing domestic standards with WHO guidelines.
3. **Operational Fraction & Instrumentation:** Confirmed dissolved assays (0.45 $\mu\text{m}$ filtered) persist at elevated levels (median Pb: 0.0250 mg/L; 84.0% WHO exceedance), and high-sensitivity spectrometry (GF-AAS/ICP-MS, $\text{DL} < 0.001\text{ mg/L}$) confirms 79.2% Lead exceedance, verifying results are independent of flame-AAS detection limits.
4. **HPI Mathematical Damping:** The Prasad & Bose HPI scales quadratically ($M_i / S_i^2$), concentrating **78.3% of linear weights** and **77.1% of median index scores** onto Cd and Pb, explaining observed panel invariance across Core-4, Core-5, and All-7 panels on identical subsets.
5. **Hydrographic Surveillance Deficit:** Compiled published literature covers only **16.5% of major river length (757.2 km)** at 25 km, significantly lower than spatial random expectation ($38.2\%$, Monte Carlo $p \le 0.001$), identifying urgent surveillance needs along major transboundary mainstems.
