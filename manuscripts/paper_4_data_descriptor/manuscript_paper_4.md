# A Curated and Snapped Geospatial Database of Heavy Metal Concentrations in River Sediments and Waters Across Bangladesh (2010–2024)

**Target Journal:** *Scientific Data* (Nature Portfolio, IF 5.8)  
**Article Type:** Data Descriptor  
**Authors:** Author One$^{1,*}$, Author Two$^{1,2}$, Author Three$^{2}$  

$^{1}$Department of Environmental Science and Engineering, University Name, Dhaka, 1000, Bangladesh  
$^{2}$Institute of Water and Flood Management, Technical University, Dhaka, 1205, Bangladesh  
$^*$Corresponding author: Author One (author.one@university.edu)  

---

## Abstract
Potentially toxic heavy metals in riverine corridors of the Ganges-Brahmaputra-Meghna delta threaten aquatic ecology and drinking water security for over 170 million people. Although numerous environmental investigations have been published across Bangladesh over the past 15 years, data remain fragmented in static PDF tables, lack standardized geospatial referencing, and conflate acute dissolved aqueous concentrations with benthic sediment sinks. Here, we present a harmonized, provenance-documented, and hydrologically snapped geospatial database of heavy metal concentrations in river waters and bed sediments across Bangladesh compiled from 28 peer-reviewed publications (2010–2024). The database contains 557 verified analytical assays—289 bed sediment records across 133 unique station centroids and 268 surface water records across 12 major river basins—covering seven key trace elements (As, Cd, Cr, Cu, Ni, Pb, Zn) alongside 106 bulk physicochemical records. All stations are snapped to topological river reach polylines from HydroSHEDS HydroRIVERS (mean offset: 357 m). The database is distributed in open formats (SQLite, CSV, Parquet, GeoPackage) to facilitate regional machine learning, spatial modeling, and water safety planning.

---

## Background & Summary
River networks of developing deltaic nations face acute environmental pressures from rapid industrial expansion, urbanization, and agrochemical runoff. In Bangladesh, located in the Bengal Delta at the confluence of the Ganges, Brahmaputra, and Meghna rivers, untreated effluents from leather tanneries, textile dyeing mills, metal finishing plants, and municipal discharges are routed directly into natural river corridors (Islam et al., 2015; Bhuiyan et al., 2015). Heavy metals and metalloids (e.g., Lead, Chromium, Cadmium, Arsenic, Nickel, Copper, Zinc) represent a premier environmental hazard due to their environmental persistence, potential for trophic bioaccumulation, and chronic human toxicity (Järup, 2003; Tchounwou et al., 2012).

Despite substantial academic research on heavy metal pollution in Bangladeshi rivers published between 2010 and 2024, existing datasets suffer from severe fragmentation and usability barriers:
1. **Isolated Static Formats:** Concentration measurements are locked within unstructured tables in supplementary PDFs, preventing automated ingestion, meta-analysis, or large-scale machine learning.
2. **Inconsistent Georeferencing:** Published sampling locations often lack verified coordinates, report coordinates in conflicting formats (DMS, decimal degrees, coordinate ranges), or report coordinates that fall on terrestrial landmasses due to typographical errors.
3. **Absence of Topological Fluvial Routing:** Environmental mapping studies typically interpolate river water and sediment metals using two-dimensional planar Euclidean methods (such as Ordinary Kriging or Inverse Distance Weighting). However, rivers are directed dendritic networks governed by upstream flow accumulation, catchment topography, and stream order. Planar interpolation creates severe boundary artifacts across dry landmasses and between hydrologically disconnected basins.
4. **Fraction Confounding:** Existing literature often fails to distinguish between dissolved aqueous fractions ($<0.45\ \mu\text{m}$ filtered) and total recoverable digestions, or conflates acute water measurements with decadal sediment repositories.

To overcome these structural limitations, we created a standardized, quality-controlled, and topologically snapped relational database consolidating published heavy metal measurements in Bangladesh rivers from 2010 through 2024. The resulting database synthesizes 557 analytical records across 28 peer-reviewed studies and 12 river systems into a relational SQLite architecture and open CSV/Parquet formats. Every station has been georeferenced and snapped to the nearest reach segment of the global HydroSHEDS HydroRIVERS hydrographic network, pairing chemical concentrations with upstream catchment area, Strahler stream order, annual discharge, and distance to the river mouth. This dataset provides an essential, ready-to-use digital foundation for researchers, environmental regulators, and spatial hydrologists.

---

## Methods

### Literature Compilation and Screening Workflow
Data compilation was performed following systematic review protocols across five scientific databases: Web of Science Core Collection, Scopus, ScienceDirect, PubMed, and BANSDOC for publications between January 2010 and March 2024. Candidate studies were screened against five strict eligibility gates:
1. Field sampling conducted within natural flowing river corridors in Bangladesh.
2. Explicit numerical reporting of elemental concentrations for at least one target heavy metal (Pb, Cr, Cd, As, Ni, Cu, Zn) with identifiable sample sizes.
3. Documented sampling coordinates or verifiable local landmarks.
4. Documented analytical instrumentation (Flame-AAS, GF-AAS, HG-AAS, or ICP-MS) and sample digestion protocols.
5. Publication in peer-reviewed scientific journals.

Screening of 1,420 initial records identified 28 eligible studies (Figure 1 in `manuscripts/paper_3_systematic_review/`), comprising:
- 11 bed sediment exclusive investigations;
- 12 surface water heavy metal investigations;
- 5 bulk physicochemical water quality investigations.

### Relational Schema Design & Data Harmonization
The database was structured into a four-table normalized relational schema implemented in SQLite (`heavy_metal.db`) and distributed as flat tables:

1. **`studies`:** Contains study-level metadata, including `Study_ID`, Digital Object Identifier (`DOI`), publication year, journal name, analytical instrument, digestion protocol, quality-assurance flags (use of Certified Reference Materials [CRMs], blanks, replicates), and overall study quality score (0–14 rubric).
2. **`stations`:** Contains spatial provenance for each unique sampling location, including `Station_ID`, standardized river name, division/district, raw published coordinate string, validated WGS84 decimal degrees (`Lat_WGS84`, `Lon_WGS84`), coordinate accuracy flag (A = exact GPS; B = published station; C = georeferenced map landmark), and snapped reach identifier (`HYRIV_ID`).
3. **`assays`:** Contains individual chemical measurements, specifying `Assay_ID`, `Station_ID`, environmental medium (`sediment` or `water`), operational fraction (`dissolved`, `total`, or `total recoverable`), element symbol, original published value and unit, harmonized value, censoring status (0 = quantified; 1 = below detection limit), and Method Detection Limit (`LOD`).
4. **`catchment_covariates`:** Contains HydroSHEDS topological stream attributes linked by `HYRIV_ID`, including cumulative upstream catchment area (`UPLAND_SKM`), mean annual discharge (`DIS_AV_CMS`), Strahler stream order (`ORD_STRA`), and fluvial distance to the marine outlet (`DIST_DN_KM`).

### Coordinate Verification & Topological HydroRIVERS Snapping
Published coordinates were audited and converted into standardized WGS84 decimal degrees (EPSG:4326). Coordinate ranges were resolved by consulting published maps and gazetteers to identify discrete sampling stations.

All sampling stations were projected to metric coordinates (EPSG:3857, Pseudo-Mercator) and snapped to the nearest HydroSHEDS HydroRIVERS v1.0 reach centerline polyline using spatial index nearest-neighbor joining. Snapping distance offsets were computed:
- 67.4% of stations snapped within 500 meters of the river polyline centerline;
- 97.7% of stations snapped within 1,000 meters;
- Maximum offset was 2,021 meters (mean offset: 357 meters), consistent with deltaic channel widths, braiding, and historical river meandering in the Bengal floodplain.

### Unit Harmonization and Censoring Protocols
Measurement units were audited against primary publications:
- **Sediment Assays ($N=289$):** Harmonized strictly to milligrams per kilogram dry weight ($\text{mg/kg dw}$).
- **Surface Water Assays ($N=268$):** Harmonized to milligrams per liter ($\text{mg/L}$) and micrograms per liter ($\mu\text{g/L}$).
- **Censored Observations ($<\text{LOD}$):** Reported non-detects were flagged explicitly (`Censored_Flag = 1`), preserving the original reported detection limit without arbitrary substitution.

---

## Data Records
All data records are available through GitHub ([https://github.com/ShMazumder/heavy-metal.git](https://github.com/ShMazumder/heavy-metal.git)) and archived on Zenodo (DOI: 10.5281/zenodo.XXXXXXX).

### File Formats & Manifest
The dataset is organized into `data/processed/` and `data/raw/`:

```
data/
├── raw/
│   ├── Final_Data_Table.xlsx          # Original literature extraction
│   ├── hydrorivers_bangladesh.gpkg    # Clipped HydroRIVERS network
│   ├── bangladesh_boundary.geojson    # National boundary polygon
│   └── source_pdfs/                   # P01–P28 primary PDF articles
└── processed/
    ├── heavy_metal.db                 # Master relational SQLite database
    ├── water_data.csv                 # Surface water chemical assays (268 rows, 49 cols)
    ├── sediment_data.csv              # Bed sediment chemical assays (289 rows, 32 cols)
    ├── stations.csv                   # Georeferenced station centroids (133 rows)
    ├── studies.csv                    # Provenance and study metadata (28 rows)
    ├── master_harmonized.csv          # Denormalized master assay table (557 rows)
    └── station_hydrorivers_matched.csv# Topological reach join table (133 rows)
```

### Data Dictionary

#### 1. `water_data.csv` (268 rows $\times$ 49 columns)
- `Obs_ID`: Unique integer observation identifier (1 to 268).
- `Station_ID`: Globally unique station code (e.g., `STN_001`).
- `Study_ID`: Study code (`P01` to `P28`).
- `River`: Standardized river name (e.g., `Buriganga`, `Karnaphuli`, `Korotoa`, `Padma`, `Rupsa`).
- `Division`: Administrative division (e.g., `Dhaka`, `Chattogram`, `Rajshahi`).
- `Sampling_Year`: Year of field sampling (2010 to 2024; `NR` where unstated).
- `Season`: Hydrological season (`Winter`, `Rainy`, `Summer`, `Spring`, `Late Autumn`).
- `Lat_WGS84`, `Lon_WGS84`: Geographic coordinates in WGS84 decimal degrees.
- `Temperature_C`, `pH`, `DO_mg_L`, `BOD_mg_L`, `COD_mg_L`, `EC_uS_cm`, `TDS_mg_L`: In-situ water quality parameters.
- `As_mg_L`, `Cr_mg_L`, `Cd_mg_L`, `Pb_mg_L`, `Cu_mg_L`, `Zn_mg_L`, `Ni_mg_L`: Trace metal concentrations in mg/L.
- `As_ug_L` to `Ni_ug_L`: Corresponding concentrations in $\mu\text{g/L}$.

#### 2. `sediment_data.csv` (289 rows $\times$ 32 columns)
- `Obs_ID`: Unique sediment record identifier (1 to 289).
- `Station_ID`, `Study_ID`, `River`, `Division`, `Lat_WGS84`, `Lon_WGS84`: Spatial and study metadata.
- `As_mg_kg_dw`, `Cr_mg_kg_dw`, `Cd_mg_kg_dw`, `Pb_mg_kg_dw`, `Cu_mg_kg_dw`, `Zn_mg_kg_dw`, `Ni_mg_kg_dw`: Heavy metal concentrations in mg/kg dry weight.
- `pH`, `Organic_Matter_pct`, `OC_pct`, `Sand_pct`, `Silt_pct`, `Clay_pct`, `Textural_Class`: Sediment physicochemical properties.

#### 3. `studies.csv` (28 rows $\times$ 8 columns)
- `Study_ID`: Primary key (`P01` to `P28`).
- `DOI`: Verified Digital Object Identifier with Crossref resolution.
- `Journal_Name`: Full journal name.
- `Author_Year`: Short citation (e.g., `Islam et al., 2015`).
- `Detection_Method`: Spectrometry instrument (e.g., `ICP-MS (Agilent 7700)`, `GF-AAS`, `Flame AAS`).
- `Total_Records`: Count of extracted assays.
- `River_List`: Monitored rivers.
- `Sample_Types`: Medium (`Water`, `Sediment`, or `Both`).

---

## Technical Validation

### Extraction Concordance Audit
To ensure 100% extraction fidelity, a dual-evaluator audit was performed. An independent researcher re-extracted 20% of randomly selected records from primary PDFs and cross-verified numerical values against the database. Zero numerical discordances were detected across the audit sample (95% CI on discordance: 0.0–2.8%).

### Instrumental Sensitivity Stratification
Historical compilations often conflate detection limits of flame atomic absorption spectrometry (Flame-AAS, $\text{DL} = 0.005\text{--}0.050$ mg/L) with genuine trace concentrations. We validated instrumental reliability by segregating observations into high-sensitivity instrumentation (GF-AAS, HG-AAS, ICP-MS with sub-$\mu\text{g/L}$ detection limits, $N=77$) versus Flame-AAS ($N=69$). Across high-sensitivity records, Lead exhibited a median of **0.0171 mg/L**, with **79.2%** of samples exceeding the WHO 0.010 mg/L potable guideline. This confirms that elevated dissolved trace metal concentrations are an authentic geochemical property of monitored river corridors and cannot be attributed to flame-AAS detection limit artifacts.

### Geochemical Baseline Plausibility
Sediment concentrations were evaluated against Upper Continental Crust (UCC) baselines (Wedepohl, 1995) and global river sediment baselines (Gaillardet et al., 2014). Background-to-peak concentration ratios spanned 1 to 2 orders of magnitude in urban corridors (e.g., Chromium exceeding 1,800 mg/kg near Hazaribagh tanneries and Lead exceeding 3,300 mg/kg near industrial battery clusters), closely mirroring known localized point-source effluent discharge profiles in the delta.

---

## Usage Notes

### Querying SQLite Database in Python
The relational database `heavy_metal.db` can be queried directly using Python's standard `sqlite3` and `pandas` libraries:

```python
import sqlite3
import pandas as pd

# Connect to master relational database
conn = sqlite3.connect('data/processed/heavy_metal.db')

# Query joined water quality and topological reach features
query = """
SELECT 
    w.Obs_ID, w.River, w.Lat_WGS84, w.Lon_WGS84, w.Season,
    w.Pb_mg_L, w.Cr_mg_L, w.Cd_mg_L, w.As_mg_L,
    s.DOI, s.Detection_Method,
    m.ORD_STRA, m.DIS_AV_CMS, m.UPLAND_SKM
FROM water_data w
JOIN studies s ON w.Study_ID = s.Study_ID
JOIN station_hydrorivers_matched m ON w.Station_ID = m.Station_ID
WHERE w.Pb_mg_L IS NOT NULL;
"""
df = pd.read_sql_query(query, conn)
conn.close()

print(f"Loaded {len(df)} records with topological reach attributes.")
```

### Computing Benchmark Exceedance in R
Users conducting regulatory audits can evaluate compliance in R:

```R
library(dplyr)

# Load harmonized surface water dataset
df_water <- read.csv("data/processed/water_data.csv")

# Compute WHO and ECR 2023 exceedance for Lead (Pb threshold = 0.010 mg/L)
pb_summary <- df_water %>%
  filter(!is.na(Pb_mg_L)) %>%
  summarise(
    Total_Assays = n(),
    Exceed_Count = sum(Pb_mg_L > 0.010),
    Exceed_Pct = (sum(Pb_mg_L > 0.010) / n()) * 100,
    Median_Pb = median(Pb_mg_L),
    IQR_Pb = IQR(Pb_mg_L)
  )

print(pb_summary)
```

---

## Code Availability
All code used for literature extraction, coordinate snapping, geostatistical benchmarking, meta-regression, and figure generation is available under the MIT license at GitHub: [https://github.com/ShMazumder/heavy-metal.git](https://github.com/ShMazumder/heavy-metal.git).

---

## References
- BBS, 2022. Population and Housing Census 2022: Preliminary Report. Bangladesh Bureau of Statistics, Dhaka.
- Bhuiyan, M.A.H., Dampare, S.B., Islam, M.A., Suzuki, S., 2015. Source apportionment and pollution evaluation of heavy metals in water and sediments of Buriganga River. *Environ. Monit. Assess.* 187, 4075.
- Gaillardet, J., Viers, J., Dupré, B., 2014. Trace elements in river waters. In: *Treatise on Geochemistry*, 2nd ed., pp. 195–235.
- Goodbred, S.L., Kuehl, S.A., 1999. Holocene and modern sediment budgets for the Ganges-Brahmaputra river system. *Geology* 27, 559–562.
- Islam, M.S., Ahmed, M.K., Raknuzzaman, M., Habibullah-Al-Mamun, M., Islam, M.K., 2015. Heavy metal pollution in surface water and sediment. *Ecol. Indic.* 48, 282–291.
- Järup, L., 2003. Hazards of heavy metal contamination. *Br. Med. Bull.* 68, 167–182.
- Lehner, B., Grill, G., 2013. Global river hydrography and network routing. *Hydrol. Process.* 27, 2171–2186.
- Mortuza, M.G., 2024. Heavy metal concentrations in water and sediment of Padma River. *Fish. Aquat. Sci.* 27, e8.
- Tchounwou, P.B., Yedjou, C.G., Patlolla, A.K., Sutton, D.J., 2012. Heavy metal toxicity and the environment. *Mol. Clin. Environ. Toxicol.* 101, 133–164.
- Wedepohl, K.H., 1995. The composition of the continental crust. *Geochim. Cosmochim. Acta* 59, 1217–1232.
- WHO, 2022. Guidelines for Drinking-water Quality, 4th ed. World Health Organization, Geneva.
