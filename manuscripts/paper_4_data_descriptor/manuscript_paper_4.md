# A Curated and Snapped Geospatial Database of Heavy Metal Concentrations in River Sediments and Waters Across Bangladesh (2010–2025)

**Target Journal:** *Scientific Data* (Nature Portfolio, IF 5.8)  
**Article Type:** Data Descriptor  
**Authors:** Author One$^{1,*}$, Author Two$^{1,2}$, Author Three$^{2}$  

$^{1}$Department of Environmental Science and Engineering, University Name, Dhaka, 1000, Bangladesh  
$^{2}$Institute of Water and Flood Management, Technical University, Dhaka, 1205, Bangladesh  
$^*$Corresponding author: Author One (author.one@university.edu)  

---

## Abstract
Potentially toxic heavy metals in riverine corridors of the Ganges-Brahmaputra-Meghna delta threaten aquatic ecology and drinking water security for over 170 million people. Although numerous environmental investigations have been published across Bangladesh over the past 15 years, data remain fragmented in static PDF tables, lack standardized geospatial referencing, and conflate acute dissolved aqueous concentrations with benthic sediment sinks. Here, we present a harmonized, provenance-documented, and hydrologically snapped geospatial database of heavy metal concentrations in river waters and bed sediments across Bangladesh compiled from 28 peer-reviewed publications (2010–2025). The database contains 557 verified analytical assays—289 bed sediment records across 133 observation events and 268 surface water records (comprising 162 trace element assays across 12 investigations and 106 bulk physicochemical records across 5 investigations) across 12 major river basins—covering seven key trace elements (As, Cd, Cr, Cu, Ni, Pb, Zn). The dataset indexes 222 distinct physical sampling stations (disambiguated by a composite `Station_UID` primary key; 85 georeferenced stations with published coordinates across 58 unique coordinate locations, and 137 descriptive local gazetteer stations). All 85 georeferenced sampling stations were projected to metric UTM Zone 45N (EPSG:32645) and snapped to topological river reach polylines from HydroSHEDS HydroRIVERS (mean offset: 379.6 m, median: 262.1 m, max: 1,850.4 m; 75.3% within 500 m, 96.5% within 1,000 m). The database is distributed in open formats (SQLite with foreign keys and validation views, CSV, Apache Parquet, GeoPackage) to facilitate regional machine learning, spatial modeling, and water safety planning.

---

## Background & Summary
River networks of developing deltaic nations face acute environmental pressures from rapid industrial expansion, urbanization, and agrochemical runoff. In Bangladesh, located in the Bengal Delta at the confluence of the Ganges, Brahmaputra, and Meghna rivers, untreated effluents from leather tanneries, textile dyeing mills, metal finishing plants, and municipal discharges are routed directly into natural river corridors (Islam et al., 2015; Bhuiyan et al., 2015). Heavy metals and metalloids (e.g., Lead, Chromium, Cadmium, Arsenic, Nickel, Copper, Zinc) represent a premier environmental hazard due to their environmental persistence, potential for trophic bioaccumulation, and chronic human toxicity (Järup, 2003; Tchounwou et al., 2012).

Despite substantial academic research on heavy metal pollution in Bangladeshi rivers published between 2010 and 2025, existing datasets suffer from severe fragmentation and usability barriers:
1. **Isolated Static Formats:** Concentration measurements are locked within unstructured tables in supplementary PDFs, preventing automated ingestion, meta-analysis, or large-scale machine learning.
2. **Inconsistent Georeferencing & Cross-Basin Collisions:** Published sampling locations often lack verified coordinates or reuse identical local station identifiers across distinct rivers (e.g., station identifiers P08_S1 through S5 recycled across five separate rivers in one study). Unchecked string joins cause artificial data conflation across geographically disparate basins.
3. **Absence of Topological Fluvial Routing:** Environmental mapping studies typically interpolate river water and sediment metals using two-dimensional planar Euclidean methods (such as Ordinary Kriging or Inverse Distance Weighting). However, rivers are directed dendritic networks governed by upstream flow accumulation, catchment topography, and stream order. Planar interpolation creates severe boundary artifacts across dry landmasses and between hydrologically disconnected basins.
4. **Fraction Confounding:** Existing literature often fails to distinguish between dissolved aqueous fractions ($<0.45\ \mu\text{m}$ filtered) and total recoverable digestions, or conflates acute water measurements with decadal sediment repositories.

To overcome these structural limitations, we created a standardized, quality-controlled, and topologically snapped relational database consolidating published heavy metal measurements in Bangladesh rivers from 2010 through 2025. The resulting database synthesizes 557 analytical records across 28 peer-reviewed studies and 12 river systems into an 8-table relational SQLite architecture (`heavy_metal.db`) and open CSV/Parquet formats. Every coordinate-resolved physical station ($n=85$, representing 222 physical sites across 58 unique coordinate locations) has been georeferenced and snapped in metric UTM coordinates to the nearest reach segment of the global HydroSHEDS HydroRIVERS hydrographic network, pairing chemical concentrations with upstream catchment area, Strahler stream order, annual discharge, and distance to the river mouth. This dataset provides an essential, ready-to-use digital foundation for researchers, environmental regulators, and spatial hydrologists.

---

## Methods

### Literature Compilation and Screening Workflow
Data compilation was performed following systematic review protocols across five scientific databases: Web of Science Core Collection, Scopus, ScienceDirect, PubMed, and BANSDOC for publications between January 2010 and March 2025. Candidate studies were screened against five strict eligibility gates:
1. Field sampling conducted within natural flowing river corridors in Bangladesh.
2. Explicit numerical reporting of elemental concentrations for at least one target heavy metal (Pb, Cr, Cd, As, Ni, Cu, Zn) with identifiable sample sizes.
3. Documented sampling coordinates or verifiable local landmarks.
4. Documented analytical instrumentation (Flame-AAS, GF-AAS, HG-AAS, or ICP-MS) and sample digestion protocols.
5. Publication in peer-reviewed scientific journals.

Screening of 1,420 initial records identified 28 eligible studies (Figure 1 in `manuscripts/paper_3_systematic_review/`), comprising:
- 11 bed sediment exclusive investigations;
- 12 surface water heavy metal investigations;
- 5 bulk physicochemical water quality investigations.

The complete screening trail (1,420 candidates $\to$ 838 non-duplicate abstracts $\to$ 74 full-text articles $\to$ 28 included studies) is distributed as `prisma_screening_records.csv`.

### Relational Schema Design & Data Harmonization
The database was structured into an 8-table normalized relational schema implemented in SQLite (`heavy_metal.db`) with foreign key integrity constraints, and distributed as flat CSV and Apache Parquet files:

1. **`studies`:** Contains study-level metadata, including `Study_ID`, Digital Object Identifier (`DOI`), publication year, journal name, analytical instrument, digestion protocol, quality-assurance flags (use of Certified Reference Materials [CRMs], blanks, replicates), and overall study quality score (0–14 rubric).
2. **`stations`:** Master register of 222 distinct physical sampling locations. To eliminate cross-river identifier collisions, each physical location is indexed by a canonical composite primary key `Station_UID` (`Paper_No_River_Station_No`), while preserving the original published `Station_ID` for backward compatibility. Contains standardized river name, administrative division, district, validated WGS84 decimal degrees (`Lat_WGS84`, `Lon_WGS84`), and coordinate classification (85 georeferenced stations, 137 descriptive gazetteer stations).
3. **`water_data`:** Contains 268 surface water observation records, linked by `Station_UID` and `Study_ID`, spanning in-situ physicochemical parameters and dissolved/total metal concentrations.
4. **`sediment_data`:** Contains 289 bed sediment observation records, linked by `Station_UID` and `Study_ID`, spanning grain size fractions, organic carbon, and trace metal concentrations.
5. **`master_harmonized`:** Denormalized synthesis of all 557 analytical records linking water and sediment assays with spatial coordinates and station identifiers.
6. **`station_hydrorivers_matched`:** Topological reach join table linking all 85 georeferenced stations via `Station_UID` to HydroSHEDS reach identifiers (`HYRIV_ID`) with Euclidean snapping distances computed in metric projection.
7. **`study_extraction_evidence`:** Comprehensive 8-domain CEE critical appraisal matrix for all 28 included studies, documenting distinct physical station counts, analytical instruments, and auditor validation signatures.
8. **`prisma_screening_records`:** Full PRISMA 2020 eligibility audit tracking all 1,420 screened publications through each filtering stage.

### Coordinate Verification & Topological HydroRIVERS Snapping
Published coordinates were audited and converted into standardized WGS84 decimal degrees (EPSG:4326). Coordinate ranges were resolved by consulting published maps and gazetteers to identify discrete sampling stations.

All coordinate-resolved physical sampling stations ($N=85$ distinct physical stations with known coordinates; 137 descriptive entries lacked coordinates in source literature) were projected to metric UTM Zone 45N (EPSG:32645)—eliminating the +9.2% distance scale distortion inherent to planar Web Mercator (EPSG:3857) projections at latitude 23.5$^\circ$N—and snapped to the nearest HydroSHEDS HydroRIVERS v1.0 reach centerline polyline using Euclidean nearest-neighbor search. Snapping distance offsets were computed:
- 75.3% of stations ($n=64$) snapped within 500 meters of the reach centerline polyline;
- 96.5% of stations ($n=82$) snapped within 1,000 meters;
- Only 3 station records (3.5%) exceeded 1,000 meters: station P20_S1 in the wide tidal Rupsa River estuary (1,850.4 meters), station P27_S1 along the 4-km-wide braided Padma River mainstem (1,124.0 meters), and station P20_S2 (1,028.5 meters), consistent with deltaic estuarine channel widths, tidal braiding, and historical river meandering in the Bengal floodplain (mean offset: 379.6 meters, median: 262.1 meters, max: 1,850.4 meters).

### Unit Harmonization and Censoring Protocols
Measurement units were audited against primary publications:
- **Sediment Assays ($N=289$):** Harmonized strictly to milligrams per kilogram dry weight ($\text{mg/kg dw}$).
- **Surface Water Assays ($N=268$):** Harmonized to milligrams per liter ($\text{mg/L}$) and micrograms per liter ($\mu\text{g/L}$).
- **Censored Observations ($<\text{LOD}$):** Reported non-detects were flagged explicitly (`Censored_Flag = 1`), preserving the original reported detection limit without arbitrary substitution.

---

## Data Records
All data records are available through GitHub ([https://github.com/ShMazumder/heavy-metal.git](https://github.com/ShMazumder/heavy-metal.git)) and archived on Zenodo (DOI: 10.5281/zenodo.24414976).

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
    ├── heavy_metal.db                 # Master relational SQLite database (8 tables, 2 views)
    ├── *.parquet                      # Columnar Apache Parquet exports for all tabular datasets
    ├── water_data.csv                 # Surface water chemical assays (268 rows, 49 cols)
    ├── sediment_data.csv              # Bed sediment chemical assays (289 rows, 32 cols)
    ├── stations.csv                   # Physical stations (222 rows: 85 georeferenced centroids, 137 descriptive)
    ├── studies.csv                    # Provenance and study metadata (28 rows)
    ├── master_harmonized.csv          # Denormalized master assay table (557 rows, 59 cols)
    ├── station_hydrorivers_matched.csv# Metric UTM 45N topological reach join table (85 rows)
    ├── study_extraction_evidence.csv  # CEE 8-domain extraction evidence table (28 rows)
    └── prisma_screening_records.csv   # Machine-readable PRISMA 2020 screening log (1,420 rows)
```

### Data Dictionary

#### 1. `water_data.csv` (268 rows $\times$ 49 columns)
- `Obs_ID`: Unique integer observation identifier (1 to 268).
- `Station_UID`: Composite canonical station code (e.g., `P08_Balu_S1`).
- `Station_ID`: Published station code (e.g., `STN_001`).
- `Study_ID`: Study code (`P01` to `P28`).
- `River`: Standardized river name (e.g., `Buriganga`, `Karnaphuli`, `Korotoa`, `Padma`, `Rupsa`).
- `Division`: Administrative division (e.g., `Dhaka`, `Chattogram`, `Rajshahi`).
- `Sampling_Year`: Year of field sampling (2010 to 2025; `NR` where unstated).
- `Season`: Hydrological season (`Winter`, `Rainy`, `Summer`, `Spring`, `Late Autumn`).
- `Lat_WGS84`, `Lon_WGS84`: Geographic coordinates in WGS84 decimal degrees.
- `Temperature_C`, `pH`, `DO_mg_L`, `BOD_mg_L`, `COD_mg_L`, `EC_uS_cm`, `TDS_mg_L`: In-situ water quality parameters.
- `As_mg_L`, `Cr_mg_L`, `Cd_mg_L`, `Pb_mg_L`, `Cu_mg_L`, `Zn_mg_L`, `Ni_mg_L`: Trace metal concentrations in mg/L.
- `As_ug_L` to `Ni_ug_L`: Corresponding concentrations in $\mu\text{g/L}$.

#### 2. `sediment_data.csv` (289 rows $\times$ 32 columns)
- `Obs_ID`: Unique sediment record identifier (1 to 289).
- `Station_UID`, `Station_ID`, `Study_ID`, `River`, `Division`, `Lat_WGS84`, `Lon_WGS84`: Spatial and study metadata.
- `As_mg_kg_dw`, `Cr_mg_kg_dw`, `Cd_mg_kg_dw`, `Pb_mg_kg_dw`, `Cu_mg_kg_dw`, `Zn_mg_kg_dw`, `Ni_mg_kg_dw`: Heavy metal concentrations in mg/kg dry weight.
- `pH`, `Organic_Matter_pct`, `OC_pct`, `Sand_pct`, `Silt_pct`, `Clay_pct`, `Textural_Class`: Sediment physicochemical properties.

#### 3. `stations.csv` (222 rows $\times$ 15 columns)
- `Station_UID`: Primary key (`Paper_No_River_Station_No`, e.g., `P08_Balu_S1`).
- `Station_ID`: Published station label.
- `Study_ID`: Study code (`P01` to `P28`).
- `River`: Standardized river name.
- `Division`, `District`: Administrative location.
- `Station_Name_Raw`: Published station name string.
- `Lat_WGS84`, `Lon_WGS84`: Coordinates (decimal degrees; blank for descriptive stations).
- `Coordinate_Type`: `Georeferenced` ($n=85$) or `Descriptive_Gazetteer` ($n=137$).
- `Coordinate_Accuracy`: Provenance code (A = exact GPS; B = published station; C = landmark).

#### 4. `studies.csv` (28 rows $\times$ 8 columns)
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
To ensure 100% extraction fidelity, a dual-evaluator audit was performed. An independent researcher re-extracted 20% of randomly selected records from primary PDFs and cross-verified numerical values against the database. Zero numerical discordances were detected across the audit sample (95% CI on discordance: 0.0–3.3%).

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
JOIN station_hydrorivers_matched m ON w.Station_UID = m.Station_UID
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
