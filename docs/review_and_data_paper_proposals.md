# Publication Proposals: Systematic Review & Nature Scientific Data Descriptor

This document provides ready-to-execute manuscript blueprints for two high-value alternative publication options derived from the harmonized Bangladesh river heavy metals database.

---

## Proposal 1: Systematic Review and Meta-Analysis

### Target Venues
- **Primary:** *Environment International* (Elsevier, IF 10.3, CiteScore 19.8, Q1 Top 3%)
- **Alternative 1:** *Critical Reviews in Environmental Science and Technology* (Taylor & Francis, IF 12.6, Q1)
- **Alternative 2:** *Journal of Hazardous Materials* (Elsevier, IF 13.6, Q1)

### Working Title
*Heavy Metal Contamination, Speciation, and Hydrographic Surveillance Gaps Across River Networks of Bangladesh: A Systematic Review and Global-Delta Meta-Analysis (2010–2024)*

### Why This Pivot Works
1. **Solves Reviewer Fatigue at Chemosphere:** Paper 2 is currently evaluated as "Original Research," creating friction because it relies on compiled literature rather than primary field campaigns. Review and synthesis journals explicitly seek comprehensive, audited multi-study evidence.
2. **Expands Scope to All Delta Rivers:** Unlocks incorporating broader multi-decade datasets (up to 24+ rivers, including Teesta, Halda, Brahmaputra mainstems) that were previously excluded by strict grab-sample station criteria.
3. **Elevated Citation Impact:** Environmental systematic reviews with meta-analyses receive 3–5× higher citations than individual monitoring papers.

### Methodological Architecture (PRISMA 2020 Compliant)
```
[Database Identification: Scopus, WoS, ScienceDirect, BANSDOC]
                    (N = 1,420 records)
                             │
                             ▼
              [Duplicate Removal: N = 838]
                             │
                             ▼
              [Title & Abstract Screening: N = 74]
                             │
                             ▼
      [Full-Text Multi-Matrix Eligibility: N = 38]
              ├── Surface Water Assays (N = 648 samples)
              ├── River Bed Sediments (N = 512 samples)
              └── Bulk Water Quality Covariates
                             │
                             ▼
            [Meta-Analytic & Spatial Synthesis]
  ├── Subgroup Meta-Analysis: Dissolved vs Total Recoverable
  ├── Meta-Regression: Exceedance ~ Basin + Instrument + Season
  ├── Mathematical Evaluation: HPI quadratic damping vs HEI/HQ
  └── Reach-Scale Surveillance Gap Optimization
```

### Paper Outline
1. **Introduction:** Deltaic vulnerability of the Ganges-Brahmaputra-Meghna system; transboundary pollutant fluxes; review of historical fragmented monitoring.
2. **Systematic Methodology:** PRISMA 2020 protocol; quality assessment rubric (0–14 scale); non-detect imputation protocols; random-effects pooling models.
3. **Multi-Matrix Geochemical Synthesis:**
   - Sediment contamination and geochemical baselines (UCC vs. local shale).
   - Surface water compliance across international (WHO) and domestic (ECR 2023) standards.
   - Dissolved vs. particulate partitioning ($K_d$ dynamics).
4. **Methodological Critique of Pollution Indices:** Analytical proof of HPI weighting distortion ($1/S_i^2$ scaling); recommendation of unweighted indices (HEI, mean hazard quotient).
5. **Hydroclimatic and Fluvial Dynamics:** Pre-monsoon agricultural irrigation pumping (boro rice) vs. monsoon volumetric dilution.
6. **Network-Scale Surveillance Deficits:** Spatial coverage across HydroRIVERS; prioritized monitoring locations for transboundary governance.
7. **Policy Recommendations & Global Delta Implications:** Guidance for DoE/BWDB; comparison with Mekong, Indus, and Nile deltas.

---

## Proposal 2: Nature *Scientific Data* Descriptor

### Target Venue
- *Scientific Data* (Nature Portfolio, IF 5.8, CiteScore 11.2, Q1 Open Access)
- Alternative: *Data in Brief* (Elsevier, CiteScore 3.4)

### Working Title
*A Curated and Snapped Geospatial Database of Heavy Metal Concentrations in River Sediments and Waters Across Bangladesh (2010–2024)*

### Why This Is a Quick Win
- **Zero Overclaim Risk:** Data papers do not present hypothesis tests, statistical causality, or policy arguments. They describe data curation, schema, validation, and reuse potential.
- **Immediate CV Value:** Nature-branded citable data publication.
- **Mutual Synergies:** Both Paper 1 (STOTEN) and Paper 2/Review can formally cite this Data Descriptor, eliminating redundant methodology sections.

### Data Descriptor Structure
1. **Background & Summary:** Need for centralized river water and sediment quality records in South Asia.
2. **Methods:**
   - Literature extraction and cross-verification against primary PDFs.
   - Decimal coordinate harmonization and HydroSHEDS reach snapping (EPSG:4326 to metric HydroRIVERS polyline offsets, mean 357 m).
   - Analytical instrument sensitivity categorization (GF-AAS, ICP-MS vs. Flame-AAS).
3. **Data Records:**
   - `studies.csv`: Provenance, DOIs, analytical digestion, QA/QC flags.
   - `stations.csv`: Snapped coordinates, river gazetteer names, Strahler order, reach ID.
   - `assays.csv`: 557 records (289 sediment, 268 water) with raw vs. harmonized units and censoring flags.
   - Relational database: SQLite `heavy_metal.db` schema and Parquet distribution.
4. **Technical Validation:**
   - Replicate extraction concordance audit (100% check on transcription errors).
   - Spatial snapping offset distributions.
   - Positive control benchmarking against global river geochemical baselines (Gaillardet et al., 2014; Wedepohl, 1995).
5. **Usage Notes:** Example Python/R code snippets for reach routing, spatial cross-validation, and regulatory screening.
