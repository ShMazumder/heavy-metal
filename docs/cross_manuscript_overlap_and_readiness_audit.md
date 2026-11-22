# 📋 Cross-Manuscript Overlap & Submission-Readiness Audit

**Date:** 2026-11-22  
**Governing Plan:** [`docs/plan_updated.md`](file:///Users/rohansmac/Documents/projects/heavy-metal/docs/plan_updated.md) (Option A: Review First with Parallel Preparation)  
**Ethical Framework:** Committee on Publication Ethics (COPE) Guidelines on Redundant Publication and Related Submissions  

---

## 1. Executive Assessment & Submission Status

| Manuscript | Working Target | APC Model | Primary Role | Submission Verdict |
|---|---|---|---|---|
| **Paper 3** | *Environmental Research* / *J. Env. Manage.* | **$0 (Subscription)** | Flagship Critical Systematic Review & Evidence Map | **REBUILD (Submit First)** |
| **Paper 2** | *Environmental Pollution* | **$0 (Subscription)** | Surface Water Regulatory Screening & Surveillance Deficits | **READY (Submit Second)** |
| **Paper 4** | Nature *Scientific Data* / *Data in Brief* | **$2,690 (OA) / $0 (DiB)** | Reusable Geospatial Data Infrastructure | **HOLD (Publish Zenodo First)** |
| **Paper 1** | *Science of The Total Environment* | **$0 (Subscription)** | River-Network ML & Sediment Spatial Transferability | **NO-GO (Validation Overhaul)** |

---

## 2. Definitive Cross-Manuscript Contribution Matrix

```
[Common 28-Study Evidence Corpus (557 Assays across 12 River Systems)]
   │
   ├── Paper 3 (Review): Evaluates RELIABILITY & REPRESENTATIVENESS of the entire corpus
   │     └── Unique: 5 RQs, 8-domain CEE appraisal, PRISMA/ROSES evidence map, surveillance gaps
   │
   ├── Paper 4 (Data): Transforms corpus into REUSABLE, RELATIONAL GEOSPATIAL INFRASTRUCTURE
   │     └── Unique: 4-table SQLite schema, Apache Parquet, topological HydroRIVERS snapping
   │
   ├── Paper 2 (Water): Rigorous STATUTORY AUDIT & HYDROLOGICAL SCREENING of surface waters
   │     └── Unique: ECR 2023 potable shift, HPI 1/S_i^2 algebraic damping proof, 23-site Monte Carlo
   │
   └── Paper 1 (Sediment): HYDROLOGICAL MACHINE LEARNING & SPATIAL TRANSFERABILITY LIMITS
         └── Unique: HydroRIVERS topological features, true LORO validation penalty, 6-metal reach cartography
```

### Detailed Feature & Asset Allocation

| Attribute | Paper 3 (Review & Evidence Map) | Paper 2 (Water Quality Audit) | Paper 4 (Data Descriptor) | Paper 1 (Sediment Spatial ML) |
|---|---|---|---|---|
| **Primary Matrix** | Water + Sediment (Comparative) | Surface Water Only ($N=268$) | Water + Sediment + Stations | Bed Sediment Only ($N=289$) |
| **Central Research Question** | *Can published literature support reliable national-scale environmental inference in Bangladesh?* | *How does regulatory modernization (ECR 2023) alter potable water risk and surveillance deficits?* | *How is the multi-matrix Bengal Delta heavy metal corpus structured, snapped, and reused?* | *Can upstream stream-network topology predict sediment metals across disconnected river basins?* |
| **Exclusive Methods** | • 5 Core Research Questions<br>• 8-domain CEE critical appraisal<br>• PRISMA 2020 screening audit ($N=1,420$)<br>• Review Evidence Atlas (21.8% coverage, 58 sites) | • ECR 2023 vs ECR 1997 vs WHO audit<br>• Confirmed 0.45 $\mu\text{m}$ dissolved sensitivity<br>• Algebraic HPI $1/S_i^2$ quadratic damping proof<br>• 1,000 Monte Carlo network null model (23 sites) | • 8-table, 2-view SQLite schema<br>• Composite `Station_UID` normalization (222 sites)<br>• Metric UTM 45N HydroRIVERS snapping ($N=85$)<br>• Coordinate provenance audit | • HydroRIVERS stream network covariates<br>• Strict Leave-One-River-Out (LORO) CV ($R^2 < 0$)<br>• 6-metal reach uncertainty propagation<br>• Hakanson composite $RI$ corridor cartography |
| **Exclusive Figures** | • Fig 1: PRISMA flow chart<br>• Fig 2: 8-domain quality appraisal heatmap<br>• Fig 3: Review Evidence Atlas (River breakdown \& Population deficit; SHA256: `5090fdf0...`) | • Fig 1: Multi-benchmark exceedance panel<br>• Fig 2: Seasonal within-study boxplots<br>• Fig 3: National 25 km river surveillance map (23 water sites; SHA256: `6c9a092c...`) | • Fig 1: Relational schema \& station map<br>• Fig 2: Snapping offset distance distribution | • Fig 1: TreeSHAP feature attribution panel<br>• Fig 2: Reach-level $RI$ interpolative corridor map |
| **Prohibited Content (To Prevent Overlap)** | *Must NOT reproduce Paper 2's algebraic HPI derivation or Paper 1's ML reach predictions.* | *Must NOT evaluate sediment contamination, ML algorithms, or PRISMA literature searches.* | *Must NOT present ML prediction models, meta-regressions, or policy conclusions.* | *Must NOT analyze surface water chemistry, ECR 2023 potable limits, or HPI water indices.* |

---

### Spatial Coverage Population Harmonization

To prevent denominator confusion across manuscripts, spatial coverage statistics are strictly demarcated across three distinct analytical populations:

1. **Surface Water Heavy Metal Surveillance Network (Paper 2):**
   - Population: $N=23$ unique coordinate stations monitoring dissolved/total water trace metals.
   - Major River Coverage (Strahler $\ge 4$, $Q \ge 50\text{ m}^3/\text{s}$, total 4,599.1 km):
     - **16.5% at 25 km radius** (757.2 km; 11.0% strictly along river network via Dijkstra algorithm).
     - 4.8% at 10 km radius (220.1 km); 40.6% at 50 km radius (1,867.7 km).
     - Monte Carlo spatial clustering test ($n=1,000$ iterations): $p \le 0.001$ against expected 38.2%.

2. **Bed Sediment Heavy Metal Surveillance Network (Paper 1):**
   - Population: $N=36$ unique coordinate stations monitoring bed sediment trace metals.
   - Major River Coverage:
     - **16.0% at 25 km radius** (735.8 km).
     - 4.5% at 10 km radius (208.2 km); 49.4% at 50 km radius (2,270.8 km).

3. **Combined National Environmental Literature Footprint (Paper 3 / Review):**
   - Population: $N=58$ unique coordinate stations spanning all 85 georeferenced physical stations across all 28 published studies.
   - Major River Coverage:
     - **21.8% at 25 km radius** (1,000.9 km monitored; **78.2% unmonitored surveillance deficit**).
     - 6.8% at 10 km radius (314.9 km monitored; **93.2% unmonitored surveillance deficit**).
     - 58.4% at 50 km radius (2,684.2 km).

---

## 3. Manuscript-by-Manuscript Forensic Audit & Action Plans

### Paper 3: Critical Systematic Review & Evidence Map
- **Target Journal:** *Environmental Research* (Primary) or *Journal of Environmental Management* (Alternative).
- **Novelty Risk Addressed:** Insulates against recently published 2025 general reviews (Pandit et al. 2025; Dec 2025 synthesis) by pivoting from a generic pollution summary to a **critical methodological and evidence-readiness appraisal**.
- **Required Overhaul:**
  1. Structure manuscript around the 5 Research Questions (`RQ1` Spatio-temporal evolution; `RQ2` Analytical comparability; `RQ3` Geographical representativeness; `RQ4` Risk index sensitivity; `RQ5` Defensible monitoring roadmap).
  2. Implement the 8-domain critical appraisal framework (sampling design, temporal design, spatial provenance, sample handling, analytical methods, QA/QC, LOD reporting, statistical reporting).
  3. Formally register/deposit the review protocol under PRISMA 2020 / ROSES guidelines.
- **Verdict:** **REBUILD AS FLAGSHIP LEAD SUBMISSION**.

---

### Paper 2: Surface Water Synthesis & Regulatory Screening
- **Target Journal:** *Environmental Pollution* (Elsevier, IF 8.9, $0 APC subscription route).
- **Technical Integrity:**
  - Patched confirmed dissolved filter (`~df_water['Study_ID'].isin(['P06', 'P11'])`).
  - Fixed Monte Carlo null model string (23 random sites) and finite $p$-value ($p \le 0.001$).
  - Clarified ECR 2023 Schedule 2 ambient surface water vs potable standards (treatment burden screening vs ambient statutory non-compliance).
- **Submission Prerequisite:** Ready for submission as soon as Paper 3 enters editorial review, with clear companion disclosure.
- **Verdict:** **READY FOR SUBMISSION (PHASE 2)**.

---

### Paper 4: Geospatial Data Descriptor
- **Target Journal:** Nature *Scientific Data* (Gold OA, standard APC US$2,690) or *Data in Brief* ($0 APC).
- **Technical Integrity:**
  - Exported all 8 tables to Apache Parquet (`data/processed/*.parquet`).
  - Reconciled station register denominators: 426 total rows (220 coordinate-resolved centroids, 206 descriptive entries); 220 reach join records.
  - Zenodo deposit package updated to 7.7 MB.
- **Submission Prerequisite:**
  1. Resolve APC: Apply for institutional Read & Publish waiver for *Scientific Data*, or pivot to *Data in Brief*.
  2. Keep Zenodo in Draft during preparation; publish live record when journal review commences.
- **Verdict:** **HOLD UNTIL APC WAIVER / LIVE PUBLICATION TRIGGER**.

---

### Paper 1: Sediment Spatial Machine Learning & Risk Cartography
- **Target Journal:** *Science of The Total Environment* (STOTEN, Elsevier, IF 8.2, $0 APC).
- **Technical Vulnerability Uncovered:**
  - Standard 5-fold cross-validation achieves $R^2 = 0.52\text{--}0.64$, but reflects interpolation within monitored corridors where 74 of 133 records are co-located on 3 coordinates.
  - Strict Leave-One-River-Out (LORO) cross-validation drops to negative $R^2$ across all metals (Pb: -0.4567, Cr: -0.4386, Cd: -1.5201, Cu: -0.5804, Ni: -0.0063, As: -0.6278).
- **Required Overhaul:**
  1. The paper must not present the national 55.76% Very High Risk claim as a definitive deterministic truth.
  2. The paper must transparently present both the standard CV (interpolation within basins) and LORO CV (out-of-basin transferability limits), reframing the study as a pioneering demonstration of why hydraulic covariates alone cannot overcome localized industrial effluent clustering.
  3. Mask high-extrapolation reaches outside the training convex hull.
- **Verdict:** **NO-GO FOR IMMEDIATE SUBMISSION; COMPLETE VALIDATION RE-FRAMING FIRST**.

---

## 4. COPE Ethical Disclosure Language (For Cover Letters)

When submitting each manuscript, insert the following mandatory disclosure in the cover letter to prevent editorial concerns regarding concurrent companion submissions:

```markdown
### Related Submissions Disclosure (COPE Compliance)
This manuscript is part of an integrated, non-overlapping multi-publication research initiative investigating heavy metal contamination in the river systems of the Bengal Delta. Each contribution addresses a distinct scientific question and evaluates separate environmental matrices:

1. Flagship Review: "Can Published Evidence Support National-Scale Inference on Metal Contamination in Bangladesh's Rivers? A Critical Systematic Review and Evidence Map" (Under review at Environmental Research) — Evaluates evidence reliability, analytical comparability, and national surveillance gaps.
2. Water Quality Study: "Heavy Metals in Monitored River Corridors of Bangladesh: A Critical Synthesis of Regulatory Benchmark Discordance, Mathematical Index Damping, and Hydrographic Surveillance Deficits" (Submitted to Environmental Pollution) — Focuses exclusively on raw surface water chemistry, ECR 2023 potable regulatory screening, and HPI algebraic damping.
3. Data Infrastructure: "A Curated and Snapped Geospatial Database of Heavy Metal Concentrations in River Sediments and Waters Across Bangladesh" (In preparation for Nature Scientific Data) — Publishes the reusable multi-format relational database (SQLite, Parquet, GeoPackage).
4. Sediment ML Study: "River-Network-Informed Spatial Machine Learning and Spatial Transferability of Heavy Metal Contamination in River Sediments Across Bangladesh" (In preparation for STOTEN) — Focuses exclusively on bed sediment geostatistics, spatial cross-validation transferability limits, and stream-network machine learning.

None of the primary analytical results, figures, or mathematical derivations in this manuscript are duplicated in the companion works. Copies of companion manuscripts are available upon editorial request.
```
