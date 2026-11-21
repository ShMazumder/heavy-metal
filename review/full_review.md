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