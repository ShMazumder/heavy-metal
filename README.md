# Heavy Metal Contamination and Fluvial Risk in Bangladesh River Systems

A multi-publication research repository consolidating, modeling, and synthesizing heavy metal contamination across river corridors of Bangladesh from published peer-reviewed investigations (2010–2024).

---

## 📚 Publications & Deliverables

| Package | Venue / Target | Description | Status | Build |
|---|---|---|:---:|:---:|
| **Paper 1** | *Science of The Total Environment* (STOTEN) | Spatial modeling & ecological risk assessment of river sediments using CatBoost & HydroSHEDS reach topology ($N=289$) | **Ready** (17 pp) | `cd manuscripts/paper_1_stoten && ./build.sh` |
| **Paper 2** | *Chemosphere* | Surface water synthesis, ECR 2023 statutory screening, HPI mathematical critique, and hydrographic surveillance gaps ($N=162$) | **Post-R6 Audit** (26 pp) | `cd manuscripts/paper_2_chemosphere && ./build.sh` |
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
│   │   ├── heavy_metal.db             # Master relational SQLite database
│   │   ├── water_data.csv             # Surface water chemical assays (N=268)
│   │   ├── sediment_data.csv          # River sediment assays (N=289)
│   │   ├── stations.csv               # Georeferenced sampling coordinates
│   │   └── studies.csv                # Study metadata and analytical instrumentation
│   └── derived/                       # Generated analysis outputs
│       ├── paper_1/                   # Spatial CV benchmarks, SHAP values, risk maps
│       └── paper_2/                   # Exceedance tables, HPI panels, figures, macros
│
├── scripts/
│   ├── common/
│   │   └── benchmarks.py              # Single source of truth (WHO / ECR / FAO / UCC)
│   ├── paper_1/                       # Sediment geospatial & ML modeling pipelines
│   └── paper_2/
│       └── reproduce_paper_2_results.py # Master reproducibility pipeline for Paper 2
│
├── manuscripts/
│   ├── shared/
│   │   ├── supplementary_table_s1_audited_studies.md  # Master 28-study catalog
│   │   └── submission_and_venue_guide.md              # Editorial & portal roadmap
│   ├── paper_1_stoten/                # STOTEN LaTeX package (main.tex, bib, build.sh)
│   ├── paper_2_chemosphere/           # Chemosphere package (main.tex, bib, build.sh)
│   ├── conference_1_igarss/           # IEEE IGARSS package
│   └── conference_2_water/            # IEEE Water Conference package
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

# Paper 2 (Chemosphere, 26 pages)
cd manuscripts/paper_2_chemosphere && ./build.sh

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
