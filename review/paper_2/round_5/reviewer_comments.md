# Review of Manuscript: *“Heavy Metals in Bangladesh River Waters: A Synthesis of Published Records (2010–2024), Benchmark Exceedances, Seasonal Contrasts, and River Network Coverage”*

**Recommendation:** **Reject** (or require a complete, foundational overhaul prior to any re-evaluation)

---

## 1. Executive Summary & Overarching Verdict

This manuscript presents a meta-analytical compilation and spatial audit of 162 heavy metal concentration records extracted from 12 peer-reviewed studies published between 2010 and 2024 across Bangladeshi river systems. The authors attempt to improve upon past syntheses by applying cluster-robust bootstrapping, random-effects pooling, index panel standardization, and HydroSHEDS-based topological spatial analysis.

While the QA/QC correction of historical literature typos (e.g., catching $100\times$ and $1,000\times$ unit transcription blunders in cited papers) is commendable, **the manuscript rests on fatal geochemical confounds, mathematical self-deceptions, obsolete regulatory benchmarking, and hydro-statistical inconsistencies.** The core narrative—that this paper provides a robust national benchmark of riverine contamination—is dismantled by the authors’ own data: the sample is hyper-concentrated in five heavily impacted rivers, $38\%$ of seasonal data were discarded to force a narrative, the multi-metal index stability is an arithmetic tautology, and the regulatory baseline used is legally defunct.

The manuscript cannot be published in its current form. Below are the critical flaws that invalidate the study's primary conclusions.

---

## 2. Fatal Methodological, Geochemical, & Regulatory Flaws

### 2.1. The Regulatory Absurdity: Benchmarking Against a Defunct Law (ECR 1997 vs. ECR 2023)
* Throughout the abstract, main text, and tables (Table 1, Figure 1, Lines 102–105), the authors benchmark national compliance against Schedule 3 of the **Bangladesh Environmental Conservation Rules (ECR) 1997**.
* The authors cite *“Ministry of Environment, Forest and Climate Change, 2023”* (Line 16, Line 486) in passing, yet **completely fail to evaluate their data against the officially gazetted ECR 2023 standards**. 
* ECR 1997 was formally superseded by ECR 2023. Publishing a 2024/2025 synthesis assessing national statutory exceedance using a repealed, 27-year-old framework is unacceptable. Did the standards for Cd, Pb, Cr, As, or Ni change, tighten, or introduce aquatic life criteria under ECR 2023? The authors do not tell us. Evaluating legal compliance against an obsolete legal instrument invalidates the policy relevance of Section 3.1.

### 2.2. The Phase Fractionation Confounder: Conflating Dissolved and Total Recoverable Metals
* In Lines 89–94 and 373–376, the authors concede that 10 studies filtered through $0.45\ \mu\text{m}$ filters (measuring the **dissolved** phase), while two studies did not state filtration protocols, which the authors conveniently **assumed to be dissolved**.
* This is geochemical malpractice:
  1. The Ganges–Brahmaputra–Meghna (GBM) system carries one of the highest suspended sediment fluxes on the planet. Suspended particulate matter (SPM) in these rivers routinely carries massive crustal and anthropogenic loads of Chromium, Lead, and Iron. If the two unstated studies digested unfiltered water, their inclusion injects whole-water total recoverable concentrations into a dissolved-phase dataset, distorting the distribution by orders of magnitude.
  2. Conversely, comparing *dissolved* river water concentrations against WHO Drinking-Water Guidelines (which are formulated for total concentrations at the point of ingestion) creates a false equivalence. 
  3. In Section 4.3 (Lines 334–344), the authors compare their compiled values to global *dissolved* baselines (Gaillardet et al., 2014) to argue that Bangladesh rivers are enriched by "one to two orders of magnitude." You cannot validate this claim while openly admitting that your historical dataset likely includes colloidal and particulate fractions from unfiltered digests.

### 2.3. The "Panel Stability" Fallacy: Trivial Arithmetic Masquerading as Scientific Discovery
* In the Abstract, Highlights (Bullet 3), and Section 3.2 (Lines 211–220), the authors claim a major methodological finding: standardizing the Heavy Metal Pollution Index (HPI) to a "Core-4" panel solves panel shift, triumphantly showing that on the common subset ($N=35$), median HPI is virtually identical across Core-4 ($254.13$), Core-5 ($253.38$), and All-7 ($253.02$).
* **This is not an empirical discovery; it is an elementary algebraic tautology.** 
  The Prasad and Bose HPI formulation weights each metal by $W_i \propto 1/S_i$. 
  * For Cadmium ($S_i = 0.003\text{ mg/L}$), $W_{\text{Cd}} = 333.33$.
  * For Lead ($S_i = 0.010\text{ mg/L}$), $W_{\text{Pb}} = 100.00$.
  * For Copper ($S_i = 2.000\text{ mg/L}$), $W_{\text{Cu}} = 0.50$.
  * For Zinc ($S_i = 3.000\text{ mg/L}$), $W_{\text{Zn}} = 0.33$.
* Cadmium and Lead account for **$78.3\%$** of the total weighting in Core-4. Adding Zinc ($W=0.33$) or Copper ($W=0.50$) alters the total weight sum and weighted sub-indices by less than $0.1\%$. The index is structurally insensitive to Cu, Zn, and Ni. 
* Presenting this intrinsic mathematical artifact of an unbalanced weighting scheme as empirical proof that *"expanding the metal panel produces negligible mathematical shift"* reflects a profound failure to understand the algebraic mechanics of the index being used.

### 2.4. Statistical Disconnect and Small-$k$ DerSimonian-Laird Abuse in Seasonal Analysis
* Look at **Table 3**:
  * **Lead (Pb):** The pooled median dry concentration is $0.0253\text{ mg/L}$ vs. wet concentration of $0.0287\text{ mg/L}$ (Ratio: **$0.88\times$**, indicating *higher* concentrations in the wet season; $p = 0.8538$). Yet, the within-study random-effects meta-analysis claims a pooled ratio of **$1.28\times$** ($95\%$ CI: $[1.05\text{--}1.56]$)!
  * **Nickel (Ni):** Pooled median ratio is **$0.73\times$** (wet higher), yet the within-study ratio is **$1.14\times$**!
* How do the authors reconcile this glaring direction reversal? By waving their hands at "competing hydrochemical hypotheses" (stormwater runoff vs. baseflow). 
* More critically, the within-study random-effects models are based on **$k_{\text{pair}} = 3\text{ to }5$ studies**. DerSimonian-Laird (DL) random-effects pooling is notoriously biased and unstable when $k < 10$. It severely underestimates the between-study variance ($\tau^2$), producing spuriously narrow confidence intervals and inflated Type I error rates. Generating a tight confidence interval of $[1.05\text{--}1.56]$ for Pb across only $4$ study pairs without applying the Hartung-Knapp-Sidik-Jonkman (HKSJ) adjustment or profile likelihood is statistically indefensible.

### 2.5. Data Truncation: Cherry-Picking the Hydrograph
* In Section 2.4 (Lines 147–148), the authors reveal that out of 162 trace element records, they discarded **$61$ records ($37.7\%$ of the dataset)** from their seasonal evaluation ($48$ pre-monsoon/summer records and $13$ unclassified records).
* In the Bengal Delta, the **pre-monsoon period (March to May)** is the absolute hydrological minimum for river discharge in many non-snowmelt-dominated basins, characterized by maximum ambient temperatures, peak irrigation abstraction, maximum evapotranspiration, and the lowest assimilative dilution capacity of the year.
* By arbitrarily defining "Dry" strictly as November–February (winter) and discarding the entire pre-monsoon summer, the authors have truncated the most extreme hydrological stress period. This invalidates their hydrochemical dilution narrative. Furthermore, this selective exclusion explains why the seasonal pooled medians in Table 3 (e.g., As dry: $0.0073$, wet: $0.0042\text{ mg/L}$) are both drastically lower than the overall pooled median reported in Table 1 ($0.0152\text{ mg/L}$). The discarded records clearly harbored the highest concentrations!

---

## 3. Hydrological & Spatial Absurdities

### 3.1. The Monte Carlo "Spatial Null Model" Straw Man
* In Section 2.5 and Section 3.4, the authors construct a 1,000-iteration Monte Carlo null model uniformly scattering 23 points across 2,224 HydroRIVERS reach segments to demonstrate that academic sampling is spatially clustered ($p < 0.0001$).
* **This is testing a trivial hypothesis.** Academic water quality surveillance in developing nations is purposive by design: researchers sample near industrial outfalls, municipal intakes, port hubs, and universities where laboratories exist. Testing against a null model of *uniform spatial randomness* across remote mangrove distributaries and uninhabited char lands is a scientific straw man. 
* Proving that sampling is clustered ($p < 0.0001$) tells the scientific community nothing new. It is an exercise in computational window dressing that dresses up an obvious sampling bias as an advanced GIS finding.

### 3.2. HydroRIVERS Failure in Coastal Deltaic Floodplains
* The authors clipped HydroSHEDS HydroRIVERS (Strahler order $\ge 4$, $Q \ge 50\text{ m}^3/\text{s}$) to Bangladesh. 
* HydroSHEDS/HydroRIVERS relies on DEM flow-direction algorithms (SRTM-based) that struggle in extremely flat, embanked, tidally reversed coastal floodplains. In southern Bangladesh, polders, artificial canals, estuarine cross-dams, and bidirectional semidiurnal tidal flows violate the dendritic routing assumptions of Dijkstra’s shortest path algorithm. 
* Calculating "along-network topological stream distances" using a static, unidirectional graph across the tidal reaches of the Meghna estuary and Sundarbans delta without explaining how tidal flow reversals and estuarine bifurcations were constrained makes the network distance metrics in Table 4 ($89.0\%$ along-network gap) highly suspect.

### 3.3. Table 5: Impractical Candidate Monitoring Reaches
* In Table 5, the authors propose 15 prioritized monitoring reaches based on catchment area and distance gaps.
* Rank 1 (`GAP_STN_01`) is located at the Chandpur–Haimchar confluence of the Lower Meghna (Catchment: $1,574,223\text{ km}^2$). This channel is several kilometers wide, with massive hydrodynamic discharge, extreme bank erosion, and incomplete cross-channel lateral mixing. Proposing a single point coordinate (`23.227°N, 90.631°E`) as a monitoring station in such a massive estuarine channel demonstrates a lack of basic field-sampling reality. Without cross-sectional, depth-integrated transect sampling protocols, single-point water quality monitoring here is meaningless.

---

## 4. Specific Detailed & Line-by-Line Deficiencies

1. **Lines 75–80 (QA/QC Audit):**
   * The authors report finding an 18-station error in P27 where $\mu\text{g/L}$ was transcribed as $\text{mg/L}$ ($1,000\times$ error) and a $100\times$ decimal error in P04. While good that these were caught, this exposes the extreme vulnerability and noise of the underlying compiled literature. If $12\%$ of the audited studies had catastrophic order-of-magnitude transcription errors, how can the authors trust the remaining unverified parameters (e.g., digestion recovery rates, calibration blanks, matrix interferences)?
2. **Line 83–86 (Analytical Detection Limits):**
   * The authors state: *"Analytical detection limits (DL) reported across primary papers ranged from 0.001 to 0.050 mg/L for flame-AAS... Only 3 of the 162 records contained non-detects."*
   * Look closely at the numbers: the WHO guideline for Cadmium is $0.003\text{ mg/L}$, and for Lead is $0.010\text{ mg/L}$. If primary flame-AAS studies had detection limits up to **$0.050\text{ mg/L}$**—which is $5\times$ higher than the WHO Lead guideline and $16\times$ higher than the Cadmium guideline—yet reported virtually *zero non-detects*, this indicates massive false-positive bias, baseline instrument noise, or baseline contamination in the historical literature. The authors cannot aggregate such compromised legacy data into modern risk estimates without a formal quantitative sensitivity analysis on analytical method limits.
3. **Table 2 vs. National Representation:**
   * The standardized Core-4 panel represents exactly **5 river systems across 7 studies ($N=112$)**. 
   * Out of these $112$ records, the Buriganga ($N=15$), Karnaphuli ($N=20$), and Korotoa ($N=40$) account for **$67\%$ of the data**. All three are infamous industrial dump sites.
   * Extrapolating a national median HPI of $156.99$ ($58.9\%$ exceeding critical limits) from a dataset where two-thirds of the rows come from three industrial hotspots is fundamentally unrepresentative of "Bangladesh River Waters." The title is misleading.
4. **Lines 226–231 (HEI vs. Mean Hazard Quotient):**
   * The authors report a median HEI of $6.70$ and state: *"Dividing by the four panel elements yields a median mean hazard quotient (HQmean = HEI/4) of 1.68..."*
   * An unweighted average of hazard quotients across distinct toxicological endpoints (nephrotoxicity of Cd vs. neurotoxicity of Pb vs. carcinogenicity of Cr) is toxicologically meaningless. Toxicological addition only applies to compounds sharing a common mechanism of action or target organ. Summing hazard quotients across four completely disparate elements and dividing by 4 should not be branded as an informative metric.
5. **Figure 1 & Figure 2:**
   * In Figure 1, the y-axis is labeled *"Benchmark Exceedance Rate (% of Assayed Records)"*, but the bars for Cr under WHO ($0.050\text{ mg/L}$) and BD ($0.050\text{ mg/L}$) are shown as identical adjacent bars with identical error bars. This visual redundancy clutter could be condensed into a single clear presentation.
   * Figure 2: The boxplots for dry vs. wet show severe outlier compression on linear scales (e.g., Cr jumping to $0.175\text{ mg/L}$, Cu to $1.3\text{ mg/L}$). A logarithmic concentration axis is mandatory for skewed trace-element environmental datasets.

---

## 5. Required Actions for Any Future Resubmission

To make this manuscript scientifically defensible, the authors must:
1. **Retract and Re-benchmark against ECR 2023:** Eliminate the obsolete ECR 1997 Schedule 3 analysis or present a side-by-side delta showing how the transition to ECR 2023 alters compliance rates.
2. **Segregate Phase Fractions:** Exclude the unverified filtration studies or run two distinct models: one strictly for validated dissolved fractions ($< 0.45\ \mu\text{m}$) and one for total recoverable digests. Stop pooling them.
3. **Correct Statistical Pooling:** Replace DerSimonian-Laird random-effects pooling on small-$k$ study pairs ($k=3\text{--}5$) with the Hartung-Knapp-Sidik-Jonkman (HKSJ) method or exact permutation tests to avoid spuriously tight confidence intervals.
4. **Re-integrate the Pre-Monsoon Season:** Stop discarding $38\%$ of the seasonal dataset. The pre-monsoon (March–May) must be analyzed as a distinct hydrological period (the true baseflow/evaporative minimum) rather than swept under the rug.
5. **Acknowledge HPI Mathematics Honestly:** Rewrite Section 3.2 to remove the absurd claim that index stability across metal additions is an empirical breakthrough; explicitly state that HPI is mathematically dominated by Cadmium due to its $1/S_i$ weighting.
6. **Reframe the Paper's Scope:** Change the title and conclusions to reflect what this dataset actually is: *“A Synthesis of Heavy Metal Records in Urban and Industrial River Reaches of Bangladesh...”* It is not, and never was, a representative assessment of the country's national river network.



This manuscript has strong bones—the cluster-bootstrapping, HKSJ meta-analytic adjustments, mathematical critique of the Heavy Metal Pollution Index (HPI), and HydroSHEDS topological gap analysis are genuinely rigorous. However, as a Desk Editor or Reviewer 2 at a top-tier journal (*Water Research*, *Environmental Science & Technology*, or *Science of the Total Environment*), I would recommend **Major Revisions (bordering on Reject & Resubmit)** due to severe literature starvation, a self-defeating regulatory comparison, and several glaring internal inconsistencies between the text, tables, and figures.

---

### 1. Major / Fatal Flaws

**A. Catastrophic Literature Under-Sampling (12 Studies in 15 Years?)**

* **The Issue:** You claim a "systematic literature compilation" across Web of Science, Scopus, and Google Scholar from 2010 to 2024, yet your entire quantitative trace metal synthesis rests on just **$k = 12$ studies ($N = 162$ records)** across a 15-year window. Even more alarming, your Reference list contains **only 6 primary field studies** on Bangladeshi river water (Ahmad 2010, Bhuiyan 2015, Islam 2015, Islam 2018, Hossain 2021, Mortuza 2024; plus Ali 2021 if counted). Where are the citations for the other 6 trace-metal studies, the 5 bulk physicochemical studies, and the 11 sediment studies from your "28-study master database"? Relegating primary data sources exclusively to Supplementary Table S0 without citing them in the main bibliography violates citation standards and denies original authors credit.


* **The Reality Check:** Dozens of peer-reviewed papers measuring heavy metals in the Buriganga, Turag, Shitalakhya, Karnaphuli, Meghna, Padma, Halda, Dhaleshwari, and Old Brahmaputra have been published between 2010 and 2024. Furthermore, there is no **PRISMA flow diagram**, no exact Boolean search string, no search date, and no record of how many ratusan/thousands of initial hits were screened and excluded. Without a PRISMA workflow, your claim that "83.5% of major river length is unmonitored by academia" is vulnerable to a fatal critique: *Is the river network actually unmonitored, or did your search just miss 70% of the literature?*



**B. The Regulatory Strawman: Drinking Standards vs. Inland Surface Water Standards**

* **The Issue:** A central thesis of your paper is the "regulatory benchmark discordance" caused by Bangladesh's ECR 2023 (Schedule 2) tightening Lead from 0.050 to 0.010 mg/L. However, **you are applying Drinking Water standards to untreated, raw industrial river water**.


* **The Reality Check:** While you add a brief caveat in Section 1 and Section 4.6 that raw river water is not tap water, framing raw river water exceedances of potable tap-water limits as *"statutory non-compliance"* and *"national regulatory violations"* (Abstract, Lines 28, 229, 346, 353) is legally and scientifically inaccurate. Both ECR 1997 and ECR 2023 explicitly distinguish between **Standards for Drinking Water** and **Standards for Inland Surface Water** (which in ECR 2023 are categorized by usage: source of drinking water after conventional treatment, recreational, pisciculture, irrigation, etc.). A river only violates statutory surface water law if it exceeds the *Inland Surface Water* criteria or if an effluent exceeds *Industrial Effluent* standards. You must clearly separate "exceedance of potable reference benchmarks (treatment burden)" from actual "statutory violation of inland surface water law."



**C. The "268 Observations" Padding (106 Orphaned Physicochemical Records)**

* **The Issue:** In the Abstract (Line 6) and Methods (Line 69), you boast an evaluation of **268 surface water observations across 17 investigations**, noting that 5 studies ($N = 106$ records) reported *exclusively* bulk physicochemical parameters (pH, EC, DO, BOD, COD, TDS, TSS).


* **The Reality Check:** Those 106 records **never appear again in the entire paper**. There is zero analysis of pH, EC, DO, or TDS in the Results, Tables, or Figures. You didn't even use pH or TDS/EC to model metal bioavailability, partitioning, or speciation. Including 5 studies and 106 records in your abstract's headline sample size when they are completely excluded from every single analysis in the paper is blatant sample-size inflation. Either integrate physicochemical controls (e.g., metal-pH regressions) or drop the 106 records from your headline numbers.

**D. Table 5 Violates its Own Methodological Rules**

* **The Issue:** In Section 2.5 (Line 206), Section 3.4 (Line 334), and the caption of Table 5, you explicitly state that your 15 candidate monitoring reaches were selected from unsampled sectors ($>25\text{ km}$ from published sites) while **"enforcing $\ge 30\text{ km}$ spatial separation"** between candidate stations.


* **The Reality Check:** Look at the coordinates in Table 5:


* `GAP_STN_01` ($23.227^\circ\text{N}, 90.631^\circ\text{E}$) to `GAP_STN_02` ($23.395^\circ\text{N}, 90.395^\circ\text{E}$) is **$\sim 30.5\text{ km}$**, and `GAP_STN_02` to `GAP_STN_03` ($23.535^\circ\text{N}, 90.144^\circ\text{E}$) is **$\sim 29.9\text{ km}$**.
* Worse, look at `GAP_STN_07` ($24.200^\circ\text{N}, 88.750^\circ\text{E}$) and `GAP_STN_08` ($24.356^\circ\text{N}, 88.492^\circ\text{E}$) — they are **$\sim 31.4\text{ km}$** apart, while `GAP_STN_08` and `GAP_STN_09` ($24.452^\circ\text{N}, 88.210^\circ\text{E}$) are only **$\sim 30.5\text{ km}$** apart.
* Even more glaringly, look at the **"Nearest Gap (km)"** column in Table 5: `GAP_STN_02` is **29.3 km**, `GAP_STN_09` is **27.9 km**, and `GAP_STN_13` is **25.5 km**. If "Nearest Gap" means distance to the nearest published site, it barely clears 25 km; if it means distance to the nearest candidate station, it directly violates your $\ge 30\text{ km}$ rule! Clarify what "Nearest Gap (km)" measures and verify your spatial buffer script.


* Additionally, **Figure 3 does not show the 15 candidate reaches!** The caption of Figure 3 explicitly states: *"showing published sampling sites and 15 geographically diverse candidate monitoring reaches"*. Yet the map and legend only plot the 23 blue dots for Published Water Quality Sites. The 15 candidate stations were left off the map entirely.





---

### 2. Statistical & Methodological Critiques

**A. Cluster Bootstrap Resampling with $k = 6$ to $12$ Clusters**

* Non-parametric cluster bootstrapping (resampling studies with replacement 5,000 times) works well asymptotically, but with only $k = 6$ (Zn) to $k = 12$ (Cr) clusters, the bootstrap distribution is highly discrete and known to suffer from under-coverage or erratic tail behavior, especially when study sample sizes ($N_j$) are severely unbalanced (e.g., Korotoa has $N = 40$ across 2 studies, while Rupsa has $N = 7$ across 2 studies).


* Furthermore, in Table 1, your header says *"reporting 95% unadjusted Wilson score and 5,000-resample study-level cluster bootstrap confidence intervals"*, and your footnote says *"Non-zero upper bounds reported for zero cells via Wilson score"*. That means you are **mixing two completely different statistical estimators in the same column** without marking which is which, or you omitted the Wilson intervals for non-zero cells despite promising them in the caption and Section 2.2 (Line 126). Also, for Cu WHO Exceedance ($1.0\%, N = 105$), the cell is *not* a zero-exceedance cell ($1/105$ is non-zero), yet the interval is `[0.0-3.2%]`. Clean this up and report your random-effects meta-analytic proportions ($79.9\%$ for Pb) in Table 1 alongside the raw pooled proportions, rather than hiding the meta-analytic estimate in the prose.



**B. What is $N = 162$? (Granularity Confounding)**

* You never define what constitutes a single "record" or "observation" in your database. In environmental literature, Paper A might publish raw individual station-season measurements ($N = 30$), whereas Paper B might publish only river-wide seasonal means ($N = 2$) or annual station means ($N = 5$).


* If you pool individual grab samples alongside multi-sample means as equal "records" in an unweighted percentage ($125/146 = 85.6\%$) or Mann-Whitney U test, studies that report disaggregated station data completely dominate studies that report summary means. You must explicitly state the aggregation level of each of the 12 studies and weight or structure your synthesis accordingly.



**C. The HPI "Damping Artifact" Critique Overshoots**

* Your mathematical decomposition of Prasad & Bose's HPI ($W_i = 1/S_i$) is spot-on: Cd ($60.2\%$) and Pb ($18.1\%$) command $78.3\%$ of the Core-4 weight.


* However, your claim that adding Cu ($W = 0.5$) and Zn ($W = 0.33$) proves that HPI is "an ill-conditioned proxy" and an "arithmetic damping artifact" misses *why* $W_i = 1/S_i$ was designed that way. Cu ($2.0\text{ mg/L}$) and Zn ($3.0\text{ mg/L}$) have guidelines 200 to 1,000 times higher than Cd ($0.003\text{ mg/L}$) and Pb ($0.010\text{ mg/L}$) precisely because they are orders of magnitude less toxic. In hazard indexing, *even in unweighted HEI*, a metal's contribution is $M_i / S_i$. What HPI actually does is weight by $1/S_i$ *twice*: once in the sub-index $Q_i = (M_i / S_i) \times 100$, and a second time in the weight $W_i = 1/S_i$, making each metal's numerator contribution proportional to **$M_i / S_i^2$**! Pointing out that **HPI scales quadratically with inverse guideline limits ($1/S_i^2$) whereas HEI scales linearly ($1/S_i$)** is a much sharper, more mathematically devastating critique than simply complaining that $W_i \propto 1/S_i$.



**D. Table 3: Copper's Pooled vs. Meta-Analytic Reversal Goes Unexplained**

* In Table 3, you highlight Pb and Ni as examples of Simpson's Paradox where pooled dry/wet ratios are $<1.0$ ($0.88\times$ and $0.73\times$), but within-study paired ratios are $\ge 1.0$ ($1.28\times$ and $1.00\times$).


* Yet you completely ignore **Copper (Cu)** in the exact same table: Cu has a pooled dry/wet ratio of **$1.52\times$** (dry enrichment), which flips to **$0.54\times$** (strong wet-season enrichment) in the within-study paired meta-analysis! Why does Copper do the exact opposite of Lead and Arsenic when controlling for station geography? You cannot cherry-pick the paradoxes that fit your dry-season concentration narrative and ignore the analyte that reverses it.



---

### 3. Internal Contradictions, Figure Flaws & Sloppiness

1. **Duplicate Figure:** Your **Graphical Abstract** (Page 1) and **Figure 1** (Page 9) are the exact same image file, down to the title. A Graphical Abstract should synthesize the whole paper (exceedances + HPI $1/S_i$ weighting + seasonal As peak + 83.5% network gap), not just copy-paste Figure 1.


2. **Figure 2 Caption vs. Plot Mismatch:** The caption for Figure 2 (Page 12) reads: *"Seasonal concentration distributions (Dry/Winter vs. Wet/Rainy) for Arsenic, Chromium, and Cadmium in Bangladesh river waters"*. Yet Figure 2 actually displays **7 boxplots** (As, Cd, Cr, Cu, Ni, Pb, and Zn)! Furthermore, the boxplots appear to omit outliers (or clip the whiskers at $1.5\times\text{IQR}$) without stating this in the caption—for instance, Cr max is $7.55\text{ mg/L}$ in Table 1, but the y-axis in Figure 2 stops at $0.175\text{ mg/L}$.


3. **Core-4 HPI Median Discrepancy ($254.13$ vs. $156.99$):**
* In the Abstract (Line 23), Section 2.3 (Line 154), and Conclusions (Line 505), you imply that Core-4 (156.99) is compared directly against expanded panels: *"explaining observed panel invariance across Core-4 (156.99) and expanded panels"* (Line 23) and *"across Core-4 (156.99), Core-5 (253.4), and All-7 (253.0) panels on identical common subsets ($N = 35$)"* (Line 154).


* That is false according to your own Results (Line 260 & Line 378): $156.99$ is the median for $N = 112$, whereas on the $N = 35$ subset, the Core-4 median is **$254.13$** (compared to $253.38$ for Core-5 and $253.02$ for All-7)! Saying "invariance across Core-4 (156.99), Core-5 (253.4), and All-7 (253.0)" in Line 154 actively contradicts your thesis by quoting numbers that differ by 100 points! Fix Line 23, Line 154, and Line 505 immediately.




4. **Missing Metal Index ($MI$) in Table 2:** Section 3.2's heading and Table 2's caption both promise **"Multi-metal pollution indices (HPI, HEI, MI)"**, yet Table 2 only lists HPI, HEI, and **Mean HQ**. If by MI you meant Metal Index (Tamasi & Cini, 2004, which is identical in formula to HEI), harmonize your terminology instead of using MI in the title and HQ in the columns.


5. **Broken LaTeX Bracket Rendering in Tables 1 & 3:** Look closely at Table 1 and Table 3. Almost every confidence interval has mangled delimiter placement from a botched regex or script output:


* Table 1: `85.6% 71.1-94.3%`, `54.8 % 21.7-79.1%)`, `44.7% 13.1-77.4[%`, `0.0% (0.0-2.6%]`.


* Table 3: `0.60-3.41[]`, `0.77-2.07[]`, `[0.11-2.50`.


* In Section 2.2 (Line 120), "Ni" and "Zn" lost their first letters in the LaTeX compile: `Ni i(0.200 mg/L)` and `n(2.000 mg/L)`.




6. **Table 2 Mean vs. Median Anomaly (Buriganga):** In Table 2, Buriganga ($N = 15, k = 1$) has a **Mean HPI of 1,607.66** and a **Median HPI of 1,977.43**. While negatively skewed data exist, environmental concentration data are almost universally right-skewed (as seen in every other row of Table 2). Double-check whether Mean and Median were transposed for Buriganga.



---

### 4. Concrete Action Plan for Revision

1. **Expand the Literature Search & Add a PRISMA Diagram:** Conduct a comprehensive search to capture the missing 2010–2024 Bangladeshi river metal studies (which should easily yield 30–50+ surface water studies), or explicitly justify why your inclusion criteria filtered out the rest of the literature. Cite all included studies in the main Reference list.
2. **Add ECR 2023 Inland Surface Water Benchmarks:** Add a column or parallel analysis comparing river concentrations against ECR 2023 Schedule 2 *Inland Surface Water* limits (or industrial effluent limits), and reframe the potable WHO/ECR drinking water comparison strictly as "raw-water potability / treatment burden screening" rather than "statutory non-compliance."
3. **Clean Up the 106 Physicochemical Records:** Either remove the 5 bulk-physicochemical-only studies ($N = 106$) from the Abstract/Methods counts, or include an analysis showing how pH, EC, and DO correlate with dissolved metal exceedances.
4. **Sharpen the HPI Critique to $1/S_i^2$:** Explicitly show algebraically that because $Q_i \propto 1/S_i$ and $W_i \propto 1/S_i$, HPI weights concentrations by $1/S_i^2$, squaring the regulatory disparity compared to linear hazard quotients (HEI).
5. **Fix All Table/Figure Errors:** Replace the duplicate Graphical Abstract, plot the 15 candidate stations on Figure 3, update Figure 2's caption to reflect all 7 metals and explain the whisker/outlier truncation, fix the $156.99$ vs. $254.13$ text error on Line 154, explain Copper's seasonal reversal in Section 3.3, and fix all broken brackets in Tables 1 and 3.

Would you like help rewriting the mathematical derivation of the $1/S_i^2$ HPI artifact or restructuring the Abstract and Discussion to reframe the ECR 2023 regulatory comparison?