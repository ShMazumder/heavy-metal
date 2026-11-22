# 🚀 Publication Launch Checklist (Authoritative: Option A — Review First)

> [!IMPORTANT]
> **Governing Publication Strategy:** [`docs/plan_updated.md`](file:///Users/rohansmac/Documents/projects/heavy-metal/docs/plan_updated.md).
> All current submission ZIPs in `manuscripts/submissions/` are **FROZEN**. No manuscript will be uploaded until it passes its independent scientific validation, data availability, and author metadata requirements.

---

## Strategic Publication Architecture (Option A: Sequential Launch)

```
[Phase 1: Flagship Review (Submit First)]
   └── Paper 3: Critical Systematic Review & Evidence Map (Environmental Research / J. Env. Manage.)
         │
         ├── [Phase 2: Parallel Technical Refinement & Data Deployment]
         │     ├── Paper 2: Surface-Water Regulatory Screening & Surveillance Deficits (Environmental Pollution)
         │     └── Paper 4: Curated Geospatial Data Descriptor (Nature Scientific Data / Data in Brief)
         │           └── Publish Zenodo Archive upon journal data review request
         │
         └── [Phase 3: Spatial ML Validation Overhaul & Launch]
               └── Paper 1: Sediment Spatial Machine Learning & Transferability (STOTEN)
```

---

## Phase 0: Pre-Flight Blockers (Applies to All Papers)

### 1. Author Metadata Injection
Replace placeholder text in all manuscript `.tex`, markdown, and `.zenodo.json` files before any portal upload:
- `Author One` $\to$ Real First Author Name
- `Author Two` $\to$ Real Second Author Name
- `Author Three` $\to$ Real Third Author Name
- `University Name` / `Technical University` $\to$ Official Affiliated Institutions
- `author.one@university.edu` $\to$ Institutional email addresses
- ORCID fields $\to$ Verified 16-digit ORCID iDs

### 2. APC & Venue Funding Verification
- **Paper 3 (*Environmental Research* / *J. Env. Manage.*):** Hybrid model $\to$ **$0 APC (Subscription route)**.
- **Paper 2 (*Environmental Pollution*):** Hybrid model $\to$ **$0 APC (Subscription route)**.
- **Paper 1 (*Science of The Total Environment*):** Hybrid model $\to$ **$0 APC (Subscription route)**.
- **Paper 4 (*Nature Scientific Data*):** **Gold Open Access ONLY $\to$ US$2,690 APC**.
  - Must request institutional Read & Publish waiver or discretionary low-income waiver upon submission.
  - *Zero-APC Fallback:* Transfer to *Data in Brief* (Elsevier, hybrid option / waiver available).

### 3. Zenodo Data Deposit Lifecycle
- Archive [`zenodo_heavy_metal_database_v1.0.0.zip`](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/submissions/zenodo_heavy_metal_database_v1.0.0.zip) (7.7 MB, with Parquet, SQLite, CSV, GIS layers) is registered under reserved DOI `10.5281/zenodo.24414976`.
- **Status:** Retained in **Draft** mode during preparation.
- **Trigger to Publish:** Click **"Publish"** only when Paper 4 or Paper 3 editors/reviewers explicitly require live data access. Manuscripts must not falsely claim live data access while the deposit remains unreleased.

---

## Manuscript-by-Manuscript Go/No-Go Roadmap

### 1. Paper 3: Critical Systematic Review & Evidence Map (FLAGSHIP — SUBMIT FIRST)
- **Status:** **REBUILDING UNDER 5 RESEARCH QUESTIONS**
- **Target Venue:** *Environmental Research* (Elsevier, IF 7.7, $0 APC) or *Journal of Environmental Management* (Elsevier, IF 8.0, $0 APC).
- **Core Contribution:**
  - Evaluates whether published research (2000–2026) can support reliable national-scale spatial inference.
  - 5 RQs: (1) Spatio-temporal evolution; (2) Analytical comparability & LOD handling; (3) Geographical representativeness & coordinate accuracy; (4) Risk index comparability ($CF, I_{\mathrm{geo}}, PLI, RI, HPI$); (5) Defensible national monitoring framework.
  - 8-domain CEE / ROSES critical appraisal framework.
- **Gate to Submit:** Complete PRISMA/ROSES search string documentation and study-quality appraisal table.

### 2. Paper 2: Surface Water Regulatory Audit & Surveillance Deficits
- **Status:** **READY FOR SUBMISSION UPON REVIEW PAPER LAUNCH**
- **Target Venue:** *Environmental Pollution* (Elsevier, IF 8.9, Q1, $0 APC).
- **Core Contribution:**
  - ECR 2023 Schedule 2 potable regulatory update (Pb potable exceedance surge to 85.6%).
  - Confirmed dissolved (0.45 $\mu\text{m}$) sensitivity analysis ($k=10$ studies).
  - HPI mathematical damping proof ($1/S_i^2$ quadratic scaling; 78.3% weight on Cd/Pb).
  - Stream network surveillance coverage (16.5% coverage; 23 random sites Monte Carlo $p \le 0.001$).
- **Gate to Submit:** Disclose companion relationship with Paper 3; submit once Paper 3 is under review.

### 3. Paper 4: Geospatial Data Descriptor
- **Status:** **TECHNICAL AUDIT COMPLETE; AWAITING APC/ZENODO LIVE ACTION**
- **Target Venue:** Nature *Scientific Data* (Gold OA, $2,690 APC) or *Data in Brief* ($0 APC).
- **Core Contribution:**
  - Reusable, multi-format (SQLite, Parquet, CSV, GeoPackage) relational dataset.
  - 426 stations (220 coordinate-resolved centroids, 206 descriptive entries); 220 reach join records.
  - 557 verified assays across 28 peer-reviewed studies (2010–2024).
- **Gate to Submit:** Secure APC waiver or confirm institutional funding; convert Zenodo from Draft to Live.

### 4. Paper 1: Sediment Spatial Machine Learning & Transferability
- **Status:** **TECHNICAL OVERHAUL IN PROGRESS (DO NOT SUBMIT)**
- **Target Venue:** *Science of The Total Environment* (STOTEN, Elsevier, IF 8.2, $0 APC).
- **Core Contribution:**
  - HydroRIVERS-informed machine learning vs planar geostatistical collapse.
  - **Empirical LORO Transferability Penalty:** Transparently reports negative $R^2$ under true Leave-One-River-Out validation to expose the boundary between local corridor interpolation ($R^2 = 0.54\text{--}0.64$) and out-of-basin cross-river generalization ($R^2 < 0$).
  - Full-suite 6-metal prediction uncertainty and composite Hakanson $RI$ cartography ($RI = 498.25 \pm 68.20$, $CV = 13.6\%$).
- **Gate to Submit:** Formalize the applicability domain and mask high-extrapolation reaches before submission.
