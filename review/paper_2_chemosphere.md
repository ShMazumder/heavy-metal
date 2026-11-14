# Peer Review: "Dissolved Heavy Metals in Bangladesh River Waters: Multi-Study Synthesis…"

## Recommendation: Reject in current form (resubmission possible after fundamental re-analysis)

The topic matters and the open-data intent is commendable. The exceedance percentages in Table 1 are arithmetically consistent (128/146 = 87.7%, and so on). Beyond that, the manuscript has a convenience sample of literature records presented as national prevalence, no data-quality control, a seasonal analysis that cannot support causal claims, and a "monitoring optimization" that is a distance filter on the authors' own citation list. The language ("proven," "catastrophic," "unmitigated environmental health emergency," "paramount") is far ahead of the evidence.

---

## 1. Major (potentially fatal) problems

**1.1 This is not a systematic synthesis, and the "national" framing is invalid.**
- There is no search strategy, database list, inclusion/exclusion criteria, PRISMA flow, or study-level quality appraisal. "Rigorous cross-auditing" (L44) is asserted, not shown.
- Only 6 of the 28 source studies are named. The study list, with river, year, n, analytical method, filtration, and detection limits, is absent.
- The authors admit that research is "heavily clustered around capital-adjacent industrial rivers" (L27–29). They then report 87.7% as the national exceedance rate. Studies are done where pollution is suspected, so this is the proportion of published records exceeding a limit, not the proportion of Bangladesh river water. The Introduction undermines the Abstract.
- No table gives records per river or per study. If Buriganga, Turag and Karnaphuli dominate, every headline number is a hotspot statistic. There is no sensitivity analysis excluding them and no study-level random effects. Exceedance proportions have no confidence intervals and no heterogeneity measure.
- "First nationwide audit" (L17–18, L192) is claimed without citing a single prior review or meta-analysis.

**1.2 It is unclear what a "record" is.**
Results speak of "samples," but Methods say "records" extracted from papers. If these are site means, ranges, or single values, the exceedance rate is not the fraction of samples exceeding. Mixing individual measurements with study-reported means makes the percentages uninterpretable. Pseudo-replication is also unaddressed: multiple records from one study or river are treated as independent.

**1.3 "Dissolved" is not established, and units and detection limits are ignored.**
- No filtration information (0.45 µm?) or digestion method is given. Many Bangladeshi studies report total or acid-extractable metals. If so, the title and the dissolved/particulate arguments in Section 4.2 collapse.
- "Standardized into mg/L and µg/L" (L49) is not a unit-harmonization protocol.
- There is no treatment of non-detects. Several values look censored or imputed. The Ni median is exactly 0.1000 and the Zn median exactly 0.5000. The Cd overall median is exactly 0.0030, which equals the WHO limit. The Cd seasonal medians (0.0015, 0.0008) are reported to one significant figure, and the Table 2 ratio doesn't even reproduce: 0.0015/0.0008 = 1.88, not 1.81. Cd at these levels is near typical FAAS detection limits, so exceedance and ratios depend on how "<DL" was handled.

**1.2b Outliers and probable data errors drive the headline statistics.**
- Max dissolved Pb is 33.0 mg/L. That is physically implausible for river water at circumneutral pH. It smells like a unit error, an sediment (mg/kg) value, or a typo.
- Mean Pb is 0.4036 mg/L over 146 records, a total of about 58.9 mg/L. That single 33.0 value is roughly 56% of the sum, so the mean Pb is essentially one data point.
- Four chemically unrelated metals (Pb, Cr, Ni, Cu) all have means of about 0.40–0.43 mg/L. That suggests a few shared outlier or unit-contaminated records. Check them against the source papers.
- Using your own HPI weights (ΣWᵢ ≈ 568 for all seven metals), one Pb value of 33 mg/L alone yields HPI ≈ 58,000. Your max HPI is 58,135. The mean HPI of 1,483 × 157 records ≈ 232,800 in total, so that one record is about a quarter of it. Reporting a mean HPI of 1,483 (Abstract, Highlights) is meaningless; the median is 208.5.

**1.3 Comparing raw river water to drinking-water standards, then calling it "violation."**
- WHO guidelines and ECR drinking-water limits apply to water at the point of consumption. Surface water is not "non-compliant"; it is untreated. The relevant frameworks are surface-water or source-water standards, aquatic-life criteria, or irrigation criteria. "Compliance failure rate" in the Graphical Abstract is a category error.
- WHO has no health-based guideline for zinc. The 3 mg/L is an old taste/acceptability value. Counting Zn "exceedances" of a WHO "guideline" is wrong.
- The ECR limits you list match the older (1997) drinking-water schedule values as far as I know. Document exactly which schedule of ECR 2023 you used.
- The text has no exposure assessment (no ingestion rates, populations, or HQ/CR calculations), yet it uses "acute public health hazard" and "substantial carcinogenic risk." Much of Bangladesh's drinking water is groundwater. You never establish how much untreated river water people actually ingest. The only support is one Buriganga paper (Ahmad et al., 2010).
- Cr, Ni, and Cd are labeled "carcinogenic" (L115–117, L162). Total Cr is measured, and carcinogenicity is a Cr(VI) issue (Cr(III) is an essential nutrient). Oral carcinogenicity of Ni and Cd is not established in the way this implies.

**1.4 The seasonal dilution analysis cannot support "proven hydraulic flushing."**
- *Confounding.* The comparison is dry-season records versus wet-season records pooled across studies, not within-site, within-study contrasts. If dry-season records come disproportionately from industrial reaches, you have measured site mix, not dilution. Year, method, detection limit, and river all vary. Cr is a good example: the 2017 relocation of Hazaribagh tanneries alone could generate a date effect. Use paired or stratified comparisons, or a mixed model with study and river as random effects.
- *Multiplicity.* Seven tests, no correction. Bonferroni gives α ≈ 0.007. Holm gives the same result: only As (p = 0.0021) survives. Cr (0.0191), Cd (0.0204), and Zn (0.0458) do not.
- *Reporting errors.* The claim "p < 0.02" for Cr, Cd, As (Highlights, L136) is false for Cd (0.0204). Cd at 1.81× and As at 1.74× are not "double." Zn at 7.31× is described as "nearly double" in the Abstract. An 86% reduction contradicts the claimed "~50% dilution."
- *The U statistics and p-values don't reconcile.* I checked with the normal approximation, using your N's, and assuming U is for the dry group as your text implies:
  - Pb: n₁n₂/2 = 850, but U = 808 is below that. Ni: 369 expected, but U = 338. For H₁: dry > wet, a U below the null mean forces a one-sided p above 0.5. You report 0.46 and 0.434.
  - Zn: U = 308 gives p ≈ 0.03, not 0.0458. As: U = 913 gives p ≈ 0.005, not 0.0021.
  - Ties shift values somewhat but cannot flip direction. Recompute everything and report exact test settings.
- *One-sided testing.* A directional H₁ chosen in advance is defensible only with pre-registration. Here it makes Ni (wet higher, ratio 0.70) look "null" when the data point the other way.
- *Excluded records.* Seasonal N's cover only about 54–66% of each metal's records (Cr 102/160, Cd 87/132, As 81/122, Pb 93/146, etc.). April–May and undated records are dropped without comment, and those excluded records may be systematically different.
- *Narrative from nulls.* Failing to reject for Pb and Ni is not evidence for "monsoon stormwater mobilizes road dust" or "battery disposal dust" (L139–141, L173–177). No data support these mechanisms.
- *Unsupported hydrology.* "Baseflow drops by over 80%" (L137, L168) and "monsoon discharge often exceeding 50,000 m³/s" (L170) are uncited. No discharge data are used, and no concentration–discharge or load analysis is done. Dissolved concentration also depends on sorption, pH, and suspended sediment.
- *Internal inconsistency.* "Dry" is defined as Nov–Mar (L82), but the Discussion invokes the "pre-monsoon dry season" (L168), which you excluded.
- *Policy contradiction.* You recommend doubling Nov–Mar sampling "when acute human exposure peaks" (L186–187). Exposure was never measured, and your own most severe metal (Pb) shows no seasonal effect.

**1.5 The HPI analysis is under-specified and the headline class is arbitrary.**
- Which metals are required for a "multi-metal record"? With different subsets of metals, HPI is not comparable across records. A Cd+Pb-only record is dominated by weights 333 and 100. A Zn+Cu record is near zero.
- L70–72 says HPI = 100 is the critical threshold, then defines the "critical" class as HPI > 200 and "moderate" as 100–200. I can't find this three-tier scheme in the cited sources; justify or cite it. By the conventional HPI > 100 criterion, 63.7% (100/157) would be "unsuitable," not 51.6%. The headline depends on an unexplained cutoff.
- HEI and MI are defined (Eqs. 3–4) and promised (Objective 2; the Section 3.2 title), but their results never appear. Also, Eq. 3 and Eq. 4 are mathematically identical (Σ concentration/limit) unless different limits are used.
- "Critical pollution concentrated in Buriganga, Turag, Korotoa, lower Karnaphuli" (L129–131) has no table, figure, or statistic behind it. "Driven by weights of Pb and Cd" is tautological, because the weights are fixed. You need contribution analysis.

**1.6 The "National Monitoring Network Optimization" is not what it claims.**
- *Wrong reference set.* "Historical monitoring points" appear to be coordinates from your own 28 papers. DoE/BWDB stations are not in the analysis, yet the conclusions are about "government monitoring station deployment" and "any routine academic or government station" (L152–153). That is a non sequitur. The number of stations used and how they were geocoded are not reported.
- *No optimization.* There is no objective function (pollution sources, population served, intake locations, variance reduction, entropy), no constraints, and no network design method. It is a >25 km buffer filter.
- *The ranking is tautological.* Ranking by drainage area and discharge always selects the downstream end of the largest river. The top 8 "stations" (Table 3) are consecutive vertices of the same reach: GAP_STN_01–03 are ~1 km apart, and all eight fit within roughly a 13 km stretch of one channel. That is one site, not eight. Your own results say contamination is concentrated in small industrial rivers, while the ranking selects the river where metals are most diluted.
- *The "4,435 reaches" is a segment count with no denominator.* How many segments met the order/discharge filter in total? What fraction is "unmonitored"? Report river length in km. The clipping domain is also unspecified. 55,668 segments is not obviously Bangladesh only; if upstream India/Nepal/Bhutan are included, "national" is wrong.
- *Projection and distance.* Distances were computed in EPSG:3857. At 23°N, Web Mercator inflates lengths by 1/cos(23°) ≈ 1.09, so your "25 km" is about 23 km of real distance. Use a UTM 45N/46N or BTM projection, or geodesic distances. Euclidean distance also ignores network position, and "network routing" (L92) is claimed but not done. The 25 km threshold is unjustified.
- *Data quality of HydroRIVERS.* It is a modeled network with known weaknesses in the tidal, braided, deltaic Lower Meghna, where channels migrate on the scale of kilometers. Reporting "exact GPS coordinates" to three decimals for stations is false precision.
- *Inconsistencies.* Abstract/Highlights promise a "top 15," but Table 3 shows 8. Methods say ranking is by stream order and drainage area; Results say drainage area and discharge.

---

## 2. Moderate problems

1. **No limitations section.** Zero. For a paper this exposed to selection bias, unit heterogeneity, and confounding, that is disqualifying on its own.
2. **Temporal heterogeneity ignored.** Data span 2010–2022 across changing industrial practices, with no trend or year-effect analysis.
3. **No covariates.** pH, hardness, TSS, and salinity (important in the Meghna estuary) are absent, though they control dissolved Cd, Pb, and Cr.
4. **Discussion is thin.** It cites two references (Ahmad 2010, Needleman 2004) and does not compare findings to other river systems (Ganga, Yangtze, etc.) or to existing Bangladeshi syntheses.
5. **Weak reference base.** Only 16 references for a 28-study synthesis. Some citations look mismatched: a Buriganga heavy-metal paper (Ahmad et al., 2010) supports a claim about GBM water for 170 million people (L4–6).
6. **Overreach in language.** "Proven," "catastrophic," "emergency," "paramount," "alarming." Observational literature records cannot "prove" a hydrological mechanism.
7. **Software and reproducibility.** No software versions, random seeds, or code description. A GitHub repository is not an archive; deposit the dataset and code on Zenodo or similar with a DOI.

---

## 3. Presentation and minor issues

- **Tables overflow the page.** Table 1 (BD exceedance column), Table 2 (p-value column), and Table 3 (target river reach) are cut off, so I could not verify several values.
- **Figure 2:** the Cd panel reverses the x-order (Wet, then Dry) and swaps the color mapping relative to the Pb and Cr panels. The Pb panel shows the lone ~33 mg/L dry-season outlier. The significant metals (As, Zn) are not plotted, while non-significant Pb is. The Cr boxes overlap heavily, so the "doubling" is within the interquartile spread.
- **Figure 1 duplicates Table 1 and the Graphical Abstract.** It has no confidence intervals, and the Graphical Abstract doesn't represent the paper's three other contributions.
- **Highlights** exceed typical Elsevier limits (3–5 bullets, ~85 characters each) and contain typesetting glitches: "HP I" and "1, 483".
- **Anonymization.** The Data Availability statement exposes a personal GitHub handle. If the journal uses double-anonymous review, this breaks blinding.
- **WHO edition.** WHO's fourth edition has since been issued with a second addendum (2022), which falls inside your data window.

---

## 4. Minimum work for a viable resubmission

1. Redo the data compilation as a documented systematic review: protocol, study table, units, filtration and digestion method, detection limits, and QA exclusion criteria.
2. Verify every extreme value (Pb 33.0, Cd 1.75, Cr 7.55, Zn 10.29 mg/L) against the source papers, and handle non-detects with proper censored-data methods.
3. Replace "national exceedance rate" with a study-weighted, random-effects estimate with CIs and a hotspot-excluded sensitivity analysis. Compare against surface-water or source-water criteria, not just potable standards.
4. Rerun the seasonal tests: within-study or mixed-effects, two-sided, multiplicity-corrected, with discharge data. Reconcile U and p. Drop "proven."
5. Fix HPI (fixed metal panel, justified thresholds, median and IQR), and report HEI and MI or remove them.
6. Rebuild the gap analysis with DoE/BWDB stations, an appropriate projection, network distance, a stated objective (exposure, source proximity, population), and non-redundant candidate sites. Or retitle it honestly as "spatial coverage of published studies."
7. Add a real limitations section and cut the rhetoric to match the evidence.

I'd also stop leading with Pb. Until the 33 mg/L record is explained, every Pb-driven number (87.7% exceedance, mean HPI, max HPI, "3,000-fold") rests on a datum that may be an error.


Fix them in dependency order: the data audit comes first because everything else rests on it, and the claims get rewritten last, bottom-up, from whatever the corrected analyses show.

One correction to my review first. The 87.7% Pb exceedance is a count, so the single 33 mg/L record barely moves it (about 0.7 points). That record mainly corrupts the mean Pb, the max, and the HPI. The exceedance rate is at risk only if there are systematic problems such as mg/kg values, unit slips, or detection limits substituted at or above the guideline. The audit below will tell you which.

---

## Step 0: Decide what paper this is

The current draft makes four separate claims, and the evidence behind them is uneven. I suggest one of two routes:

- **Route A (realistic):** Keep the synthesis, exceedance, HPI and seasonal parts. Reframe them as a *descriptive synthesis of published records*, and retitle the spatial part "spatial coverage of published studies." Drop "national" and "optimization" from the title.
- **Route B (ambitious):** Split into two papers. One is the systematic review/meta-analysis of metals in Bangladeshi rivers. The other is a monitoring-network design paper that includes the real DoE/BWDB stations.

Example Route A title: *"Dissolved and Unspecified-Fraction Heavy Metals in Bangladesh River Waters: A Synthesis of Published Records (2010–2022), Benchmark Exceedance, and Seasonal Contrasts."*

---

## Step 1: Rebuild the dataset

**1.1 Study-level extraction sheet.** Put this in the repo and in the supplement, one row per record:

| Field | Why |
|---|---|
| study_id, DOI, river, site name, lat/lon (and how geocoded) | traceability, spatial analysis |
| sampling date (month and year) | seasonal and temporal analysis |
| value type (individual sample / site mean / median / range) | defines what "record" means |
| fraction (dissolved / total / unspecified), filtration size, digestion | justifies the word "dissolved" |
| reported units and converted units | auditable unit handling |
| instrument and detection limit per metal | censored data |
| QA/QC reported (blanks, CRMs, recovery) | quality screening |

**1.2 Search protocol.** Document databases (Scopus, Web of Science, Google Scholar, BanglaJOL), the search string, search date, de-duplication, inclusion/exclusion criteria, and a PRISMA flow diagram. Add a simple 5–6 item risk-of-bias checklist: filtration stated, DL reported, QA/QC, sampling design, date reported.

**1.3 Re-verify extremes against the source papers.** Pull every value above roughly the 99th percentile per metal, plus the exact-round medians (Ni 0.1000, Zn 0.5000), plus the Cd values near the DL. Check:
- Is the 33.0 mg/L Pb a typo, a sediment or biota value in mg/kg, an effluent sample, or a real measurement?
- Why do four unrelated metals have means of about 0.4 mg/L?
- Were any sediment or fish tissue values pulled in?

Have a second person independently re-extract a random 20–30% and report agreement. That turns "rigorous cross-auditing" into something checkable.

**1.4 Define "record" and handle it consistently.**
- Analyze individual-sample data and site-mean data in separate strata.
- Never compute "percentage of samples exceeding" from site means.
- Rename "samples" to "records" or "site-level observations" wherever that is what they are.

**1.5 Fraction.** If you can't confirm filtration for most records, drop "dissolved" from the title and use "dissolved or unspecified-fraction." Run a sensitivity analysis restricted to confirmed-dissolved records.

**1.6 Non-detects.**
- Record the DL per record and flag each non-detect.
- Use left-censored methods (Kaplan–Meier or ROS) for summary statistics. In R this is `NADA`/`NADA2`; in Python, `lifelines` offers left-censored fitting.
- For exceedance, treat "<DL with DL > guideline" as *undetermined*, not as exceedance or compliance.

---

## Step 2: Reframe and recompute exceedance

**2.1 Use the right benchmarks.**
- Compare against the *surface/source-water* schedules in ECR 2023 (read the gazette text directly and cite the schedule), plus WHO values as a *reference benchmark*, plus an aquatic-life criterion as a secondary comparison.
- Drop Zn from the WHO health comparison. 3 mg/L is an acceptability value, not a health-based guideline.
- Replace "violate" and "compliance failure" with "exceeded the drinking-water guideline value."

**2.2 Account for clustering.** Records from one study are not independent.

```python
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.proportion import proportion_confint

# naive Wilson CI (reported alongside, not instead)
lo, hi = proportion_confint(128, 146, method="wilson")

# cluster-robust estimate: intercept-only GEE, study as the cluster
m = smf.gee("exceed ~ 1", groups="study_id", data=pb_df,
            family=sm.families.Binomial(),
            cov_struct=sm.cov_struct.Exchangeable()).fit()
```

For the formal route, use a random-effects meta-analysis of proportions (R `meta::metaprop` or `metafor`) and report I² and a prediction interval.

**2.3 Sensitivity analyses.**
- Leave-one-river-out.
- Exclude Buriganga, Turag, and Shitalakhya.
- Individual-sample records only.
- Confirmed-dissolved records only.

Report a per-river table (n records, n studies, years, median, exceedance with CI).

**2.4 Rewrite the claim.** Say "X% of records in the published literature (95% CI …), dominated by studies of industrial peri-urban rivers; excluding these, Y%."

**2.5 Health language.** Either do a real risk assessment (hazard quotient and cancer risk using ingestion and dermal pathways, with stated assumptions) or delete the "emergency," "carcinogenic," and "acute hazard" language. Also:
- Say "total Cr" throughout.
- Don't call Cr, Ni, Cd "carcinogenic" for the oral route without citing IARC/WHO classifications precisely.
- Don't claim people drink raw river water without data on intake and treatment.

---

## Step 3: Fix the HPI analysis

1. **Fix the metal panel.** Compute HPI only for records with the same core set (for example As, Cd, Cr, Pb), and show a sensitivity analysis with an alternative panel. Don't mix subsets.
2. **Cite the thresholds exactly.** Use the Prasad & Bose/Mohan critical value of 100. If you want a 100–200 and >200 scheme, justify and cite it. Report the share above 100 as well (100/157 = 63.7% in your current data).
3. **Report robust statistics.** Median and IQR with bootstrap CIs, and log₁₀HPI in figures. Drop the mean of 1,483.
4. **Replace the tautology with contribution analysis.** For each river, compute the share of ΣWᵢQᵢ contributed by each metal.
5. **HEI and MI.** Compute and report both, or remove them from the objectives and Section 3.2 title. Note that Eqs. 3 and 4 are mathematically identical unless you use different limits (say WHO for HEI and ECR for MI), and state that explicitly.
6. **Support the river claims.** A table or boxplot by river, with n, backs "critical pollution in Buriganga, Turag, Korotoa, lower Karnaphuli." Otherwise delete the sentence.

---

## Step 4: Redo the seasonal analysis properly

**4.1 Primary analysis: within-study contrasts.** Select studies (or study × river units) that sampled both seasons. Compute a log-ratio of dry to wet for each, then pool with a random-effects model. This is the cleanest test of dilution. If few studies qualify, say so and weaken the claim accordingly.

**4.2 Secondary analysis: mixed model on all dated records.**

```python
import numpy as np
import statsmodels.formula.api as smf

df["logc"] = np.log10(df["conc"])  # after censored-data handling / DL substitution sensitivity
m = smf.mixedlm("logc ~ C(season)", df, groups=df["study_id"]).fit()
```

Add river and year as covariates or random effects. For proper censoring, use `brms` with `cens()` in R. Add `log(discharge)` from BWDB gauges where available, and show concentration–discharge plots.

**4.3 Testing hygiene.**
- Two-sided tests (or a pre-specified direction, committed in the repo before you run anything).
- Holm or Benjamini–Hochberg across the seven metals.
- Report effect sizes with CIs, such as the Hodges–Lehmann shift or a bootstrapped ratio of medians, not just p.
- Use four seasons if the dates allow (dry, pre-monsoon, monsoon, post-monsoon), rather than discarding April–May and undated records. Report how many records were dropped for missing dates and whether the missingness differs by study or river.

**4.4 Reconcile the U/p mismatch.** Re-run with an explicit call, save its output, and record the settings.

```python
from scipy.stats import mannwhitneyu
from statsmodels.stats.multitest import multipletests

res = mannwhitneyu(dry, wet, alternative="two-sided", method="asymptotic")
# collect p-values across metals, then:
reject, p_adj, *_ = multipletests(pvals, method="holm")
```

Find out why the current U and p values disagree (different filtered subsets, a different direction, or a table built from another run) and regenerate Table 2 from a single script.

**4.5 Rewrite the claims.** Expect that only As (and possibly Cr) will remain supported. Use "associated with," not "proven." Present Pb/Ni mechanisms (road dust, battery waste) as *hypotheses* in the Discussion. Cite or delete "baseflow drops by over 80%" and "50,000 m³/s," and fix the Nov–Mar vs "pre-monsoon" inconsistency.

**4.6 Drop or rework Policy Recommendation 2.** "Double the Nov–Mar frequency" is not supported by exposure data, and it doesn't apply to Pb. If you keep it, restrict it to the metals with a robust seasonal signal.

---

## Step 5: Rebuild the spatial analysis

**5.1 Quick fixes (needed either way).**
- Reproject to UTM 46N (EPSG:32646); scale error across Bangladesh is below roughly 0.3%. Don't use EPSG:3857.
- Clip HydroRIVERS to the Bangladesh boundary and state the clip. Check whether the 55,668 segments are Bangladesh-only.
- Use along-network distance. HydroRIVERS gives `NEXT_DOWN`, `LENGTH_KM`, `DIST_DN_KM`, `ORD_STRA`, `DIS_AV_CMS`, and `UPLAND_SKM`, so you can build a directed graph in `networkx` and measure distance along the river.
- Report **river length** (km) beyond the threshold with the total as the denominator, instead of "4,435 segments." Test thresholds of 10, 25 and 50 km.
- Deduplicate candidates. Take one candidate per reach or one per ~20 km spacing, so the "top 15" are real distinct sites rather than adjacent vertices.
- Add a **map**. The paper has none. Show study locations, rivers, and candidate sites.
- Show all 15 candidates in a table or the supplement, and make the ranking criteria consistent between Methods and Results.

**5.2 Choose your claim.**
- *Cheap and honest:* keep the analysis as a "coverage of published studies" analysis. Rename the section, the title, and the conclusions. Remove "government monitoring" and "optimization."
- *As promised:* obtain the DoE and BWDB station lists (official requests, annual reports, or published tables) and rerun against them. Then define an objective, such as a score combining population within a buffer (WorldPop), industrial clusters (tannery, textile, EPZ), observed hotspots (for example kriged HPI), intake locations, and distance to the nearest station. Select sites with a maximal-coverage or p-median formulation (`pulp` or OR-Tools) instead of ranking by drainage area. State the constraints: tidal/saline reaches, accessibility, and channel migration in the lower Meghna. Drop three-decimal "exact" coordinates in favor of reach-level recommendations.

---

## Step 6: Writing and presentation

- **Limitations section.** Cover selection and publication bias, mixed analytical methods, unspecified fractions, detection-limit handling, between-study confounding in the seasonal comparison, modeled river network, and no exposure assessment.
- **Tone.** Replace "proven," "catastrophic," "unmitigated environmental health emergency," and "paramount" with calibrated language.
- **Novelty.** Search for prior Bangladesh and regional syntheses, cite them, and either drop "first" or state precisely what is new.
- **Discussion.** Compare with other river systems (Ganga, Yangtze, and similar) and with earlier Bangladeshi reviews. Fix mismatched citations, and expect a longer reference list than 16.
- **Tables.** Fix the overflow with `\small`, `tabularx`, `\resizebox`, or `sidewaystable`. Make sure all columns (BD exceedance, p-values, target reach) are visible.
- **Figure 2.** Use the same order and colors in every panel, overlay the points, and include As and Zn alongside Cr, Cd, and Pb.
- **Graphical abstract.** Redesign it as a workflow of data, exceedance, season, and coverage, with two or three headline numbers. A duplicate of Figure 1 doesn't do that job.
- **Highlights.** Use 3–5 bullets of about 85 characters or fewer, and write them last from the final numbers.
- **Typesetting.** Use `\mathrm{HPI}` and fix "1, 483."
- **Reproducibility.** Deposit data and code on Zenodo with a DOI, with software versions and seeds. For double-anonymous submission, use an anonymized repository link and remove the personal GitHub handle.
- **WHO edition.** Cite the current edition with its addenda, and note which guideline values changed.

---

## Suggested execution order

1. Audit and rebuild the dataset (Step 1). Freeze it with a version tag.
2. Commit a short pre-analysis plan in the repo: tests, direction, corrections, metal panel.
3. Run everything from one script that regenerates every table and figure.
4. Rewrite the Abstract, Highlights, and Conclusions last, from the new numbers.
5. Decide Route A or B for the spatial component before you invest in station data.

Expect some headline numbers to change. The most likely outcomes are Pb and the HPI mean shifting after the outlier audit, and the seasonal story narrowing to As, possibly with Cr. A modest paper whose claims survive scrutiny will fare much better than the current version.

I can draft the extraction template, a single reproducible analysis script, the limitations section, or rewritten Highlights and Abstract for whichever route you choose.