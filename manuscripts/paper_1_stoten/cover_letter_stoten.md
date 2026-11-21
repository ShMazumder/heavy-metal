# Cover Letter for Submission to Science of The Total Environment

**Date:** November 13, 2026  

**To:**  
The Editors-in-Chief  
*Science of The Total Environment* (STOTEN)  
Elsevier  

**Subject:** Submission of Original Research Article: *"Spatial Modeling and Ecological Risk Assessment of Heavy Metal Contamination in River Sediments Across Bangladesh Using River-Network Machine Learning and Geostatistics"*

Dear Editors-in-Chief,

We are pleased to submit our original research article titled **"Spatial Modeling and Ecological Risk Assessment of Heavy Metal Contamination in River Sediments Across Bangladesh Using River-Network Machine Learning and Geostatistics"** for consideration for publication as a Regular Research Paper in *Science of The Total Environment*.

### Overview and Novelty
River sediments in densely populated developing deltas represent critical sinks for legacy industrial contaminants. However, environmental monitoring in these regions is severely hindered by fragmented observations and the fundamental inability of classical geostatistical interpolation (e.g., Ordinary Kriging, IDW) to generalize across non-continuous, directed river networks without severe terrestrial boundary artifacts.

In this work, we present the first nationwide, river-network-constrained machine learning framework for heavy metal spatial prediction and ecological risk assessment in Bangladesh:
1. **Multi-Study Synthesis & Autocorrelation Proof:** We consolidated and harmonized 289 sediment records across 10 major river systems from 17 peer-reviewed studies (within a wider 28-study, 12-river national database spanning 2010–2024, with field sampling spanning 2010–2022). Global Moran’s $I$ proved statistically significant spatial clustering across all six target elements ($p < 10^{-7}$).
2. **Topological HydroSHEDS Network Coupling:** We integrated the HydroSHEDS HydroRIVERS reach network (**55,668 segments**) to parameterize machine learning models with physical drainage metrics (`UPLAND_SKM`, `DIS_AV_CMS`, `ORD_STRA`).
3. **Overcoming Geostatistical Failure:** Under rigorous 5-fold spatial cross-validation, we demonstrate that while classical Ordinary Kriging collapses when predicting across disconnected river basins ($R^2 = -63.85$ for Cr), CatBoost gradient boosting achieves superior predictive power ($R^2 = 0.639$ for Pb, $0.569$ for Cd, $0.520$ for Cr).
4. **Explainable AI (TreeSHAP):** We demonstrate that upstream sub-catchment retention area, geographic longitudinal gradient, and sediment pH drive over 65% of predictive variance.
5. **National Cartography:** We provide contiguous reach-level predictions across all 55,668 reaches, revealing that **55.8% of the national river network exhibits Very High Ecological Risk ($RI \ge 600$)**.

### Relevance to STOTEN
This manuscript directly aligns with the scope of *Science of The Total Environment*, specifically within the domains of heavy metal environmental partitioning, catchment-scale geospatial modeling, and ecological risk evaluation in anthropogenically stressed aquatic systems.

### Author Confirmations
- This manuscript is original, has not been published previously, and is not currently under consideration for publication elsewhere.
- All authors have approved the manuscript and agree with its submission to *Science of The Total Environment*.
- There are no known conflicts of interest associated with this publication.
- All underlying data, code, GIS layers, and trained models have been made publicly accessible in our repository: `https://github.com/ShMazumder/heavy-metal.git`.

### Suggested Reviewers
1. **Prof. Dr. Md. Saiful Islam** — Department of Soil Science, Patuakhali Science and Technology University, Bangladesh. *Expert in trace element contamination and ecological risk in Bangladesh rivers.* Email: `msaifulpstu@yahoo.com`
2. **Prof. Dr. Bernhard Lehner** — Department of Geography, McGill University, Canada. *Lead developer of the HydroSHEDS global hydrographic database and river routing analysis.* Email: `bernhard.lehner@mcgill.ca`
3. **Dr. Scott M. Lundberg** — Microsoft Research / Paul G. Allen School of Computer Science & Engineering, University of Washington, USA. *Pioneer of TreeSHAP and explainable machine learning.* Email: `scott.lundberg@microsoft.com`

Thank you very much for your time and consideration of our work.

Sincerely,

**The Authors**  
Corresponding Author: `sh.mazumder@example.edu`
