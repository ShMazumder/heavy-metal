# **Comprehensive Research Evaluation and Methodological Roadmap**

**Proposed research title:**

*Spatial Prediction of Heavy Metal Contamination in Rivers of Bangladesh Using Geospatial Analysis and Machine Learning*

My recommendation is to retain the research topic but substantially strengthen its scientific design before proceeding with model development.

The research has a potentially valuable contribution: consolidating fragmented heavy-metal measurements from published studies across Bangladesh, integrating them with geospatial and environmental information, identifying contamination hotspots, and developing spatial prediction models to support environmental monitoring and policymaking.

However, there is one fundamental methodological issue:

**Predicting the 2026–2027 heavy-metal concentration from historical measurements is not the same as predicting its spatial distribution.**

These are two different scientific problems, requiring different datasets, assumptions, validation strategies, and modelling approaches. The research should distinguish them rather than treating them as one ML task.

I have also examined the uploaded `Final Data Table.xlsx`. The assessment below combines the actual dataset structure with a proposed research methodology.

# **1. Critical evaluation of the research idea**

## **1.1 Research strengths**

There are several worthwhile aspects of the proposed research.

| Research component                     | Scientific value                                         |
| -------------------------------------- | -------------------------------------------------------- |
| Literature-based data compilation      | Consolidates fragmented environmental measurements       |
| Bangladesh-wide geographical coverage  | Allows identification of regional contamination patterns |
| Water and sediment analysis            | Provides complementary perspectives on contamination     |
| Multiple heavy metals                  | Enables element-specific contamination assessment        |
| Potential pollution-source integration | Adds environmental and policy relevance                  |
| Machine learning and GIS               | Enables spatial modelling and visualization              |
| Future scenario development            | Potentially supports environmental planning              |

One particularly important aspect is the integration of sediment and water measurements.

Heavy metals in river water represent dissolved and suspended concentrations at the sampling time, whereas sediment can act as a longer-term repository of accumulated metals. These measurements should not be treated as interchangeable indicators.

## **1.2 Major scientific weaknesses and risks**

**Issue 1: Temporal prediction without sufficient temporal observations**

Critical

If most sampling locations were measured only once or during one sampling campaign, an ML model cannot reliably learn how concentrations change over time.

A model trained on measurements from 2010–2022 cannot automatically predict 2026 or 2027 merely because the year is included as a feature.

**Recommendation:** Separate spatial prediction from temporal forecasting. Treat future-year predictions as exploratory scenarios unless repeated temporal observations are available.

**Issue 2: Heterogeneous literature-derived measurements**

Critical

Different publications may use different digestion procedures, analytical instruments, detection limits, sampling depths, filtration protocols, and reporting units.

**Recommendation:** Develop a measurement harmonization and quality-control protocol before modelling.

**Issue 3: Spatial coverage and representativeness**

Critical

Measurements concentrated around industrial rivers and urban centres may not represent the entire river network of Bangladesh.

**Recommendation:** Quantify spatial sampling bias and report prediction uncertainty. Do not claim nationwide representativeness without demonstrating it.

**Issue 4: Water and sediment data integration**

Critical

Water and sediment concentrations have different units, distributions, environmental processes, and interpretation.

**Recommendation:** Develop separate modelling pipelines for water and sediment.

**Issue 5: Pollution-source attribution**

High

Proximity to an industrial area does not establish that the industry caused the observed contamination.

**Recommendation:** Use source-proximity variables as explanatory predictors, not proof of causation. Combine them with hydrological connectivity, upstream–downstream comparisons, and source-specific evidence.

**Issue 6: Spatial data leakage**

Critical

Randomly splitting sampling stations into training and testing datasets can produce overly optimistic performance because nearby observations are spatially correlated.

**Recommendation:** Use spatially blocked cross-validation and independent river-level or geographical holdouts.

## **1.3 What should the actual research contribution be?**

I would position the contribution around four scientific objectives:

1. **National-scale evidence synthesis:** Develop a harmonized geospatial database of historical heavy-metal contamination in Bangladesh's rivers.
2. **Spatial contamination modelling:** Identify and predict spatial patterns of selected heavy metals in water and sediment.
3. **Environmental driver analysis:** Investigate relationships between contamination and industrial, urban, agricultural, hydrological, and geochemical factors.
4. **Uncertainty-aware scenario assessment:** Identify areas that may require additional monitoring and evaluate plausible future contamination scenarios where the evidence supports them.

This is a stronger and more defensible contribution than simply training several ML algorithms and displaying predicted concentrations on a map.

# **2. Preliminary audit of the uploaded dataset**

Workbook inspected

# **557**

Data records (excluding header)

# **28**

Paper identifiers

# **12**

Distinct named rivers

# **10**

Heavy-metal variables

# **259**

Sediment records

# **258**

Water records

Counts are based on the current spreadsheet entries. They are not necessarily independent sampling locations or independent measurements.

## **2.1 Dataset coverage**

The workbook contains measurements associated with the following rivers:

| River              | Records |
| ------------------ | ------- |
| Karnaphuli         | 142     |
| Buriganga          | 100     |
| Rupsa              | 53      |
| Surma              | 27      |
| Turag              | 23      |
| Padma              | 21      |
| Paira              | 17      |
| Korotoa            | 13      |
| Old Brahmaputra    | 5       |
| Meghna             | 3       |
| Shitalakhya        | 3       |
| Kirtankhola        | 1       |
| Missing river name | 149     |



Important

&#x20;The dataset currently has substantial geographical concentration. Karnaphuli and Buriganga alone account for 242 records, approximately 43.4% of the dataset.



Consequently, the current dataset should not yet be described as a representative national river-monitoring dataset.

## **2.2 Heavy-metal availability**

Number of records containing a reported concentration for each heavy metal, out of 557 records.

0150300450600PbCrCdAsCuNiZnFeMnCo

The six strongest candidates based on simple availability are:

- Lead (Pb)
- Chromium (Cr)
- Cadmium (Cd)
- Arsenic (As)
- Copper (Cu)
- Nickel (Ni)

However, availability alone is insufficient for selecting target metals.

For example, Pb has 445 observations overall, but those observations may be concentrated in a few rivers, studies, or sample types. A metal with fewer observations may actually have better geographical coverage.

**My initial recommendation:** Evaluate Pb, Cr, Cd, As, Cu, and Ni as candidate targets. Consider Zn as a secondary target. Fe and Mn should be assessed separately because of their potentially different geochemical controls and limited availability in this dataset. Co currently has insufficient observations for a robust nationwide model.

## **2.3 Water and sediment coverage**

The following is the actual number of non-missing observations by sample type.

| Metal | Sediment | Water |
| ----- | -------- | ----- |
| As    | 220      | 124   |
| Cr    | 264      | 160   |
| Cd    | 244      | 142   |
| Pb    | 264      | 156   |
| Cu    | 210      | 112   |
| Zn    | 73       | 85    |
| Ni    | 210      | 106   |
| Fe    | 35       | 76    |
| Mn    | 32       | 59    |
| Co    | 15       | 15    |

Note that the workbook contains some inconsistent capitalization of `Sediment` and `sediment`, which should be standardized.

The important observation is that the water and sediment datasets have different metal coverage. Separate models are therefore necessary.

## **2.4 Temporal coverage**

The reported sampling years range from 2010 to 2022, but coverage is uneven.

Records by reported sampling year. NR and missing years are excluded from the chart.

02040608020102012201320142015201620172018201920212022

Important observations:

- 2013 has the highest number of records.
- 2018 and 2015 also have substantial representation.
- 2020 has no reported observations.
- 2021 and 2022 have relatively few observations.
- 52 records have an unknown year or an `NR` entry.

This temporal structure is insufficient to establish a consistent national time series.

## **2.5 Major data-quality problems**

| Problem                         | Current finding           | Required action                          |
| ------------------------------- | ------------------------- | ---------------------------------------- |
| Missing river names             | 149 records               | Recover from original publications       |
| Missing latitude                | 252 records               | Georeference sampling locations          |
| Missing longitude               | 254 records               | Georeference sampling locations          |
| Missing sampling year           | 52 records                | Recover or explicitly mark unknown       |
| Missing analytical method       | Most records              | Extract from original papers             |
| Missing water-quality variables | Substantial               | Retain missingness; do not invent values |
| Coordinate formatting           | Inconsistent              | Standardize and validate                 |
| Units                           | Not sufficiently explicit | Verify against source papers             |
| Duplicate station identifiers   | Present across studies    | Create unique sampling IDs               |

One particularly serious issue is the coordinate representation.

Some entries are geographical ranges, such as:

`23° 36′ N–23° 46′ N`

Others are individual coordinates, and some use inconsistent notation.

These cannot simply be converted into latitude and longitude using a basic string replacement. The original publication must be checked to determine whether a coordinate represents a sampling station, a river segment, or a study-area boundary.

### **The most important spreadsheet issue: measurement units**

The spreadsheet has one general header:

`Heavy metal concentration (mg/kg)`

But the workbook contains both water and sediment measurements.

This needs immediate investigation.

- Sediment concentrations are commonly reported as mg/kg dry weight.
- Water concentrations are commonly reported as mg/L or µg/L.
- Some studies may report dissolved concentrations, while others report total or total recoverable concentrations.

If water measurements are incorrectly labelled as mg/kg, the entire modelling pipeline can become scientifically invalid.

Do not perform unit conversion based on assumptions. Return to each source publication.

## **2.6 Another important issue: independent sample size**

There are 557 rows, but there are only 28 paper identifiers.

Furthermore, the spreadsheet has 57 rows involved in repeated combinations of paper number, station number, year, season, and sample type.

These are not necessarily duplicate measurements: they may represent repeated observations or extraction inconsistencies. Each must be checked against its original source.

The effective independent sample size is therefore not 557.

For modelling, the study should identify the hierarchy:

- Publication
- Sampling campaign
- River
- Sampling location
- Sample type
- Measurement
- Analytical replicate, if applicable

Without this hierarchy, models can inadvertently learn publication-specific characteristics rather than genuine environmental patterns.

# **3. Recommended research design**

I recommend organizing the research into two connected but independent modelling tracks.

## **Proposed research architecture**

**Phase 1: Literature-based data compilation**

Historical measurements + geospatial information + environmental covariates

**Phase 2: Data harmonization and quality assurance**

Units, coordinates, sampling periods, sample types, analytical methods

**Track A**

Primary study

**Spatial modelling**

Where is contamination likely to occur?

GIS + spatial ML + spatial validation

**Track B**

Conditional study

**Temporal scenarios**

How might contamination change in the future?

Repeated measurements + temporal models

**Phase 3: Environmental interpretation**

Hotspot identification + pollution-source investigation + uncertainty assessment

**Phase 4: Policy-oriented decision support**

Priority monitoring locations, risk screening, and pollution management recommendations

## **Track A: Spatial prediction of heavy-metal contamination**

This should be the primary research component because it is more compatible with the available historical dataset.

The objective is to estimate the spatial distribution of heavy metals across selected river reaches using observed measurements and environmental predictors.

For example:

- Which river segments have elevated Pb concentrations?
- Which regions are likely to have higher Cr concentrations?
- Are contamination hotspots associated with industrial clusters?
- Can the model identify potentially contaminated locations where no published measurements exist?

The output should be a continuous spatial prediction surface or a river-segment-level prediction map.

However, a prediction for an unsampled location is an estimate, not an actual measurement.

## **Track B: Temporal prediction and future scenarios**

This component should be attempted only if the dataset provides sufficient repeated observations across locations and years.

For a given river location, the model would need observations such as:

| Location | Year | Pb    |
| -------- | ---- | ----- |
| A        | 2012 | 0.025 |
| A        | 2014 | 0.031 |
| A        | 2016 | 0.039 |
| A        | 2018 | 0.047 |
| A        | 2020 | 0.052 |
| A        | 2022 | 0.061 |

These are illustrative values, not measurements from your dataset.

If sufficient observations exist, temporal modelling can estimate changes in concentration.

If not, you should not claim that the model predicts actual 2026 or 2027 concentrations.

Instead, you can produce scenario-based estimates using explicitly stated assumptions about pollution-source activity, land-use change, and other environmental conditions.

# **4. Phase I — Literature review and systematic data extraction**

The first task is to establish a reproducible literature review.

## **4.1 Literature search strategy**

Search the following academic databases:

- Google Scholar
- Scopus
- Web of Science
- ScienceDirect
- SpringerLink
- PubMed

Suggested search queries:

```
("heavy metals" OR "trace metals")
AND ("river water" OR "river sediment")
AND Bangladesh

("metal contamination" OR "metal pollution")
AND Bangladesh
AND (water OR sediment)

(arsenic OR chromium OR cadmium OR lead)
AND Bangladesh
AND river

("heavy metal" AND "machine learning")
AND (river OR freshwater)
AND spatial prediction
```

Include publications that provide:

1. Heavy-metal concentration measurements.
2. Sampling location or identifiable sampling area.
3. Sampling year or period.
4. Sample type.
5. Analytical methods.
6. Sufficient information to determine measurement units.

Do not include papers merely because they discuss heavy-metal contamination without providing usable measurements.

## **4.2 Develop a standardized extraction template**

The existing workbook should be redesigned into a relational dataset rather than continuing to add information to one increasingly complex spreadsheet.

I recommend four linked tables.

**Table A: Publication metadata**

| Field            | Description                   |
| ---------------- | ----------------------------- |
| Paper_ID         | Unique publication identifier |
| DOI              | Digital object identifier     |
| Authors          | Authors                       |
| Publication_Year | Publication year              |
| Journal          | Journal name                  |
| Study_Method     | Research methodology          |
| Data_Source      | Original publication          |

**Table B: Sampling observations**

| Field               | Description                     |
| ------------------- | ------------------------------- |
| Sample_ID           | Unique observation ID           |
| Paper_ID            | Foreign key                     |
| River               | River name                      |
| Station_ID          | Original station identifier     |
| Latitude            | Decimal degrees                 |
| Longitude           | Decimal degrees                 |
| Coordinate_Accuracy | Exact, approximate, or inferred |
| Sampling_Year       | Actual sampling year            |
| Sampling_Date       | If available                    |
| Season              | Winter, summer, monsoon, etc.   |
| Sample_Type         | Water or sediment               |
| Sampling_Depth      | If available                    |
| Replicate_ID        | If applicable                   |

**Table C: Chemical measurements**

| Field                | Description                         |
| -------------------- | ----------------------------------- |
| Sample_ID            | Foreign key                         |
| Analyte              | Pb, Cr, Cd, etc.                    |
| Concentration        | Numerical value                     |
| Original_Unit        | Unit in the publication             |
| Standardized_Unit    | Harmonized unit                     |
| Detection_Limit      | LOD                                 |
| Quantification_Limit | LOQ                                 |
| Analytical_Method    | ICP-MS, AAS, etc.                   |
| Fraction             | Dissolved, total, recoverable, etc. |
| QA_Flag              | Quality-control status              |

**Table D: Environmental and pollution-source variables**

| Field                 | Description                       |
| --------------------- | --------------------------------- |
| Sample_ID             | Foreign key                       |
| pH                    | Water pH                          |
| EC                    | Electrical conductivity           |
| DO                    | Dissolved oxygen                  |
| BOD                   | Biological oxygen demand          |
| COD                   | Chemical oxygen demand            |
| Industrial_Distance   | Distance to industrial facilities |
| Urban_Distance        | Distance to urban areas           |
| Agricultural_Cover    | Agricultural land proportion      |
| Population_Density    | Population density                |
| Upstream_Industry     | Upstream industrial pressure      |
| Discharge_Information | Available discharge information   |

This structure makes it possible to add new publications without changing the underlying data architecture.

## **4.3 Literature quality assessment**

Create a quality score for each study.

Possible criteria:

| Criterion                            | Score  |
| ------------------------------------ | ------ |
| Clearly identified sampling location | 0–2    |
| Sampling date/year documented        | 0–2    |
| Analytical method documented         | 0–2    |
| Measurement units clearly documented | 0–2    |
| Sample preparation documented        | 0–2    |
| QA/QC information available          | 0–2    |
| Replication information available    | 0–2    |
| **Total**                            | **14** |

Use the score to characterize evidence quality, not to automatically discard studies with lower scores.

A study lacking a clearly documented analytical method may still contribute to descriptive analysis, but its measurements should not automatically be treated as equally reliable as measurements with full QA/QC documentation.

# **5. Phase II — Data cleaning and harmonization**

This is arguably the most important technical phase.

## **5.1 Coordinate standardization**

Convert all coordinates to WGS84 decimal degrees (EPSG:4326).

For example:

```
23° 44' 36.61" N
90° 24' 00.29" E
```

becomes:

```
Latitude  = 23.743503
Longitude = 90.400081
```

The coordinate conversion pipeline should:

1. Parse degrees, minutes, and seconds.
2. Handle Unicode degree and prime characters.
3. Handle inconsistent whitespace and hemisphere notation.
4. Detect coordinate ranges.
5. Flag coordinates outside Bangladesh's geographical extent.
6. Verify coordinates against the river network.
7. Preserve original coordinates for traceability.

For coordinate ranges, do not automatically use the midpoint as a sampling point. A river-segment geometry may be more appropriate.

Assign each location a confidence level:

- A: Exact GPS coordinate.
- B: Published station coordinate.
- C: Georeferenced from a map or named locality.
- D: Approximate study-area coordinate.
- E: Unknown.

For the main spatial model, prioritize A and B. C may be included in sensitivity analyses. D should not be treated as an exact point.

## **5.2 Unit harmonization**

Maintain the original concentration and create a standardized concentration column.

For water:

\\[ 1\ \text{mg/L}=1000\ \mu\text{g/L} \\]

For sediment, use a consistent dry-weight basis, typically mg/kg dry weight.

Do not convert water concentration into sediment concentration or combine them in one regression model.

Also distinguish:

- Dissolved metals.
- Total metals.
- Total recoverable metals.
- Acid-extractable metals.
- Sediment total digestion measurements.

These are analytically different quantities.

## **5.3 Treatment of non-detects**

Suppose a publication reports:

\\[ Pb < 0.01\ \text{mg/L} \\]

This is not equivalent to Pb = 0.

Likewise, replacing every non-detect with half the detection limit can introduce bias, particularly when detection limits differ between studies.

Recommended approaches:

- Censored-data statistical models.
- Regression on order statistics (ROS), where appropriate.
- Multiple imputation methods designed for censored environmental measurements.
- Sensitivity analysis under different non-detect treatments.

Preserve the original censoring information.

## **5.4 Missing values**

Avoid indiscriminate mean or median imputation.

For example, if pH is missing in 60% of observations, imputing the mean pH can artificially reduce environmental variation and create misleading relationships.

I recommend:

- Exclude variables with inadequate coverage from the primary model.
- Consider multiple imputation only where its assumptions are defensible.
- Use missingness indicators where justified.
- Report missingness patterns by publication, river, sample type, and year.
- Compare models with and without imputed predictors.

## **5.5 Outlier analysis**

Heavy-metal concentrations often have right-skewed distributions.

Do not automatically remove high concentrations using the IQR rule.

A very high concentration may represent genuine industrial contamination.

Instead:

1. Check the original paper.
2. Verify units.
3. Check decimal-point errors.
4. Check analytical detection limits.
5. Compare with other stations in the same study.
6. Flag unusual values.
7. Perform robust modelling and sensitivity analysis.

For positive concentration measurements, logarithmic transformations may be useful:

\\[ Y=\log\_{10}(C+\epsilon) \\]

where \\(C\\) is the concentration and \\(\epsilon\\) is a small, justified offset.

For censored measurements, use an appropriate censored-data approach rather than arbitrary offsets.

# **6. Phase III — Geospatial and environmental feature engineering**

This is where the project can become substantially more interesting than a conventional ML comparison.

The model should not rely exclusively on latitude and longitude.

It should incorporate variables that have plausible physical relationships with heavy-metal contamination.

## **6.1 Potential data sources**

The following are useful candidate sources to investigate.

[#gis #mapping #datavisualization #bangladesh #qgis #rivers #hydrosheds #waterislife #bangladeshrivers #riversofbangladesh #mapsofbdriver | Durjoy Biswas](https://images.openai.com/static-rsc-4/jxNbO3hONDKGi8ZcMk9I_znV-5YKrFSzKtnXRN_UPclaB-7_X7iHJHArYnCVzXR3frX6GA6pwVG4Uz5GIanVEWB7pbjsXgc1KMgjgUaJWhAl_FnydQM5kwf3fhWfVwAqn7ssl9K4wga0gHI-TSHlK-qieSjsJhJaxRKLeHonuiQ?purpose=inline)

**HydroSHEDS**

River networks, flow direction, catchment boundaries, and drainage characteristics.

[Official dataset](https://www.hydrosheds.org/?utm_source=chatgpt.com)

[Release of ESA's WorldCover map | WORLDCOVER](https://images.openai.com/static-rsc-4/92mkbELWph8pQBLhChpwr5QgrtXI05Kk2-ogXMu1Wm9fs4BYbiQ0BM4LHqsTIVxiFHTZw2k4pC2-glRf8RB6KnhNgnFWc2_5_jcxypuj7PjWmaSFHbtgXE-TbZMxq90O4pM8fd7UNHBddSlpLnQswSviP7pyphAExUO1bd9H3iw?purpose=inline)

**ESA WorldCover**

Land-cover classes including built-up areas, cropland, vegetation, and water.

[Official dataset](https://worldcover2021.esa.int/?utm_source=chatgpt.com)

[World of Change: Padma River, All Images - NASA Science](https://images.openai.com/static-rsc-4/hGwQicp0pCRSuPY89YDN97HEUhgwe76d7HqBiLpqdTFd3DNhdLYfo_SrLherNK4KysFviHFTS0tVtHcUA1_xJ0CSQznKNTvIDrs9tapWP_ZqKX11_OLtyMQeA5C8ZKqwf5eB0HD_igK2bVyDtH17b7-MMdh-7XUL1agXh1t7wkI?purpose=inline)

**Landsat**

Historical land-use changes, urban expansion, surface characteristics, and potentially river changes.

[Official resource](https://landsat.gsfc.nasa.gov/?utm_source=chatgpt.com)

[A Global Tour of Precipitation from NASA | NASA Global Precipitation Measurement Mission](https://images.openai.com/static-rsc-4/fx2SjEsEUSDOAG9t6UVH8DHczLzBeKvkExYm3CD2MGBu4HmdXrjT9jT3gS9QbBGkCpI36aZP2c5GvnXVGvltf5T6kRj4eNF2xxI2vRzEWN72JpbMPkYgZ-M7va3wXTVdohSn4UoMXL0DXPoNoJCBf32eMcRd56t8rbWrFuUE8ys?purpose=inline)

**NASA GPM**

Precipitation and rainfall characteristics relevant to runoff and seasonal variation.

[Official resource](https://gpm.nasa.gov/?utm_source=chatgpt.com)

[Forecasting dengue in Bangladesh using meteorological variables with a novel feature selection approach | Scientific Reports](https://images.openai.com/static-rsc-4/MrGjCkP7rIAplOi-8A3mreZnOFLu4-qBQ1wsOBGr5K4ER-hAncrS0hRZ3FVOnkGCXnBAog__VLiF1t5WlYZPareftZ1Klful-O_I03b4Ab5Z6-Qja-GexW_F9UfecSGOBXn8-cs9F2Xx58lKk8JsdOk1CMpO5qZPOIXza-YhiVo?purpose=inline)

**WorldPop**

Population density and spatial population distribution.

[Official dataset](https://www.worldpop.org/?utm_source=chatgpt.com)

[Battle: Dar es Salaam vs Nairobi | Page 21326 | JamiiForums](https://images.openai.com/static-rsc-4/NvCxXPXMq0GWMqmZFk4Pe7r1jbr--nWqBaZV2Q0KOqy28MURa098mRvpLs7C4EDFXACkD7Q3GS-NKN41MlYULep1QPJg2rk0IlIm3qV4xwzXpn3Ha4BhSZcoSVb-dxy-2DyvKCuDFEXOvp_xlN_nmPG60HxFN_lYZRJ-69FUwLQ?purpose=inline)

**Global Power Plant Database**

Power-generation facilities as one industrial-pressure indicator, not a complete industrial inventory.

[Dataset](https://datasets.wri.org/dataset/globalpowerplantdatabase?utm_source=chatgpt.com)

[Climate reanalysis | Copernicus](https://images.openai.com/static-rsc-4/9WlPG_fDPJ2fKSo6Xkz1e19zknaQOw37vyzcNJMRNmMzvX0suuG-DVC3GTm9CMA1hE9k7gBMBik2u-6IxUkJsl4YnpNtH71OxQDG92A0M4Du1prMTGH73Woc6H3900p5NXTpjS1u-X4Upqh0Y3b03lMtKH8m4BMl8-FxSGf4K-c?purpose=inline)

**ERA5**

Historical precipitation, temperature, and other meteorological variables.

[Climate Data Store](https://cds.climate.copernicus.eu/?utm_source=chatgpt.com)

Additional Bangladesh-specific sources should be investigated:

- Bangladesh Water Development Board (BWDB): river discharge, water levels, and hydrological monitoring.
- Department of Environment, Bangladesh (DoE): environmental monitoring, industrial pollution, and relevant compliance records.
- Bangladesh Bureau of Statistics (BBS): population, economic activity, and industrial statistics.
- Bangladesh Meteorological Department (BMD): rainfall and meteorological records.

## **6.2 Feature engineering strategy**

I would organize predictors into five categories.

| Category         | Candidate features                                                     |
| ---------------- | ---------------------------------------------------------------------- |
| Geographic       | Latitude, longitude, river identity, elevation                         |
| Hydrological     | Flow accumulation, drainage area, discharge, upstream catchment        |
| Anthropogenic    | Industrial density, population, urban land cover, wastewater discharge |
| Environmental    | Rainfall, temperature, pH, DO, EC, salinity                            |
| Sediment-related | Organic matter, clay, silt, sand, sediment texture                     |

A particularly useful set of features would be:

### **A. Distance-based pollution features**

For each sampling location, calculate:

- Distance to nearest industrial facility.
- Number of industries within 1 km, 5 km, and 10 km.
- Distance to wastewater discharge points.
- Distance to urban centres.
- Distance to major roads.
- Distance to ports and shipping facilities.
- Distance to known landfill sites.

### **B. Upstream pollution features**

Simple Euclidean distance is not enough for rivers.

A factory 500 metres away but located downstream may have less relevance to an upstream sampling station than a factory several kilometres upstream.

Therefore, calculate:

- Number of industrial facilities upstream.
- Upstream industrial density.
- Upstream population density.
- Upstream urban land-cover proportion.
- Upstream agricultural land-cover proportion.
- Upstream wastewater discharge points.

These features should be based on the river network and flow direction, not merely circular buffers.

### **C. Seasonal and hydrological features**

Bangladesh has strong seasonal hydrological variation.

Consider:

- Monsoon precipitation.
- Dry-season precipitation.
- Sampling season.
- River discharge.
- Water level.
- Flood frequency.
- Seasonal land-cover conditions.

The influence of rainfall and discharge may differ between dissolved and sediment-associated metals.

## **6.3 Avoid temporal mismatches**

This is essential.

For example, if a metal measurement was collected in 2013, using a 2024 industrial-density map as its predictor may introduce serious temporal leakage.

Ideally, each sample should be matched to environmental predictors corresponding to its sampling period.

Where historical covariates are unavailable, either:

- Exclude that variable from historical modelling.
- Use an explicitly justified time-invariant approximation.
- Conduct a separate current-condition assessment using contemporary environmental covariates.

Clearly document the difference.

# **7. Phase IV — Exploratory data analysis and environmental statistics**

Before training ML models, perform a thorough statistical investigation.

## **7.1 Descriptive analysis**

For each heavy metal, calculate:

- Sample count.
- Mean.
- Median.
- Standard deviation.
- Minimum and maximum.
- Interquartile range.
- Coefficient of variation.
- Skewness.
- Detection frequency.

Perform these separately for:

1. Water.
2. Sediment.
3. Each river.
4. Each season.
5. Each sampling year.
6. Each publication.

## **7.2 Distribution analysis**

Use:

- Histograms.
- Log-scale histograms.
- Boxplots.
- Violin plots.
- ECDF plots.
- Q-Q plots.

Heavy-metal data are often non-normal, so do not assume that conventional parametric tests are automatically appropriate.

## **7.3 Statistical comparisons**

Potential analyses include:

| Research question                       | Method                              |
| --------------------------------------- | ----------------------------------- |
| Do concentrations differ across rivers? | Kruskal–Wallis test                 |
| Do seasonal concentrations differ?      | Kruskal–Wallis test or mixed models |
| Are concentrations associated with pH?  | Spearman correlation                |
| Are metals associated with one another? | Spearman correlation                |
| Are there multivariate metal patterns?  | PCA                                 |
| Are there spatial clusters?             | Global Moran's I                    |
| Where are local hotspots?               | Local Moran's I / Getis-Ord Gi\*    |

Use post-hoc comparisons with appropriate multiple-testing correction.

For comparisons across papers, use hierarchical models where possible, because observations from the same publication may share methodological biases.

## **7.4 Pollution indices**

I strongly recommend incorporating environmental contamination indices.

These make the research more interpretable to environmental scientists and policymakers.

For sediment, possible indices include:

**Contamination factor:**

\\[ CF_i=\frac{C_i}{B_i} \\]

where \\(C_i\\) is the observed metal concentration and \\(B_i\\) is an appropriate background concentration.

**Geo-accumulation index:**

\\[ I\_{\mathrm{geo}}= \log_2\left(\frac{C_i}{1.5B_i}\right) \\]

**Potential ecological risk index:**

\\[ E_r^i=T_r^i \times CF_i \\]

where \\(T_r^i\\) is the toxic-response factor for the selected metal.

**Pollution Load Index:**

\\[ PLI=(CF_1 \times CF_2 \times \cdots \times CF_n)^{1/n} \\]

Use background values appropriate to the regional geology. A generic global background concentration may produce misleading classifications in Bangladesh.

For water, compare concentrations with relevant water-quality standards and clearly state the intended use: drinking water, aquatic ecosystem protection, irrigation, or another purpose. These standards are not interchangeable.

A pollution index should not be confused with a predictive ML target. For the primary modelling, predict the actual measured concentration; use indices for environmental interpretation.

# **8. Phase V — Machine-learning modelling**

This is where the research should establish its technical contribution.

## **8.1 Define the prediction targets**

Develop separate target variables:

| Model  | Target                             | Sample type |
| ------ | ---------------------------------- | ----------- |
| M1     | Pb concentration                   | Water       |
| M2     | Cr concentration                   | Water       |
| M3     | Cd concentration                   | Water       |
| M4     | As concentration                   | Water       |
| M5     | Cu concentration                   | Water       |
| M6     | Ni concentration                   | Water       |
| M7–M12 | Corresponding metal concentrations | Sediment    |

These are candidate models, not a commitment to train all 12.

Select the final targets after checking the number of independent studies, unique sites, geographical coverage, and data quality.

## **8.2 Recommended algorithms**

Do not begin with deep learning.

With approximately 557 total observations, divided between two sample types and ten metals, sophisticated neural architectures may overfit.

I recommend the following model hierarchy.

**Baseline models**

- Mean/median predictor.
- Linear regression.
- Ridge regression.
- Random forest.

**Primary nonlinear models**

- XGBoost.
- LightGBM.
- CatBoost.

**Spatial-statistical models**

- Ordinary kriging.
- Regression kriging.
- Generalized additive models (GAM).
- Spatial regression.
- Gaussian process regression, if computationally and statistically feasible.

**Advanced comparative models**

- Support vector regression.
- Extra Trees.
- Quantile regression forests.

My preferred initial comparison would be:

1. Random Forest.
2. XGBoost.
3. CatBoost.
4. LightGBM.
5. Regression kriging.
6. GAM.

The inclusion of regression kriging is important. A study claiming spatial prediction should compare ML with a geostatistical approach, not just compare several generic ML algorithms.

## **8.3 Suggested model architecture**

A particularly defensible approach is a hybrid model.

First, learn the relationship between environmental predictors and heavy-metal concentrations:

\\[ \hat{y}\_{ML}=f(X) \\]

Then model the spatially correlated residuals:

\\[ e_i=y_i-\hat{y}\_{ML,i} \\]

Use a spatial interpolation method to estimate residuals at unsampled locations:

\\[ \hat{y}\_{hybrid}(s)= \hat{y}\_{ML}(s)+\hat{e}\_{spatial}(s) \\]

This is regression kriging.

It combines:

- Nonlinear environmental relationships.
- Spatial autocorrelation.
- Geographic structure.

However, spatial residual modelling must also be evaluated using spatially independent validation. It should not be assumed to improve predictive accuracy automatically.

## **8.4 Model training and hyperparameter optimization**

Use nested spatial cross-validation rather than a random train/test split.

A possible approach:

- Outer loop: spatially blocked 5-fold cross-validation.
- Inner loop: 3-fold spatial cross-validation for hyperparameter optimization.
- Hyperparameter optimization: Optuna or randomized search.
- Final model: retrain using the complete eligible training dataset after model selection.

The exact number of folds should depend on the number of independent spatial blocks. If there are too few independent geographical groups, use fewer folds rather than forcing five.

Use publication-level grouping as an additional safeguard. Measurements from one publication should not be allowed to appear in both training and test partitions when the objective is generalization to new studies.

## **8.5 Evaluation metrics**

Use several complementary metrics.

**Mean Absolute Error:**

\\[ MAE=\frac{1}{n}\sum\_{i=1}^{n}|y_i-\hat{y}\_i| \\]

**Root Mean Squared Error:**

\\[ RMSE= \sqrt{\frac{1}{n}\sum\_{i=1}^{n}(y_i-\hat{y}\_i)^2} \\]

**Coefficient of determination:**

\\[ R^2= 1-\frac{\sum_i(y_i-\hat{y}\_i)^2} {\sum_i(y_i-\bar{y})^2} \\]

Also report:

- Median absolute error.
- Mean absolute percentage error only where mathematically meaningful.
- Bias (mean error).
- Spearman correlation.
- Prediction interval coverage.
- Spatial-block-specific errors.

For skewed concentration distributions, consider reporting performance on both the original concentration scale and the log scale.

A model with high random-split \\(R^2\\) but poor spatial-block performance is not a reliable spatial prediction model.

# **9. Phase VI — Spatial validation and uncertainty estimation**

This section will significantly influence the credibility of the paper.

## **9.1 Spatial cross-validation**

Suppose five neighbouring sampling stations are in the same industrial area.

If four are used for training and one for testing, the model may effectively be interpolating between nearby observations.

That does not demonstrate the ability to generalize to a new river or region.

Instead, use:

- Spatial block cross-validation.
- Leave-one-river-out validation where feasible.
- Leave-one-study-out validation.
- Geographical holdout testing.

I would report at least two evaluation settings:

**Experiment A: Spatial interpolation**

Training and test locations are geographically separated by blocks, but may belong to the same broader river systems.

**Experiment B: Geographical transfer**

Hold out entire rivers or regions to investigate whether the model can generalize to previously unseen river systems.

These experiments answer different scientific questions and should not be combined into one performance number.

## **9.2 Uncertainty estimation**

A national prediction map without uncertainty is potentially misleading.

I recommend:

- Quantile regression.
- Quantile regression forests.
- Conformal prediction with appropriate spatial calibration.
- Spatial bootstrap.
- Prediction interval maps.

For every predicted river segment, produce:

1. Predicted concentration.
2. Lower uncertainty bound.
3. Upper uncertainty bound.
4. Distance to nearest observation.
5. Number of nearby supporting observations.
6. Data-quality or extrapolation flag.

An area with a high predicted concentration but very sparse supporting data should not be presented with the same confidence as a well-sampled area.

## **9.3 Applicability domain**

Calculate whether each prediction location is within the environmental and geographic domain of the training data.

For example, if the model was trained on industrial urban rivers and then applied to a remote river with very different hydrological and sediment conditions, the prediction may be extrapolation.

Flag these locations explicitly.

# **10. Phase VII — Pollution-source investigation**

This should be a separate and carefully designed research component.

The initial group discussion proposes identifying the possible pollution sources associated with contamination hotspots.

That is scientifically reasonable, but proximity alone is insufficient.

## **10.1 Develop a pollution-source inventory**

Consider:

| Potential source                   | Relevant metals to investigate                      |
| ---------------------------------- | --------------------------------------------------- |
| Textile and dyeing industries      | Cr, Cu, Pb and other metals depending on processes  |
| Tannery activities                 | Cr, Pb and other metals                             |
| Battery manufacturing/recycling    | Pb, Cd and other metals                             |
| Metal processing/electroplating    | Cr, Ni, Cu, Cd, Zn                                  |
| Fertilizer and agricultural runoff | Cd, As and other metals depending on inputs         |
| Urban wastewater                   | Multiple metals                                     |
| Mining and natural geology         | Metal-specific geogenic contributions               |
| Shipbuilding and port activity     | Pb, Cu, Zn and other metals depending on activities |

These are potential associations, not universal source signatures.

## **10.2 Source-related feature extraction**

For each river sampling station, calculate:

- Distance to potential source.
- Number of potential sources upstream.
- Industrial density within upstream catchment.
- Estimated wastewater discharge, if available.
- Land-use distribution upstream.
- Population density upstream.

## **10.3 Statistical investigation**

Recommended methods:

**A. SHAP analysis**

Use SHAP values to understand which predictors contribute to model outputs.

For example, the model may identify upstream industrial density and sediment organic matter as important predictors of Pb.

However, SHAP describes model attribution, not physical causation.

**B. Partial dependence / ALE**

Investigate how predicted concentration varies with a particular predictor while accounting for the model's learned structure. Accumulated Local Effects (ALE) are often preferable when predictors are correlated.

**C. PCA and correlation analysis**

Investigate co-occurring metals and their associations with environmental variables.

**D. Positive Matrix Factorization (PMF)**

If the data have sufficiently complete and comparable multi-element chemical profiles, PMF may help identify possible source factors.

PMF should not be forced onto the current dataset without checking its assumptions, uncertainty information, and missing-data structure.

**E. Hydrological upstream–downstream analysis**

Compare concentrations upstream and downstream of identified potential pollution sources, preferably with repeated observations and appropriate controls.

This is much more convincing than drawing circles around industrial locations.

## **10.4 What can the research legitimately conclude?**

Appropriate:

> Elevated predicted Pb concentrations are spatially associated with regions exhibiting high upstream industrial activity and urban land-use intensity.

Not justified without additional evidence:

> The identified factories caused the Pb contamination.

For causal source attribution, you would need stronger evidence, such as direct discharge measurements, source-specific chemical fingerprints, or a robust upstream–downstream study design.

# **11. Phase VIII — Producing the 2026–2027 contamination maps**

This needs a specific methodological decision.

I recommend the following three-level output.

## **Level 1: Historical contamination map**

Recommended primary output

Generate maps using the available historical measurements.

For example:

- Pb concentration in sediment.
- Cr concentration in sediment.
- Cd concentration in water.
- As concentration in water.

Use the sampling-year information to identify the period represented by each map.

If measurements span multiple years, do not simply label their combined predictions as the current condition.

## **Level 2: Current-condition assessment**

If you want to estimate current conditions in 2026, you will need additional contemporary information.

The strongest option would be a limited field-sampling campaign.

For example, select 20–30 strategically chosen locations based on:

- Existing contamination hotspots.
- Industrial discharge locations.
- Major upstream–downstream transitions.
- Underrepresented river systems.
- Areas where the spatial model has high uncertainty.

This is an illustrative sample-design target, not a statistically guaranteed sufficient sample size.

Collect water and sediment samples, document analytical methods, and measure the same selected metals.

These new observations can be used for independent validation and model updating.

If field sampling is not possible, describe the output as a historical-data-based spatial estimate, not a measured 2026 contamination assessment.

## **Level 3: Future scenarios for 2027**

Develop scenarios rather than unsupported point forecasts.

**Scenario 1: Baseline / Business as Usual**

Reference scenario

Existing industrial and environmental conditions are assumed to continue, with explicitly specified covariate assumptions.

**Scenario 2: Increased Industrial Pressure**

Stress scenario

Industrial activity, wastewater discharge, or relevant pressure indicators increase according to documented assumptions.

**Scenario 3: Improved Pollution Management**

Mitigation scenario

Model the effect of specified reductions in industrial discharge or improved wastewater treatment, where quantitative relationships and scenario parameters can be supported by evidence.

For each scenario, produce:

- Predicted concentration.
- Difference from baseline.
- Percentage difference.
- Uncertainty interval.
- Areas with insufficient supporting evidence.

A key limitation: changing an industrial-density feature in an ML model does not automatically predict the physical effect of reducing pollution. Scenario results must be calibrated against observed relationships and interpreted as conditional model outputs, not causal intervention estimates.

**My recommendation:** Make the historical spatial model the main contribution and the 2027 scenario assessment a secondary, explicitly exploratory contribution.

# **12. Phase IX — GIS implementation and visualization**

Use QGIS as the primary GIS platform, with Python for spatial data processing and modelling.

[Contamination Assessment of Toxic Elements in River Sediments from Baia Mare, Romania—Extreme Pollution from Mining Activities](https://images.openai.com/static-rsc-4/ZMwbjh7GNvQP26CYL3EwrSDFMWNv9BZUA4yhsVB4zljWIsyrqGIdpBlWP-XVJYhSNzr8kNLMKSeW_q54uUR7iLAyjnWum0OMw4z3_cgFfDEd77URzKZ0S-ERmGrY82MFIHIbR-aOSFGd2QYctk_M9FMqYe0m09G_120g-Tct7K0?purpose=inline)

[Full article: Spatial prediction of groundwater nitrate by explainable machine learning models and remote sensing indicators under conditions of imbalanced datasets](https://images.openai.com/static-rsc-4/YHD_u66arFreJxYW7bXTrCy9QRfaE0Ohset5nIZ2pwavBgFbzz1PW0wrEgmwQf8xbxteEATR2rU4COx6wq_m_0Gu9s-C_I1AgDxvxmauSAy_hBPbMEjWOBCAG3x0-NHt_jK0JSZIo_7nZMkfcelT5LtMEonYSC2RrItPZcKCoWw?purpose=inline)

[Distance and weightage-based identification of most critical and vulnerable locations of surface water pollution in Kabul river tributaries | Scientific Reports](https://images.openai.com/static-rsc-4/958WpnxyWsWQOka18H4sfCuV7weUn3345_772-dolQO1nXlMFxSyQBRfjpIkkUHMOUrhK-1lNcaQf7Rwmgmt1c0yehB4nyZrhovSQZHN4lWCx_GXVPMgHfFxDpn01VDc05IgL8mQwRcMJErO-QSCKs8opaMbEYkAenjJg8uY9sQ?purpose=inline)

12

## **12.1 Recommended map outputs**

I recommend preparing the following maps for each selected metal.

| Map                          | Purpose                                     |
| ---------------------------- | ------------------------------------------- |
| Sampling location map        | Show the actual measurement locations       |
| Historical concentration map | Display observed concentrations             |
| Predicted concentration map  | Display spatial model predictions           |
| Contamination hotspot map    | Identify statistically significant clusters |
| Prediction uncertainty map   | Show reliability of predictions             |
| Pollution-source map         | Show potential pollution sources            |
| River-level comparison map   | Compare contamination among river systems   |
| Scenario difference map      | Show baseline versus 2027 scenarios         |

## **12.2 Use river segments rather than only a national raster**

This is an important design decision.

A raster interpolation method may predict contamination over land areas that are not part of the river network.

For example, a conventional inverse distance weighting (IDW) map may show high Pb concentrations in an area between two rivers simply because of nearby sampling points.

That is not necessarily meaningful.

I recommend two spatial representations:

1. A continuous raster surface for exploratory environmental visualization, with appropriate restrictions.
2. A river-network-based prediction map as the primary scientific output.

For the river-network approach:

- Divide selected rivers into reaches.
- Associate each reach with hydrological and environmental features.
- Estimate concentrations for each reach.
- Display predicted concentrations along the river network.

Where the model is intended to represent water flowing downstream, use flow connectivity and upstream–downstream relationships rather than treating all points as independent Euclidean locations.

## **12.3 Suggested final visualization structure**

For each selected metal, create a four-panel figure:

## **Illustrative Pb contamination analysis**

[Frontiers | Investigating Dissolved Organic Matter Dynamics in the Downstream Reaches of the Ganges and Brahmaputra Rivers Using Fluorescence Spectroscopy](https://images.openai.com/static-rsc-4/FbPHAQay6aZGOzrteao4jamOXN9BmyOTVRf0EBWp8kDF636F-vp6pUQvLJqx_PZdR7nNJ_lXbtErjf5icEAsMYGNBWnI2GLCdiS9RERtr466JHAfzrSKZN3UEcO12jCTwUXcDxITj7wgEcOEEimHyfi8k5DgWp_Rxh5jS6auaSs?purpose=inline)

**A. Sampling locations**

Actual observations and spatial coverage

[A Spatial–Seasonal Study on the Danube River in the Adjacent Danube Delta Area: Case Study—Monitored Heavy Metals](https://images.openai.com/static-rsc-4/iv74fsmdCGoOW57YIBid0-fHO-MeB4SkIOntA_-kIa4X_ka-b-Nv8Jm1ZuoqYKWuajmcVTSTY19gHJwkWtuEw9PUA791bvR7JFBjP5Hiw7omnhn1REO9ZeIlo1ezlokdkO050IA6lejOeh0WK8nRTZfGHicmQ1a6cIiONF3KC5U?purpose=inline)

**B. Predicted concentration**

Spatial ML prediction

[A Bayesian Approach to Estimate the Spatial Distribution of Crowdsourced Radiation Measurements around Fukushima](https://images.openai.com/static-rsc-4/CiBvGNg-SWxL51LM1GWsJBY_QgSZeVkZVE_-2295dZhHhmajtnG3lOlnXomcpdKIrTpR_Tr-s9dCmGj5wlJYlkkbpFO6FPFnRO8H9U0avX9GC4vRBczDawLxhemNkh872HUN9nHbLQLxxBsfYjcQ0ibwjIGDjdbui0gbkELqgEo?purpose=inline)

**C. Prediction uncertainty**

Model confidence and uncertainty

[Frontiers | Contaminant Discharge From Outfalls and Subsequent Aquatic Ecological Risks in the River Systems in Dhaka City: Extent of Waste Load Contribution in Pollution](https://images.openai.com/static-rsc-4/-1ux6tDFXoVolAyMJrzvnw_ZfM6FSOeWIXFcA-lKm6JBBbGx6GdbSiuBmEdN8U395NeRkNlTdcPC-qZu8ny5v1M0BAql9MLVZn9Fmp94j3HzbyvkNXsn3j01OCFS0nysDx4EpemTsjPucdQI1oyjLV2bNNbLf2n4skjPbtmkXZ4?purpose=inline)

**D. Potential pollution sources**

Industrial and urban pressure indicators

Illustrative layouts only, not maps generated from your dataset.

This presentation will communicate the scientific findings more effectively than showing a single heatmap.

# **13. Phase X — Explainability and scientific interpretation**

I recommend making explainable ML a core part of the study.

Use:

- SHAP summary plots.
- SHAP dependence plots.
- ALE plots.
- Feature importance comparisons across models.
- Spatial distribution of prediction errors.
- Feature importance stability across spatial folds.

For example, consider a hypothetical model where the most influential predictors are:

1. Upstream industrial density.
2. Sediment organic matter.
3. River discharge.
4. pH.
5. Urban land-cover proportion.

The interpretation should explain why these variables might be environmentally relevant.

However, avoid claiming that a feature is the dominant physical cause merely because it has a high SHAP value.

A stronger result would compare whether feature importance remains consistent across different rivers, publications, and spatial validation folds.

# **14. Proposed software and technical implementation**

I would use a Python-based research pipeline.

| Task                   | Recommended tools            |
| ---------------------- | ---------------------------- |
| Data extraction        | Excel, Python, pandas        |
| Data validation        | Pandera, Great Expectations  |
| Literature management  | Zotero                       |
| Geospatial processing  | GeoPandas, Shapely, Rasterio |
| River-network analysis | PySheds, NetworkX            |
| Remote sensing         | Google Earth Engine          |
| Statistical analysis   | SciPy, statsmodels           |
| Spatial statistics     | PySAL, esda                  |
| Geostatistics          | PyKrige, GSTools             |
| Machine learning       | scikit-learn                 |
| Gradient boosting      | XGBoost, LightGBM, CatBoost  |
| Hyperparameter tuning  | Optuna                       |
| Explainability         | SHAP                         |
| Visualization          | QGIS, Matplotlib, Plotly     |
| Reproducibility        | Git, MLflow                  |

## **Recommended project structure**

```
Bangladesh_River_Heavy_Metal_Research/
│
├── 01_Literature_Review/
│   ├── search_strategy/
│   ├── screening/
│   └── reference_library/
│
├── 02_Raw_Data/
│   ├── literature_extraction/
│   ├── environmental_data/
│   ├── industrial_sources/
│   └── river_networks/
│
├── 03_Data_Processing/
│   ├── coordinate_conversion/
│   ├── unit_harmonization/
│   ├── missing_values/
│   └── quality_control/
│
├── 04_Exploratory_Analysis/
│   ├── descriptive_statistics/
│   ├── correlation/
│   └── pollution_indices/
│
├── 05_Geospatial_Analysis/
│   ├── feature_engineering/
│   ├── river_network/
│   └── spatial_autocorrelation/
│
├── 06_Machine_Learning/
│   ├── water_models/
│   ├── sediment_models/
│   ├── spatial_validation/
│   └── hyperparameter_tuning/
│
├── 07_Explainable_AI/
│   ├── shap/
│   └── ale/
│
├── 08_Prediction/
│   ├── historical/
│   ├── current_assessment/
│   └── future_scenarios/
│
├── 09_GIS_Maps/
│
├── 10_Results/
│
└── 11_Manuscript/
```

# **15. Experimental design: What exactly should you compare?**

A strong paper needs clearly defined experiments, not simply a list of algorithms.

I suggest the following.

| Experiment | Objective                       | Comparison                                               |
| ---------- | ------------------------------- | -------------------------------------------------------- |
| E1         | Establish baseline performance  | Mean, median, linear regression                          |
| E2         | Evaluate nonlinear ML           | RF, XGBoost, LightGBM, CatBoost                          |
| E3         | Evaluate spatial modelling      | Kriging, GAM, regression kriging                         |
| E4         | Evaluate additional predictors  | Geographic-only vs environmental vs anthropogenic        |
| E5         | Evaluate generalization         | Random vs spatial vs river-level validation              |
| E6         | Evaluate explainability         | SHAP and ALE                                             |
| E7         | Evaluate pollution associations | Industrial and upstream source variables                 |
| E8         | Evaluate robustness             | Missingness, outlier, and unit-quality sensitivity       |
| E9         | Evaluate future scenarios       | Baseline vs increased-pressure vs mitigation assumptions |

## **Essential ablation study**

One particularly valuable experiment would be to investigate the contribution of different feature groups.

| Model | Geographic features | Environmental features | Industrial features |
| ----- | ------------------- | ---------------------- | ------------------- |
| A     | Yes                 | No                     | No                  |
| B     | Yes                 | Yes                    | No                  |
| C     | Yes                 | No                     | Yes                 |
| D     | Yes                 | Yes                    | Yes                 |

This will help answer:

- Does environmental information improve spatial prediction?
- Do industrial-source indicators add measurable predictive value?
- Does the combination outperform simpler spatial models?

Compare all four using identical spatial folds.

This experiment can provide a more meaningful scientific contribution than demonstrating that XGBoost performs slightly better than Random Forest.

# **16. Statistical and methodological safeguards**

Before accepting any model, establish the following conditions.

| Check                     | Why it matters                                           |
| ------------------------- | -------------------------------------------------------- |
| Spatial autocorrelation   | Detects spatial dependence                               |
| Publication-level leakage | Prevents learning paper-specific patterns                |
| Unit consistency          | Prevents scientifically invalid target values            |
| Coordinate validity       | Prevents geographical misplacement                       |
| Temporal alignment        | Prevents predictor/target time mismatch                  |
| Multicollinearity         | Helps interpret correlated environmental variables       |
| Applicability domain      | Identifies unsupported extrapolation                     |
| Prediction uncertainty    | Prevents false confidence                                |
| Sensitivity analysis      | Tests whether conclusions depend on questionable records |
| Independent validation    | Establishes generalization beyond training data          |

Also, distinguish between the following:

- Prediction accuracy.
- Statistical association.
- Environmental contamination classification.
- Source attribution.
- Causal impact of pollution-control policies.

These are different claims and require different evidence.

# **17. Proposed research timeline**

Assuming a team of three researchers and a reasonably consistent commitment, I would plan for approximately 20 weeks.

## **20-week execution plan**

1. **Weeks 1–2: Research design and literature review**
   - Finalize research questions.
   - Define inclusion/exclusion criteria.
   - Review comparable studies.
   - Establish the data schema.
2. **Weeks 3–5: Data collection and validation**
   - Extract measurements.
   - Verify source publications.
   - Standardize coordinates and units.
   - Resolve duplicate records.
   - Assess study quality.
3. **Weeks 6–7: Geospatial data acquisition**
   - Acquire river networks.
   - Collect land-cover and population data.
   - Compile industrial-source information.
   - Generate environmental predictors.
4. **Weeks 8–9: Exploratory and statistical analysis**
   - Analyze concentration distributions.
   - Calculate contamination indices.
   - Assess spatial autocorrelation.
   - Identify suitable target metals.
5. **Weeks 10–13: Machine-learning development**
   - Train baseline models.
   - Train nonlinear ML models.
   - Develop geostatistical models.
   - Conduct spatial cross-validation.
   - Tune hyperparameters.
6. **Weeks 14–15: Explainability and source investigation**
   - Conduct SHAP and ALE analysis.
   - Examine industrial associations.
   - Investigate upstream–downstream patterns.
7. **Weeks 16–17: Mapping and uncertainty analysis**
   - Produce river-level predictions.
   - Generate uncertainty maps.
   - Perform sensitivity analysis.
   - Prepare scenario outputs if justified.
8. **Weeks 18–20: Manuscript preparation**
   - Prepare figures and tables.
   - Write methodology and results.
   - Discuss limitations.
   - Validate reproducibility.
   - Prepare the final manuscript.

The timeline assumes that sufficient literature data are already available. If the team must collect substantial additional data or conduct field sampling, the project will need more time.

# **18. Suggested division of work among three researchers**

Based on the three-person collaboration described in the group discussion, I suggest the following division.

| Researcher   | Primary responsibility              | Deliverables                                                  |
| ------------ | ----------------------------------- | ------------------------------------------------------------- |
| Researcher 1 | Literature review and chemical data | Verified observations, units, QA/QC, metal selection          |
| Researcher 2 | Geospatial and environmental data   | Coordinates, river networks, industrial sources, GIS features |
| Researcher 3 | ML, statistics, and integration     | Statistical analysis, modelling, validation, SHAP, prediction |

All three should participate in:

- Research question refinement.
- Methodological decisions.
- Interpretation of findings.
- Manuscript writing.
- Final quality assurance.

One important recommendation: appoint one person as the data curator. Every correction to the master dataset should be traceable to the original publication.

# **19. Recommended research questions and hypotheses**

The manuscript should have clearly defined research questions.

I recommend these six:

**RQ1.** What are the spatial and temporal distributions of selected heavy metals in the water and sediment of Bangladesh's rivers based on available published measurements?

**RQ2.** Which geographical, hydrological, environmental, and anthropogenic factors are associated with heavy-metal concentrations?

**RQ3.** Can machine-learning and geostatistical models reliably estimate heavy-metal concentrations at unsampled river locations?

**RQ4.** How does model performance differ between water and sediment, between metals, and across different river systems?

**RQ5.** Which geographical areas demonstrate elevated contamination estimates, and how are these areas associated with potential pollution sources?

**RQ6.** Under explicitly defined environmental and industrial-pressure scenarios, how might predicted contamination patterns change?

Possible hypotheses:

- H1: Heavy-metal concentrations exhibit significant spatial heterogeneity across river systems.
- H2: Environmental and anthropogenic predictors improve spatial prediction beyond geographical coordinates alone.
- H3: Spatially aware ML models outperform conventional non-spatial baseline models under spatially independent validation.
- H4: Different heavy metals exhibit different spatial associations with environmental and anthropogenic factors.
- H5: Contamination hotspots exhibit spatial associations with potential industrial and urban pollution pressures.

Do not assume these hypotheses will be supported. They should be tested.

# **20. Potential publication structure**

I suggest the following manuscript structure:

| Section                           | Content                                                                     |
| --------------------------------- | --------------------------------------------------------------------------- |
| 1. Introduction                   | Heavy-metal contamination, Bangladesh context, research gaps, contributions |
| 2. Related Work                   | Environmental contamination mapping, geostatistics, ML                      |
| 3. Study Area                     | Bangladesh river systems and geographical characteristics                   |
| 4. Data Collection                | Literature search, extraction, data harmonization                           |
| 5. Methodology                    | Statistical analysis, GIS, feature engineering, ML                          |
| 6. Experimental Design            | Baselines, spatial validation, metrics, ablation                            |
| 7. Results                        | Descriptive statistics, spatial patterns, model performance                 |
| 8. Explainability                 | SHAP, ALE, environmental associations                                       |
| 9. Pollution-Source Investigation | Potential sources and hydrological relationships                            |
| 10. Discussion                    | Environmental interpretation, comparison with previous studies              |
| 11. Limitations                   | Sampling bias, measurement heterogeneity, uncertainty                       |
| 12. Conclusion                    | Scientific findings and policy implications                                 |

# **21. What I would change in the current research direction**

Here is my final assessment of the proposed project.

| Original proposal                             | My recommendation                                                                                  |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Predict heavy metals for 2026–2027            | Make spatial prediction the primary objective; future scenarios secondary                          |
| Use all available river measurements          | Use only records meeting defined quality and eligibility criteria for each model                   |
| Select metals based only on data availability | Select based on availability, independent sites, river coverage, and quality                       |
| Combine water and sediment                    | Develop separate modelling pipelines                                                               |
| Use latitude and longitude                    | Add environmental, hydrological, and upstream anthropogenic predictors                             |
| Compare several ML algorithms                 | Compare ML against geostatistical and statistical baselines                                        |
| Random train/test split                       | Spatial and publication-level validation                                                           |
| Show predicted contamination maps             | Show predictions, uncertainty, sampling coverage, and applicability domain                         |
| Identify industries responsible for pollution | Investigate potential source associations; avoid unsupported causal claims                         |
| Produce national predictions                  | Produce national predictions only where geographical coverage and model applicability support them |

## **22. Three decisions I would make before proceeding**

Decision 1

**Finalize the primary research objective**

I would choose:

*Spatial prediction and explainable assessment of heavy-metal contamination in selected river systems of Bangladesh.*

Temporal forecasting should be conditional on data adequacy.

Decision 2

**Reconstruct the master dataset**

Do not immediately begin model training using the current Excel workbook.

First resolve the missing locations, coordinate formats, concentration units, publication metadata, and sample-type inconsistencies.

Decision 3

**Establish a minimum data-adequacy assessment**

Before training each model, report:

- Number of independent publications.
- Number of independent sampling locations.
- Number of represented rivers.
- Geographical distribution.
- Number of measurements by sample type.
- Number of measurements by year.
- Analytical-method compatibility.
- Missingness and data-quality levels.

There should not be an arbitrary universal minimum number of observations. Model feasibility should be determined by the number of independent spatial groups and the complexity of the proposed model.

# **23. My recommended final research direction**

I would slightly revise the title to emphasize the actual scientific contribution.

Preferred title

# **Explainable Geospatial Machine Learning for Mapping Heavy Metal Contamination and Identifying Potential Pollution Hotspots in the Rivers of Bangladesh**

**Why this title?**

- Explainable ML establishes the computational contribution.
- Geospatial mapping establishes the primary research task.
- Pollution hotspots provide environmental relevance.
- Potential pollution sources can be investigated without claiming unsupported causality.
- It does not promise temporal forecasting that the current dataset may not support.

An alternative, if future scenarios become a scientifically defensible component, is:

*Spatiotemporal Assessment and Explainable Machine Learning-Based Prediction of Heavy Metal Contamination in Bangladesh's River Systems.*

# **24. Immediate action plan for your research team**

I would not start with XGBoost, Random Forest, or SHAP yet.

I would start with these five deliverables, in this order:

## **Research execution checklist**

**Progress**

## **0/5**

Audit all 28 publications against their original papers.

Resolve the 149 records with missing river names and recover geographical coordinates wherever possible.

Verify water and sediment concentration units, analytical methods, and detection limits.

Create separate, clean water and sediment datasets with unique sampling identifiers.

Generate a data-adequacy report and finalize the target metals and research questions.

## **What I recommend doing next**

The most valuable next step is a **complete data audit and feasibility assessment of your uploaded Excel workbook**, not immediate model development.

I would turn this into a reproducible data-analysis pipeline that produces:

1. A cleaned and normalized master dataset.
2. A paper-wise data-quality report.
3. A river-wise geographical coverage report.
4. A metal-wise and sample-type-wise feasibility report.
5. A coordinate validation and missing-location report.
6. Duplicate and measurement-consistency reports.
7. A ranked selection of suitable metals for water and sediment modelling.
8. A final recommendation on whether spatial prediction, temporal forecasting, or both are scientifically feasible.

I can also help develop the complete Python notebook for this audit and then use its results to finalize the actual experimental design.

For ongoing project management, I can provide a weekly research-progress review and identify unresolved methodological issues as the team advances.

Weekly research progress review

**My overall verdict:** The research idea is worthwhile, but its publication potential will depend much more on the quality of data harmonization, spatial validation, and environmental interpretation than on the number of ML algorithms used. The current dataset is a promising starting point, not yet a validated modelling dataset.