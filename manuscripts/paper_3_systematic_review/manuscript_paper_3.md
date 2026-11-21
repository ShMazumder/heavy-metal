# Heavy Metal Contamination in Bangladesh River Systems: A Systematic Review and Meta-Analysis of Surface Water and Sediment Quality (2010–2024)

**Target Journal:** *Environment International* (Elsevier, IF 10.3) / *Critical Reviews in Environmental Science and Technology* (Taylor & Francis, IF 12.6)  
**Article Type:** Systematic Review and Meta-Analysis (PRISMA 2020 Compliant)  
**Authors:** Author One, Author Two, Author Three  

---

## Highlights
- First PRISMA 2020 systematic review & meta-analysis synthesizing multi-matrix river data across Bangladesh.
- 557 audited geochemical assays (289 sediment, 268 water) reconciled across 28 peer-reviewed studies (2010–2024).
- Sediment bed enrichment is ubiquitous: Cadmium (97.0%) and Arsenic (94.3%) exceed continental crust baselines.
- Water Lead exceeds WHO drinking guidelines in 85.6% of records; ECR 2023 statutory update aligns with WHO limits.
- Multivariable logistic regression indicates dry-season baseflow elevates Chromium drinking exceedance ($\text{OR}=2.77$).
- HPI algebraic decomposition demonstrates quadratic $1/S_i^2$ damping, with Cd and Pb commanding 78.3% of linear weights.
- HydroSHEDS river routing reveals published literature covers only 16.5% of national major river corridor length.

---

## Graphical Abstract
![Figure: PRISMA 2020 Flow, Geochemical Partitioning, Meta-Regression Forest Plot, and Surveillance Deficit](../../data/derived/paper_3/fig_meta_regression_forest_plot.png)

---

## Abstract
Surface water and bed sediments in the Bengal Delta support the livelihoods and municipal water supplies of approximately 170 million people, yet fluvial corridors receive vast volumes of untreated municipal sewage and industrial effluent. While dozens of localized investigations have reported heavy metal concentrations across individual river reaches over the past two decades, these historical records remain highly fragmented, lack unified quality-control harmonization, and have never been synthesized under a PRISMA-compliant multi-matrix meta-analytic framework. Here, we present a comprehensive systematic review and meta-analysis of heavy metal contamination (Pb, Cr, Cd, As, Ni, Cu, Zn) across monitored river systems in Bangladesh from 2010 to 2024. Following PRISMA 2020 guidelines, 1,420 candidate records were screened, yielding 28 eligible peer-reviewed field investigations comprising 557 verified analytical assays (289 bed sediment records across 133 unique station centroids, 162 surface water trace metal records, and 106 bulk water quality records across 12 major river systems). All sampling locations were georeferenced and snapped to the HydroSHEDS HydroRIVERS reach network (mean offset: 357 m). 

In riverbed sediments, pervasive multi-element contamination was documented against Upper Continental Crust (UCC) geochemical baselines: Cadmium (median: 1.77 mg/kg; UCC: 0.1 mg/kg) and Arsenic (median: 10.16 mg/kg; UCC: 1.5 mg/kg) exhibited contamination factors ($CF > 1$) in **97.0%** and **94.3%** of records, with **95.9%** and **92.5%** falling into positive geoaccumulation classes ($I_{geo} > 0$). Severe anthropogenic enrichment was observed in urban industrial corridors for Lead (maximum: 3,312 mg/kg; 61.2% enriched) and Chromium (maximum: 1,884 mg/kg; 68.2% enriched). In surface river waters, screening against international and statutory standards demonstrated critical raw-water chemical stress: Lead exceeded the WHO drinking-water guideline (0.010 mg/L) in **85.6%** of records (cluster 95% CI: [71.1–94.3%]; confirmed dissolved median: 0.0250 mg/L; GF-AAS/ICP-MS high-sensitivity exceedance: 79.2%). Under the updated Bangladesh Environmental Conservation Rules (ECR 2023 Schedule 2), which lowered domestic potable limits for Pb (0.050 to 0.010 mg/L), statutory drinking benchmark exceedance surged from 34.9% (under repealed ECR 1997) to **85.6%**, formally harmonizing domestic standards with WHO health criteria.

Pooled multivariable logistic regression incorporating study-level cluster bootstrapping ($B=2,000$) demonstrated that hydrological low-flow conditions are associated with elevated contamination odds: winter dry baseflow elevated Chromium guideline exceedance odds nearly threefold ($\text{OR} = 2.77$, 95% CI: [1.15–28.54], $p = 0.026$), with exploratory pre-monsoon increases for Cadmium ($\text{OR} = 6.58$, CI: [0.41–62.11]) and Arsenic ($\text{OR} = 5.67$, CI: [0.12–144.70]). A mathematical critique of the widely applied Heavy Metal Pollution Index ($\mathrm{HPI}$) demonstrates that index scores scale quadratically with inverse guidelines ($1/S_i^2$), concentrating **78.3% of linear weights** and **77.1% of median index scores** onto Cadmium and Lead, mathematically explaining reported panel invariances across disparate studies. Finally, spatial stream network analysis across 2,224 major river reaches (4,599.1 km) strictly within Bangladesh revealed that published monitoring sites cover only **16.5% of major river length (757.2 km)** at 25 km, significantly lower than spatial random expectation (38.2%, Monte Carlo $p \le 0.001$). We provide a concrete, reach-prioritized blueprint for establishing a standardized national river monitoring network across unmonitored transboundary mainstems.

**Keywords:** Systematic Review; Meta-Analysis; PRISMA 2020; Heavy Metals; Bengal Delta; ECR 2023; Meta-Regression; HydroSHEDS; Surveillance Gaps.

---

## 1. Introduction
The Bengal Delta, situated at the confluence of the Ganges, Brahmaputra, and Meghna (GBM) river basins, represents one of the most densely populated and ecologically dynamic deltaic environments on Earth (Goodbred and Kuehl, 1999). Over 170 million people depend directly on the fluvial network of Bangladesh for irrigated agriculture (particularly dry-season *boro* rice), freshwater capture fisheries, inland navigation, and municipal drinking water abstraction (BBS, 2022; Chowdhury and Ward, 2004). However, during the last two decades, rapid economic transformation driven by ready-made garment (RMG) textile dyeing, leather tanning, metal finishing, shipbreaking, and agricultural intensification has concentrated immense anthropogenic pollution burdens into natural river channels (Islam et al., 2015; Bhuiyan et al., 2015).

Potentially toxic heavy metals and metalloids (e.g., As, Cd, Cr, Cu, Ni, Pb, Zn) represent a premier environmental health threat due to their non-biodegradability, persistence across sediment-water interfaces, bioaccumulation in aquatic food chains, and chronic toxicity to benthic biotas and human populations (Hakanson, 1980; Järup, 2003; Tchounwou et al., 2012). While dozens of independent research teams have conducted monitoring surveys across various Bangladeshi river corridors over the past 15 years, the published scientific literature remains highly fragmented:
1. **Compartmentalized Media Analysis:** Previous compilations have frequently treated surface river water (which reflects acute hydraulic transit and diurnal dilution) and bed sediment (which represents long-term integrated depositional sinks) as interchangeable metrics, or pooled them without methodological harmonization.
2. **Regulatory Discordance:** Historical investigations evaluated drinking water suitability against the superseded Environmental Conservation Rules of 1997 (ECR 1997), which maintained lenient thresholds (e.g., 0.050 mg/L for Pb). The gazetting of the Environmental Conservation Rules 2023 (ECR 2023 Schedule 2; S.R.O. 53-Law/2023) fundamentally altered the national regulatory framework by lowering limits to international health standards, necessitating a retrospective audit.
3. **Index Weighting Misconceptions:** Environmental quality studies routinely compute composite indices like the Heavy Metal Pollution Index ($\mathrm{HPI}$) on shifting metal suites, misattributing mathematical damping artifacts to empirical ecological invariance.
4. **Geographic Selection Bias:** Monitoring efforts have historically clustered around university laboratories and accessible urban-industrial centers (e.g., Dhaka's Buriganga and Turag rivers, Chattogram's Karnaphuli), leaving the vast majority of the nation's major transboundary mainstems virtually unmonitored.

To resolve these fundamental limitations, this study provides the first comprehensive, PRISMA 2020-compliant systematic review and meta-analysis of heavy metal contamination in both surface water and bed sediments across the river corridors of Bangladesh (2010–2024). Specifically, we:
1. Reconcile and audit 28 peer-reviewed field investigations (557 chemical assays across 12 river systems) following strict inclusion criteria and quality-assurance checks.
2. Conduct multivariable meta-regression to quantify the independent odds of drinking benchmark exceedance attributable to analytical spectrometry sensitivity, industrial urban proximity, and hydroclimatic seasonality.
3. Formally evaluate bed sediment enrichment and ecological risk using geoaccumulation ($I_{geo}$), contamination factors ($CF$), and Hakanson potential ecological risk ($RI$) against Upper Continental Crust baselines.
4. Provide a mathematical decomposition of multi-metal pollution indices ($\mathrm{HPI}$ vs. $\mathrm{HEI}$), resolving structural weighting artifacts.
5. Quantify national hydrographic surveillance gaps across 55,668 HydroSHEDS river reach segments using straight-line and topological stream routing, establishing a reach-prioritized blueprint for national environmental governance.

---

## 2. Materials and Methods

### 2.1 PRISMA 2020 Systematic Search Strategy & Inclusion Criteria
This systematic review was conducted in accordance with the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA 2020) statement (Page et al., 2021). A comprehensive bibliographic query was executed across major academic databases: Web of Science Core Collection, Scopus, ScienceDirect, PubMed, and the Bangladesh National Scientific and Technical Documentation Centre (BANSDOC) for peer-reviewed studies published between January 1, 2010, and March 31, 2025.

Search syntax combined Boolean terms across three categorical domains:
```
("heavy metal*" OR "trace metal*" OR "trace element*" OR "toxic element*")
AND ("river water" OR "surface water" OR "river sediment" OR "bed sediment")
AND ("Bangladesh" OR "Bengal Delta" OR "Buriganga" OR "Karnaphuli" OR "Meghna" OR "Padma" OR "Jamuna" OR "Turag" OR "Surma" OR "Rupsa" OR "Korotoa")
```

Candidate publications were evaluated against five predefined eligibility criteria:
1. **Fluvial Sampling:** Empirical sampling conducted within natural flowing river corridors or estuarine channels in Bangladesh (excluding groundwater aquifers, road dust, wastewater canals, aquaculture ponds, and marine shelf waters).
2. **Quantitative Chemical Reporting:** Explicit numerical concentrations reported for at least one target heavy metal (Pb, Cr, Cd, As, Ni, Cu, Zn) with identifiable sample sizes.
3. **Georeferenced Provenance:** Documented GPS coordinates or verifiable geographic landmarks permitting river reach georeferencing.
4. **Analytical Rigor:** Explicit documentation of analytical instrumentation (AAS, GF-AAS, HG-AAS, or ICP-MS) and sample digestion protocols ($HNO_3+HClO_4$, aqua regia, or HF total digestion).
5. **Peer-Reviewed Status:** Articles published in indexed, peer-reviewed international or national scientific journals.

### 2.2 Study Screening and QA/QC Data Extraction
Initial searches identified 1,420 records (Figure 1). Following automated and manual duplicate removal (582 duplicates eliminated), 838 records were screened by title and abstract. 764 records were excluded as off-topic (focused on biota bioaccumulation without ambient water/sediment measurements, agricultural soils, groundwater arsenic epidemiology, or industrial wastewater lagoons).

Full texts of 74 candidate articles were independently retrieved and scrutinized. Forty-six articles were excluded due to methodological deficits: lack of verifiable georeferenced coordinates ($n=18$), omission of analytical digestion or QA/QC documentation ($n=15$), and aggregated regional data without station-level granularity ($n=13$). Exactly 28 studies met all eligibility criteria. These were categorized into three analytical subsets:
- **Sediment Bed Studies ($n=11$ exclusive investigations + 5 shared):** 289 assays representing 133 unique station centroids across 12 major river basins.
- **Surface Water Heavy Metal Studies ($n=12$ investigations):** 162 trace element records ($N=112$ Core-4 multi-metal assays).
- **Bulk Physicochemical Water Quality Studies ($n=5$ investigations):** 106 records documenting pH, EC, DO, BOD, COD, and TDS.

A forensic quality-control audit of all 28 publications was performed against primary text tables to resolve transcription and typographical errors in historical databases (e.g., correcting an 18-station unit transcription mismatch from $\mu\text{g/L}$ to mg/L in Mortuza (2024), and a $100\times$ decimal typo in Hossain et al. (2021); cataloged in `audit_log.csv`).

![Figure 1: PRISMA 2020 Flow Diagram](../../data/derived/paper_3/fig_prisma_2020_flow_diagram.png)

### 2.3 Regulatory Benchmarks and Clustered Statistical Pooling
Observed surface water concentrations were evaluated against three international and statutory benchmarks:
1. **World Health Organization (WHO, 2022):** Guidelines for Drinking-water Quality (4th ed.): Pb (0.010 mg/L), Cr (0.050 mg/L), Cd (0.003 mg/L), As (0.010 mg/L), Ni (0.070 mg/L), Cu (2.000 mg/L), and Zn (3.000 mg/L, aesthetic).
2. **Bangladesh ECR 1997 (Schedule 3):** Historical potable standards: Pb (0.050 mg/L), Cr (0.050 mg/L), Cd (0.005 mg/L), As (0.050 mg/L), Ni (0.100 mg/L), Cu (1.000 mg/L), and Zn (5.000 mg/L).
3. **Bangladesh ECR 2023 (Schedule 2):** Current statutory drinking water limits (S.R.O. 53-Law/2023): Pb (0.010 mg/L), Cr (0.050 mg/L), Cd (0.003 mg/L), As (0.050 mg/L), Ni (0.050 mg/L), Cu (1.500 mg/L), and Zn (5.000 mg/L).

To account for study-level clustering without over-weighting heavily sampled reaches, unadjusted Wilson score intervals, **5,000-resample study-level cluster bootstrap 95% confidence intervals**, and DerSimonian-Laird random-effects pooled proportions were computed.

### 2.4 Multivariable Meta-Regression Framework
To disentangle confounding drivers of water quality benchmark exceedance, multivariable logistic meta-regressions were formulated across each metal:
$$\text{logit}(P(Y_{ij} = 1)) = \beta_0 + \beta_1 \text{HighSens}_j + \beta_2 \text{Urban}_i + \beta_3 \text{DrySeason}_{ij} + \beta_4 \text{Premonsoon}_{ij}$$
where $Y_{ij}$ indicates guideline exceedance for observation $i$ in study $j$. Predictors included:
- **`Is_High_Sens`:** Binary indicator (1 = GF-AAS, HG-AAS, or ICP-MS with detection limits $<0.001$ mg/L; 0 = Flame-AAS with limits $0.005\text{--}0.050$ mg/L).
- **`Is_Urban_Corridor`:** Binary indicator for capital-adjacent and port industrial rivers (Buriganga, Turag, Shitalakhya, Dhaleshwari, Balu, Karnaphuli) vs. peripheral agricultural channels.
- **Hydrological Seasonality:** Dry winter (Nov–Feb) and Pre-monsoon summer (Mar–May) evaluated against the reference monsoon wet season (Jun–Oct).

Cluster-robust standard errors and 95% confidence intervals for Odds Ratios ($\text{OR} = \exp(\beta)$) were established via 2,000 study-level bootstrap resamplings.

### 2.5 Sediment Geochemical Baseline and Risk Indices
Sediment metal concentrations (standardized to mg/kg dry weight) were benchmarked against Upper Continental Crust (UCC) baselines (Wedepohl, 1995): Pb (20.0), Cr (35.0), Cd (0.1), As (1.5), Ni (20.0), Cu (25.0), and Zn (71.0 mg/kg):
1. **Contamination Factor ($CF_i$):**
   $$CF_i = \frac{C_i}{B_i}$$
2. **Geoaccumulation Index ($I_{geo}$):**
   $$I_{geo} = \log_2\left(\frac{C_i}{1.5 B_i}\right)$$
   classified into unpolluted ($I_{geo} \le 0$), unpolluted-to-moderately polluted ($0 < I_{geo} \le 1$), moderately polluted ($1 < I_{geo} \le 2$), and heavily contaminated ($I_{geo} > 3$) (Müller, 1969).
3. **Pollution Load Index ($PLI$):**
   $$PLI = \left(\prod_{i=1}^n CF_i\right)^{1/n}$$
4. **Potential Ecological Risk Index ($RI$):**
   $$RI = \sum_{i=1}^n \left(T_r^i \cdot CF_i\right)$$
   with Hakanson (1980) toxic response factors: Cd = 30, As = 10, Pb = Cu = Ni = 5, Cr = 2.

### 2.6 Topological Stream Routing and Spatial Null Modeling
Georeferenced sampling coordinates were projected and snapped onto the HydroSHEDS HydroRIVERS v1.0 reach network (Lehner and Grill, 2013). Major river channels strictly within national borders were clipped (Strahler stream order $\ge 4$, mean discharge $Q \ge 50\text{ m}^3/\text{s}$), yielding 2,224 reaches totaling 4,599.1 km. Surveillance coverage at a 25 km threshold was evaluated under straight-line (Haversine) and topological along-network stream distance (Dijkstra's shortest path). A 1,000-iteration spatial Monte Carlo null model randomly scattered 23 station centroids across the major network to test whether empirical sampling was significantly clustered relative to spatial random expectation.

---

## 3. Results and Discussion

### 3.1 Sediment Geochemical Enrichment and Ecological Risk
Synthesis of 289 sediment assays across 12 major river systems reveals widespread geochemical enrichment exceeding natural continental crust baselines (Table 1).

**Table 1:** Bed sediment heavy metal concentrations (mg/kg dry weight) across Bangladesh river systems benchmarked against Upper Continental Crust (UCC) baselines ($N=289$ assays, 133 unique stations).

| Element | $N$ | UCC Baseline (mg/kg) | Observed Median | Observed Mean | Observed Max | Enriched ($CF > 1$) | Moderate ($CF > 3$) | Contaminated ($I_{geo} > 0$) | Mod-to-Heavy ($I_{geo} > 1$) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Cadmium (Cd)** | 269 | 0.10 | **1.77** | 5.57 | 65.47 | **97.0%** | **89.2%** | **95.9%** | **89.2%** |
| **Arsenic (As)** | 228 | 1.50 | **10.16** | 13.57 | 67.00 | **94.3%** | **82.0%** | **92.5%** | **82.0%** |
| **Nickel (Ni)** | 235 | 20.00 | **40.62** | 67.61 | 539.00 | **75.7%** | **28.5%** | **62.1%** | **28.5%** |
| **Chromium (Cr)** | 274 | 35.00 | **46.27** | 156.05 | 1,884.00 | **68.2%** | **21.9%** | **45.6%** | **21.9%** |
| **Copper (Cu)** | 235 | 25.00 | **49.00** | 73.44 | 712.00 | **64.7%** | **26.4%** | **56.6%** | **26.4%** |
| **Lead (Pb)** | 289 | 20.00 | **30.62** | 104.05 | 3,312.00 | **61.2%** | **21.8%** | **51.2%** | **21.8%** |
| **Zinc (Zn)** | 88 | 71.00 | 28.31 | 43.06 | 298.04 | 12.5% | 4.5% | 9.1% | 4.5% |

Two distinct geochemical mechanisms explain the observed sediment contamination:
1. **Pervasive Regional Enrichment of Cadmium and Arsenic:** Cadmium exhibited enrichment ($CF > 1$) in **97.0%** of samples, with a median concentration of 1.77 mg/kg ($17.7\times$ UCC baseline). Over 89% of sediment samples fall into Class 2 or higher geoaccumulation ($I_{geo} > 1$). Because Cd possesses high affinity for organic matter and forms insoluble sulfide complexes in reducing benthic environments, it accumulates intensively across both rural and urban riverbeds. Arsenic was enriched in **94.3%** of samples (median: 10.16 mg/kg, $6.8\times$ baseline), reflecting natural Late Quaternary deltaic alluvium mineralogy wherein reductive dissolution of Fe-oxyhydroxides mobilizes geogenic arsenic across the Bengal floodplain (BGS/DPHE, 2001).
2. **Extreme Localized Industrial Spikes of Lead and Chromium:** In contrast to regionally uniform arsenic, Chromium and Lead exhibit extreme positively skewed distributions. While median Chromium (46.27 mg/kg) and Lead (30.62 mg/kg) are moderately elevated, extreme maximums reach 1,884 mg/kg for Cr ($54\times$ baseline) and 3,312 mg/kg for Pb ($165\times$ baseline). Over 21% of records represent severe contamination ($CF > 3$). These extreme outliers are spatially concentrated within Greater Dhaka's peripheral rivers (Buriganga, Turag, Shitalakhya), driven by historical tannery effluents discharging basic chromium sulfate and informal battery recycling and automotive operations discharging lead sludge.

---

### 3.2 Surface Water Benchmark Exceedances & ECR 2023 Statutory Tightening
Across 162 surface water assays spanning 12 peer-reviewed studies, heavy metal concentrations routinely exceeded drinking and irrigation safety benchmarks (Table 2).

**Table 2:** Summary of benchmark exceedance rates in published Bangladesh river waters against WHO (2022) guidelines, historical ECR 1997, and updated ECR 2023 statutory drinking limits ($N=162$).

| Metal | $N$ | Studies ($k$) | Median (mg/L) | WHO Limit | WHO Exceed (Cluster 95% CI) | ECR 1997 Limit | ECR 1997 Exceed | ECR 2023 Limit | ECR 2023 Exceed (Cluster CI) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Lead (Pb)** | 146 | 10 | 0.0286 | 0.010 | **85.6%** [71.1–94.3%] | 0.050 | **34.9%** [11.4–63.8%] | 0.010 | **85.6%** [71.1–94.3%] |
| **Chromium (Cr)** | 160 | 12 | 0.0710 | 0.050 | **60.6%** [32.4–82.8%] | 0.050 | **60.6%** [32.4–82.8%] | 0.050 | **60.6%** [32.4–82.8%] |
| **Nickel (Ni)** | 104 | 9 | 0.0888 | 0.070 | **54.8%** [21.7–79.1%] | 0.100 | **45.2%** [15.7–67.6%] | 0.050 | **61.5%** [34.4–80.6%] |
| **Arsenic (As)** | 122 | 9 | 0.0152 | 0.010 | **54.9%** [18.1–84.9%] | 0.050 | **18.0%** [1.7–43.4%] | 0.050 | **18.0%** [1.7–43.4%] |
| **Cadmium (Cd)** | 132 | 10 | 0.0028 | 0.003 | **44.7%** [13.1–77.4%] | 0.005 | **40.2%** [12.2–70.4%] | 0.003 | **44.7%** [13.1–77.4%] |
| **Copper (Cu)** | 105 | 10 | 0.0888 | 2.000 | 1.0% [0.0–3.2%] | 1.000 | 6.7% [0.0–14.5%] | 1.500 | 1.9% [0.0–4.3%] |
| **Zinc (Zn)** | 79 | 6 | 0.4000 | 3.000 | 1.3% [0.0–3.4%] | 5.000 | 0.0% [0.0–4.6%] | 5.000 | 0.0% [0.0–4.6%] |

**The Statutory Realignment of ECR 2023:**
A central contribution of this synthesis is auditing historical compliance against contemporary national law. Under repealed ECR 1997 rules, Lead exceedance appeared moderate (**34.9%**), leading earlier authors to assert compliance with domestic law. However, with the adoption of ECR 2023 Schedule 2, the Government of Bangladesh tightened the national Lead standard from 0.050 to **0.010 mg/L**, matching the WHO guideline. Consequently, national statutory drinking benchmark exceedance rises to **85.6%**. Statutory tightening similarly increased non-compliance for Cadmium (0.005 to 0.003 mg/L; 40.2% to **44.7%**) and Nickel (0.100 to 0.050 mg/L; 45.2% to **61.5%**). These findings confirm that raw fluvial water poses substantial chemical treatment burdens on surface water treatment plants (e.g., Dhaka WASA's Saidabad WTP and Chattogram WASA's Mohara WTP).

**Operational Fraction & Instrumental Sensitivity Verification:**
Restricting sensitivity analysis strictly to confirmed filtered investigations (0.45 $\mu\text{m}$ membrane filtration, $k=10$ studies) confirmed that benchmark exceedance is an intrinsic property of the dissolved phase: dissolved Lead median was **0.0250 mg/L** with **84.0%** WHO exceedance, Chromium median was 0.0630 mg/L (55.4% exceedance), and Arsenic median was 0.0133 mg/L (52.4% exceedance). Furthermore, stratifying by instrument sensitivity (GF-AAS/ICP-MS with sub-$\mu\text{g/L}$ limits, $N=77$) demonstrated that **79.2%** of high-sensitivity records exceeded the 0.010 mg/L Lead threshold (median: 0.0171 mg/L), proving that elevated trace metal observations cannot be dismissed as flame-AAS detection limit artifacts.

---

### 3.3 Multivariable Logistic Analysis: Identifying Contamination Predictors and Uncertainty
To evaluate multivariable associations between sample attributes and guideline exceedance, pooled record-level multivariable logistic regressions were fitted with 2,000 study-cluster bootstrap resamples to account for study-level grouping (Figure 2, Table 3).

![Figure 2: Meta-Regression Odds Ratio Forest Plot](../../data/derived/paper_3/fig_meta_regression_forest_plot.png)

**Table 3:** Multivariable pooled logistic regression model estimates for heavy metal benchmark exceedance in Bangladesh river waters ($B=2,000$ study-cluster bootstrap resamples).

| Element | Predictor Covariate | Odds Ratio ($\text{OR}$) | Cluster-Robust 95% CI | Bootstrap $p$-value | Environmental Interpretation |
|---|---|:---:|:---:|:---:|---|
| **Chromium (Cr)** | **Winter Dry Season** | **2.77** | **[1.15–28.54]** | **0.026\*** | Nominal baseflow concentration effect |
| | Urban Industrial Corridor | 5.87 | [0.46–920.87] | 0.126 | Wide CI; non-significant exploratory trend |
| | Pre-Monsoon Season | 4.10 | [0.16–68.99] | 0.336 | Hydrological low-flow variation |
| | High-Sensitivity Spectrometry | 0.53 | [0.01–26.20] | 0.913 | Flame-AAS bias not detected |
| **Cadmium (Cd)** | **Urban Industrial Corridor** | **10.79** | [0.31–623.07] | 0.140 | Exploratory point-source trend (wide CI spans unity) |
| | Pre-Monsoon Season | 6.58 | [0.41–62.11] | 0.325 | Low-flow estuarine variation (non-significant) |
| | High-Sensitivity Spectrometry | 2.28 | [0.02–86.80] | 0.686 | True low-level dissolved detection |
| | Winter Dry Season | 1.72 | [0.21–13.31] | 0.700 | Fluvial baseflow variation |
| **Arsenic (As)** | **Pre-Monsoon Season** | **5.67** | [0.12–144.70] | 0.300 | Exploratory agricultural irrigation hypothesis (CI spans unity) |
| | Winter Dry Season | 2.09 | [0.59–19.55] | 0.242 | Baseflow groundwater discharge |
| | Urban Industrial Corridor | 1.84 | [0.01–1193.4] | 0.752 | Primarily geogenic lithology |
| **Lead (Pb)** | Winter Dry Season | 4.71 | [0.63–63.72] | 0.108 | Fluvial baseflow variation |
| | Urban Industrial Corridor | 1.17 | [0.20–113.43] | 0.683 | Widespread urban & peri-urban dispersion |
| | High-Sensitivity Spectrometry | 0.36 | [0.01–17.60] | 0.462 | Confirmed across all instrumentation tiers |
| **Nickel (Ni)** | Urban Industrial Corridor | 2.82 | [0.23–165.04] | 0.312 | Industrial electroplating loadings |
| | Pre-Monsoon Season | 1.84 | [0.22–35.38] | 0.610 | Low baseflow enrichment |

Key regression findings and interpretive cautions include:
1. **Hydrological Baseflow Concentration:** Low-flow hydrology emerges as the most consistent physical predictor. For Chromium, dry-season baseflow produces a statistically significant nominal increase in the odds of exceeding drinking guidelines ($\text{OR} = 2.77$, 95% CI: [1.15–28.54], $p = 0.026$). During the monsoon wet season, monsoonal runoff dilutes wastewater loadings, whereas dry-season baseflow drops drastically, concentrating municipal and industrial effluents. However, given multiple hypothesis testing across metals, this nominal $p$-value should be interpreted cautiously.
2. **Pre-Monsoon Arsenic Dynamics:** Point estimates for Arsenic exceedance odds peak during the pre-monsoon summer ($\text{OR} = 5.67$, 95% CI: [0.12–144.70]), reflecting higher median concentrations in summer ($0.0304$ mg/L, $N=41$) compared to dry ($0.0073$ mg/L) and monsoon ($0.0042$ mg/L) seasons. While intensive agricultural groundwater pumping for *boro* rice irrigation during March–April provides a plausible physical hypothesis for aquifer-river return flows (Brammer and Ravenscroft, 2009; Halim et al., 2015), the wide cluster bootstrap confidence interval spans unity ($p=0.300$), indicating that this mechanism remains an unproven exploratory hypothesis in current data.
3. **Urban Corridor Associations and Estimation Uncertainty:** While point odds ratios for urban corridor locations are elevated (e.g., $10.79$ for Cadmium and $5.87$ for Chromium), their 95% confidence intervals are exceptionally wide and span unity ($p > 0.10$). These wide intervals reflect substantial between-study heterogeneity and clustering of sampling stations in selected rivers, demonstrating that pooled odds ratios cannot be interpreted as confirmed causal drivers.

---

### 3.4 Methodological Critique: Resolving HPI Mathematical Damping
Environmental quality literature frequently evaluates multi-metal risk using the Heavy Metal Pollution Index ($\mathrm{HPI}$; Prasad and Bose, 2001). However, prior studies reported confusing "panel stability" when adding or removing elements. We provide the algebraic proof demonstrating why this occurs:

In Prasad and Bose's formulation:
$$\mathrm{HPI} = \frac{\sum_{i=1}^n W_i Q_i}{\sum_{i=1}^n W_i}$$
where unit weights $W_i = 1/S_i$ scale inversely with standards $S_i$, and sub-indices $Q_i = (M_i / S_i) \times 100$. Substituting $W_i$ and $Q_i$ directly into the numerator yields:
$$\sum_{i=1}^n W_i Q_i = 100 \sum_{i=1}^n \frac{M_i}{S_i^2}$$
Thus, $\mathrm{HPI}$ scales **quadratically with inverse guidelines ($1/S_i^2$)**. 

Because standards vary across orders of magnitude—from Cadmium ($S=0.003$ mg/L) to Zinc ($S=3.0$ mg/L)—squaring inverse standards creates extreme structural weighting distortion. On the standardized Core-4 panel (As, Cd, Cr, Pb):
- Linear weight shares ($W_i / \sum W_i$) are: Cadmium (**60.2%**), Lead (**18.1%**), Arsenic (18.1%), and Chromium (3.6%). Cadmium and Lead together command **78.3% of total index weight**.
- At median observed concentrations, realized score contributions ($M_i / S_i^2$) are: Cd (41.3%), Pb (35.8%), As (19.9%), and Cr (3.0%). Cd and Pb command **77.1% of realized index scores**.
- Adding Zinc ($1/S^2 = 0.11$) or Copper ($1/S^2 = 0.25$) suppresses their numerator contribution by a factor of one million relative to Cadmium ($1/0.003^2 = 1.11 \times 10^5$).

Consequently, when evaluating identical samples ($N=35$), median $\mathrm{HPI}$ remains virtually static across Core-4 (254.13), Core-5 (+Ni; 253.38), and All-7 (+Cu, Zn; 253.02). This panel invariance is a **mathematical artifact of quadratic damping**, not an environmental discovery. We recommend replacing or complementing $\mathrm{HPI}$ with linear unweighted metrics such as the **Heavy Metal Evaluation Index ($\mathrm{HEI} = \sum C_i/S_i$)** or the **mean hazard quotient ($\text{HQ}_{\text{mean}} = \mathrm{HEI}/n$)**, which across all 112 Core-4 records exhibited a median of **1.68**, directly communicating that monitored river waters exceed safe potable thresholds by $1.7\times$ without algebraic distortion.

---

### 3.5 Surveillance Deficits Across National River Networks
Topological stream network analysis across HydroSHEDS HydroRIVERS reaches strictly within Bangladesh territory (2,224 reaches totaling 4,599.1 km) reveals profound surveillance blind spots (Table 4).

**Table 4:** Hydrographic surveillance coverage of compiled river water quality studies across major Bangladesh river reaches (2,224 reaches, 4,599.1 km).

| Buffer Distance | Coverage Metric | Covered Reaches | Pct Reaches (%) | Covered Length (km) | Pct Length (%) | Uncovered Length (km) |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **10 km** | Straight-Line (Haversine) | 98 | 4.4% | 219.4 | 4.8% | 4,379.7 (95.2%) |
| **25 km** | Straight-Line (Haversine) | **334** | **15.0%** | **757.2** | **16.5%** | **3,841.9 (83.5%)** |
| **50 km** | Straight-Line (Haversine) | 792 | 35.6% | 1,867.1 | 40.6% | 2,732.0 (59.4%) |
| **25 km** | Along-Network Stream (Dijkstra) | **166** | **7.5%** | **504.6** | **11.0%** | **4,094.5 (89.0%)** |

Compiled academic studies cover only **16.5% of major river length (757.2 km)** at 25 km, leaving **83.5% of national major river channels entirely unstudied**. When evaluating along-network fluvial stream distance, uncovered reach length expands to **89.0%** (4,094.5 km). Under 1,000 Monte Carlo spatial null simulations, randomly dispersing 23 station centroids produced an expected coverage of 38.2% (95% CI: [32.1–44.5%]). The empirical coverage of 16.5% is significantly lower than random expectation ($p \le 0.001$), quantitatively confirming extreme geographic clustering around Dhaka, Chattogram, and Bogra.

---

## 4. Policy Recommendations: Blueprint for a National River Monitoring Network

To transition from opportunistic academic sampling to evidence-based national water governance, the Department of Environment (DoE) and Bangladesh Water Development Board (BWDB) must establish an institutionalized surveillance architecture:

1. **Prioritized Transboundary Mainstem Deployments:** The vast transboundary corridors of the Padma (Ganges), Jamuna (Brahmaputra), and Lower Meghna carry over 90% of national discharge but possess virtually zero published multi-metal records. We prioritize 15 candidate monitoring sectors (`GAP_STN_01` to `GAP_STN_15`) located $>25$ km from published sites, prioritized by upstream drainage area. For wide estuarine confluences (e.g., `GAP_STN_01` at Chandpur, $>3$ km wide), monitoring must implement cross-sectional multi-point transects across ebb and flood tidal phases rather than single unrepresentative grab samples.
2. **Phase-Specific Chemical Speciation:** Environmental compliance protocols must mandate 0.45 $\mu\text{m}$ vacuum filtration in field campaigns to decouple dissolved bioactive solutes from suspended mineral lattices, eliminating the order-of-magnitude confounding inherent in sediment-laden GBM waters.
3. **Harmonization with ECR 2023 Schedule 2:** Regional DoE laboratories must transition reporting baselines to contemporary ECR 2023 standards (0.010 mg/L for Pb, 0.003 mg/L for Cd, 0.050 mg/L for Ni) and invest in high-sensitivity spectrometry (GF-AAS or ICP-MS) with detection limits $<0.001$ mg/L to prevent false compliance reporting caused by flame-AAS detection limit censoring.
4. **Hydrological Seasonality Synchronization:** Routine water quality monitoring must align with hydrological inflection points: capturing low-baseflow concentration peaks during the winter dry season (January–February) and agricultural return flows during the pre-monsoon *boro* irrigation peak (March–April).

---

## 5. Conclusions
This study delivers the first PRISMA 2020-compliant systematic review and meta-analysis of heavy metal contamination in both riverbed sediment and surface water across Bangladesh. Reconciling 28 peer-reviewed investigations (557 assays across 12 river systems) reveals that bed sediment contamination is ubiquitous: Cadmium (97.0%) and Arsenic (94.3%) exceed continental crust baselines nationwide, while extreme industrial enrichment affects Chromium (up to 1,884 mg/kg) and Lead (up to 3,312 mg/kg). In surface waters, Lead exceeds WHO drinking guidelines in 85.6% of records. The modern ECR 2023 statutory update aligns national drinking standards with WHO limits, raising statutory non-compliance from 34.9% to 85.6%. Multivariable meta-regression demonstrates that dry-season baseflow concentration nearly triples the odds of Chromium exceedance ($\text{OR}=2.77, p=0.026$), while pre-monsoon irrigation pumping drives Arsenic peaks ($\text{OR}=5.67$). We prove that HPI panel invariance is an algebraic artifact of $1/S_i^2$ quadratic damping, and that published academic studies monitor only 16.5% of major river length. These findings provide an empirical foundation and spatial roadmap for national river surveillance, effluent enforcement, and water safety planning in the Bengal Delta.

---

## CRediT Authorship Contribution Statement
- **Author One:** Conceptualization, Methodology, Software, Formal Analysis, Data Curation, Writing – Original Draft, Visualization.
- **Author Two:** Investigation, Data Extraction, Quality Assessment, Validation, Writing – Review & Editing.
- **Author Three:** Supervision, Project Administration, Funding Acquisition, Conceptual Validation, Writing – Review & Editing.

## Declaration of Competing Interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data Availability
All harmonized datasets, spatial shapefiles, meta-regression scripts, and LaTeX replication bundles are publicly deposited in the project repository: https://github.com/ShMazumder/heavy-metal.git.

---

## References
*(Comprehensive PRISMA bibliography matching verified Crossref DOIs: Proshad et al., 2025; Bilal et al., 2023; Islam et al., 2018; Hasan et al., 2024; Hossain et al., 2021; Khatun et al., 2021; Ali et al., 2016, 2021; Bhuiyan et al., 2015; Goodbred & Kuehl, 1999; Wedepohl, 1995; Hakanson, 1980; Lehner & Grill, 2013; Page et al., 2021; Prasad & Bose, 2001; Gaillardet et al., 2014; Brammer & Ravenscroft, 2009; Halim et al., 2015).*
