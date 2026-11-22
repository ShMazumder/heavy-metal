Latest repository review — 22 November 2026
Latest HEAD verified
Not publication-ready

I checked the repository again from its current default branch, rather than relying on the previous review.

Repository: ShMazumder/heavy-metal
Branch: main
Latest commit: b7340516ad8d
Commit time: 22 November 2026, 05:20 UTC (11:20 Bangladesh time)

The latest work is meaningful. In particular, you have added a documented extraction-evidence matrix, rebuilt Paper 3 around five research questions, introduced an eight-domain appraisal pipeline, and made the negative Leave-One-River-Out (LORO) results more visible.

However, the repository still has important data-integrity, methodological, and publication-readiness problems. Some of the updated manuscripts make claims that their own data or code do not adequately support.

This is a source-level forensic review of the current repository, including its code, manuscripts and processed CSV files. I could not execute the full research pipelines or independently re-extract the 28 source PDFs in this review, so I am not certifying the underlying published measurements.
1. Overall assessment
Component	Current assessment	My verdict
Paper 1 — Sediment ML	LORO exposes serious transferability limitations; some manuscript conclusions remain inconsistent with the validation results	No-go
Paper 2 — Surface-water synthesis	Strongest and most developed manuscript; important spatial and cross-paper consistency issues remain	Conditional
Paper 3 — Systematic review	Better research positioning, but appraisal, PRISMA reproducibility, spatial denominators and overlap need further work	Rebuild
Paper 4 — Data descriptor	Useful data infrastructure, but station identity, provenance and schema claims need correction	Hold
Conference papers	Substantial overlap with the journal papers needs to be addressed	Reassess
Repository reproducibility	Improved scripts and evidence files, but no complete end-to-end reproduction or adequate automated testing	Incomplete

The newer internal readiness audit is much more realistic than the README. The audit correctly identifies Paper 3 as needing rebuilding and Paper 1 as unsuitable for immediate submission.

The README still describes all six deliverables as Ready. That is no longer defensible.

2. Critical findings
Finding 1 — The station database has an identity problem
Critical — data architecture
This is one of the most important findings from the current data.

I checked the following files together:
- stations.csv
- water_data.csv
- sediment_data.csv
- station_hydrorivers_matched.csv
The actual counts are:
Metric	Count
Rows in station register	426
Rows with coordinates	220
Unique Station_ID values	213
Georeferenced Station_ID values	81
Unique coordinate pairs in the register	54
Rows in HydroRIVERS matching file	220
Unique Station_ID values in matching file	81

The distinction matters. The 220 records are not 220 independent geographic locations. They include repeated observations across seasons and years, and sometimes repeated coordinates.

More seriously, I found actual station identifier collisions across different rivers.

For example:
- P08_S1 is used for five different rivers: Buriganga, Karnaphuli, Padma, Meghna and Shitalakhya.
- P04_S1 through P04_S5 are used for both Buriganga and Turag.
The water dataset contains coordinates for all five P08 river locations, but the station register contains only the Buriganga entries for P08_S1. The four other river locations are absent from the register.

Similarly, the P04 Turag records do not have separate entries in the station register.

When I reconcile the records using (Study_ID, River, Station_No), I find:
9
Distinct study–river–station combinations missing from the station register

Five P04 Turag stations and four additional P08 river locations.

This is not merely a presentation problem. A normalized database cannot safely use the current Station_ID as a unique station key.

Required correction: Introduce a stable station identifier that is unique per actual location, with a key such as:

Study_ID + River + Station_No

Separate the physical station from its sampling events. Keep year, season and assay information in observation tables, rather than allowing repeated observations or reused identifiers to masquerade as independent stations.

Also audit the suspicious within-study coordinate repetition in P14, P18 and P28. Multiple station identifiers in each of these studies share the same coordinate pair. This might reflect source limitations or coordinate approximation, but it needs source-level verification before being described as GPS precision.

Impact: Paper 3's spatial appraisal, Paper 4's database architecture, Paper 1's spatial validation and Paper 2's coverage analysis all depend on this information.

Finding 2 — The 16.5% spatial coverage result has a population-definition mismatch
Critical — denominator consistency
The 16.5% result is one of the central findings of this research. However, different repository documents describe its underlying population differently.

The actual calculation in reproduce_paper_2_results.py uses the georeferenced coordinates from the surface-water records containing at least one trace metal, deduplicated by coordinate.

I independently checked the corresponding dataset:
- 162 surface-water trace-metal records.
- 99 georeferenced trace-metal records.
- 37 distinct Station_ID values among those georeferenced records.
- 23 unique coordinate pairs.
The derived spatial summary also explicitly records 23 sites.

Yet Paper 3 describes 220 coordinate-resolved stations as the input to the national spatial coverage assessment.

These are different populations.
23
Unique coordinates actually used in Paper 2's coverage calculation

220
Coordinate-resolved event rows in the combined station register

The second number is not the denominator used to calculate the published 16.5% result.

The result itself may remain valid for the 23-point surface-water subset. The problem is the inconsistent explanation of what it represents.

Required correction:
1. Define the spatial population precisely.
2. State whether the analysis represents surface-water metal sampling, sediment sampling, or combined monitoring.
3. Reconcile coordinates using the corrected station identities.
4. Recalculate the 10 km, 25 km and 50 km coverage estimates for each appropriate population.
5. Recompute the Monte Carlo null model with the same sampling unit and a defensible spatial sampling design.
Do not simply replace 23 with 220. The georeferenced rows are not independent locations.

The current 16.5% figure should be described as coverage by the 23 unique coordinates in the georeferenced surface-water heavy-metal subset, until the broader analysis is properly reconstructed.

Finding 3 — Paper 3 still overlaps substantially with Paper 2
Critical — publication ethics and contribution separation
The updated cross-manuscript audit establishes a contribution boundary:
Paper 3 must not reproduce Paper 2's detailed HPI mathematical derivation.

But the current Paper 3 manuscript still contains:
- The full HPI equation.
- The \(1/S_i^2\) quadratic weighting derivation.
- The 60.2% Cd and 18.1% Pb weight calculations.
- The combined 78.3% weight result.
- The 77.1% realized score contribution.
- The same-subset Core-4, Core-5 and All-7 HPI comparisons.
These are also central results of Paper 2.

There is also a direct figure duplication:
File	SHA
Paper 2 fig3_spatial_coverage_map.png	498c6c5a775ca37dcb6b7a87616bb95c6783064f
Paper 3 fig3_spatial.png	498c6c5a775ca37dcb6b7a87616bb95c6783064f

These are byte-for-byte identical files.

That contradicts the cross-manuscript audit's claim that the two manuscripts have exclusive figures and no duplicated primary analytical results.

My recommendation: Reposition Paper 3 as a genuinely critical systematic review and evidence-readiness assessment. It can discuss the weaknesses of HPI as part of the literature appraisal, but the complete mathematical derivation, dataset-specific calculations and detailed results should remain in Paper 2.

Paper 3 should concentrate on:
- Analytical comparability.
- Evidence quality and QA/QC.
- Geographical representativeness.
- Limitations of published risk-index applications.
- National evidence and monitoring readiness.
The PRISMA diagram, eight-domain appraisal and review-specific evidence map should become its distinctive analytical contribution.

The COPE disclosure also needs revision. Do not claim that no results, figures or derivations overlap until the actual manuscripts have been separated and audited.

Finding 4 — Paper 3's new reproducibility pipeline is not yet a complete research pipeline
Critical — systematic review methodology
The new reproduce_paper_3_evidence_map.py is a useful improvement.

However, its actual implementation does not reproduce all the analyses promised in the manuscript or the script's own description.

For instance, it does generate the eight-domain appraisal and figures, but it does not independently reproduce the complete five-RQ results, spatial coverage calculations, HPI/RI analyses or all the manuscript's central numerical claims.
Problems with the eight-domain appraisal
The current code includes:
def eval_sampling_design(records):    if records >= 30:        return 'High'    elif records >= 10:        return 'Moderate'    else:        return 'Low'



The manuscript defines sampling design in terms of distinct sampling locations or replicated reach designs. The code instead uses Total_Records.

A study with repeated seasonal measurements at a handful of locations can therefore receive a high sampling-design rating without having a high spatial sampling density.

The sample-handling classifier also treats a study as high quality if it documents either filtered water or dry-weight-standardized sediment. This can be misleading for studies containing both matrices: proper sediment handling does not establish proper water filtration.
Problems with PRISMA reproducibility
The PRISMA flow chart still uses hard-coded counts:
- 1,420 identified records.
- 582 duplicates removed.
- 838 screened.
- 764 excluded.
- 74 assessed in full text.
- 46 excluded.
- 28 included.
The repository does not provide a complete machine-readable screening log, database-specific search exports, individual exclusion decisions and full-text exclusion reasons sufficient to independently reconstruct that flow.

The existence of a PRISMA-looking diagram does not establish that the search and selection process is reproducible.
Problems with evidence provenance
The new study_extraction_evidence.csv is a good step, but its records do not provide enough audit information for a fully reproducible systematic review.

I would expect each critical appraisal decision to be linked to the primary source using:
- Source page number.
- Table, figure or paragraph identifier.
- Supporting quotation or extracted evidence.
- Extractor and independent verifier.
- Disagreement-resolution record.
The custom eight-domain framework also needs an explicit scoring protocol and inter-rater agreement assessment. Merely defining High, Moderate and Low categories does not validate the appraisal framework.

Verdict: The new pipeline is a useful foundation, not yet a complete reproduction system for a publication-grade systematic review.

Finding 5 — Paper 1's validation results are more informative than its positive conclusions
Critical — model validation
The LORO work is a major methodological improvement. It exposes a problem that the earlier random validation could obscure.

The current script uses:
KFold(n_splits=5, shuffle=True, random_state=SEED)



That is shuffled random five-fold cross-validation, not spatial block cross-validation.

Given repeated observations and co-located records, nearby or identical sampling locations can enter both training and validation folds.

The manuscript's description of this as “5-Fold Spatial Cross-Validation” is therefore inaccurate.

The new LORO results are:
Metal	Random 5-fold \(R^2\)	LORO \(R^2\)
Pb	0.5858	'-0.4567
Cr	0.5537	'-0.4386
Cd	0.5420	'-1.5201
Cu	0.6072	'-0.5804
Ni	0.6460	'-0.0063
As	0.4429	'-0.6278

Cross-basin transferability under LORO
Negative R² indicates that the held-out river predictions perform worse than predicting the held-out observations using their mean.


-1.6-1.2-0.8-0.40PbCrCdCuNiAs















These results do not support national out-of-basin predictive generalization.

That does not mean the research is worthless. In fact, it suggests a potentially stronger research positioning:
A critical empirical evaluation of the limits of river-network-informed machine learning for sediment-contamination prediction in a spatially sparse, highly clustered deltaic monitoring environment.

That is a more defensible contribution than claiming successful nationwide prediction.

There are also two implementation problems:
1. The current model script's model dictionary runs RF, XGBoost, LightGBM and CatBoost. It does not independently reproduce the Ordinary Kriging and Regression Kriging results shown in the benchmark CSV.
2. The national prediction and risk workflow depends on an already-existing reach-prediction file. The script does not independently generate the entire national prediction workflow from raw data.
The uncertainty calculation also assumes independent metal prediction errors when it combines variances for the composite RI. Cross-metal covariance is omitted. With correlated metal predictions, that can misrepresent composite uncertainty.

Required correction: Make LORO and spatial block validation the primary evidence, remove the word “spatial” from random K-fold results, audit sampling-unit leakage, and stop presenting the 55.76% national Very High Risk estimate as a validated deterministic result.

The current internal readiness audit is right to put Paper 1 on hold.

Finding 6 — Paper 4's data descriptor overstates what its station table represents
Major — data publication readiness
Paper 4 describes a normalized relational database with a stations table containing each unique sampling location.

The current stations.csv does not represent that cleanly.

It has repeated station identifiers across observation events, cross-river identifier collisions and missing river-specific location entries. Consequently, its stated 220 coordinate-resolved stations and corresponding snapping statistics should not be described as 220 independent sites.

There is also a coordinate-system inconsistency:
- Paper 3 methods describe UTM Zone 45N.
- Paper 4 methods use EPSG:3857 for snapping offsets.
Web Mercator is not a locally distance-preserving projection at Bangladesh latitudes. That matters when reporting snapping offsets in metres. Recompute distances using a suitable local projected coordinate system or a geodesic method, and document it consistently.

The manuscript also states that the Zenodo record is openly available, while the launch checklist says the deposit remains in Draft mode. I could not independently verify the public status of the DOI. This internal contradiction must be resolved before submission.

Finally, the paper describes the dataset as 2010–2024, yet includes a 2025 study (P12). The record for Ahmed et al. is a 2025 publication, so the date range needs to be corrected consistently across the manuscript, README, search protocol and dataset documentation. 

sciencedirect.com


3. What has genuinely improved
There are several positive developments worth preserving.

First, the research positioning is better. Paper 3 has moved beyond a generic contamination compilation toward evidence reliability, methodological comparability and surveillance readiness.

Second, the LORO analysis is valuable. It reveals the limits of national spatial generalization, and it gives Paper 1 a more credible potential contribution.

Third, the extraction-evidence matrix is a useful foundation. It creates a starting point for transparent study-level critical appraisal, although it still needs source-level traceability and independent verification.

Fourth, Paper 2 handles an important regulatory distinction correctly. The ECR 2023 Schedule 2 includes distinct potable-water and inland surface-water standards. The manuscript explicitly treats potable-benchmark exceedance in raw river water as a treatment-burden screening measure, rather than automatically declaring ambient river-water statutory non-compliance. The Bangladesh Gazette supports the cited potable limits, including Pb 0.010 mg/L, Cd 0.003 mg/L and Ni 0.050 mg/L. 

file-chittagong.portal.gov.bd

That qualification is important and should remain.

4. Recommended correction sequence
I would not spend the next development cycle polishing manuscript language or figures. The underlying data model should be fixed first.
Priority	Task	Expected outcome
1	Rebuild station identity and observation relationships	Trustworthy spatial data foundation
2	Reconcile all coordinates against P01–P28 source PDFs	Auditable geospatial provenance
3	Recalculate spatial coverage for clearly defined water, sediment and combined populations	Consistent spatial results
4	Rebuild Paper 3's PRISMA, appraisal and five-RQ analysis pipeline	Reproducible systematic review
5	Separate Paper 3 and Paper 2 contributions and figures	Defensible publication boundaries
6	Revise Paper 1 around spatial generalization failure and applicability limits	Scientifically defensible ML manuscript
7	Rebuild Paper 4's schema, manifest and coordinate validation	Credible data descriptor
8	Update README, submission packages, author metadata and reproducibility tests	Consistent release package

The repository also needs automated validation: duplicate-key tests, coordinate-range checks, foreign-key checks, dataset-denominator assertions, reproducible build checks and a pinned dependency environment.
5. Final verdict
My assessment is that the repository has improved substantially as a research workspace, but it has not yet reached the standard implied by its publication-readiness labels.

The most serious issue is not the writing quality. It is the relationship between the underlying observations, spatial identities, derived results and manuscript claims.

In particular:
- Paper 2 is the closest to being a viable journal submission, subject to the spatial and overlap corrections.
- Paper 3 has a promising research position, but its evidence appraisal and reproduction workflow need significant work.
- Paper 4 could become a useful data publication after the station model and coordinate provenance are repaired.
- Paper 1 should be reframed around the demonstrated limits of transferability rather than nationwide predictive success.
I would not submit any of the four journal manuscripts in their current repository state. That is a stricter verdict than the internal audit's Paper 2 assessment, because my review found additional cross-paper and data-integrity problems.

One important qualification: I did not change repository files or execute the complete pipeline. This is a direct source and processed-data audit, not a fresh numerical reproduction from all 28 source PDFs.

The next most useful step would be to turn these findings into a prioritized, file-by-file remediation checklist with specific code changes and validation criteria.