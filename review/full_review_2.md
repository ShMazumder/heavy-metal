# **Brutal peer review:&#x20;**`ShMazumder/heavy-metal`

Not submission-ready

Review of the current default-branch repository

**Overall verdict: The research has a worthwhile foundation, but the repository currently makes claims that its own data, analysis code and validation evidence do not adequately support.**

This is no longer just a collection of preliminary experiments. There is substantial work here: 28-study literature compilation, a multi-matrix dataset, river-network processing, several analytical manuscripts, statistical outputs and supplementary materials. The separation of sediment contamination, surface-water screening, systematic synthesis and data publication is also a sensible research architecture.

However, the central problem is that **the research outputs look more mature than the underlying evidence chain**. The most serious weaknesses concern spatial validation, georeferencing completeness, statistical inference, reproducibility and overlap between manuscripts.

I reviewed the current `main` branch, including the README, manuscript sources, analysis scripts, processed CSVs, derived results, launch checklist and recent repository changes. The latest visible commit I examined was dated **21 November 2026**. I did not execute every analysis pipeline, inspect the SQLite database internally, or independently re-extract all 28 source publications. Consequently, this is a forensic review of the repository's current evidence and implementation—not a claim that every underlying source measurement has been independently verified.

## **1. Executive assessment**

| Research package                                       | Main contribution                                                          | Current verdict                                            |
| ------------------------------------------------------ | -------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Paper 1 — Spatial ML and sediment ecological risk      | HydroRIVERS-informed spatial prediction and national risk mapping          | **Reject / substantial methodological rebuild**            |
| Paper 2 — Surface-water synthesis and regulatory audit | Benchmark exceedance, HPI critique, seasonal and spatial coverage analysis | **Major revision**                                         |
| Paper 3 — Systematic review and meta-analysis          | Multi-matrix synthesis, meta-regression and surveillance analysis          | **Reject / rebuild systematic-review methodology**         |
| Paper 4 — Geospatial data descriptor                   | Harmonized and georeferenced river-water and sediment database             | **Major revision**                                         |
| Conference 1 — IGARSS                                  | River-network ML versus conventional geostatistics                         | Inherits Paper 1's validation and reproducibility problems |
| Conference 2 — Water conference                        | Water-quality screening and surveillance deficits                          | Inherits Paper 2's analytical limitations                  |

### **My subjective quality scores**

These are reviewer judgements, not calculated metrics.

| Dimension                           | Score |
| ----------------------------------- | ----- |
| Research ambition                   | 8/10  |
| Potential practical value           | 7/10  |
| Data-curation effort                | 7/10  |
| Novelty of the overall project      | 6/10  |
| Statistical methodological strength | 4/10  |
| Geospatial evidence quality         | 4/10  |
| Reproducibility from the repository | 2/10  |
| Current publication readiness       | 2/10  |

The main conclusion is not that the research is worthless. It is that **the claims need to be reduced or the evidence substantially strengthened before these manuscripts can withstand serious peer review.**

# **2. Critical problems across the entire research programme**

## **CRITICAL 1 — The central spatial ML results cannot currently be reproduced from the repository**

Major reproducibility blocker

Paper 1 is arguably the most technically ambitious manuscript. It compares Random Forest, XGBoost, LightGBM, CatBoost, Ordinary Kriging and Regression Kriging, then produces predictions for 55,668 river reaches.

Yet the current repository does not contain the corresponding end-to-end Paper 1 modelling pipeline.

The README claims that a `scripts/paper_1/` directory contains the sediment geospatial and ML modelling pipelines. However, that directory does not appear in the repository tree I inspected. A repository search for `CatBoostRegressor` and `train_test_split` also returned no matching implementation.

What is present includes derived outputs such as:

- `model_benchmark_all_metals.csv`
- `global_moran_results.csv`
- `shap_summary_metrics.csv`
- `national_river_reach_predictions_risk.csv`
- uncertainty summaries and publication figures

These are useful results, but they are not a substitute for the code that generated them.

**A reviewer should be able to answer:**

1. How were the features assembled for each metal?
2. Which observations were excluded and why?
3. How were missing values handled?
4. What were the exact model configurations and hyperparameters?
5. Was tuning nested inside the validation process?
6. How were the spatial folds created?
7. Were all transformations fitted exclusively on training data?
8. How were the final models trained and applied to the 55,668 reaches?
9. Can the reported results be reproduced from a clean environment?

At present, the repository does not let an independent researcher answer these questions for Paper 1.

Relevant files: [README](https://github.com/ShMazumder/heavy-metal/blob/main/README.md?utm_source=chatgpt.com) · [benchmark results](https://github.com/ShMazumder/heavy-metal/blob/main/data/derived/paper_1/phase_v_results/model_benchmark_all_metals.csv?utm_source=chatgpt.com)

**My verdict:** This alone is sufficient reason to reject Paper 1 in its current form. Restore or reconstruct the complete modelling pipeline before treating the reported performance as publication-grade evidence.

## **CRITICAL 2 — The claimed spatial validation is not convincingly demonstrated**

Potentially invalid performance estimates

Paper 1 says that the models were evaluated using five-fold spatial cross-validation.

But the Markdown manuscript describes the fold procedure as:

> Data folds were partitioned with fixed random seed stratification to ensure identical training and evaluation subsets across all seven algorithms.

This is a serious methodological concern.

A fixed random seed makes an experiment repeatable. Stratification helps preserve a target distribution across folds. **Neither, by itself, establishes spatial separation.**

For spatially clustered environmental datasets, random partitioning can place observations from the same river, study, sampling campaign or even physical location in both training and test sets.

That can produce an overly optimistic estimate of performance.

The problem is particularly important here because the sediment dataset contains repeated and geographically clustered observations. In the supplied `sediment_features_hydro.csv`, 133 records have geospatial features, but those records contain only 36 distinct coordinate pairs and 33 distinct HydroRIVERS identifiers.

Consequently, the nominal model sample size may substantially overstate the number of independently represented spatial locations.

### **What I would demand as a reviewer**

Re-run the full benchmark using at least three validation strategies:

| Validation strategy           | What it tests                                            |
| ----------------------------- | -------------------------------------------------------- |
| Random five-fold CV           | Conventional interpolation performance                   |
| Spatial block CV              | Generalization to geographically separated areas         |
| Leave-one-river-system-out CV | Generalization to an unseen river system                 |
| Leave-one-study-out CV        | Generalization beyond the source-study sampling patterns |

I would place particular emphasis on leave-one-study-out and leave-one-river-out testing.

A model that predicts another observation from a river already represented in training is not necessarily capable of predicting contamination in an unsampled river system.

**Do not continue describing the model as nationally generalizable until these tests have been completed.**

Relevant file: [Paper 1 manuscript](https://github.com/ShMazumder/heavy-metal/blob/main/manuscripts/paper_1_stoten/manuscript_paper_1.md?utm_source=chatgpt.com)

## **CRITICAL 3 — Georeferencing coverage is substantially weaker than the manuscript presentation suggests**

Data-integrity concern

This is one of the most important findings in the repository review.

Paper 4 repeatedly presents the dataset as a harmonized, georeferenced and topologically snapped database. The manuscripts also describe the station snapping success rate and average offset.

However, the actual processed files show a more complicated picture.

**Station register —&#x20;**`stations.csv`

# **426**

Rows in the station register

Coordinate-resolved rows

**220**

Unresolved rows

**206 (48.4%)**

**Sediment feature table**

Total records

**289**

Records with geospatial features

**133**

Records missing those features

**156 (54.0%)**

The 133 coordinate-populated rows contain only 36 distinct coordinate pairs in the supplied feature table. This needs reconciliation with the manuscript's description of 133 unique station centroids.

**Water feature table**

Total records

**268**

Records with geospatial features

**171**

Records missing those features

**97 (36.2%)**

There may be legitimate reasons for unresolved coordinates. Some publications may report only approximate station descriptions, some locations may be repeated across years, and some records may not be relevant to every spatial analysis.

But the manuscript must distinguish:

- unique physical sampling locations;
- station identifiers;
- station-year-season records;
- coordinate-resolved records;
- HydroRIVERS-matched records;
- records excluded from spatial modelling.

These are different denominators.

The current presentation makes it too easy to interpret the reported snapping statistics as applying to the complete dataset.

### **Required correction**

Provide a georeferencing audit table with one row per source station, containing:

`Study_ID`, `Station_ID`, `Station_No`, original location text, original coordinates, corrected coordinates, coordinate provenance, confidence category, matched `HYRIV_ID`, snapping distance and resolution status.

Then report exact counts at each stage.

Do not quietly discard the 206 unresolved station-register rows, and do not describe the entire collection as georeferenced if a substantial proportion remains unresolved.

Relevant files: [stations.csv](https://github.com/ShMazumder/heavy-metal/blob/main/data/processed/stations.csv?utm_source=chatgpt.com) · [sediment features](https://github.com/ShMazumder/heavy-metal/blob/main/data/processed/sediment_features_hydro.csv?utm_source=chatgpt.com) · [water features](https://github.com/ShMazumder/heavy-metal/blob/main/data/processed/water_features_hydro.csv?utm_source=chatgpt.com)

## **CRITICAL 4 — The systematic review is not yet sufficiently auditable as a PRISMA review**

Paper 3 claims compliance with PRISMA 2020.

The flow counts are arithmetically consistent:

| Screening stage           | Records |
| ------------------------- | ------- |
| Identified                | 1,420   |
| Duplicates removed        | 582     |
| Titles/abstracts screened | 838     |
| Excluded                  | 764     |
| Full texts assessed       | 74      |
| Full texts excluded       | 46      |
| Studies included          | 28      |

That is a good starting point. But a correct flow diagram does not, by itself, make a systematic review reproducible.

The current manuscript does not provide enough information to independently reconstruct the literature search and screening process.

Important omissions include:

- Full search syntax separately for each database.
- Exact date of the last search in each database.
- Database-specific identification counts.
- A complete record-level deduplication and screening audit.
- The list of 46 excluded full-text publications and their individual exclusion reasons.
- Number of reviewers involved in title/abstract screening and full-text screening.
- Whether screening was independent or performed by one researcher.
- How reviewer disagreements were resolved.
- An explicit risk-of-bias or study-quality assessment suitable for this synthesis.

PRISMA 2020 explicitly requires transparent reporting of database sources, dates, complete search strategies, reviewer processes, data collection and risk-of-bias methods.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://pmc.ncbi.nlm.nih.gov\&sz=32)

PMC



There are also inconsistencies in the stated search coverage and temporal window across the manuscripts. For example, Paper 3 describes searching through 31 March 2025, while other manuscript methods describe a 2010–2024 search window or a March 2024 cutoff. Database lists also vary between manuscripts.

These differences need to be resolved, not left to editorial interpretation.

**My verdict:** Paper 3 currently reads more like a substantial retrospective evidence synthesis than a fully reproducible systematic review. Either complete the systematic-review reporting and screening audit or reposition the paper more modestly.

# **3. Paper-by-paper review**

## **Paper 1 — Spatial modelling and ecological risk assessment**

[Open Paper 1](https://github.com/ShMazumder/heavy-metal/blob/main/manuscripts/paper_1_stoten/main.tex?utm_source=chatgpt.com)

Reject / substantial rebuild

### **What is genuinely promising**

The core idea is worth pursuing: river sediment contamination is not simply a continuous planar interpolation problem. The use of HydroRIVERS attributes such as upstream area, stream order, discharge and distance to river outlet provides a potentially useful way to incorporate hydrographic context into environmental prediction.

The model benchmark also presents an interesting result:

| Metal | Model highlighted in results | Reported \\(R^2\\) | Test observations |
| ----- | ---------------------------- | ------------------ | ----------------- |
| Pb    | CatBoost                     | 0.6393             | 132               |
| Cr    | CatBoost                     | 0.5201             | 131               |
| Cd    | CatBoost                     | 0.5689             | 132               |
| Cu    | Ordinary Kriging             | 0.5267             | 82                |
| Ni    | Ordinary Kriging             | 0.6118             | 82                |
| As    | LightGBM                     | 0.3713             | 127               |

These numbers do not describe a uniformly strong model. In particular, the Arsenic result on the native scale is modest, and the Ni/Cu results are based on substantially fewer observations than the headline database size of 289.

The manuscript should make the per-metal effective sample sizes prominent.

### **Major problem: 55,668 predictions are being given national significance without sufficient validation**

The manuscript applies the models to 55,668 HydroRIVERS reaches and concludes that **55.76% are in the Very High Ecological Risk class**.

This is an exceptionally consequential conclusion.

Yet the available uncertainty summary provides estimates only for Pb, Cr and Cd:

| Metal | Mean coefficient of variation | Reaches with CV above 0.5 |
| ----- | ----------------------------- | ------------------------- |
| Pb    | 0.364                         | 19.34%                    |
| Cr    | 0.438                         | 38.42%                    |
| Cd    | 0.385                         | 23.49%                    |

The paper's ecological risk index uses six metals. The repository output I inspected does not provide a corresponding six-metal uncertainty assessment or propagate prediction uncertainty into the final RI classifications.

This is not a minor reporting omission.

The risk index is a weighted combination of predicted concentrations. If uncertainty in individual metal predictions is substantial, then a reach classified just above the RI threshold of 600 may not reliably belong in the Very High Risk category.

I would require:

1. Prediction uncertainty for all six metals.
2. Uncertainty propagation through \\(CF_i\\), \\(E_r^i\\) and RI.
3. Probability of each reach belonging to each risk class.
4. An extrapolation or out-of-domain indicator.
5. A map showing where the model is predicting beyond the geographical support of the training observations.

Instead of reporting only “55.76% of reaches are Very High Risk,” report something like:

> Estimated proportion of reaches exceeding RI = 600, with uncertainty intervals and the percentage of reaches for which the classification is robust.

### **Ecological interpretation is too strong**

The paper uses Hakanson's potential ecological risk index and UCC background values.

That is a legitimate screening framework, but the results do not directly demonstrate:

- Benthic community collapse.
- Actual ecological toxicity at individual reaches.
- Bioaccumulation in fish.
- Human exposure through fish consumption.
- The effectiveness or necessity of dredging.

An RI classification is not equivalent to a field-verified ecological-impact assessment.

You need biological or ecotoxicological evidence before making those claims. At minimum, describe RI as a **potential ecological risk screening indicator**, not proof of biological damage.

The use of one continental crust reference across diverse deltaic sediment types also requires stronger justification. Local geogenic backgrounds, grain-size composition and digestion protocols can materially alter enrichment estimates.

### **SHAP is not a causal mechanism**

The manuscript interprets features such as pH, longitude and upstream area as environmental drivers.

TreeSHAP explains how features influence a fitted model. It does not prove the geochemical mechanisms described in the discussion.

Longitude may capture geographical clustering, study selection and the concentration of published measurements around industrial rivers. Catchment area may act as a proxy for other unmeasured factors.

Rephrase the claims as model-attribution findings and distinguish them from independently established environmental mechanisms.

### **Moran's I reporting needs correction**

The repository contains extremely small analytical p-values, such as \\(p \approx 9.97 \times 10^{-75}\\) for log-transformed Arsenic.

But the manuscript also refers to 999 permutation tests and says the empirical permutation results were \\(p \leq 0.001\\).

These are two different inferential results:

- Asymptotic normal p-values derived from the z-score.
- Empirical permutation p-values with a finite number of permutations.

With 999 permutations, the empirical p-value cannot justify a claim of \\(10^{-75}\\).

Report the asymptotic and permutation results separately. Do not present the asymptotic p-value as though it were obtained from the permutation experiment.

### **Paper 1 verdict**

The study has a potentially publishable research question, but the present version makes its strongest claim—the national risk map—before establishing reliable spatial generalization and uncertainty.

I would not send this to STOTEN in the current form.

## **Paper 2 — Surface-water synthesis and regulatory benchmark audit**

[Open Paper 2](https://github.com/ShMazumder/heavy-metal/blob/main/manuscripts/paper_2_environmental_pollution/main.tex?utm_source=chatgpt.com)

Major revision

This is arguably the most defensible manuscript in the current collection.

### **What works well**

There are several good decisions here.

**First, the paper separates water chemistry from sediment chemistry.** That avoids a major conceptual error common in environmental synthesis.

**Second, it examines different operational fractions.** The dedicated analysis of confirmed 0.45 µm-filtered records is particularly valuable.

**Third, it recognises study clustering.** The use of study-level resampling is preferable to treating every published measurement as fully independent.

**Fourth, the seasonal analysis has appropriate caution.** The paired within-study estimates use small numbers of studies, and the HKSJ confidence intervals cross unity for every metal. The manuscript acknowledges that the evidence is insufficient to claim statistically significant within-study seasonal differences.

That restraint should be preserved.

### **Major problem: drinking-water exceedance is not the same as river-water legal non-compliance**

The manuscript compares raw river-water measurements against WHO drinking-water guideline values and Bangladesh ECR 2023 potable-water standards.

The numerical comparison is useful, but the regulatory interpretation must be precise.

The official ECR 2023 Schedule 2 distinguishes **surface-water standards** from a separate **potable/drinking-water standards** section.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://file-chittagong.portal.gov.bd\&sz=32)

file-chittagong.portal.gov.bd+4



Therefore, comparing raw river-water concentrations against potable-water thresholds is a useful screening exercise for potential treatment burdens. It does not automatically establish that the river itself violates the statutory standards applicable to its surface-water use category.

The paper should consistently distinguish:

- Raw surface-water quality.
- Drinking-water treatment requirements.
- Potable-water guideline exceedance.
- Legal compliance with the applicable surface-water category.

For example, the result that 85.6% of Pb records exceed 0.010 mg/L is informative as a drinking-water screening result. It should not be interpreted as 85.6% of river-water samples violating the river's legal ambient standard.

### **The 85.6% headline needs an estimand explanation**

The Pb estimate is based on 146 records from 10 studies. Its reported statistics are:

- Median: 0.0286 mg/L.
- Exceedance: 85.6%.
- Cluster-bootstrap CI: [71.1–94.3%].
- Random-effects pooled proportion: 79.9%.

Those are meaningful findings, but the raw-record proportion weights studies according to their number of reported observations.

Some studies contribute many more records than others. For example, the water data contain studies with 60, 30 and 20 records, alongside studies with only a handful.

The manuscript needs to state clearly what the headline percentage estimates:

1. The proportion of all compiled measurements exceeding a benchmark; or
2. The average prevalence across studies.

These are not equivalent.

I would report both a record-weighted pooled proportion and a study-level synthesis, with the intended estimand clearly stated.

### **HPI critique: valuable, but not sufficient as a central scientific contribution**

The algebraic discussion of inverse-standard weighting is worthwhile.

The Prasad–Bose formulation uses inverse-standard weights and a standardised sub-index. This produces numerator contributions proportional to \\(M_i/S_i^2\\), which can structurally emphasise low-standard metals.

That is an interesting methodological warning.

However, the HPI analysis should not be presented as though the discovered panel invariance establishes a new environmental phenomenon. It primarily demonstrates a mathematical property of the index.

The paper would be stronger if it compared HPI against alternative index formulations and conducted a transparent sensitivity analysis over reference standards, metal panels and concentration distributions.

### **Spatial null-model reporting contains a concrete error**

The spatial coverage script performs 1,000 Monte Carlo simulations.

The results CSV reports an empirical p-value of `0.0000 (p < 0.0001)`.

That level of precision is not justified by 1,000 simulations. Even with zero simulated values as extreme as the observed result, a conventional finite-simulation correction gives a minimum p-value of approximately \\(1/1001\\), not below 0.0001.

There is also an output-label inconsistency:

- The summary reports 23 unique sampling coordinates.
- The CSV labels its null-model comparison as “24 Random Sites”.
- The code actually uses `n_station_points` dynamically, despite a comment referring to 24 points.

This is straightforward to correct, but it indicates that derived tables should receive a final automated consistency audit.

### **WHO citation needs updating**

The manuscript refers to the WHO Guidelines for Drinking-water Quality, fourth edition with 2022 addenda. WHO has since published the fourth edition incorporating the first, second and third addenda, dated **17 June 2026**. Update the reference if the paper is claiming to use the latest WHO guidance. This does not, by itself, mean the metal-specific benchmark values used in the paper have changed.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.who.int\&sz=32)

who.int



### **Paper 2 verdict**

This paper has a coherent research question and a reasonably promising analytical structure. Its biggest improvements are interpretive and statistical rather than requiring an entirely new project.

I would recommend major revision rather than rejection, provided the authors correct the legal interpretation, define the estimands and strengthen the study-level analysis.

## **Paper 3 — Systematic review and meta-analysis**

[Open Paper 3](https://github.com/ShMazumder/heavy-metal/blob/main/manuscripts/paper_3_systematic_review/main.tex?utm_source=chatgpt.com)

Reject / methodological rebuild

This paper has the largest gap between its stated methodological identity and what the analysis actually implements.

### **Major problem: the meta-regression is not a conventional study-level meta-regression**

This is the most serious statistical issue in Paper 3.

The script `run_systematic_review_meta_regression.py` imports scikit-learn's `LogisticRegression` and fits a pooled record-level logistic regression.

The model is fitted on individual observations using:

- Instrument sensitivity.
- Urban corridor membership.
- Dry season.
- Pre-monsoon season.

Study IDs are then used for bootstrap resampling.

That is not the same as fitting a conventional random-effects meta-regression with study-level effect estimates or a multilevel model with study-specific random effects.

The bootstrap attempts to account for clustering at the study level, which is a useful step. But it does not change the fact that the point-estimate model is fitted to pooled records and does not explicitly model study-level heterogeneity or repeated sampling locations.

I would describe the existing implementation as a **pooled record-level logistic analysis with study-cluster bootstrap uncertainty**, not a conventional meta-regression.

You have two defensible options:

**Option A — Multilevel model**

Use a hierarchical logistic model with study-level random effects, and a suitable structure for repeated station-level observations where the data support it.

**Option B — Study-level meta-analysis**

Calculate study-specific effect estimates, then pool them using a justified random-effects meta-analytic framework.

The current script should not be presented as though it has already solved these problems.

### **The strongest highlighted finding is weak**

Paper 3 highlights the Chromium dry-season result:

\\[ OR = 2.77,\quad 95\\%\\,CI=[1.15,28.54],\quad p=0.026 \\]

The point estimate is interesting, but the confidence interval is extremely wide.

Additionally, the manuscript evaluates several metals and multiple predictors. The reported p-value is nominal, and there is no clear multiple-testing correction for the collection of meta-regression comparisons.

The other large odds ratios are not statistically convincing:

| Element / predictor | OR    | 95% CI        | p-value |
| ------------------- | ----- | ------------- | ------- |
| Cd — Urban corridor | 10.79 | [0.31–623.07] | 0.140   |
| Cd — Pre-monsoon    | 6.58  | [0.41–62.11]  | 0.325   |
| As — Pre-monsoon    | 5.67  | [0.12–144.70] | 0.300   |
| Pb — Dry season     | 4.71  | [0.63–63.72]  | 0.108   |

These are exploratory estimates with substantial uncertainty. They do not justify the manuscript's stronger language about hydrological or industrial effects.

In particular, the Arsenic pre-monsoon result is described as an irrigation-pumping effect even though the reported regression estimate is not statistically significant.

A plausible environmental mechanism is not proof that the mechanism explains the observed data.

### **The predictor definitions are too crude for the interpretation**

The code defines urban status by membership in a fixed list of rivers:

`Buriganga`, `Turag`, `Shitalakhya`, `Dhaleshwari`, `Balu`, and `Karnaphuli`.

This is a river-category proxy, not a measured industrial exposure variable.

Similarly, the high-sensitivity variable is assigned from instrument-name keywords. Yet the manuscript describes sensitivity in terms of detection limits below 0.001 mg/L. The code does not demonstrate that this detection-limit classification was performed using record-level LOD data.

The model is therefore not measuring industrial exposure or analytical sensitivity as precisely as the manuscript suggests.

### **Season coding needs a more explicit design**

The code constructs only two seasonal indicator variables: dry and pre-monsoon.

Consequently, the reference category includes wet-season records and any observations classified as post-monsoon or unclassified. Those categories are not necessarily interchangeable.

For a seasonal model, I would define a mutually exclusive categorical variable, explicitly exclude observations with unclear season, and state the reference category.

### **Systematic-review reporting still needs substantial work**

Beyond the PRISMA flow counts, the manuscript needs the complete search and screening audit described earlier.

It also needs to distinguish:

- Study-quality appraisal.
- Extraction concordance.
- Analytical measurement quality.
- Risk of bias in the evidence synthesis.

A transcription audit is valuable, but it is not a substitute for assessing the reliability and limitations of the underlying studies.

### **Paper 3 verdict**

I would not submit this as a PRISMA-compliant systematic review to *Environment International* in the current form.

The descriptive synthesis is potentially useful. The review methodology, meta-regression and inferential claims require substantial rebuilding.

## **Paper 4 — Data descriptor**

[Open Paper 4](https://github.com/ShMazumder/heavy-metal/blob/main/manuscripts/paper_4_data_descriptor/main.tex?utm_source=chatgpt.com)

Major revision

This may become an important contribution, but data descriptors are judged by whether the dataset is complete, accessible, documented and independently reusable.

A dataset that is partly georeferenced can still be valuable. A dataset that is described as completely georeferenced when a substantial portion is unresolved is not adequately described.

### **Main concern: the claims about geospatial completeness are too broad**

The manuscript says all stations were georeferenced and snapped to HydroRIVERS.

The actual station register contains 206 unresolved rows out of 426. The sediment and water feature tables also contain substantial missing geospatial information.

The paper must state exactly which subset received coordinate validation and river-network snapping.

### **The paper has two versions with inconsistent metadata**

The Markdown manuscript describes `stations.csv` as containing 133 rows, whereas the current LaTeX manuscript's data manifest describes 426 rows.

This matters because the Markdown copy is not just an editorial draft; it is part of the repository's manuscript package.

The source files should be harmonised, and one should be designated as the canonical manuscript source.

### **Claimed Parquet availability is not demonstrated in GitHub**

The paper advertises CSV, SQLite, Parquet and GeoPackage formats. I could not find any `.parquet` files in the current GitHub tree.

The Parquet files may exist in the Zenodo archive, but that needs to be demonstrated through a public download manifest and checksum list.

There is also an availability conflict in your repository: the launch checklist says to keep the Zenodo deposit in **Draft** until other papers are under journal review, while the manuscript says the complete dataset is publicly accessible without restriction.

Unless the deposit has since been published, those statements cannot both be correct.

### **The data dictionary is insufficiently auditable**

The paper describes a rich relational schema with study-level information, digestion methods, certified reference materials, blanks, replicates, LODs and other quality-control metadata.

However, the visible `studies.csv` export has only eight columns, and the flat-file exports do not make all the claimed provenance and QA/QC fields easy to audit.

The data descriptor needs a definitive data dictionary showing every field, unit, permitted value, missing-value meaning, provenance and table relationship.

I could not inspect the SQLite binary internally through the repository text interface, so I am not claiming that every field is absent from the database. I am saying that the exported data and documentation do not make the full metadata structure sufficiently transparent.

### **Paper 4 verdict**

The dataset could become independently publishable. But its description must match the actual data, and the release must be genuinely accessible and reproducible.

# **4. Cross-paper publication risk: are there too many manuscripts from one dataset?**

This is an important editorial issue.

The four papers are not independent research projects. They use overlapping subsets of the same 28-study evidence base.

**Shared evidence base**

# **28 studies · 557 records**

The repository's combined literature database

Sediment: 289 records

**Paper 1 / Paper 3 / Paper 4**

Water metals: 162 records

**Paper 2 / Paper 3 / Paper 4**

Bulk water chemistry: 106 records

**Paper 3 / Paper 4**

There is a legitimate publication strategy here:

- Paper 1: spatial prediction of sediment contamination.
- Paper 2: raw-water screening, benchmark discordance and surveillance gaps.
- Paper 3: systematic evidence synthesis across media.
- Paper 4: reusable data infrastructure.

But Paper 3 repeats important results from Papers 1 and 2, including the sediment enrichment findings, water benchmark exceedance figures, HPI critique and spatial coverage statistics.

The manuscripts need a much clearer contribution boundary.

### **My concern**

Paper 3 currently risks looking like a larger combined version of Papers 1 and 2 rather than an independently justified systematic-review contribution.

The conference papers also appear to be derived from the journal-paper analyses. That is not automatically inappropriate, but the relationship must be disclosed and the publications must contain genuinely distinct contributions.

**Recommendation:** Create a contribution matrix listing, for every paper, the unique research question, unique analyses, unique tables/figures, reused dataset components and reused text. Cross-cite related work where appropriate and disclose related submissions to editors.

# **5. Submission-readiness and repository-quality problems**

These are not scientific findings, but some are fatal to submission.

### **Author placeholders remain**

The launch checklist itself acknowledges that manuscripts still contain:

- Author One / Author Two / Author Three.
- University Name.
- `author.one@university.edu`.
- Placeholder ORCID information.

The README currently labels the papers “Ready”. That status is misleading.

### **Internal LLM reviews are not external peer review**

The publication checklist explicitly states that the reviews stored under the Paper 2 review history are internal LLM peer reviews, not actual journal reviews.

That is fine as an internal quality-control process. But those reviews should not be presented as independent external validation.

### **Reproducible environment is not frozen**

The `requirements.txt` file uses minimum-version constraints such as `numpy>=...` and `scikit-learn>=...`.

This is insufficient for exact reproduction of numerical results across changing library versions.

Use a lock file or a fully pinned environment and record the Python, GDAL, PROJ, scikit-learn, CatBoost, LightGBM and XGBoost versions used for the final published results.

### **The manuscript package needs one canonical source**

The Markdown and LaTeX versions have already drifted. The latest changes updated one version of the Paper 4 manifest without fully updating the other.

Use a controlled source-generation workflow, or at minimum add an automated consistency check for:

- Study counts.
- Record counts.
- Unique stations.
- Georeferencing denominators.
- Benchmark values.
- Statistical results.
- Figure and table versions.
- Data availability statements.

Relevant file: [publication launch checklist](https://github.com/ShMazumder/heavy-metal/blob/main/docs/publication_launch_checklist.md?utm_source=chatgpt.com)

# **6. Priority remediation plan**

I would not spend the next development cycle polishing figures or improving the manuscript language. The underlying evidence should be fixed first.

| Priority | Required work                                                                                        | Why it matters                                                             |
| -------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **P0**   | Restore Paper 1's full modelling and prediction pipeline                                             | The most important ML findings are currently unverifiable                  |
| **P0**   | Resolve and audit station georeferencing, including repeated coordinates and unresolved records      | The spatial support of the entire project is uncertain                     |
| **P0**   | Rebuild Paper 1 validation using spatial blocks, leave-one-river-out and leave-one-study-out testing | Current performance claims do not establish geographical generalization    |
| **P0**   | Rebuild Paper 3's inferential model and correct its meta-regression description                      | Current effect estimates are too weak for the causal/mechanistic narrative |
| **P1**   | Complete PRISMA search, screening, exclusion and study-quality documentation                         | Necessary to defend Paper 3 as a systematic review                         |
| **P1**   | Correct Paper 2's regulatory framing and Monte Carlo p-value reporting                               | Prevents misleading compliance claims and statistical reporting            |
| **P1**   | Propagate uncertainty into Paper 1's six-metal RI estimates                                          | The national risk-classification result needs defensible uncertainty       |
| **P1**   | Publish and verify all Paper 4 data formats and metadata                                             | The data descriptor depends on actual independent access                   |
| **P2**   | Harmonise all manuscript copies, author details and submission packages                              | Prevents avoidable editorial rejection                                     |
| **P2**   | Freeze dependencies and add clean-run reproduction tests                                             | Makes the results independently reproducible                               |

## **The three most important experiments to perform next**

**Experiment A — Spatial generalization test**

Take Paper 1 and run:

1. Random five-fold CV.
2. Spatial block CV.
3. Leave-one-river-out CV.
4. Leave-one-study-out CV.

Report all model metrics side by side. This experiment may materially change the conclusions, but it will tell you whether the work is genuinely a national spatial modelling contribution or primarily an interpolation study.

**Experiment B — Geospatial audit and effective sample size**

Create one authoritative station register. Resolve coordinate provenance and duplicate locations. Then calculate the effective number of distinct coordinate pairs, unique river reaches, source studies and river systems for every model.

This is essential before any model is trained or validated again.

**Experiment C — Rebuild Paper 3's water meta-regression**

Compare three approaches:

- Current pooled record-level logistic regression.
- Mixed-effects logistic regression with study-level random effects.
- Study-level pooled effect estimates.

Use explicit season categories, a defensible instrument-quality variable and correction for multiple testing. Then determine whether the Chromium dry-season result survives.

# **7. What I would preserve**

Despite the critical findings, I would not abandon the project.

There are several genuinely useful pieces of work here:

1\. **The curated Bangladesh river-metal evidence base.** Consolidating published sediment and water observations into structured formats is a valuable contribution, even before the national modelling claims are established.

2\. **The distinction between sediment contamination and raw-water screening.** The separate research questions are scientifically sensible.

3\. **The attention to measurement fractions and instrumental sensitivity.** The filtered dissolved subset and the comparison of analytical methods are particularly useful.

4\. **The HPI mathematical critique.** This is a worthwhile methodological warning and can improve environmental-index interpretation.

5\. **The river-network surveillance analysis.** The finding that the published evidence is spatially concentrated deserves further investigation, although the coverage model and null test need refinement.

6\. **The willingness to maintain multiple manuscript packages and derived outputs.** The repository has a stronger research-engineering structure than many early-stage academic projects.

# **8. Final editorial recommendation**

My recommended order of publication effort would be:

**First: Paper 2**

Best current candidate

The most defensible analytical narrative. Correct the regulatory interpretation, estimands and spatial null-model reporting, then submit.

**Second: Paper 4**

Fix georeferencing completeness, reconcile the station counts, document the full schema and verify that the data deposit is publicly accessible.

**Third: Paper 1**

Rebuild the modelling pipeline and validation. Do not preserve the national 55.76% risk conclusion as a headline until the six-metal uncertainty and out-of-domain issues are resolved.

**Fourth: Paper 3**

Rebuild the systematic-review audit and meta-regression. Its contribution should be clearly distinguished from Papers 1 and 2.

**My final assessment:** The repository contains a potentially valuable environmental research programme, but I would not consider the four papers or the two conference packages submission-ready today. Paper 2 is the closest to a defensible manuscript. Paper 4 could become a useful data publication. Papers 1 and 3 need deeper methodological work—not merely another round of writing and statistical presentation.

The most dangerous outcome would be to submit Paper 1 with its current national risk map and discover, during peer review, that the model's apparent spatial performance depends on repeated locations or source-study patterns that were not properly held out.

**Fix the evidence chain before polishing the claims.**

**Repository files that deserve immediate attention:** [Paper 1 benchmark](https://github.com/ShMazumder/heavy-metal/blob/main/data/derived/paper_1/phase_v_results/model_benchmark_all_metals.csv?utm_source=chatgpt.com) · [Paper 1 spatial features](https://github.com/ShMazumder/heavy-metal/blob/main/data/processed/sediment_features_hydro.csv?utm_source=chatgpt.com) · [Paper 2 analysis code](https://github.com/ShMazumder/heavy-metal/blob/main/scripts/paper_2/reproduce_paper_2_results.py?utm_source=chatgpt.com) · [Paper 3 meta-regression code](https://github.com/ShMazumder/heavy-metal/blob/main/scripts/paper_3/run_systematic_review_meta_regression.py?utm_source=chatgpt.com) · [Paper 4 data descriptor](https://github.com/ShMazumder/heavy-metal/blob/main/manuscripts/paper_4_data_descriptor/main.tex?utm_source=chatgpt.com)