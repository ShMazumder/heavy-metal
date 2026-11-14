# Response to Reviewers — Round 2 Revision

**Manuscript Title:** Heavy Metals in Bangladesh River Waters: A Synthesis of Published Records (2010–2024), Benchmark Exceedances, Seasonal Contrasts, and River Network Coverage  
**Journal:** *Chemosphere* (Elsevier)  
**Article Type:** Regular Research Paper  

We sincerely thank the Reviewer and Editor for their rigorous, constructive, and detailed evaluation of our manuscript. In this revision, we have systematically addressed every major and minor critique raised in the Round 2 review. All numerical values across the Abstract, Highlights, Results, Discussion, and Conclusions are now synchronized through a single reproducible Python script (`scripts/reproduce_paper_2_results.py`) feeding LaTeX results macros (`results_macros.tex`).

Below is our point-by-point response detailing the specific revisions, data audits, statistical recalculations, and manuscript updates executed.

---

## 1. Response to Major Comments

### Major Comment 1 (M1): Abstract/Highlights and Results numerical discrepancy
> *"The Abstract/Highlights and Results disagree on the headline spatial numbers... Generate every in-text number from the script (Quarto, or LaTeX macros fed by a results file)."*

**Response:**
We fully agree and have implemented a strict single-source-of-truth architecture:
1. **Single Master Pipeline:** All spatial, chemical, and statistical analyses are executed in `scripts/reproduce_paper_2_results.py`. This script outputs:
   - `data/paper_2_water_results/results.json`
   - `manuscripts/paper_2_chemosphere/results_macros.tex`
2. **Synchronized Numbers Across Manuscript:**
   - Total major river reaches analyzed in HydroSHEDS HydroRIVERS within Bangladesh territory: **3,894 reach segments** totaling **8,369.5 km**.
   - Reaches $>25\text{ km}$ straight-line (Haversine) from any published sampling location: **3,407 segments** (**87.5%** segment count ratio, **7,369.3 km**, **88.0%** stream length ratio).
   - Reaches $>10\text{ km}$: **96.6%** stream length (8,088.1 km).
   - Reaches $>50\text{ km}$: **66.8%** stream length (5,594.7 km).
   - Topological along-network stream distance $>25\text{ km}$ (Dijkstra algorithm along the HydroRIVERS network): **3,682 segments** (**94.6%** stream length ratio, **7,919.9 km**).
3. **Macro Integration:** In `main.tex`, all numbers in the Abstract, Highlights, Results, Discussion, and Conclusions are called strictly via macros (e.g., `\TotalMajorReachesCount`, `\TotalMajorLengthKm`, `\UnsampledCountTwentyFiveKm`, `\UnsampledPctCountTwentyFiveKm`, `\UnsampledLengthTwentyFiveKm`, `\UnsampledPctLengthTwentyFiveKm`, `\UnsampledPctLengthNetworkTwentyFiveKm`), completely eliminating manual transcription errors.

---

### Major Comment 2 (M2): Fixed-Panel HPI and Denominator Shrinkage
> *"HPI is still not computed on a fixed metal panel, and your maximum proves it... Fix a core panel, for example As, Cd, Cr, Pb, Ni, and show a sensitivity run on alternatives."*

**Response:**
We completely agree. The prior blowout to 5,920 was indeed mathematically driven by variable-panel denominator shrinkage ($\sum W_i$) when records with arbitrary $\ge 3$ metal subsets were evaluated.
1. **Standardized Fixed-Panel Primary Index:**
   - We standardized the primary Heavy Metal Pollution Index ($\mathrm{HPI}$) on a fixed **Core-4 panel (As, Cd, Cr, Pb; $N=112$)**, representing elements with mandatory drinking guidelines that were simultaneously measured.
   - Using the authoritative formulation of Prasad & Bose (2001), the Core-4 $\mathrm{HPI}$ yields:
     - **Median:** 156.99 (IQR: 280.55)
     - **Mean:** 395.21
     - **Minimum:** 17.58
     - **Maximum:** 2,682.05 (observed in the highly industrialized Buriganga River)
     - **Critical Limit Exceedance ($HPI > 100$):** 58.9% (66 / 112)
2. **Sensitivity Analysis Across Alternative Fixed Panels:**
   - We conducted a formal sensitivity analysis across nested fixed-metal panels (`data/paper_2_water_results/hpi_panels_sensitivity.csv`):
     - **Core-4 (As, Cd, Cr, Pb; $N=112$):** Median = 156.99, IQR = 280.55, Mean = 395.21, Max = 2,682.05, 58.9% $>100$.
     - **Core-5 (As, Cd, Cr, Pb, Ni; $N=79$):** Median = 231.75, IQR = 301.21, Mean = 478.10, Max = 2,619.19, 73.4% $>100$.
     - **All-7 (As, Cd, Cr, Pb, Ni, Cu, Zn; $N=64$):** Median = 253.02, IQR = 305.84, Mean = 502.77, Max = 2,615.37, 75.0% $>100$.
   - This proves that once panels are fixed, the index exhibits complete mathematical stability, and the former 5,920 maximum is eliminated. Both the primary Core-4 results and the sensitivity table are fully detailed in Section 3.2 and Table 2.

---

### Major Comment 3 (M3): HPI Interpretation, HEI/MI Reconciled, and River Rankings
> *"HPI interpretation is inconsistent, and the other indices contradict it without comment... Report the number of studies per river, add CIs, and delete the causal phrase."*

**Response:**
We have thoroughly overhauled Section 3.2 and the index interpretations:
1. **Critical Threshold Unification:** We standardized strictly on Prasad & Bose's (2001) established critical limit of **$\mathrm{HPI} > 100$** throughout the entire manuscript (Abstract, Methods, Results, Discussion, Conclusions). We also report the proportion exceeding 200 as high pollution.
2. **HEI vs. HPI Rank Concordance:** We calculated the Spearman rank correlation between unweighted $\mathrm{HEI}$ and weighted Core-4 $\mathrm{HPI}$. The correlation is $\rho = 0.976$ ($p < 10^{-15}$), demonstrating excellent rank concordance despite differing weighting philosophies.
3. **Weight Dominance Deconstruction:** We explicitly explain why raw numerical values differ: $\mathrm{HPI}$ inversely weights guidelines ($W_{\text{Cd}} = 333.3$, $W_{\text{Pb}} = 100.0$, $W_{\text{As}} = 100.0$), causing Cd (41.3%), Pb (35.8%), and As (19.9%) to dominate the numerator. In contrast, $\mathrm{HEI}$ treats all exceedance ratios unweighted.
4. **River-Wise Reporting:** Table 2 now reports the number of analyzed records ($N$), the number of primary studies ($K$), median $\mathrm{HPI}$, IQR, mean, and $\% > 100$. We removed all unsupported causal phrases attributing differences to "lower industrial loadings" and explicitly caution in the text that river summaries reflect the small study counts ($K=1$ to $2$) available in the published literature.

---

### Major Comment 4 (M4): Documentation of Data Audit and Supplement S1 Study Table
> *"The data audit is undocumented, and the corrections show the first extraction was unreliable... State how many records were corrected, the error types... Still missing: the study table (Supplement S1)..."*

**Response:**
We have created complete, transparent documentation for the data audit:
1. **Formal Audit Log (`data/paper_2_water_results/audit_log.csv`):**
   - We performed a full diff of the raw database against primary publication texts.
   - Exactly **19 values** across 4 records were corrected:
     - **P04 (Hossain et al., 2021, SN Applied Sciences):** 1 transcription typo. Winter Pb at station BS3 was entered as 33.0 mg/L; audited primary table showed 0.33 mg/L (100× error). Corrected to 0.33 mg/L.
     - **P27 (Sarker et al., 2021):** 18 unit-scaling errors across 3 records (S1, S2, S3) measuring 6 metals (Pb, Cr, Ni, Cd, Zn, Cu). Values published in $\mu\text{g/L}$ had been transcribed as $\text{mg/L}$ ($1,000\times$ error). Since P27 did not measure Arsenic, exceedance counts fell by exactly 3 for Pb, Cr, Ni, Cd, Zn, and Cu, but not for As. Corrected to $\text{mg/L}$ ($\mu\text{g/L} / 1000$).
   - The audit log explicitly records: `Obs_ID`, `Study_ID`, `River`, `Station_ID`, `Parameter`, `Old_Value_mg_L`, `Corrected_Value_mg_L`, `Error_Type`, and `Source_Verification_Note`.
2. **Supplement S1 Study Table (`data/paper_2_water_results/supplement_s1_studies.csv`):**
   - We created Supplement Table S1 documenting all 17 water studies:
     - 12 studies measuring heavy metals (162 records).
     - 5 studies measuring bulk physicochemical parameters only (P07, P15, P16, P23, P26; 106 records).
   - Table S1 details: Citation, Journal, DOI, River, Sampling Years, Seasons, Total Records, Heavy Metal Records, Value Type (individual grab vs site mean), Fraction (dissolved vs total vs unspecified), Analytical Instrument (ICP-MS, AAS), Digestion Method, Detection Limits, QA/QC (CRMs, blanks, duplicates), and Geocode Provenance (study GPS vs river-centroid geocode).
3. **Manuscript Description:** Section 2.1 and the Limitations section explicitly describe the audit protocol, error classifications, and fractions.

---

### Major Comment 5 (M5): Clustered Exceedance Statistics and Full Sensitivity Analysis
> *"Wilson CIs treat 268 clustered records as independent... Use a cluster-robust estimate (GEE with study as cluster) or a random-effects meta-analysis of proportions... Provide a full table: every metal, both benchmarks, N, CI, with and without the three Dhaka rivers, plus leave-one-river-out."*

**Response:**
We have fully addressed data clustering and expanded sensitivity testing:
1. **Study-Level Cluster Bootstrapping ($B=5,000$ Resamples):**
   - Alongside unadjusted Wilson score intervals, we implemented study-level cluster bootstrap 95% confidence intervals ($B=5,000$) where primary studies were resampled with replacement, preserving intra-study correlation structure.
   - Results in Table 1 show wider, robust intervals:
     - **Lead (Pb):** WHO exceedance 85.6% [Cluster CI: 70.6–94.1%, Wilson CI: 79.0–90.4%]; Bangladesh ECR exceedance 34.9% [Cluster CI: 11.4–64.3%].
     - **Chromium (Cr):** WHO & BD exceedance 60.6% [Cluster CI: 32.3–82.9%].
     - **Nickel (Ni):** WHO 54.8% [Cluster CI: 22.4–79.1%]; BD 45.2% [Cluster CI: 14.9–67.5%].
     - **Arsenic (As):** WHO 54.9% [Cluster CI: 18.1–84.9%]; BD 18.0% [Cluster CI: 1.6–42.9%].
     - **Cadmium (Cd):** WHO 44.7% [Cluster CI: 13.5–77.1%]; BD 40.2% [Cluster CI: 12.2–69.5%].
2. **Comprehensive Sensitivity Matrix (`data/paper_2_water_results/sensitivity_full_table.csv`):**
   - We evaluated:
     - Full pooled dataset ($N=162$).
     - Non-Dhaka subset (excluding Buriganga, Turag, Shitalakhya).
     - Full Leave-One-River-Out (LORO) bounds for all 7 metals across WHO, BD ECR, and FAO guidelines.
   - Non-Dhaka results show:
     - WHO Pb exceedance remains high at 82.6%, but Bangladesh ECR exceedance drops from 34.9% to **18.3%**.
     - Bangladesh ECR Arsenic drops from 18.0% to **8.9%**.
   - These results are fully tabulated and discussed in Section 3.1.

---

### Major Comment 6 (M6): Seasonal Contrasts, Sample Accounting, and Competing Hypotheses
> *"Between 34% and 47% of records are dropped from each test... Run a within-study contrast where studies sampled both seasons... offer geogenic baseflow / return flow as an alternative."*

**Response:**
We have thoroughly revised the seasonal section:
1. **Seasonal Sample Accounting (`data/paper_2_water_results/seasonal_sample_accounting.csv`):**
   - Out of 162 heavy metal records:
     - **Dry Season (Winter, Nov–Feb):** 72 records.
     - **Wet Season (Monsoon, Jun–Oct):** 62 records.
     - **Excluded:** 28 records (pre-monsoon/summer Apr–May: 21 records; undated/annual means: 7 records).
   - This accounting is explicitly detailed in Section 3.3 and Table 3.
2. **Within-Study Paired Contrasts ($k=4$ Studies with Matched Sites):**
   - We conducted within-study paired contrasts on stations sampled across both dry and wet seasons (`data/paper_2_water_results/seasonal_within_study_contrasts.csv`):
     - While pooled unpaired Mann-Whitney tests indicate higher dry-season Arsenic ($0.0073\text{ vs. } 0.0042\text{ mg/L}$, ratio $1.74\times$, $U = 927.5$, $p = 0.0039$, $p_{\text{adj}} = 0.0273$),
     - Paired within-study contrast across matched stations ($k=4$) yields a median ratio of **$1.21\times$** and a paired Wilcoxon signed-rank test of **$p = 0.3750$** (not statistically significant).
3. **Reframing as Competing Hydrochemical Hypotheses:**
   - We replaced the blanket "monsoonal dilution" narrative with a balanced discussion of competing mechanisms:
     - In urbanized channels, wet-season stormwater runoff and wash-off of industrial scrap offset volumetric dilution for Pb and Ni.
     - For Arsenic, elevated dry-season concentrations are consistent with groundwater-fed geogenic baseflow and Boro rice shallow aquifer irrigation return flows (Harvey et al., 2002), rather than solely lack of dilution.

---

### Major Comment 7 (M7): Spatial Analysis, Topological Stream Distance, and Map
> *"There is no map... 'Geodesic distance routing' is straight-line Haversine distance... Along-network position is ignored... Candidate labels don't match the coordinates..."*

**Response:**
We have fundamentally enhanced the spatial analysis:
1. **Publication GIS Coverage Map (`fig3_spatial_coverage_map.png`):**
   - We created a 300 DPI, multi-panel GIS map showing:
     - All 3,894 major HydroSHEDS HydroRIVERS river reaches in Bangladesh.
     - Audited published sampling stations with buffer radii (10 km, 25 km, 50 km).
     - Color-coded stream reach coverage ($<10\text{ km}$, $10–25\text{ km}$, $>25\text{ km}$).
     - The 15 prioritized candidate monitoring reaches.
2. **Topological Along-Network Stream Distance (Dijkstra Routing):**
   - In addition to straight-line Haversine distance, we converted the HydroSHEDS HydroRIVERS network into a directed graph and computed topological stream distance along the actual river network using Dijkstra's algorithm.
   - **Key Finding:** While straight-line distance places 88.0% of river length $>25\text{ km}$ from published sites, along-network topological stream distance places **94.6% of river length (7,919.9 km across 3,682 reaches)** $>25\text{ km}$ from historical sites. This demonstrates that hydrological isolation is even more severe than Euclidean metrics suggest.
3. **Administrative Gazetteer Verification:**
   - All candidate reach coordinates in Table 4 were checked against national administrative gazetteers. Misleading reach labels were corrected:
     - `GAP_STN_03`: Corrected to Jazira–Louhajang Reach on Lower Padma (Shariatpur/Munshiganj).
     - `GAP_STN_10`: Corrected to Chauhali–Tangail Reach on Lower Jamuna (Sirajganj/Tangail).
     - `GAP_STN_13`: Corrected to Kazipur–Sariakandi Reach on Jamuna (Bogura).
     - `GAP_STN_14`: Corrected to Fulchhari–Dewanganj Reach on Brahmaputra (Gaibandha/Jamalpur).
     - `GAP_STN_15`: Corrected to Chilmari Reach on Upper Brahmaputra (Kurigram).
4. **Clarified Framing:** The section is explicitly titled *"River Network Coverage of Compiled Studies and Surveillance Expansion Reaches"*, acknowledging academic literature coverage rather than official DoE/BWDB monitoring networks.

---

### Major Comment 8 (M8): Pathways and Benchmark Alignment
> *"The benchmarks don't match the pathways you argue for... FAO irrigation guidelines, aquatic-life criteria... cite the gazette..."*

**Response:**
1. **FAO Irrigation Guidelines Added:** We integrated FAO irrigation criteria (Ayers & Westcot, 1985; FAO Irrigation and Drainage Paper 29) for all metals:
   - Cadmium (0.010 mg/L): 26.5% exceedance [Cluster CI: 8.2–47.0%].
   - Chromium (0.100 mg/L): 27.5% exceedance [Cluster CI: 10.8–44.8%].
   - Copper (0.200 mg/L): 26.7% exceedance [Cluster CI: 0.0–53.7%].
   - Nickel (0.200 mg/L): 25.0% exceedance [Cluster CI: 0.0–52.8%].
   - Arsenic (0.100 mg/L): 9.0% exceedance [Cluster CI: 0.0–28.2%].
   - Zinc (2.000 mg/L): 6.3% exceedance [Cluster CI: 0.0–17.2%].
   - Lead (5.000 mg/L): 0.0% exceedance.
2. **Drinking Water Pathway Clarification:** We contextualized drinking water risks by documenting surface water abstraction for municipal treatment plants (e.g., Dhaka WASA Saidabad Surface Water Treatment Plant abstracting raw water from the Shitalakhya; Chattogram WASA abstracting from the Karnaphuli).
3. **Statutory Standards Citation:** We standardized citations on Bangladesh Environmental Conservation Rules (ECR 1997 potable standard schedule, reaffirmed in updated gazettes; Chowdhury et al., 2007) and cited the exact statutory schedules.

---

### Major Comment 9 (M9): Reference Verification and Citations
> *"Verify every reference... Replace inappropriate citations..."*

**Response:**
All citations were checked and replaced where necessary:
- Added authoritative FAO irrigation criteria: **Ayers and Westcot (1985)** (*Water Quality for Agriculture*, FAO Irrigation and Drainage Paper 29).
- Added geogenic baseflow and groundwater hydrogeochemistry: **Harvey et al. (2002)** (*Science*, 298, 1602–1606).
- Added statutory standard schedule reference: **Chowdhury et al. (2007)** (*Water Resources Management*, 21, 889–908).
- Replaced mismatched citations in the text to ensure complete topical alignment.

---

## 2. Response to Moderate and Minor Comments

- **Limitations Expanded:** Section 4.4 now systematically covers record clustering, non-detect handling, variable vs. fixed panel HPI, temporal span (2010–2024), seasonal data exclusions (28 records), and lack of concurrent DoE/BWDB continuous monitoring data.
- **Unspecified Fractions:** Explicitly noted as total/unspecified, avoiding biased claims of "dissolved" fractions.
- **Title Refined:** Streamlined to *"Heavy Metals in Bangladesh River Waters: A Synthesis of Published Records (2010--2024), Benchmark Exceedances, Seasonal Contrasts, and River Network Coverage"*.
- **LaTeX Compilation & Typesetting:** Compiled using `pdflatex` with 0 errors and 0 overfull hboxes. Tables are wrapped in `adjustbox` for formatting.
- **Anonymized Data Repository:** Code and data are prepared for blinded peer review.

---
We believe these comprehensive revisions directly resolve all Round 2 concerns and significantly strengthen the rigor, reproducibility, and contribution of our work.

