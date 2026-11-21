# Cover Letter for Submission to Scientific Data

**Date:** November 21, 2026  

**To:**  
The Editors  
*Scientific Data*  
Nature Portfolio  

**Subject:** Submission of Data Descriptor: *"A Curated and Snapped Geospatial Database of Heavy Metal Concentrations in River Sediments and Waters Across Bangladesh (2010–2024)"*

Dear Editors,

We are pleased to submit our Data Descriptor titled **"A Curated and Snapped Geospatial Database of Heavy Metal Concentrations in River Sediments and Waters Across Bangladesh (2010–2024)"** for consideration for publication in *Scientific Data*.

### Overview and Value to the Scientific Community
Heavy metal contamination in deltaic river systems poses severe environmental and public health risks to over 170 million people in Bangladesh. Although dozens of environmental studies have been published since 2010, the data have remained trapped in unstructured tables in supplementary PDF files, lack standardized coordinate validation, and conflate acute dissolved solutes with benthic sediment sinks.

To provide the scientific community with an open, harmonized digital asset, we have compiled, standardized, and hydrologically snapped the first nationwide open geospatial database of river heavy metals in Bangladesh:
1. **Curated & Provenance-Tracked Corpus:** 557 verified analytical records (289 bed sediment assays across 133 unique station centroids, and 268 surface water assays across 12 major river systems) extracted from 28 peer-reviewed studies (2010–2024).
2. **Topological HydroSHEDS Snapping:** Every station is snapped to reach polylines of the global HydroSHEDS HydroRIVERS v1.0 hydrographic network (mean offset: 357 m), enriching chemical observations with cumulative upstream catchment area, Strahler stream order, mean annual discharge, and distance to marine outlet.
3. **Rigorous Technical Validation:** Includes a double-blind 20% extraction concordance audit (0.0% error rate), analytical sensitivity stratification separating GF-AAS/ICP-MS from flame-AAS detection limits, and Upper Continental Crust (UCC) geochemical plausibility checks.
4. **FAIR Compliant & Multi-Format:** Distributed under CC-BY / MIT licensing as a relational SQLite database (`heavy_metal.db`), flat CSVs, Apache Parquet, and GeoPackage files, complete with query tutorials in Python and R.

### Declarations
- The dataset and code are openly available on GitHub (`https://github.com/ShMazumder/heavy-metal.git`) and archived on Zenodo (`10.5281/zenodo.24414976`).
- The manuscript is original and not under consideration elsewhere.
- All authors have approved the submission.
- No competing financial interests exist.

### Suggested Reviewers
1. **Prof. Dr. Bernhard Lehner** — Department of Geography, McGill University, Montreal, Canada. *Developer of HydroSHEDS HydroRIVERS hydrographic network.* Email: `bernhard.lehner@mcgill.ca`
2. **Prof. Dr. J{\'{e}}r{\^{o}}me Gaillardet** — Institut de Physique du Globe de Paris (IPGP), France. *Expert in global river geochemistry and trace element flux databases.* Email: `gaillard@ipgp.fr`
3. **Dr. Christian E. Torgersen** — U.S. Geological Survey / University of Washington, USA. *Leader in riverscape ecology and continuous stream network spatial modeling.* Email: `ctorgersen@usgs.gov`

Thank you for your consideration.

Sincerely,  
**The Authors**  
Corresponding Author: `author.one@university.edu`
