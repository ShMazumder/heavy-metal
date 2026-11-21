Brutal Peer Review: Heavy Metal Contamination and Fluvial Risk in Bangladesh River Systems
Repository: ShMazumder/heavy-metal · Branch: main · Review date: 21 November 2026
Overall verdict: NOT PUBLICATION-READY
My overall assessment: 4/10 in research maturity.

There is a potentially valuable environmental research programme here. The national literature compilation, geospatial integration, statistical analyses and effort to create multiple research outputs demonstrate considerable work.

However, my primary concern is that the repository appears to have progressed further in producing manuscripts than in establishing the scientific validity of all the conclusions.

Several findings are potentially interesting, but some are substantially stronger than the evidence supporting them. There are also problems involving statistical independence, spatial extrapolation, data harmonization, publication overlap and research reproducibility.

I would not recommend submitting the current versions to the proposed journals.

This is not a cosmetic-revision situation. Some of the research questions and analytical designs need to be reconsidered.

1. Executive assessment
1.1 What the repository contains
The repository presents six research outputs:
ID	Research output	Target venue
P1	Sediment spatial modelling and ecological risk assessment using ML	Science of the Total Environment
P2	Surface-water contamination synthesis and regulatory benchmark analysis	Environmental Pollution
P3	Systematic review and multi-matrix meta-analysis	Environment International
P4	Geospatial heavy-metal database and data descriptor	Nature Scientific Data
C1	River-network ML for sediment contamination	IEEE IGARSS
C2	Regulatory benchmark discordance and surveillance deficits	IWA World Water Congress

The underlying database is described as containing 557 records across 28 studies and 12 river systems, comprising 289 sediment records, 162 trace-metal water records and 106 bulk physicochemical records. 

ShMazumder/heavy-metal · GitHub+2

That is a substantial compilation effort.

However, the first architectural problem is immediately apparent.
Six manuscripts do not represent six independent scientific contributions.

The repository has essentially three research assets:
1. A sediment contamination dataset.
2. A surface-water contamination dataset.
3. A shared geospatial and literature-derived infrastructure.
These assets are being reused across multiple manuscripts, sometimes with substantially overlapping research questions and findings.

This does not automatically constitute inappropriate publication splitting. Multiple legitimate publications can emerge from a shared dataset.

But each publication must contribute a demonstrably distinct scientific result.

That distinction is not yet sufficiently established.
1.2 Overall scorecard
These scores are my reviewer judgments, not objective measurements.
Dimension	Score / 10	Assessment
Research problem relevance	9	Strong environmental and policy relevance
Dataset potential	8	Valuable national compilation
Dataset reliability	5	Requires deeper source-level auditing
Research novelty	5	Some interesting ideas; several incremental contributions
Statistical methodology	5	Good techniques, but important validity concerns
Geospatial methodology	4	Significant extrapolation and topology concerns
ML methodology	5	Reasonable algorithms, insufficient generalization evidence
Reproducibility	6	Good structural effort; execution not independently verified
Publication architecture	3	Excessive overlap
Submission readiness	2	Important scientific and production issues remain

The strongest asset is the dataset. The weakest element is the confidence with which the manuscripts interpret the resulting predictions and statistical associations.

2. Critical portfolio-level problems
Before discussing individual manuscripts, there are five problems affecting the entire research programme.
2.1 Research fragmentation and publication overlap
Major concern
Consider the following relationships:
Sediment research
Paper 1: Spatial ML, geostatistics, SHAP and ecological risk

Paper 3: Systematic review, sediment enrichment, risk indices and geographical coverage

Conference 1: River-network ML and sediment risk



Water research
Paper 2: Regulatory benchmarks, HPI, seasonal contrasts and coverage

Paper 3: Water meta-analysis, regulatory exceedance and meta-regression

Conference 2: Regulatory exceedance and monitoring gaps



Shared research infrastructure
Paper 4: The compiled geospatial database itself



The repository's own publication roadmap identifies the need to separate sediment and water research because their environmental meanings and measurement characteristics differ. That is a sound decision. 

raw.githubusercontent.com

However, Paper 3 subsequently reintroduces much of the analysis from Papers 1 and 2.

My concern is that Paper 3 becomes a container for previously analysed findings rather than an independent systematic-review contribution.

My recommendation:

Build the publication programme around three genuinely distinct contributions:
- Sediment: spatial modelling and ecological risk.
- Water: water-quality synthesis, benchmark analysis and monitoring gaps.
- Data: a properly documented, independently validated national geospatial dataset.
Paper 3 should be reconsidered as a standalone article unless its systematic-review question and analytical contribution can be made genuinely independent.

The conference papers should not simply be repackaged versions of the journal submissions. Any previous publication and substantial-overlap issues must be handled according to the relevant conference and journal policies.
2.2 The 28-study database is not necessarily representative of Bangladesh's rivers
Fundamental limitation
The dataset is a compilation of published research, not a probability-based national environmental monitoring survey.

This distinction is extremely important.

Published environmental studies tend to concentrate on:
- Industrially affected rivers.
- Urban centres.
- Economically important river systems.
- Locations where contamination is already suspected.
- Rivers with convenient sampling access.
The repository itself reports considerable concentration around the Greater Dhaka and Chattogram areas. 

raw.githubusercontent.com

Consequently:
\[
P(\text{location included})
\neq
P(\text{location represents Bangladesh})
\]

The 289 sediment records and 162 water-metal records cannot automatically be interpreted as representative national samples.

For example, suppose published research contains disproportionately many samples from the Buriganga and Karnaphuli rivers.

A model trained on these observations might successfully identify their contamination characteristics.

That does not establish that it can reliably predict contamination in relatively unstudied rivers such as the upper Brahmaputra or peripheral transboundary tributaries.

What is required:

A comprehensive spatial sampling-bias assessment, including:
1. River-system representation.
2. Geographic clustering and sampling density.
3. Distribution of sampling years.
4. Study-level sampling effort.
5. Analytical-method distribution.
6. Differences between observed and unsampled geographic conditions.
The limitations must be reflected in the conclusions, not merely acknowledged in the Discussion section.
2.3 Data harmonization needs stronger scientific justification
This is particularly problematic for both sediment and water measurements.

Different research studies may use different:
- Analytical instruments.
- Digestion protocols.
- Detection limits.
- Sample preservation procedures.
- Filtration procedures.
- Sediment grain-size fractions.
- Dry-weight correction methods.
- Laboratory quality-control protocols.
Two measurements reported as Pb concentrations in mg/kg are not automatically comparable.

For example, sediment extracted using aqua regia is not necessarily analytically equivalent to sediment subjected to complete HF-based digestion.

Likewise, a filtered water sample and an unfiltered, digested water sample do not represent the same operational fraction.

The repository does document analytical methods and quality-control information in its intended relational database. That is positive. 

raw.githubusercontent.com

But recording the differences is not equivalent to harmonizing their scientific effects.

The manuscripts need to show exactly how these methodological differences were handled in each analysis.

At minimum, I would require sensitivity analyses stratified by analytical method, digestion protocol, sample fraction and study.
2.4 The systematic review methodology needs a stronger audit trail
Paper 3 claims a PRISMA 2020 systematic review, with 1,420 candidate records, 74 full-text articles and 28 eligible studies. 

raw.githubusercontent.com+1

This is a reasonable starting point.

However, a convincing systematic review requires more than a PRISMA flowchart and a list of included papers.

I would expect:
- Search execution dates for each database.
- Complete database-specific search queries.
- Duplicate identification and removal methodology.
- Title and abstract screening records.
- Full-text exclusion reasons.
- Independent screening by at least two reviewers.
- Disagreement resolution procedures.
- A documented protocol or protocol registration.
- A transparent study-quality assessment.
I also found differences in the stated search sources and strategies between manuscripts.

Paper 1 describes one search-source combination, Paper 2 another, and Paper 3 a broader combination involving BANSDOC and other databases. 

raw.githubusercontent.com+2

That may reflect different research scopes, but the authors must demonstrate that the underlying study inclusion decisions are reproducible and consistently documented.

There is also a direct date inconsistency: the systematic-review methods specify a search window ending on 31 March 2024, while the shared study catalog includes Ahmed et al. (2025). 

raw.githubusercontent.com+1

This needs correction before publication.
2.5 The repository's publication-readiness claims are premature
The README labels the four journal manuscripts and conference papers as ready.

However, the manuscripts currently contain placeholder author information such as:
- Author One.
- University Name.
- author.one@university.edu.
These are present in the actual LaTeX manuscript sources. 

raw.githubusercontent.com+3

This may be intentional anonymization, but the public repository should not describe those files as fully submission-ready.

I also found inconsistent venue references. The Paper 2 reproduction script identifies Chemosphere, while the manuscript identifies Environmental Pollution. The publication roadmap and submission guide also disagree about the target journal. 

raw.githubusercontent.com+3

This indicates that the manuscript packages and project documentation need stronger version synchronization.

3. Paper 1 — Sediment spatial modelling and ecological risk assessment
Major scientific redesign required
Target: Science of the Total Environment

Research proposition: Integrate HydroSHEDS river-network information with machine learning and geostatistical techniques to predict sediment contamination and ecological risk throughout Bangladesh.

This is arguably the most ambitious research contribution in the repository.

It is also one of the most scientifically vulnerable.
3.1 What is good
There are several positive aspects.

The paper:
- Separates sediment measurements from water measurements.
- Compiles 289 sediment records across 17 studies.
- Georeferences sampling locations.
- Incorporates HydroSHEDS HydroRIVERS information.
- Compares Random Forest, XGBoost, LightGBM and CatBoost.
- Includes Ordinary Kriging and Regression Kriging.
- Uses spatial cross-validation.
- Includes SHAP explanations.
- Attempts nationwide reach-level ecological-risk mapping.
The manuscript reports CatBoost performance of:
Metal	Reported \(R^2\)
Pb	0.6393
Cd	0.5689
Cr	0.5201
As	0.3713*

*The reported As champion is LightGBM rather than CatBoost.

These are potentially useful predictive results, particularly given the relatively small dataset. 

raw.githubusercontent.com+1

However, they do not yet justify the national-level claims.
3.2 Major problem 1: The model's geographic generalization is not established
Critical
The paper trains on 289 measurements, representing approximately 133 unique station centroids.

It then predicts contamination across 55,668 HydroRIVERS reach segments.

That is a substantial extrapolation problem.

The important question is not:

Can CatBoost fit and predict the available observations?

The important question is:

Can a model trained on a small, geographically biased collection of published samples predict contamination in river systems that have never been measured?

These are different problems.

Even spatial cross-validation does not automatically answer the second question.

The paper needs to establish:
- Whether spatial blocks are genuinely independent.
- Whether observations from the same sampling station can enter different folds.
- Whether observations from the same study can enter different folds.
- Whether nearby reaches are leaking geographic information between training and testing.
- Whether entire river basins can be withheld during validation.
I would specifically require:

Leave-one-river-system-out validation.

For example:

Train using all available river systems except the Surma system, predict Surma, and evaluate against its withheld observations.

Repeat for other river systems.

This is a much more convincing test of geographical transferability.

A further improvement would be an independent field-validation dataset collected after model development.

Without these tests, the national map is primarily a spatial extrapolation exercise.
3.3 Major problem 2: The term River-Network Machine Learning is not adequately demonstrated
This is an important novelty concern.

The repository describes the model as topological river-network ML.

But the manuscript's visible methodology describes CatBoost, planar-coordinate Ordinary Kriging and Regression Kriging using ordinary-kriging residual interpolation. 

raw.githubusercontent.com+2

These methods do not automatically constitute a genuinely network-constrained spatial model.

There is a distinction between:

A. Hydrographic feature-engineered ML

A model using:
- Upstream catchment area.
- Strahler order.
- Annual discharge.
- Distance to river mouth.
- Longitude and latitude.
B. Genuine river-network spatial modelling

A model explicitly representing:
- Directed flow connectivity.
- Upstream/downstream relationships.
- Flow-connected distances.
- Network-constrained spatial dependence.
- River-network covariance structures.
The former can be useful, but it does not establish the methodological novelty of the latter.

My concern is that the manuscript currently seems to emphasize the second while primarily demonstrating the first.

Recommendation: Either implement a genuine network-based model or reposition the contribution as hydrographic-feature-enhanced spatial ML.

That would be a more defensible scientific claim.
3.4 Major problem 3: National prediction of ecological risk is insufficiently validated
The most concerning result is the reported 55.76% of river reaches classified as Very High Ecological Risk.
55.76%
Reported nationwide Very High Risk classification, based on RI ≥ 600.

ShMazumder/heavy-metal · GitHub+1
This is an extraordinary national-level conclusion.

The problem is that these are predicted risk classifications rather than direct ecological measurements from 55,668 river reaches.

There are at least four issues.

First: prediction uncertainty.

A point estimate of metal concentration is insufficient for ecological-risk classification.

You need to propagate prediction uncertainty through the contamination-factor calculations and the RI calculation.

For example:
\[
RI = \sum_i T_r^i \frac{C_i}{B_i}
\]

A predicted RI of 610 and one of 1,200 should not be interpreted as equally reliable merely because both cross the 600 threshold.

Second: geographic extrapolation.

A reach with environmental characteristics far outside the training distribution should not receive the same level of predictive confidence as a reach surrounded by observations.

Third: geochemical background.

The use of Upper Continental Crust concentrations is defensible as a reference framework, but it is not necessarily an appropriate local geochemical background for every river system.

Natural sediment composition in the Ganges-Brahmaputra-Meghna system is heterogeneous.

Local background measurements or region-specific reference values would substantially strengthen this assessment.

Fourth: ecological interpretation.

Hakanson's Potential Ecological Risk Index is a screening index.

It is not direct evidence of observed ecological damage, biological toxicity or ecosystem impairment.

The manuscript should consistently distinguish potential ecological risk from demonstrated ecological effects.

My recommendation is to report:
- Predicted contamination.
- Prediction uncertainty.
- Potential ecological risk.
- Confidence of risk classification.
- Regions where the model is extrapolating beyond its supported domain.
Do not present the 55.76% result as an established measurement of nationwide ecological damage.
3.5 Major problem 4: Feature availability and SHAP interpretation
The manuscript and conference abstract identify catchment characteristics, longitude and sediment pH as important predictors. 

raw.githubusercontent.com+1

This raises an important question.

Where do sediment pH values come from for all 55,668 predicted river reaches?

Sediment pH is not a standard nationwide attribute of HydroRIVERS.

If it is measured only at the literature sampling stations, how is it supplied for unsampled reaches?

Possible approaches include:
- Independent national pH datasets.
- Spatial interpolation.
- River-system-level estimates.
- Excluding pH from nationwide inference.
Each approach has different scientific implications.

If pH is used in training but cannot be supplied independently at prediction time, the nationwide prediction framework has a serious operational gap.

The same question applies to all geochemical predictors.

I would also require a clear distinction between feature importance and causal interpretation.

SHAP identifies how a trained model uses variables; it does not establish that the variable causes contamination.
3.6 Major problem 5: The Kriging comparison is not sufficiently convincing
The manuscript reports catastrophic negative \(R^2\) results for Ordinary Kriging, including:
- Cr: approximately -63.85.
- As: approximately -21.90.

raw.githubusercontent.com+1
These findings may be genuine for the particular implementation.

However, they do not prove that Euclidean geostatistics fundamentally fail across disconnected river basins.

A poorly specified variogram, unsuitable coordinate system, inappropriate cross-validation strategy or inadequate spatial model can all produce disastrous results.

I would require:
1. Variogram diagnostics.
2. Anisotropy assessment.
3. Alternative variogram models.
4. Spatial-block configuration details.
5. A geographically appropriate projection.
6. Comparisons with optimized spatial baselines.
7. Flow-connected or network-constrained geostatistical alternatives.
The conclusion should be about the comparative performance of tested implementations, not an entire class of geostatistical methods.
3.7 Paper 1 decision
Major redesign
Component	Verdict
Research question	Strong
Dataset	Useful but biased
ML approach	Reasonable
Network-method novelty	Insufficiently established
Spatial validation	Needs stronger design
National risk maps	Not yet defensible
Publication potential	High after substantial redesign

My recommendation: Retain Paper 1, but make geographical generalization and uncertainty-aware river-network prediction the central scientific contribution.

Do not prioritize generating more risk maps. Prioritize proving that the existing map can be trusted.

4. Paper 2 — Surface-water contamination and regulatory benchmark analysis
Major revision required
Target: Environmental Pollution

This paper has a more clearly defined research question than Paper 1.

Its potentially valuable contribution is the examination of:
- Contamination benchmarks.
- Historical versus current Bangladesh standards.
- Operational water-quality concerns.
- Seasonal variation.
- HPI mathematical properties.
- Published monitoring coverage.
I particularly like the attempt to distinguish filtered and unfiltered measurements.

However, the statistical and environmental interpretation needs improvement.
4.1 Major problem 1: Dissolved and total-recoverable metal measurements
Critical
This is arguably the most important problem in Paper 2.

The manuscript acknowledges that unfiltered, digested water samples can capture particulate-bound metals and produce concentrations one to three orders of magnitude higher than dissolved fractions.

It then performs a confirmed dissolved-only sensitivity analysis using studies documenting 0.45 μm filtration. 

raw.githubusercontent.com

That is a good decision.

But why is the primary analysis still based on a mixture of potentially different operational fractions?

Consider two hypothetical measurements:
Sample	Analytical fraction	Pb concentration
A	Filtered, dissolved	0.015 mg/L
B	Unfiltered, digested	0.090 mg/L

These are not equivalent environmental observations.

The second potentially includes particulate-bound Pb.

Pooling them into the same primary distribution introduces a measurement-definition problem.

The sensitivity analysis is useful, but it does not fully resolve the comparability issue.

My recommendation:

Create three explicitly separated datasets:
1. Confirmed dissolved concentrations.
2. Total-recoverable or unfiltered concentrations.
3. Fraction-unknown concentrations.
The primary benchmark analysis should use a clearly defined operational fraction.

The other datasets should support separate sensitivity analyses.

Otherwise, a reviewer can legitimately question whether elevated concentrations reflect dissolved pollution, suspended sediments or differences in analytical preparation.
4.2 Major problem 2: Detection limits and censored measurements
The repository correctly recognizes analytical detection limits as an important issue.

However, this needs to be treated as a central statistical problem rather than an instrumentation-related sensitivity exercise.

Consider a study using Flame-AAS with an effective detection limit of:
\[
LOD = 0.050 \text{ mg/L}
\]

Now consider a regulatory benchmark:
\[
S_{\text{Pb}} = 0.010 \text{ mg/L}
\]

Suppose that the sample is reported as:
\[
Pb < 0.050 \text{ mg/L}
\]

The result does not tell us whether the true concentration is:
- 0.003 mg/L;
- 0.015 mg/L;
- 0.040 mg/L.
Two of those values would have different benchmark classifications.

The observation is therefore not safely classifiable as compliant.

This is especially important when estimating national exceedance percentages.

The data descriptor mentions preserving censored observations and their detection limits, which is encouraging. 

raw.githubusercontent.com

But the manuscript must demonstrate how the statistical analysis handles observations whose LOD exceeds the regulatory threshold.

Required correction:

Use an explicit censored-data framework or provide lower and upper bounds for exceedance estimates.

Do not automatically classify such observations as non-exceedances.

Also, instrument family alone should not define sensitivity. Detection limits should be recorded per element, per study and, wherever available, per analytical procedure.
4.3 Major problem 3: Drinking-water standards versus raw river water
This requires more careful environmental and regulatory interpretation.

The manuscript compares river-water measurements against:
- WHO drinking-water guidelines.
- ECR 1997 potable-water standards.
- ECR 2023 potable-water standards.
- FAO irrigation benchmarks.
The comparison is useful as a screening exercise.

However, river water before treatment is not equivalent to supplied drinking water.

The ECR 2023 Schedule 2 actually distinguishes inland surface-water quality standards from a separate potable-water quality standards table.

For example, the Gazette specifies a Pb limit of 0.01 mg/L in the potable-water table. 

file-chittagong.portal.gov.bd

It also separately specifies surface-water use categories. 

file-chittagong.portal.gov.bd

The authors need to explain which standard is appropriate for which environmental question.

I would separate the interpretations into:
Benchmark	Appropriate interpretation
WHO drinking-water guideline	Drinking-water health-based screening
ECR 2023 potable standard	National potable-water quality benchmark
ECR surface-water standards	Raw surface-water use classification
FAO irrigation guidelines	Agricultural water suitability

For raw river water, exceeding a drinking-water benchmark does not automatically establish that consumers are exposed to that concentration.

It can indicate the treatment burden or contamination pressure faced by a water abstraction system.

That distinction needs to be maintained throughout the abstract, results and conclusion.
4.4 Major problem 4: HPI analysis is interesting but not particularly novel
One of the more interesting mathematical discussions concerns the Heavy Metal Pollution Index.

The manuscript observes that:
\[
W_i = \frac{1}{S_i}
\]

and:
\[
Q_i = \frac{M_i}{S_i}\times100
\]

Therefore:
\[
W_i Q_i
=
100\frac{M_i}{S_i^2}
\]

This means the contribution of an element to the numerator depends quadratically on its benchmark concentration. 

raw.githubusercontent.com

The authors use this to explain the dominance of Cd and Pb in the selected HPI panels.

I agree that this is worth investigating.

However, there is a distinction between identifying a mathematical property of an existing index and establishing a new methodology.

The inverse-standard weighting structure is inherent to the selected HPI formulation.

Demonstrating that it emphasizes elements with lower regulatory limits is not, by itself, a major methodological breakthrough.

How to strengthen it:

Compare:
- Original HPI.
- Heavy Metal Evaluation Index.
- Metal Index.
- Equal-weight normalized index.
- Benchmark-normalized concentration index.
- Alternative weighting schemes.
Then investigate whether the resulting classification remains stable when benchmark values change.

That would turn the exercise into a more useful methodological sensitivity study.
4.5 Major problem 5: Statistical independence and seasonal comparisons
The paper uses pooled non-parametric comparisons and within-study random-effects meta-analysis for seasonal differences.

Using within-study comparisons is a good decision.

However, the paper needs to make the study-level dependence structure central to its inference.

The nominal number of measurements is not the same as the effective number of independent studies.

For instance, 40 observations from one study do not necessarily provide the same independent information as 40 observations from 10 geographically independent studies.

The pooled Mann-Whitney tests can overstate statistical significance when repeated measurements from the same study are treated as independent.

I would give priority to:
- Study-stratified comparisons.
- Within-study seasonal effects.
- Hierarchical random-effects modelling.
- Explicit sample-size accounting.
- Prediction intervals.
- Sensitivity to studies with unusually large sample counts.
The authors already use HKSJ adjustments in some analyses. That is positive, but the broader statistical structure still deserves attention. 

raw.githubusercontent.com+1

4.6 Major problem 6: The national surveillance-gap analysis
This is an excellent potential research direction.

The proposition is simple:

Existing studies are spatially concentrated, leaving substantial river corridors under-investigated.

The README reports:
- 757.2 km of covered major river length.
- 16.5% coverage.
- 38.2% expected coverage under the spatial random null model.

ShMazumder/heavy-metal · GitHub
The manuscript also presents proposed monitoring locations.

However, I would challenge the null model.

Why should a randomly selected river location represent an appropriate expectation for environmental monitoring?

Real monitoring locations are constrained by:
- Population density.
- Industrial activity.
- Accessibility.
- Water abstraction infrastructure.
- River discharge.
- Environmental sensitivity.
- Administrative boundaries.
A uniform random-location null model might demonstrate geographical concentration, but it does not necessarily identify the locations with the greatest environmental monitoring need.

I would recommend a weighted monitoring-priority framework.

For example:
\[
Priority_j =
w_1 Gap_j +
w_2 Population_j +
w_3 IndustrialPressure_j +
w_4 Discharge_j +
w_5 EcologicalSensitivity_j
\]

The weights need transparent justification and sensitivity analysis.

Also, the paper uses 2,224 filtered major reaches for its coverage analysis, whereas the sediment research and systematic review refer to 55,668 total reach segments.

This distinction should be explicitly documented rather than treating both numbers as equivalent geographic populations. 

raw.githubusercontent.com+1

4.7 Paper 2 decision
Major revision
Component	Verdict
Research question	Good
Regulatory analysis	Valuable
HPI critique	Interesting but incremental
Dissolved/total fraction handling	Major weakness
Detection-limit handling	Requires stronger inference
Seasonal analysis	Needs stronger clustering treatment
Monitoring-gap analysis	Promising
Publication potential	Good after methodological correction

My recommendation: Make Paper 2 primarily about analytical comparability, regulatory benchmark interpretation and surveillance deficits.

The HPI mathematics should support the paper rather than dominate its novelty claim.

5. Paper 3 — Systematic review and multi-matrix meta-analysis
Do not submit in current form
Target: Environment International

This is probably the most problematic publication in the portfolio from a publication-strategy perspective.

Its scope is extremely broad:
- Surface-water contamination.
- Sediment contamination.
- Ecological risk.
- Water-quality exceedances.
- Analytical-method sensitivity.
- Seasonal variation.
- Multivariable meta-regression.
- HPI mathematical decomposition.
- Nationwide monitoring coverage.
That sounds comprehensive.

But comprehensiveness is not the same as scientific coherence.
5.1 The central problem: What is the paper's independent contribution?
Paper 3 reuses:
- The 289 sediment observations.
- The 162 trace-metal water records.
- The 106 physicochemical records.
- The same ecological risk indices.
- The same water-quality benchmarks.
- The same hydrographic surveillance analysis.
These are already central components of Papers 1 and 2.

raw.githubusercontent.com+3
The systematic-review paper needs a stronger reason to exist independently.

A systematic review may legitimately reuse a dataset to perform different analyses.

But this manuscript currently appears to combine results that already form the main contributions of the other two manuscripts.

That is a serious concern for Environment International.
5.2 The meta-regression is insufficiently supported
Critical statistical concern
This is where I would be particularly strict.

The paper describes a multivariable logistic meta-regression:
\[
\operatorname{logit}(P(Y_{ij}=1))
=
\beta_0+
\beta_1 HighSens_j+
\beta_2 Urban_i+
\beta_3 DrySeason_{ij}+
\beta_4 Premonsoon_{ij}
\]

There are four predictors plus an intercept.

The underlying water synthesis contains 12 investigations, despite having many individual measurements. 

raw.githubusercontent.com+1

The independent information is therefore much closer to 12 study clusters than 162 independent studies.

That is an extremely small effective sample for stable multivariable inference.

It raises concerns about:
- Overfitting.
- Cluster-robust standard-error reliability.
- Study-level confounding.
- Correlation between instruments and sampling locations.
- Geographical imbalance.
- Seasonal classification differences.
Consider some reported results:
Association	OR	95% CI	p-value
Cd, urban industrial corridor	10.79	0.31–623.07	0.140
As, pre-monsoon	5.67	0.12–144.70	0.300


raw.githubusercontent.com
These intervals are extraordinarily wide.

They do not provide convincing evidence of stable independent effects.

The point estimates may look impressive, but the uncertainty is enormous.

My recommendation:

Do not present these findings as established contamination drivers.

Either:
1. Rebuild the analysis using a properly specified hierarchical model and acknowledge its exploratory nature; or
2. Remove the multivariable meta-regression and concentrate on more defensible descriptive and stratified analyses.
I would prefer the second approach unless additional independent studies can be identified.
5.3 The review needs a more precise research question
A much stronger research question would be:

How do analytical measurement practices, operational water fractions and study-level heterogeneity influence reported heavy-metal contamination estimates in Bangladesh river systems?

That is a coherent systematic-review problem.

It also offers a potentially meaningful scientific contribution beyond simply aggregating pollution levels.

A review could investigate:
- Measurement comparability.
- Analytical detection limits.
- Sample fraction differences.
- Study-quality effects.
- Geographic publication bias.
- Uncertainty in national contamination estimates.
It would be more scientifically defensible than attempting to fit every available analysis into a single paper.
5.4 Paper 3 decision
Reframe or merge
I would not submit the current manuscript to Environment International.

The paper needs either substantial restructuring into a focused systematic review or integration of its non-independent findings into Papers 1 and 2.

Its strongest potential contribution is the systematic assessment of research bias, analytical heterogeneity and the limitations of national heavy-metal evidence.

That could become a respectable and meaningful review article.

6. Paper 4 — Geospatial heavy-metal database and data descriptor
Most promising independent publication
Target: Nature Scientific Data

This might be the most strategically valuable publication in the repository.

I actually consider the dataset a more promising long-term contribution than some of the individual modelling results.

A carefully validated national geospatial database can support many future studies.

It could become a reusable research resource rather than a one-time publication.

However, the current descriptor needs stronger technical validation.
6.1 What is good
The intended database includes:
- Study metadata.
- Sampling stations.
- Elemental measurements.
- Analytical-method information.
- Coordinates.
- HydroSHEDS reach identifiers.
- Detection-limit information.
- Quality-control information.
The paper describes a normalized relational SQLite database and corresponding flat files. 

raw.githubusercontent.com+1

This is a sensible architecture.

The decision to preserve original source values and maintain operational measurement information is particularly important.
6.2 Major problem 1: The station counts are unclear
The manuscript's data manifest reports:
- Water data: 268 rows.
- Sediment data: 289 rows.
- Stations: 426 rows.
It also describes the station data as containing 133 sediment centroids and 23 water-metal sites. 

raw.githubusercontent.com

These counts need reconciliation.

Why does the station table contain 426 rows when the described unique station categories account for only 156 locations?

There may be a legitimate explanation involving repeated sampling locations, water-quality records or source-specific stations.

But the manuscript needs to specify the exact data grain.

For every table, explain:
- What one row represents.
- Whether a row represents a physical site, sampling event or measurement.
- How repeated measurements are represented.
- How shared locations across multiple studies are linked.
- Whether station identifiers are globally unique.
- How observations from multiple studies at the same location are handled.
A proper entity-relationship diagram would help substantially.
6.3 Major problem 2: Geospatial accuracy
The manuscript uses EPSG:3857 for metric projection and river-network snapping.

It reports that:
- 67.4% of locations are within 500 metres.
- 97.7% are within 1,000 metres.
- 100% are within 2,021 metres.

raw.githubusercontent.com+1
There is a technical issue here.

EPSG:3857 is Web Mercator, not an appropriate local metric reference system for accurate distance calculations in Bangladesh.

At Bangladesh's latitude, its distance scale is approximately 9% larger than ground distance.

For example, a projected 1,000-metre distance does not correspond exactly to 1,000 metres on the ground.

For accurate geospatial processing, use a suitable local projected coordinate reference system, potentially with separate UTM zones or an appropriate national projection.

More importantly, nearest-line snapping is not sufficient to establish that the correct river reach was identified.

In Bangladesh's braided and deltaic river systems, a coordinate may be closer to the wrong channel or tributary.

I would require:
- Original coordinate preservation.
- Coordinate accuracy classes.
- River-name consistency checks.
- Catchment consistency checks.
- Manual review of large snapping offsets.
- A maximum acceptable snapping threshold.
- Separate treatment of approximate coordinates.
A location 2 km from a river centreline should not automatically be considered correctly mapped.
6.4 Major problem 3: The extraction validation claim needs correction
The manuscript claims that an independent double-blind re-extraction of 112 assays produced zero numerical discrepancies, with a 95% Wilson confidence interval of 0.0–2.8%. 

raw.githubusercontent.com

There appears to be a numerical inconsistency.

Assuming the validation denominator really is 112 observations and there were zero errors, the upper bound of the conventional two-sided 95% Wilson interval is approximately:
\[
\frac{1.96^2}{112+1.96^2}
\approx 3.32\%
\]

Not 2.8%.

The authors should recalculate this interval using the actual denominator.

More importantly, numerical agreement alone is insufficient to validate an environmental database.

The audit should also examine:
- Unit conversion.
- Detection-limit interpretation.
- Sample fraction classification.
- Digestion methods.
- Coordinate transcription.
- Station identity.
- Sampling year.
- Duplicate observations.
- Missing-value treatment.
I would also publish the extraction audit protocol and the sampled study identifiers.
6.5 Major problem 4: Public data availability and licensing
The manuscript identifies a Zenodo DOI:

10.5281/zenodo.24414976

raw.githubusercontent.com
I could not independently verify the corresponding public record during this review.

That does not establish that it is invalid, but the DOI must be checked before submission.

The authors should ensure that:
1. The record is publicly accessible.
2. The deposited version matches the manuscript.
3. The database and source files are included.
4. The release is immutable and versioned.
5. The data and code have explicit licences.
6. The data have a persistent citation.
I did not see an explicit repository-level LICENSE file in the root file listing. 

ShMazumder/heavy-metal · GitHub

The manuscript also describes distributing primary research PDFs.

Their redistribution rights must be checked individually. Publisher PDFs should not automatically be redistributed merely because their metadata and extracted measurements are publicly useful.
6.6 Paper 4 decision
Worth developing
Component	Verdict
Research contribution	Valuable
Dataset concept	Strong
Database structure	Good direction
Geospatial accuracy	Requires correction
Data extraction validation	Needs stronger evidence
Public data availability	Requires verification
Publication potential	Strongest independent candidate

My recommendation is to prioritize this manuscript, subject to genuine data-quality verification.

7. Conference papers: Are they independent research?
This is a publication-strategy problem.
Conference 1 — IEEE IGARSS
The paper presents:
- HydroSHEDS.
- CatBoost.
- Sediment metal predictions.
- Spatial cross-validation.
- SHAP.
- Nationwide ecological risk.
These are already the central contributions of Paper 1. 

raw.githubusercontent.com+1

I do not see a clearly differentiated remote-sensing contribution in the current manuscript.

For IGARSS, I would expect a stronger geospatial or Earth-observation methodological contribution.

Possible directions include:
- Remote-sensing-derived land-use predictors.
- Satellite-based industrial expansion indicators.
- Hydrographic network connectivity modelling.
- Remote-sensing-based environmental covariates.
- Spatial transfer learning across river systems.
The present paper looks more like a shortened version of Paper 1 than an independent conference contribution.

Verdict: Do not submit in its current form as a separate research contribution.
Conference 2 — IWA World Water Congress
The same problem occurs here.

The paper focuses on:
- Benchmark exceedances.
- HPI.
- Seasonal variation.
- Monitoring gaps.
- National surveillance priorities.
These are substantially the same components as Paper 2. 

raw.githubusercontent.com+1

For IWA, I would prefer a more operational contribution.

For example:

A Risk-Based Monitoring Network Design for Bangladesh River Systems

The study could develop and evaluate a monitoring-priority framework based on:
- Existing sampling gaps.
- Water abstraction points.
- Population served.
- Industrial pressure.
- River discharge.
- Ecological sensitivity.
This would be more useful to water-management practitioners and more clearly distinguishable from Paper 2.

Verdict: Reposition substantially or merge into the journal research programme.

8. Additional statistical and technical inconsistencies
These are smaller than the major problems above but demonstrate why I would not consider the repository fully audited.
Issue	Observation	Required action
Study inclusion period	2024 cutoff, but P12 is from 2025	Reconcile review scope
Missing instrument metadata	P07 is blank and P11 is NR in the study catalog	Resolve eligibility and source metadata
Reach definitions	55,668 total reaches versus 2,224 filtered major reaches	Explicitly define denominators
Spatial coordinate system	EPSG:3857 used for metric distances	Use a geographically appropriate CRS
Monte Carlo precision	Script header refers to 1,000 runs and p below 0.0001	Correct the reported resolution
Manuscript metadata	Placeholder author names and affiliations	Populate genuine submission metadata
Paper 2 venue	Environmental Pollution versus Chemosphere in project documents	Synchronize all files
Data licence	No visible root LICENSE file	Establish explicit licences

Two deserve particular explanation.

Monte Carlo precision: The Paper 2 script describes a 1,000-iteration spatial null model and reports a p-value below 0.0001 in its header. 

raw.githubusercontent.com
 Under the standard plus-one empirical Monte Carlo calculation, 1,000 simulations provide a minimum attainable p-value of approximately:
\[
p_{\min}=\frac{1}{1001}\approx0.001
\]

The repository should either report the appropriate bound or use a substantially larger number of simulations.

Instrument metadata: The study catalog contains blank or unreported analytical-method entries for studies P07 and P11. The Paper 2 inclusion criteria, meanwhile, require documented instrumentation and detection-limit or recovery information. 

raw.githubusercontent.com+1

The authors must demonstrate whether those studies were excluded from the affected analyses or whether the inclusion criteria were not consistently applied.

9. What I would change: A revised research architecture
I would not abandon this research.

I would make it more focused.

My recommended publication architecture is:
Revised research programme
Priority 1
Research A — National sediment geospatial modelling

Geographically Validated River-Network Machine Learning for Sediment Heavy-Metal Contamination in Bangladesh

Focus: Study-independent validation, network topology, predictive uncertainty and ecological risk.

Target: Science of the Total Environment or a suitably matched environmental geoscience journal.


Priority 2
Research B — Surface-water quality and monitoring

Analytical Heterogeneity, Regulatory Benchmark Exceedance and Monitoring Priorities for Heavy Metals in Bangladesh River Systems

Focus: Measurement comparability, censored data, operational water fractions, standards and monitoring gaps.

Target: Environmental Pollution or an appropriate water-quality journal.


Priority 3
Research C — National geospatial database

A Harmonized, Georeferenced and Quality-Assessed Database of Heavy Metal Concentrations in Bangladesh River Systems

Focus: Data provenance, standardized records, geospatial accuracy, uncertainty metadata and validation.

Target: Scientific Data.


Reconsider
Paper 3 — Systematic review

Retain only if it develops an independent, rigorous synthesis of analytical measurement heterogeneity and publication bias. Otherwise, incorporate relevant findings into Research B.


This structure gives each publication a clear purpose.

It also reduces the risk of salami slicing.

10. The most important experiments and improvements
Here is what I would prioritize before another submission round.
Priority 1 — Dataset audit
Must fix
Establish one authoritative observation-level dataset.

Every observation should have:
Field	Purpose
Study_ID	Source study
Observation_ID	Globally unique observation
Station_ID	Physical sampling location
Sampling_Date	Temporal identification
River_System	Geographic grouping
Element	Pb, Cd, Cr, etc.
Concentration	Original reported value
Unit	Original and harmonized unit
Water_Fraction	Dissolved, total-recoverable or unknown
Analytical_Method	Instrument
Digestion_Method	Sample preparation
LOD	Detection limit
LOQ	Quantification limit
Censored_Flag	Non-detect status
Coordinate_Quality	GPS, published coordinate or estimated
Source_Location	DOI, table, page or supplementary file

The source provenance is essential.

A published dataset should allow another researcher to trace any individual value back to its original article and source table.
Priority 2 — Rebuild the sediment ML validation
Must fix
My proposed experiment:
Validation framework
1. Random cross-validation
   
   Baseline performance only.
2. Spatial-block cross-validation
   
   Evaluate geographic interpolation.
3. Leave-one-study-out validation
   
   Evaluate transfer to unseen literature studies.
4. Leave-one-river-system-out validation
   
   Evaluate transfer to unseen river systems.
5. Independent field validation
   
   Evaluate actual geographical generalization.

For all models, report:
- \(R^2\)
- RMSE
- MAE
- Bias
- Prediction intervals
- Residual spatial autocorrelation
- Performance by river system
I would additionally test whether study-level analytical differences are responsible for part of the apparent predictive signal.
Priority 3 — Redesign national ecological-risk prediction
Produce three separate maps:
1. Predicted metal concentration.
2. Prediction uncertainty.
3. Risk classification confidence.
Then distinguish regions where:
- The model has strong validation support.
- The model has limited geographic support.
- The model is extrapolating beyond its training conditions.
This would be considerably more scientifically defensible than a single nationwide categorical risk map.
Priority 4 — Rebuild Paper 2's water-quality inference
Prioritize:
- Dissolved versus total-recoverable fractions.
- Left-censored measurements.
- Study-level dependence.
- Analytical-method sensitivity.
- Regulatory benchmark suitability.
- Hierarchical modelling.
- Monitoring-priority sensitivity.
Make the conclusions robust to reasonable alternative assumptions.
Priority 5 — Independent database validation
For Paper 4, validate:
- Measurement provenance.
- Unit conversions.
- Coordinate accuracy.
- Station identity.
- Data completeness.
- Referential integrity.
- Duplicate identification.
- Source extraction agreement.
Publish the validation results with the database rather than merely describing them in the manuscript.

11. Final ranking and editorial recommendations
My assessment of each output:
Research	Current assessment	Recommendation
Paper 1 – Sediment ML	Major redesign	Retain, strengthen validation
Paper 2 – Water synthesis	Major revision	Retain, correct measurement/statistical inference
Paper 3 – Systematic review	Reframe	Merge or develop an independent review question
Paper 4 – Data descriptor	Promising	Prioritize database validation
Conference 1 – IGARSS	Not differentiated	Develop genuine geospatial novelty
Conference 2 – IWA	Reposition	Emphasize operational monitoring strategy

My top three priorities
1
Make Paper 4 the foundation of the research programme.

Establish a trusted, transparent, versioned and properly validated national database.

2
Rebuild Paper 1's validation architecture.

Its national prediction claims are the most scientifically ambitious and need considerably stronger evidence.

3
Consolidate Papers 2 and 3 into a defensible publication strategy.

Avoid presenting overlapping statistical findings as separate scientific contributions.


12. Final reviewer verdict
I want to distinguish two things.

The research programme has genuine potential. The current manuscripts do not yet demonstrate that potential convincingly.

The repository has some important strengths:
- A meaningful national environmental research problem.
- A valuable literature-derived dataset.
- Serious attempts at geospatial integration.
- Multiple statistical techniques.
- Reproducibility-oriented scripting.
- A potentially reusable national data resource.
But I would raise serious concerns about the following claims:
1. That the ML framework reliably generalizes across Bangladesh's unmeasured river systems.
2. That 55.76% of national river reaches can confidently be classified as Very High Ecological Risk.
3. That the water-quality exceedance estimates are unaffected by analytical fraction and detection-limit heterogeneity.
4. That the multivariable meta-regression provides reliable evidence of independent contamination drivers.
5. That all six research outputs offer distinct scientific contributions.
My decision as a hypothetical peer reviewer would be reject in current form for the ambitious journal submissions, with encouragement to resubmit after substantial methodological reconstruction.

The data descriptor would receive the most positive consideration, provided the underlying dataset and its provenance pass independent validation.

One important limitation of this review: I inspected the current repository overview, accessible LaTeX manuscripts, study metadata, and the visible Paper 2 analysis script. I could not clone and execute the complete repository or independently recalculate all results from its binary SQLite database and full CSV assets. Accordingly, this is a source-level scientific peer review, not a completed clean-room numerical reproduction. A connected GitHub account would enable a deeper examination of those underlying assets.

My final advice: Do not spend the next development cycle writing more manuscripts or generating additional figures. Spend it making the existing evidence scientifically defensible. That is likely to produce fewer papers, but considerably stronger research.


# **Updated brutal peer review: source-level and data-level audit**

Repository: [github.com/ShMazumder/heavy-metal](https://github.com/ShMazumder/heavy-metal?utm_source=chatgpt.com) · Default branch: main · Audited repository tree SHA: `32cb9796a23e7f9794b5d9e25014e9c1628d7faa`

Major scientific and reproducibility concerns confirmed

The direct examination of the repository reveals a more serious issue than manuscript overlap: **the spatial sample-size hierarchy and geolocation quality are not adequately represented in the research claims.**

This is particularly consequential for Paper 1, because its central contribution depends on spatially meaningful observations.

## **1. A significant problem with the sediment dataset**

I independently inspected `stations.csv`, `sediment_data.csv` and `sediment_features_hydro.csv`.

The actual counts are:

# **289**

**Sediment observations**

Compiled records

# **132**

**Geolocated observations**

With coordinate values

# **36**

**Distinct coordinate pairs**

Across the 132 geolocated records

# **157**

**Ungeolocated observations**

54.3% of the sediment dataset

The most alarming result is the concentration of records at three coordinates.

| Study                        | Records | Coordinate pairs |
| ---------------------------- | ------- | ---------------- |
| P18                          | 30      | 1                |
| P14                          | 24      | 1                |
| P28                          | 20      | 1                |
| All other geolocated records | 58      | 33               |
| **Total**                    | **132** | **36**           |

P18 has 30 records across ten station labels and multiple sampling years, but all 30 carry the same coordinates.

P14 has 24 records across eight station labels, again with the same coordinates.

P28 has 20 records, all assigned to one approximate district centroid.

There is an important distinction here:

- 132 geolocated observation records;
- 133 HydroRIVERS-matched records;
- 36 distinct coordinate pairs;
- 289 total sediment observations.

These are not interchangeable quantities.

The repository describes 133 unique spatial station centroids. However, its actual coordinate data contain only 36 distinct coordinate pairs among the 132 geolocated sediment observations.

This raises a major question: were study-level or river-level coordinates copied across multiple sampling stations when the original papers did not supply individual station coordinates?

P28 is explicitly classified as an approximate district centroid. P14 and P18, despite their repeated coordinates, are classified as exact points.

That classification needs source-level verification.

**Why this matters:** A spatial machine-learning model cannot treat repeated observations at the same geographic coordinate as independent spatial locations. Spatial cross-validation must group observations by their true physical location, not merely by their Station_ID.

Until this is resolved, the reported spatial validation results are not sufficiently trustworthy.

## **2. The ML reproducibility problem is confirmed**

The repository contains:

- Model benchmark CSVs.
- Moran's I results.
- SHAP outputs.
- National prediction maps.
- Reach-level prediction files.
- Prediction uncertainty summaries.

However, the current Git tree does not contain the `scripts/paper_1/` implementation described in the README.

I found the Paper 2 and Paper 3 analysis scripts, but not the corresponding Paper 1 training, spatial-fold generation, model tuning and national inference pipeline.

This means that the most ambitious research output cannot currently be independently reproduced from the published repository's documented code.

The benchmark results are also aggregated into a single CSV without fold-level predictions or uncertainty estimates.

Furthermore, the model comparison does not establish that CatBoost is universally superior: Ordinary Kriging actually achieves higher reported \\(R^2\\) for Cu and Ni, while LightGBM and Regression Kriging have advantages for As under particular metrics.

The manuscript acknowledges some of this, but its broader description of geostatistical failure needs qualification.

## **3. Paper 1 — Additional scientific problems**

**My assessment: Reject current version; substantial redesign.**

[Read Paper 1 manuscript](https://github.com/ShMazumder/heavy-metal/blob/main/manuscripts/paper_1_stoten/main.tex?utm_source=chatgpt.com)

### **3.1 Spatial autocorrelation statistics are internally inconsistent**

The manuscript reports Moran's I results using 999 Monte Carlo permutations, with p-values such as:

\\[ p\_{\mathrm{As}}=9.97\times10^{-75} \\]

This is not an attainable empirical permutation p-value with only 999 permutations.

The minimum conventional plus-one Monte Carlo p-value would be:

\\[ p\_{\min}=\frac{1}{999+1}=0.001 \\]

Extremely small values could be obtained from a normal approximation to the permutation z-score. However, that is a different p-value and must be labelled accordingly.

This needs correction in the manuscript and statistical output.

There is also the more fundamental coordinate problem identified above: calculating Moran's I using 132 station records at only 36 distinct coordinates risks artificially inflating spatial autocorrelation through co-located observations.

**Required:** Recalculate Moran's I after consolidating physically identical coordinates and accounting for study-level dependence. Report the actual permutation p-values separately from asymptotic normal p-values.

### **3.2 Your national prediction model has a predictor-availability problem**

This is a particularly important issue.

The manuscript identifies sediment pH as a significant predictor:

- Pb: mean absolute SHAP 2.35.
- Cu: 4.51.
- Ni: 5.91.
- As: 1.76.

It then applies the champion models to 55,668 river reaches.

But pH measured at published sediment sampling locations is not a standard attribute of HydroRIVERS.

I could find the following nationwide reach-level attributes described in the manuscript:

- Upstream catchment area.
- Average discharge.
- Strahler order.
- Distance to marine outlet.
- Local sub-basin area.

I could not identify a corresponding nationwide sediment-pH dataset or an explicit method for generating pH values at unsampled reaches.

This creates a prediction-time feature problem.

The authors must explain whether pH was:

1. Interpolated spatially.
2. Assigned using river-level averages.
3. Imputed using another environmental dataset.
4. Excluded from the national prediction model.

Each produces different scientific implications.

There must be a reproducible, independent source for every predictor supplied to a nationwide inference model.

The same scrutiny should be applied to sediment grain size, organic matter and other sample-specific properties.

### **3.3 Six-metal ecological risk requires uncertainty propagation**

The manuscript calculates RI using six elements:

\\[ RI=\sum\_{i=1}^{6}T_r^i\frac{C_i}{B_i} \\]

However, the repository's `reach_prediction_uncertainty_summary.csv` reports uncertainty summaries for only three:

- Pb.
- Cr.
- Cd.

There are no corresponding summaries for As, Cu and Ni, and no uncertainty summary for aggregate RI.

This is an important gap because a reach can cross the RI = 600 boundary due to relatively uncertain predictions.

I would require an uncertainty-aware RI classification.

For example:

| Reach classification       | Interpretation                                                            |
| -------------------------- | ------------------------------------------------------------------------- |
| High-confidence high risk  | Probability of RI ≥ 600 is high                                           |
| Uncertain high risk        | Point estimate exceeds 600, but classification uncertainty is substantial |
| High-confidence lower risk | Probability of RI below 600 is high                                       |

Also, clearly identify the index as a six-element adaptation of Hakanson's RI. The original framework's full element composition and reference thresholds should not be assumed automatically interchangeable with a reduced-panel implementation.

### **3.4 The geographical denominator needs clarification**

Paper 1 describes its network extraction using the rectangle:

\\[ 87.5^\circ E-93.0^\circ E \\]

\\[ 20.0^\circ N-27.0^\circ N \\]

This is a bounding extent, not Bangladesh's sovereign polygon.

The manuscript must distinguish between the transboundary analysis domain and the reaches strictly inside Bangladesh.

Otherwise, the term *national distribution* and the 55,668-reach denominator could be misunderstood.

Paper 2 already has a separate country-polygon analysis. Both papers should use consistent geographic definitions.

### **3.5 Novelty: Hydrographic-feature ML versus river-network ML**

I would also challenge the central methodological novelty claim.

Using HydroRIVERS-derived attributes in CatBoost does not automatically establish river-network-aware machine learning.

The described methodology primarily demonstrates feature-engineered ML with:

- Hydrological covariates.
- Geographic coordinates.
- Catchment characteristics.
- Conventional Euclidean geostatistics.

That is valuable, but different from modelling network connectivity directly.

I would either implement a true network-constrained approach or rename the contribution:

*Hydrographic-feature-enhanced spatial machine learning for river sediment contamination.*

That is a scientifically more defensible description.

**Paper 1's essential problem:** The study has more prediction ambition than independent geographical evidence.

## **4. Paper 2 — A confirmed error that changes the main results**

Critical quantitative correction required

**My assessment: Major revision, including recalculation of the dissolved-phase results.**

[Read Paper 2 manuscript](https://github.com/ShMazumder/heavy-metal/blob/main/manuscripts/paper_2_environmental_pollution/main.tex?utm_source=chatgpt.com)

This is the most important new finding from the detailed code audit.

### **4.1 The confirmed dissolved dataset is incorrectly constructed**

The current script contains:

```
df_confirmed_dissolved = df_water[    ~df_water['Study_ID'].isin(['P02', 'P11'])]
```

But the repository's own supplementary study table says:

| Study | Fraction in Supplementary S1 | Correct treatment |
| ----- | ---------------------------- | ----------------- |
| P02   | Filtered (0.45 μm)           | Include           |
| P04   | Filtered (acid digested)     | Include           |
| P06   | Unspecified                  | Exclude           |
| P08   | Filtered (dissolved)         | Include           |
| P09   | Filtered (0.45 μm)           | Include           |
| P11   | Unspecified                  | Exclude           |
| P18   | Filtered (0.45 μm)           | Include           |
| P20   | Filtered (0.45 μm)           | Include           |
| P21   | Filtered (0.45 μm)           | Include           |
| P22   | Filtered (acid digested)     | Include           |
| P27   | Filtered (0.45 μm)           | Include           |
| P28   | Filtered (0.45 μm)           | Include           |

The current script excludes P02, which is explicitly documented as filtered, and retains P06, whose fraction is unspecified.

The correct set, according to the repository's own metadata, should include P02 and exclude P06 and P11.

This is not an interpretation difference. It is a code-to-metadata contradiction.

### **4.2 I recalculated the affected results**

I parsed the actual `water_data.csv` and applied the fraction classifications in `supplement_s1_studies.csv`.

The following comparison uses WHO guideline thresholds.

Current script versus corrected filtered-study membership. Values are recalculations from the repository's CSV files, not independently collected environmental measurements.

| Metal | Current N | Current median | Current exceedance | Correct N | Correct median | Correct exceedance |
| ----- | --------- | -------------- | ------------------ | --------- | -------------- | ------------------ |
| Pb    | 131       | 0.0250         | 84.0%              | 146       | 0.02856        | 85.6%              |
| Cr    | 139       | 0.0630         | 55.4%              | 150       | 0.0705         | 60.7%              |
| Cd    | 117       | 0.00158        | 37.6%              | 126       | 0.001935       | 46.8%              |
| As    | 103       | 0.0133         | 52.4%              | 112       | 0.017495       | 59.8%              |
| Ni    | 89        | 0.0560         | 47.2%              | 98        | 0.1000         | 58.2%              |

Concentrations and medians are in mg/L.

This has important implications.

The paper currently reports Pb dissolved median around 0.025 mg/L and 84.0% exceedance.

Under the supplementary table's stated classification, the corrected subset produces approximately 0.02856 mg/L and 85.6%.

The changes are particularly substantial for Cd, As and Ni.

The paper's overall conclusion that dissolved-phase contamination exists is not necessarily invalidated. But the numerical results supporting that conclusion are not reliable in the current version.

**This entire sensitivity analysis must be regenerated, including the abstract, graphical abstract, tables, figures and manuscript result macros.**

Source files:

- [P2 reproducibility script](https://github.com/ShMazumder/heavy-metal/blob/main/scripts/paper_2/reproduce_paper_2_results.py?utm_source=chatgpt.com)
- [Supplementary S1 study metadata](https://github.com/ShMazumder/heavy-metal/blob/main/data/derived/paper_2/supplement_s1_studies.csv?utm_source=chatgpt.com)
- [Water dataset](https://github.com/ShMazumder/heavy-metal/blob/main/data/processed/water_data.csv?utm_source=chatgpt.com)

### **4.3 The non-detect classification is also wrong**

The manuscript claims that the three non-detect observations (two As and one Cd) all come from ICP-MS investigations with sub-μg/L detection limits.

I checked the actual zero-valued records.

| Observation | Study | Metal | Instrument in S1 |
| ----------- | ----- | ----- | ---------------- |
| OBS_0210    | P11   | As    | AAS              |
| OBS_0213    | P11   | As    | AAS              |
| OBS_0142    | P08   | Cd    | Flame-AAS        |

None of these three entries belongs to the claimed ICP-MS group.

P11 also has an unspecified water fraction, while P08 is marked as filtered dissolved water.

This invalidates the present description of the non-detects as uniformly high-sensitivity ICP-MS measurements.

There is a related dataset problem: the delivered water CSV stores these values as zero but does not provide an observation-level censored flag or numerical LOD.

The supplementary file contains categorical LOD information (`Yes`, `No`, `Yes (BDL defined)`), but not the actual per-element detection-limit values required to reproduce the claimed censoring treatment.

The paper needs an observation-level metadata structure containing:

- Original reported value.
- Original unit.
- Harmonized concentration.
- Analytical fraction.
- Detection limit.
- Quantification limit.
- Censored/non-detect flag.
- Source table and page.

Without that, the treatment of non-detects cannot be independently audited.

### **4.4 High-sensitivity instrumentation does not establish measurement independence**

The paper compares GF-AAS/HG-AAS/ICP-MS results against Flame-AAS results using Mann-Whitney tests.

This is not a clean validation of analytical accuracy.

Different instrument groups correspond to different investigations, potentially with different:

- Rivers.
- Sampling years.
- Sampling seasons.
- Water fractions.
- Industrial exposure conditions.

Consequently, a lower median in one instrument group cannot automatically be attributed to its measurement sensitivity.

There is also a discrepancy between the claim that high-sensitivity instruments achieved detection limits below 0.001 mg/L and Supplementary S1, where several GF-AAS, HG-AAS and ICP-MS studies have `DL_Reported = No`.

The authors need actual study- and element-specific detection limits, or must soften the claim.

### **4.5 Hazard Quotient terminology needs correction**

The manuscript defines:

\\[ HEI=\sum_i\frac{C_i}{S_i} \\]

and then:

\\[ HQ\_{\mathrm{mean}}=\frac{HEI}{4} \\]

The script implements exactly this relationship.

This is a mean normalized concentration-to-guideline ratio, not a conventional human-health hazard quotient based on exposure dose relative to a toxicological reference dose.

A standard exposure-based hazard quotient requires exposure estimation, such as average daily dose, and an appropriate reference dose.

I recommend renaming this quantity to something like:

**Mean Core-4 benchmark-normalized concentration ratio.**

Do not present it as an independent toxicological risk assessment without the required exposure calculations.

### **4.6 The HPI derivation is a useful contribution, with limitations**

I find the mathematical analysis more defensible than the paper's broader novelty claims.

The derivation:

\\[ W_iQ_i=100\frac{C_i}{S_i^2} \\]

is correct for the selected Prasad–Bose formulation.

It explains why low-guideline metals such as Cd and Pb dominate the index.

The manuscript also correctly acknowledges that HEI and MI are algebraically equivalent under the identical standard values used in its implementation.

However, this remains a methodological critique and sensitivity analysis, not a new pollution index.

It should be presented as a critical assessment of index behaviour rather than an entirely new mathematical framework.

### **4.7 Monitoring gap: the geometric calculation needs redesign**

The Paper 2 script has several limitations:

1. It uses a reach's arithmetic midpoint to represent the entire reach.
2. It counts the entire reach length as covered or uncovered based on midpoint distance.
3. Its country-boundary selection uses midpoint-in-polygon rather than exact line-geometry clipping.
4. It selects random river reaches uniformly by reach count, not proportional to river length.
5. It treats the 23 unique monitoring coordinates as independent random locations, without preserving study-level spatial clustering.

The algorithm therefore estimates a particular centroid-based coverage statistic, not an exact percentage of network length within a monitoring buffer.

The manuscript needs to describe it as an approximation or rebuild it using geometric buffer intersections and a justified spatial null model.

There is also a minor but revealing reproducibility error:

- The script's comments and output label refer to 24 random sites.
- The actual coordinate table contains 23 unique monitoring coordinates.
- The code takes the number from the computed coordinate list, so the label is stale.

For the empirical p-value, 1,000 simulations cannot justify a reported p-value below 0.0001 using the standard Monte Carlo estimator. If zero simulated values are as low as the observation, use the appropriate plus-one correction, approximately \\(p=0.001\\).

### **4.8 A more positive point: seasonal HKSJ implementation**

I checked the actual seasonal-analysis code against the previous review concerns.

The implementation does include:

\\[ Q\_{\mathrm{HK}}/(k-1) \\]

with a lower bound of 1, followed by a Student-t critical value.

That is a modified Hartung-Knapp approach. I would not classify it as merely replacing a normal critical value with a t critical value without variance adjustment.

However, the paired evidence remains weak: only 3–5 investigations contribute to individual metal contrasts, and the confidence intervals span unity.

The current paper is right to avoid claiming statistically established seasonal differences. The descriptive pre-monsoon arsenic pattern should also remain exploratory; the groundwater irrigation mechanism has not been causally demonstrated.

## **5. Paper 3 — The meta-analysis is not sufficiently defensible**

Do not submit

[Read Paper 3 manuscript](https://github.com/ShMazumder/heavy-metal/blob/main/manuscripts/paper_3_systematic_review/main.tex?utm_source=chatgpt.com)

### **5.1 The publication window is demonstrably violated**

Paper 3 states that the literature search ended on 31 March 2024.

However, the 28-study catalog contains P12:

*Ahmed et al. (2025), Journal of Trace Elements and Minerals*, DOI:

`10.1016/j.jtemin.2025.100220`

This study was published in 2025, with the article available online on 25 February 2025 and appearing in the June 2025 volume. Its underlying samples were collected in 2021.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

sciencedirect.com+1



P12 contributes six sediment records to the repository.

Therefore, the sampling period and publication period have been conflated.

This study could legitimately be included in a 2025 dataset, but it cannot have been identified through a search that ended in March 2024.

**Either update the systematic-review search and PRISMA flow or exclude the study from the review's eligible corpus.**

### **5.2 PRISMA screening is not reproducible**

The Paper 3 script hardcodes:

```
prisma_counts = {    'Identified_Records_Databases': 1420,    'Duplicates_Removed': 582,    'Screened_Titles_Abstracts': 838,    'Excluded_NonFlvial_OffTopic': 764,    'FullText_Articles_Retrieved': 74,    'Excluded_Methodological_Deficits': 46,    'Included_Studies_Total': 28}
```

The arithmetic is internally consistent.

But I cannot find the actual 1,420-record search export, complete duplicate-removal log, screening decisions or the 46 individually documented full-text exclusions.

A PRISMA diagram generated from fixed constants is not a reproducible PRISMA screening workflow.

The eligibility definitions also conflict with the study allocation:

- The manuscript requires quantitative heavy-metal measurements.
- Its included corpus contains five physicochemical-only studies.
- It also counts sediment-only investigations in the same overall inclusion total.

A multi-matrix review can legitimately have separate sediment, water-metal and ancillary physicochemical branches. But the PRISMA flow must explicitly show those branches and their distinct eligibility rules.

### **5.3 The meta-regression is a record-level logistic regression**

The manuscript labels the method a multivariable meta-regression.

The implementation actually uses:

```
LogisticRegression(penalty='l2', C=10.0)
```

on individual sample records, followed by study-level cluster bootstrap resampling.

That can be a useful exploratory model, but it is not equivalent to a conventional random-effects meta-regression of study-level effect estimates.

It does not adequately model the hierarchical study structure through random effects.

The independent study counts are only 9–12 for the different metals.

The model includes four predictors:

- Instrument sensitivity.
- Urban industrial corridor.
- Dry season.
- Pre-monsoon season.

This is too ambitious for the available independent study clusters.

### **5.4 The only nominally significant result disappears after multiple-testing correction**

Paper 3 reports:

| Parameter        | Result     |
| ---------------- | ---------- |
| Metal            | Cr         |
| Predictor        | Dry season |
| OR               | 2.77       |
| 95% CI           | 1.15–28.54 |
| Reported p-value | 0.026      |

However, the analysis generates 20 coefficients/tests across five metals and four covariates.

Applying a Holm correction to the reported p-values gives:

\\[ p\_{\mathrm{adjusted}}=0.52 \\]

for the smallest observed p-value.

Thus, none of the 20 associations remains significant under this correction.

The manuscript's designation of dry-season chromium as an independently significant driver is not robust.

### **5.5 The regression reference category is incorrectly described**

The code maps:

- Winter → dry.
- Rainy → wet.
- Summer/Spring → pre-monsoon.
- Late Autumn → post-monsoon.
- Missing or other values → unclassified.

But it then creates:

```
Season_Dry = 1 if dry else 0Season_Premonsoon = 1 if pre_monsoon else 0
```

Consequently, the reference category includes wet, post-monsoon and unclassified observations.

The manuscript describes it as monsoon wet season only.

That is a model specification and reporting mismatch.

The unclassified observations should be excluded or handled as an explicit category.

### **5.6 Independent literature review has moved ahead of this paper**

There is already a substantial 2025 review by Proshad et al. examining Bangladeshi surface-river water metals from 2012–2022.

It aggregates 648 samples across 24 rivers and examines multiple pollution indices, source patterns and health risks.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://doi.org\&sz=32)

doi.org



Paper 2 acknowledges this study, which is good.

But Paper 3 needs to position its independent contribution much more carefully. A second multi-matrix review cannot claim novelty merely by expanding the number of tables and applying another regression.

I would reposition Paper 3 around:

**Analytical heterogeneity, evidence quality and uncertainty in cross-study heavy-metal contamination estimates across water and sediment systems.**

That is a more distinctive scientific question.

## **6. Paper 4 — The dataset is valuable, but the descriptor is not ready**

Major data-quality revision

[Read Paper 4 manuscript](https://github.com/ShMazumder/heavy-metal/blob/main/manuscripts/paper_4_data_descriptor/main.tex?utm_source=chatgpt.com)

This remains one of the most strategically worthwhile outputs, but it needs a much stronger technical description.

### **6.1 The summary statistics are correct**

I independently recalculated the water and sediment descriptive statistics from the processed CSV files.

The table's sample counts, medians, means, IQRs, minima and maxima match the underlying data to the reported precision.

This is a positive finding.

### **6.2 The geospatial manifest overstates completeness**

The data descriptor says that all stations were snapped to HydroRIVERS reaches.

However, `stations.csv` contains:

- 426 station records.
- 220 resolved coordinates.
- 206 unresolved coordinates.

The descriptor should explicitly distinguish:

- Station records.
- Unique physical locations.
- Unique coordinate pairs.
- Successfully georeferenced stations.
- Successfully matched HydroRIVERS reaches.

The present wording makes the spatial completeness appear stronger than it is.

### **6.3 Important machine-readable measurement metadata is missing**

The descriptor refers to detailed measurement provenance and censoring information.

Yet the processed CSV structure does not expose the required observation-level fields:

- Raw analytical value.
- Original raw measurement unit.
- Numerical LOD.
- Numerical LOQ.
- Censored flag.
- Per-observation water fraction.
- Source table/page reference.

Some methodological information exists in separate supplementary tables, but those do not replace observation-level metadata.

This is particularly problematic for studies combining filtered/unfiltered samples or reporting non-detects.

A researcher should be able to query a sample and identify the original analytical result and its operational definition without manually reopening the PDF.

### **6.4 The extraction-validation confidence interval is incorrect**

Paper 4 reports zero discrepancies across 112 assays and a 95% Wilson interval of 0.0–2.8%.

For 0 discrepancies among 112 independent observations, the conventional two-sided 95% Wilson upper limit is approximately 3.3%, not 2.8%.

There is a further issue: those 112 records are drawn from only six articles.

The independence assumption underlying an ordinary 112-observation Wilson interval is questionable.

Report the number of sampled source articles, the sampling procedure, and the article-level clustering. Do not present an artificially narrow uncertainty interval as proof of perfect extraction quality.

### **6.5 The format manifest is not consistent with the repository**

The manuscript and Zenodo metadata refer to Parquet distribution.

There are no `.parquet` files in the current Git tree, and the Zenodo packaging script does not generate or package Parquet files.

Either supply the advertised files or remove the claim.

### **6.6 Zenodo availability is not yet established**

The launch checklist describes DOI `10.5281/zenodo.24414976` as reserved and explicitly instructs the authors to keep the deposit in Draft.

Yet Paper 4's Data Availability section describes the dataset as publicly accessible without restriction.

A reserved DOI and a publicly released data record are not the same thing.

Publish the deposit or provide an appropriate reviewer-access mechanism before claiming unrestricted public availability.

### **6.7 Licensing and provenance**

The repository claims MIT licensing for code, but the current root tree has no `LICENSE` file.

It also assigns CC-BY 4.0 to the dataset package. This needs to be carefully separated from the rights associated with third-party source PDFs and geospatial materials.

HydroSHEDS explicitly specifies product-specific licence and attribution conditions for HydroRIVERS. Its current product documentation permits scientific, educational and commercial use, subject to those terms.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.hydrosheds.org\&sz=32)

hydrosheds.org+1



The 28 primary research PDFs in `data/raw/source_pdfs/` also need individual redistribution-rights verification.

This is a repository-distribution issue, not necessarily a problem with using those articles as research sources.

## **7. Conference papers and publication integrity**

The conference papers currently look too close to journal-manuscript derivatives.

I compared the actual Git blob hashes of the figures.

**Verified figure duplication**

Paper 1 vs Conference 1

Identical

SHAP figure and ecological-risk map have identical Git blob hashes.

Paper 2 vs Conference 2

Identical

Exceedance, seasonal dilution and spatial coverage figures have identical Git blob hashes.

This does not automatically constitute duplicate publication. A conference paper can be an earlier, shorter publication of work that is subsequently extended into a journal paper, provided the applicable policies are followed.

However, the conference contributions should contain a clear, differentiated contribution and the authors must disclose the relationship.

### **Conference 1 — IGARSS**

The existing paper mostly restates the sediment ML work.

I do not find a sufficiently developed satellite Earth-observation contribution to justify its current positioning as a distinctive IGARSS study.

Adding satellite-derived land use, industrial growth, upstream land-cover metrics or remote-sensing-assisted monitoring would help.

### **Conference 2 — IWA World Water Congress**

There is a venue-format mismatch.

The README and launch checklist identify IWA World Water Congress, but the manuscript uses:

```
\documentclass[conference]{IEEEtran}
```

and IEEE author blocks.

The conference package must be matched to the actual target.

A stronger IWA contribution would be an operational monitoring-network design, not another compressed version of the journal's benchmark-exceedance figures.

### **Six deliverables versus two-paper architecture**

There is also an unresolved strategy conflict:

- README: four journal articles and two conference papers.
- `docs/publication_plan.md`: a two-paper publication architecture.
- `docs/publication_launch_checklist.md`: plans to submit four journal papers.

The research programme needs one authoritative publication strategy.

Finally, the launch checklist explicitly states that the six manuscript review packages are internal LLM reviews (Claude, ChatGPT and Gemini), not actual journal peer-review reports.

That is a useful transparency statement, but these reviews should not be treated as independent external peer review.

# **8. Final revised scorecard**

The ratings below reflect the direct data and code checks, including the new Paper 2 subset error.

| Research output             | Score / 10 | Editorial recommendation                           |
| --------------------------- | ---------- | -------------------------------------------------- |
| Paper 1 — Sediment ML       | 3.0        | Reject current version; rebuild spatial validation |
| Paper 2 — Water synthesis   | 4.5        | Major revision; recalculate key results            |
| Paper 3 — Systematic review | 2.0        | Reject/reframe; redesign review and regression     |
| Paper 4 — Data descriptor   | 4.0        | Major technical and data-quality revision          |
| Conference 1 — IGARSS       | 2.0        | Develop genuinely new EO contribution              |
| Conference 2 — IWA          | 2.0        | Reposition and correct venue formatting            |

# **3.0 / 10**

**Overall current publication readiness**

Reviewer judgment, not a statistical measure.

**The research programme is worth continuing. The current manuscripts are not ready for the proposed journal submissions.**

# **9. My recommended order of work**

I would stop manuscript polishing temporarily and execute these corrections in this order.

P0 — Immediate

**Correct Paper 2's dissolved-phase dataset.**

Fix the P02/P06 membership, recalculate all metal statistics and identify the actual non-detects. Correct all corresponding manuscript and presentation values.

P0 — Immediate

**Reconstruct the sediment spatial sampling database.**

Verify P14 and P18 coordinates against the original papers, distinguish study-level coordinates from station GPS coordinates, and group true co-located observations.

P0 — Immediate

**Publish the complete Paper 1 analysis pipeline.**

Supply the actual training, spatial-fold construction, hyperparameter selection, feature processing and prediction scripts. Include the pH input source and uncertainty-propagation procedure.

P1 — High

**Rebuild the systematic-review evidence pipeline.**

Update the PRISMA window, resolve the 2025 P12 inclusion, publish the 46 full-text exclusions, and introduce proper multi-matrix selection branches.

P1 — High

**Rebuild the monitoring-gap calculation.**

Use exact river geometry, a length-aware null model and corrected Monte Carlo inference. Reconcile candidate primary studies against broader published reviews.

P1 — High

**Reframe Paper 3's regression.**

Remove unsupported contamination-driver conclusions. Apply multiplicity adjustment and use a defensible hierarchical or study-level meta-analytic design.

P2 — Before submission

**Complete Paper 4's metadata, validation and licensing.**

Publish actual LOD/censoring fields, accurate coordinate-quality statistics, the missing distribution formats, valid Zenodo access and author metadata.

P2 — Before submission

**Consolidate the publication portfolio.**

Decide which papers are genuinely independent and remove conference/journal overlap that does not meet the respective venue policies.

## **10. My final judgment**

There is one thing I would preserve at almost any cost: the underlying national literature-derived research database.

That is the strongest foundation for this entire programme.

However, the current repository has a recurring scientific problem:

**The number of observations, the number of spatial locations, the number of independent studies and the number of validated prediction locations are repeatedly treated as though they represent equivalent evidence.**

They do not.

This affects the spatial ML, Moran's I, risk mapping, regulatory exceedance calculations and national surveillance estimates.

The current manuscripts also need to distinguish three different things:

1. What the original published studies actually measured.
2. What the repository successfully extracted and harmonized.
3. What the models infer beyond the measured locations.

That distinction should become the organizing principle of the research programme.

I would not submit all four journal papers in their present forms. I would concentrate on correcting the database, rebuilding Paper 1's spatial evidence, and recalculating Paper 2. Those corrections will determine whether the other manuscripts have independent publication value.

**Review scope:** I inspected the current `main` commit dated 21 November 2026, the processed CSV datasets, manuscript sources, visible analysis scripts, derived results and publication documentation. I independently recalculated the descriptive statistics, coordinate counts, and corrected dissolved-subset comparisons. I did not execute the complete SQLite/GeoPackage and ML inference pipelines. In particular, the absence of the Paper 1 implementation prevents me from independently validating its national predictions.

The most useful next deliverable would be a **forensic correction ledger**, mapping every confirmed problem to the exact source row, script, manuscript section and recalculation required before submission.