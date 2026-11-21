Yes—this is a scientifically valid research direction, and the two-paper structure is sensible. However, the current plan is not yet methodologically strong enough to execute unchanged or to guarantee a defensible national prediction map. I would approve it as a revised research framework, subject to several important changes.

The strongest idea is the separation between:
1. Phase 1: a systematic review that builds a harmonized, georeferenced evidence database; and
2. Phase 2: a separate modelling study using only observations sufficiently reliable for spatial prediction.
That separation is explicit in your document and is the right foundation. The eligibility rules, site-level extraction, separation of water and sediment, coordinate-confidence levels, and warning against mapping poorly sampled areas as confirmed hotspots are also good decisions (pages 1–2 and 4–5).
1. The biggest issue: novelty of Paper 1
A general systematic review of heavy-metal contamination in Bangladesh’s rivers is now a difficult publication proposition.

Two directly relevant reviews already exist:
- A 2024/2025 review examined 55 documents on heavy metals in Bangladesh's rivers, focusing on river-water contamination over 2001–2020. It covered ten metals. 
  
  pubmed.ncbi.nlm.nih.gov
- A December 2025 review synthesized 100 studies covering soil, water, plants, and river sediments across Bangladesh for 2010–2024. 
  
  doi.org
Your proposed Paper 1 therefore needs to contribute something substantially different from another summary of metal concentrations, polluted rivers, and contamination hotspots.

My recommended positioning:
Can published research on Bangladesh's rivers support reliable national-scale spatial assessment of heavy-metal contamination?

The review should investigate:
- How many published measurements can actually be georeferenced reliably?
- How representative are the observations across rivers, basins, districts, and sampling years?
- How comparable are the laboratory methods, digestion procedures, detection limits, and measurement fractions?
- How much of the published evidence is suitable for GIS and predictive modelling?
- What geographical areas and periods are poorly represented?
- Are existing contamination and ecological-risk conclusions supported by the available evidence?
This makes the paper a critical assessment of the quality, coverage, and modelling readiness of the evidence, rather than another general contamination review.

A suitable revised title would be:

Can Published Evidence Support National-Scale Mapping of Heavy-Metal Contamination in Bangladesh's Rivers? A Systematic Evidence Map of Spatial Coverage, Analytical Comparability, and Data Quality.
2. My assessment of Phase 1
Strong foundation
The data extraction categories and harmonization principles are sensible. In particular, separating water and sediment, retaining sampling year, recording coordinate confidence, and not treating river-wide average concentrations as individual sampling points are all important decisions. 
research plan.docx

However, I would change the eligibility framework.
Separate review eligibility from modelling eligibility
Your current criteria require individual sampling-site concentrations and usable location information, although you also intend to retain some aggregate-only studies for narrative review.

Formalize this into three levels:
Level	Eligibility	Use
A. Review eligible	Relevant Bangladesh river-water or sediment research reporting metal measurements	Systematic evidence synthesis
B. Database eligible	Individual site/campaign measurements with identifiable sampling context	Harmonized evidence database
C. Spatial-model eligible	Reliable coordinates, concentration data, time information, and suitable analytical metadata	GIS and ML

This distinction is important. A study should not disappear from the systematic review simply because its locations cannot be geocoded accurately.

Also, a district name is not equivalent to a sampling-site coordinate. Do not assign a district centroid and present it as an actual monitoring location. Preserve the original location description and record the uncertainty of any reconstructed coordinates.
Strengthen the extraction database
Your proposed site-level fields are a good starting point, but I recommend a relational structure:
Study
Publication, DOI, authors, source and study quality

Sampling campaign
Year, season, sampling design and campaign identity

Sampling station / sample
Location, coordinates, precision, date and sample identity

Analytical measurements
Metal, concentration, unit, fraction, instrument, digestion, LOD/LOQ and QA/QC

This structure will help prevent repeated measurements from being mistaken for independent sampling locations.

I would also add:
- Exact source of each extracted value: table, page, supplementary file, or digitized figure.
- Sample depth and sampling type, where available.
- Total versus dissolved water-metal concentrations.
- Sediment digestion/extraction method and dry-weight basis.
- Limit of detection (LOD), limit of quantification (LOQ), and non-detect status.
- Replicate counts and reported measurement uncertainty.
One particularly important issue: non-detect values should be stored as censored observations with their detection limits, not silently converted to zero. Substituting arbitrary numerical values can bias environmental concentration analyses. 

pmc.ncbi.nlm.nih.gov+1

Make the review reproducible
The document does not yet describe a complete systematic-review protocol. Before screening, specify the databases, exact search strings, search dates, eligibility rules, duplicate handling, independent screening procedure, extraction process, and critical appraisal method.

I recommend using:
- PRISMA 2020 for systematic-review reporting. 
  
  bmj.com
- ROSES for environmental systematic evidence synthesis. 
  
  Environmental Evidence
- CEE evidence-synthesis guidelines for protocol preparation, search comprehensiveness, screening, critical appraisal, and synthesis. 
  
  Environmental Evidence+1
Register or publicly deposit the protocol before the main screening and extraction work.
3. My assessment of Phase 2
Promising, but needs methodological safeguards
The proposed predictors, separate water/sediment models, concentration-level prediction targets, and spatial-validation approach are appropriate starting points. 
research plan.docx

However, I see six important issues.
A. The 100-observation rule is not a scientific threshold
Your document recommends approximately 100 observations per metal-medium model and exploratory analysis with 30–60 observations. 
research plan.docx

These can be preliminary planning heuristics, but they are not universal sample-size requirements.

Consider this example:
Dataset	Raw observations	Independent spatial locations	Number of studies
A	150	25	3
B	100	85	20

Dataset A has more measurements, but many may represent repeated measurements from a small number of sites and studies. Dataset B may provide much stronger evidence for spatial generalization.

Therefore, assess:
- Unique sampling locations.
- Independent river reaches and catchments.
- Number of contributing studies.
- Geographic distribution.
- Number of usable independent spatial validation groups.
I would replace the fixed threshold with a feasibility assessment based on these quantities, supplemented by learning curves or simulation where appropriate.
B. Spatial validation must be stricter
Your spatial block cross-validation proposal is good. However, I recommend three validation experiments:
Validation strategy	What it tests
Spatial-block CV	Prediction in geographically separated areas
Leave-one-river/basin-out	Generalization to rivers or basins not represented in training
Leave-one-study-out	Generalization across independent published studies

This is especially important because several studies may share stations, sampling campaigns, or nearby locations.

Do not randomly divide individual measurement rows into training and testing sets. That could place measurements from the same station or study in both sets and produce misleadingly optimistic performance.

Hyperparameter tuning must also occur inside the training portion of the validation process.
C. Do not use Study ID as an ordinary prediction feature
The plan mentions including study ID and year in the analysis.

Study ID is useful for identifying study-specific differences, grouping observations during validation, and potentially modelling between-study variation. But using it as an ordinary predictor in a national prediction model is problematic: a new location may come from a study never represented during training.

Use study-aware hierarchical modelling or study-level effects where suitable, and test generalization using leave-one-study-out validation. Do not rely on a study identifier that will not be available for future predictions.
D. Improve the GIS predictor design
The proposed land-use buffers and distances to industries are reasonable, but river pollution is influenced by upstream catchment processes.

I would prioritize:
- Upstream catchment land-use proportions.
- Industrial and wastewater sources upstream along the river network.
- Population and urbanization pressure within the contributing catchment.
- Catchment area, elevation, slope, river order, and drainage characteristics.
- Rainfall and seasonal variables aligned with sampling time.
The 1 km, 5 km, and 10 km buffers can be retained as complementary predictors, but they should not replace catchment and river-network analysis.

Most importantly, environmental predictors should be aligned with the sampling year whenever possible. Using current land cover to predict a 2005 metal measurement could introduce temporal mismatch.
E. National prediction maps need an explicit support assessment
This is probably the most important limitation for Paper 2.

Published research observations are usually opportunistic rather than collected through a nationally representative sampling design. The model may learn where researchers chose to sample rather than the actual national distribution of contamination.

Consequently:
- Map the sampling locations and their density before presenting prediction maps.
- Identify geographic areas beyond the support of observed data.
- Restrict prediction to the relevant river network.
- Produce uncertainty maps and extrapolation masks.
- Avoid interpreting an unobserved area as uncontaminated or contaminated simply because the model predicts a value there.
Your document already recognizes that poorly sampled areas should not be shown as confirmed hotspots. I would make this a formal modelling constraint, not just a reporting recommendation. 
research plan.docx

F. Add appropriate statistical baselines
Random Forest, XGBoost, and SVR are reasonable candidates, but comparing only ML algorithms is insufficient.

Include suitable baseline models, such as:
- Simple mean or study/river-level baseline.
- Linear or regularized regression.
- Generalized additive model, where appropriate.
- Kriging or regression kriging where spatial sampling and variogram assumptions support it.
Report R², RMSE, MAE, and bias, but also prediction-interval coverage and uncertainty. Consider log-scale modelling if concentrations are strongly right-skewed, while reporting interpretable performance on the original concentration scale.

Your existing proposed workflow is a good beginning, but it needs these safeguards. 
research plan.docx

4. A few changes to the two-paper structure
I support publishing two separate papers from this project, provided their research questions and contributions are genuinely distinct.
	Paper 1	Paper 2
Main contribution	Systematic evidence map and quality assessment	Spatial prediction and uncertainty analysis
Main question	Can the published evidence support reliable spatial assessment?	Can harmonized observations support defensible predictions?
Main methods	Systematic search, extraction, critical appraisal, geospatial coverage analysis	GIS, spatial statistics, ML and spatial validation
Main output	Reusable evidence database and evidence-gap assessment	Validated prediction models and uncertainty maps

I would revise the second title to avoid promising national-scale prediction before you establish feasibility:

Spatial Prediction of Selected Heavy Metals in Bangladesh's River Networks Using Harmonized Published Observations: A Spatially Validated Machine-Learning Approach

Only retain the national-scale claim after the evidence demonstrates adequate spatial and temporal coverage.

Also, treat HPI, PLI, and PERI as optional downstream assessments, not automatically as additional ML targets. Their interpretation depends on appropriate standards, background values, and matrix-specific definitions. Distinguish ambient surface-water criteria from drinking-water standards; they are not interchangeable.
5. Recommended final workflow
1. Stage 1 — Novelty and feasibility audit
   
   Compare the existing reviews, prepare a gap matrix, and run a pilot search. Confirm that the critical evidence-quality and geospatial-readiness focus is genuinely distinct.
2. Stage 2 — Protocol and database design
   
   Define review eligibility, modelling eligibility, protocol, extraction schema, quality appraisal, and coordinate-confidence framework.
3. Stage 3 — Systematic review and evidence database
   
   Search comprehensively, screen independently, extract all eligible studies, and distinguish review-only, database-eligible, and model-eligible observations.
4. Stage 4 — Spatial feasibility assessment
   
   Quantify independent stations, rivers, studies, sampling periods, spatial gaps, and metal-medium-specific sample support.
5. Stage 5 — Modelling go/no-go decision
   
   Select only the metal-medium combinations with adequate evidence. Choose national, basin-level, or exploratory modelling according to the actual evidence.
6. Stage 6 — Separate manuscripts
   
   Submit the evidence-map/review paper and subsequently the spatial modelling paper, with transparent cross-referencing and no duplicated results.

Final verdict
Valid research direction
My assessment of the uploaded five-page plan
Component	Verdict
Two-phase research architecture	Strong
Data extraction and harmonization	Good foundation
Systematic review eligibility	Revise
Review novelty	Critical risk
GIS predictor strategy	Improve
ML validation design	Strengthen
National-scale prediction claim	Conditional
Two-paper publication strategy	Sound


My recommendation: Proceed with this plan, but do not start extracting hundreds of records under the current criteria yet. First, finalize the novelty question, the three levels of eligibility, the database architecture, and the spatial validation strategy.

The critical distinction is that Paper 1 must establish whether the evidence is reliable and sufficiently representative; Paper 2 must demonstrate whether that evidence can actually predict concentrations in places that were not used to train the model.

That would make this a much stronger and more defensible research programme than simply applying Random Forest or XGBoost to published heavy-metal measurements.