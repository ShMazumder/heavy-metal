# Round 2 Peer Review

## Recommendation: Major revision (up from reject)

The revision fixed most of the statistical hygiene and presentation problems from round 1, and the underlying data changed substantially. It is still not publishable. The Abstract and Results quote different headline numbers, HPI is computed on inconsistent metal sets, the data audit is undocumented, and the spatial section is still a distance-to-nearest-dot exercise presented as surveillance guidance.

---

## 1. Were the round-1 issues addressed?

| Round-1 issue | Status | Comment |
|---|---|---|
| Title/scope; "first nationwide"; "proven"; alarmist tone | **Fixed** | Retitled and toned down. Residue remains: the Abstract still says "systematic," and "national exceedances" appears at L203–204 and in the Abstract and Conclusions. |
| Search protocol, PRISMA, study-level table, QA appraisal | **Not addressed** | Only 8 of the 28 studies are named. The Intro says "descriptive synthesis" while the Abstract says "systematic." |
| Define "record" (individual sample vs site mean) | **Not addressed** | Still "records" throughout. |
| Dissolved vs total fraction | **Partial** | Honest relabel, but no count of confirmed-dissolved records and no sensitivity run. |
| Non-detects | **Not addressed** | Only acknowledged in Limitations. |
| Outliers and unit errors | **Partial** | Values were corrected, but the audit is undocumented (see M4). |
| Drinking-water framing, Zn footnote, Cr(VI) caveat, exposure caveat, "violation" language | **Mostly fixed** | No pathway-appropriate benchmarks (see M8). |
| Confidence intervals | **Partial** | Wilson CIs added, but they assume independent records. |
| Sensitivity excluding Dhaka rivers | **Partial** | Reported only for the BD standard and only for Pb and As (see M5). |
| Seasonal: two-sided tests, Holm, consistent U/p, no "proven" | **Fixed** | I recomputed them (below). |
| Seasonal: within-study or mixed model, discharge, excluded records, effect-size CIs | **Not addressed** | Confounding is acknowledged in Limitations but not analyzed. |
| HPI: median/IQR, share above 100, HEI/MI reported | **Partial** | See M2 and M3. |
| HPI: fixed metal panel; threshold labels | **Not addressed** | |
| Spatial: projection, border clip, km denominators, 10/25/50 km, 30 km dispersion, all 15 candidates | **Fixed** | |
| Spatial: map, network distance, sampling-point provenance, objective function, DoE/BWDB | **Not addressed** | See M7. |
| Limitations section | **Added** | Incomplete. |
| Table overflow, Fig. 2 order/colors, Highlights format, "HP I," WHO 2022 | **Fixed** | |
| Graphical abstract; anonymization; archival DOI | **Not addressed** | |
| Citation mismatches | **Not addressed** | New ones introduced (see M9). |

**What I re-verified, and it holds:**
- Table 1 percentages and the Wilson intervals reproduce. I recomputed Pb and Zn.
- Table 3's U statistics now reproduce the two-sided p-values under the normal approximation (As z≈2.89 gives 0.0038; Pb z≈0.19 gives 0.85), and the Holm adjustments are correct.
- Table 2's per-river N sum to 157, the N-weighted mean HPI reproduces 718.74, and the above-100 and above-200 counts reproduce 99 and 79.

The remaining problems are design and consistency, not arithmetic.

---

## 2. Major problems

**M1. The Abstract/Highlights and Results disagree on the headline spatial numbers.**
- Abstract: 89.8% of 9,915.9 km across 4,389 reaches. Highlights: "over 89%."
- Results (L180–183): 3,894 segments totaling 8,369.5 km, of which 3,408 reaches (87.5%) and 7,372.3 km lie more than 25 km from a sampling point.
- By length, 7,372.3/8,369.5 is 88.1%. The 87.5% is a segment *count* ratio (3,408/3,894). The Conclusions (L283) then call 87.5% "reach length," and Limitations say "over 87%."
- Your 10 km and 50 km figures are length-based (8,041.2/8,369.5 = 96.1%; 5,844.7/8,369.5 = 69.8%), so the 25 km figure should be 88.1%.
- The Abstract numbers look like leftovers from an earlier run, before the border clip. Generate every in-text number from the script (Quarto, or LaTeX macros fed by a results file).

**M2. HPI is still not computed on a fixed metal panel, and your maximum proves it.**
- Methods use "records with ≥3 analyzed metals" (L80), so ΣWᵢ differs from record to record.
- With your own weights (Wᵢ = 1/Sᵢ, ΣWᵢ ≈ 568 for all seven) and the Table 1 maxima, a hypothetical record with *every* metal at its dataset maximum would score about 4,890 (Cd ≈2,400, Pb ≈1,230, As ≈620, Cr ≈530, Ni ≈100).
- Your reported maximum is 5,920. That is only possible if the denominator shrinks, meaning a record with just a few high-weight metals.
- HPI values from different metal subsets are not comparable. Fix a core panel, for example As, Cd, Cr, Pb, Ni, and show a sensitivity run on alternatives.

**M3. HPI interpretation is inconsistent, and the other indices contradict it without comment.**
- "Critical" means HPI > 200 in L85–87. It means HPI > 100 in the Abstract, L149 and the Conclusions. L150 calls HPI > 200 "high."
- L85 calls the three-tier scheme "standard." Prasad and Bose's critical limit is 100. Cite a source for the 100–200 "moderate" tier or present it as your own convention.
- By your own HEI thresholds, a median HEI of 8.21 is "low risk" (<10), while the median HPI of 202 is "critical." Turag has HPI 172 but HEI 4.99; Karnaphuli has HPI 232 but HEI 8.15.
- The explanation is presumably that HPI up-weights Cd (333), Pb and As, while HEI weights all metals equally. L157 says HEI/MI "corroborate" HPI, which is false without a test (a rank correlation, say). MI has no thresholds defined at all.
- River rankings rest on tiny N: Meghna 3, Shitalakhya 3, Padma 6, Rupsa 7. Yet the Conclusions name Meghna, Buriganga and Shitalakhya as the most contaminated. L155 attributes low HPI in Rupsa and Kirtankhola to "lower industrial metal loadings," with no evidence. Report the number of studies per river, add CIs, and delete the causal phrase.

**M4. The data audit is undocumented, and the corrections show the first extraction was unreliable.**
- Compared with the previous version, N per metal is identical while values moved a lot: Pb max 33.0→0.700 and mean 0.404→0.082; Cd max 1.75→0.123; Zn max 10.29→3.20; Cu max 6.32→2.18; Cr mean 0.417→0.313.
- Exceedance counts fell by *exactly three* for Pb, Cr, Ni, Cd, Zn and Cu, but not for As. That is consistent with a small block of mis-scaled records driving the earlier extremes (my inference).
- Dry-season N dropped by one for six metals while wet N and totals did not change, so one record seems to have changed season. This is also undocumented.
- L50–51 says extremes were "audited against primary texts, verifying … instrument calibrations." You can't verify calibration from a paper's text. State how many records were corrected, the error types (unit scaling, sediment mg/kg vs water, transcription), whether the audit covered all 268 records or only extremes, and whether a second person re-extracted a random subset.
- Heavy tails remain: Cr max 7.55 mg/L, Ni 2.89, Cu 2.18. Mean/median ratios are 3–4.6× for Pb, Cr, Ni, Cu and Cd. Verify these against the sources too.
- Still missing: the study table (Supplement S1) with river, year, n, value type, fraction, method, DL and coordinates per record, plus the number of studies per metal. Mortuza (2024) is cited as a data source but falls outside your stated 2010–2022 window (L45–48).

**M5. Exceedance statistics: clustering ignored, sensitivity analysis selective, "national" language lingers.**
- Wilson CIs treat 268 clustered records as independent. Korotoa alone has 40 multi-metal records, probably from one or two studies, so effective sample sizes are much smaller. Use a cluster-robust estimate (GEE with study as cluster) or a random-effects meta-analysis of proportions, and report studies per metal.
- The sensitivity analysis (L137–143) reports only BD-standard exceedance for Pb and As. The headline, WHO Pb at 85.6%, has no non-Dhaka counterpart, and neither do Cr, Ni, Cd, Cu or Zn. No CIs are given. Provide a full table: every metal, both benchmarks, N, CI, with and without the three Dhaka rivers, plus leave-one-river-out.
- L73–74 says "Wilson with continuity adjustment," but Eq. 1 is the plain Wilson interval, and your numbers match it.

**M6. The seasonal result rests on pooled, clustered, partly excluded data, and the narrative still outruns it.**
- Between 34% and 47% of records are dropped from each test (As 80/122 retained, Cr 101/160, Cd 86/132, Pb 92/146, Zn 44/79, Ni 58/104, Cu 56/105). April–May and undated records are excluded without comment. Report how many are undated, how many fall in Apr–May, and whether they differ.
- Mann–Whitney assumes independence, but records cluster by study and river, and the dry and wet samples come from different studies. The As result (padj = 0.027) is fragile under clustering. Run a within-study contrast where studies sampled both seasons, or a mixed model with study as a random effect. Add effect-size CIs; the Cd ratio comes from one-significant-figure medians (0.0015/0.0008).
- The Highlights say testing "confirms seasonal dilution," while Limitation 4 admits confounding. Pick one.
- "Dilution" is not demonstrated without discharge data, and the As mechanism in the Discussion (L239–241, "point-source industrial effluents") is doubtful. As in the Bengal Basin is largely geogenic. Higher dry-season As could reflect groundwater-fed baseflow or irrigation return flow, not a lack of dilution. Offer this as an alternative.
- L237–246 again builds a mechanism for Pb and Ni out of non-significant results (ratios 0.88 and 0.73), and the Conclusions repeat "compensatory non-point source wash-off." That is speculation presented as inference. Also, "increases by orders of magnitude" (L241) is uncited and overstated for major-river discharge.

**M7. The spatial analysis still doesn't deliver what the framing implies.**
- There is no map. For a spatial claim, the paper has no map of sampling points, rivers, or candidates.
- The number of unique sampling points, how they were geocoded (study GPS vs approximate), and sensitivity to location error (±5 km) are all unreported. With 12 rivers, a handful of coarse geocodes could decide an 88% gap statistic.
- "Geodesic distance routing" (L178) is straight-line Haversine distance to a segment centroid. It is not routing, and it isn't geodesic (ellipsoidal) either. A sampling point on a parallel channel or a different river counts as "coverage," while along-network position is ignored.
- Coverage is measured against your 28-study compilation, not "the published literature" and not DoE/BWDB monitoring. Yet the Abstract, Highlights ("lacks published water quality monitoring") and Conclusions speak of "surveillance gaps" and "future surveillance deployments." The Intro's "published monitoring stations" is also a misnomer; one-off academic sampling sites are not monitoring stations.
- Table 4 is sorted purely by drainage area (1.57M→0.50 M km²) and then thinned to ≥30 km spacing. It is a walk up the Meghna–Padma, then the Ganges, then the Jamuna. There is no objective function (population, intakes, industrial clusters, observed hotspots), and none of the polluted small rivers from Table 2 appear. It does not prioritize anything.
- Several "Target River Reach" labels don't match the coordinates. From my recollection of town positions (check a gazetteer): Madaripur lies about 40 km south of GAP_STN_03, Sirajganj about 40 km north of STN_10, Gaibandha about 50 km north of STN_13, and Kurigram about 70 km north of STN_14.
- Q increases upstream along the Jamuna (20,698 at STN_10 to 21,061 at STN_15). That is HydroRIVERS modeling noise, and your ranking uses Q.

**M8. The benchmarks don't match the pathways you argue for.**
- Section 4.2 says irrigation, bioaccumulation and direct contact are the relevant pathways, but no benchmark for any of them is used (FAO irrigation guidelines, aquatic-life criteria, ECR surface-water or irrigation schedules).
- "Direct potable use is relatively uncommon" (L208–213) is uncited and skips the main drinking-water link: treated surface-water intakes. As far as I know, Dhaka WASA's Saidabad plant draws from the Shitalakhya, and Chattogram uses surface sources. Your own Shitalakhya HPI (N=3) bears on that. Verify and cite. Likewise, "river water is heavily abstracted for boro rice" (L216) is uncited, and I believe overstated given how much dry-season irrigation is groundwater.
- The figure legend says "ECR 2023 / 1997," while the text says "ECR 2023 Schedule 3." Pick one and cite the gazette, schedule, and date. A generic "Technical Report" is not verifiable. The Fig. 1 legend also calls the WHO bars "Health Benchmark," which conflicts with the Zn footnote.

**M9. References.**
- Datta and Subramanian (1998), a *sediment* geochemistry paper, supports the claim that GBM water supports 170 million people (L3–4).
- Hossain et al. (2021), a primary Buriganga/Turag study, supports a claim about the whole literature being clustered (L24). It is one of the clustered studies.
- Li and Zhang (2018) underpins two load-bearing claims: raw-water screening (L19) and the stormwater mechanism (L243). I couldn't confirm that paper (title, volume, DOI) from memory. Verify it, and replace it with Bangladesh-specific or Ganges–Brahmaputra evidence for the Bangladesh mechanism.
- The Discussion still doesn't compare against other river systems or prior Bangladeshi syntheses. "Comprehensive" in the Conclusions is not earned by a 28-study sample.

---

## 3. Moderate and minor

- **Limitations are incomplete.** Missing: record independence/clustering, record definition, non-detect handling (what *did* you do?), variable-panel HPI, temporal heterogeneity (2010–2022), absence of covariates (pH, TSS, salinity), exclusion of 34–47% of records from seasonal tests, and no DoE/BWDB data. Limitation 1 states a *finding* (87% unmonitored), not a limitation. Limitation 3 lists instruments and digestions that no table in the paper supports.
- **Treating unspecified-fraction data as dissolved** biases toward exceedance. Describe it that way instead of "conservative."
- **Graphical abstract** is still a copy of Fig. 1, covering one of four results.
- **Highlights** omit the paper's own central caveat (hotspot clustering), contain stale numbers (M1), and use literal "p_adj" and "1.74x."
- **Reproducibility.** The Data Availability statement still exposes a personal GitHub handle (a blinding problem under double-anonymous review), has no archival DOI, and gives no tag for a dataset that changed materially between versions. Add software versions.
- **Title** is clumsy: "Dissolved and Unspecified-Fraction" reads as contradictory. Consider dropping "Dissolved."
- "Audited maximum" (L196) and "audited literature database" mean nothing without M4's documentation.

---

## 4. Suggested fix order

1. Regenerate every number in the Abstract, Highlights, text and Conclusions from one script (M1).
2. Fix the HPI panel, unify the labels, and reconcile or drop HEI/MI (M2, M3).
3. Write the audit log and study table, and tag a dataset release (M4).
4. Run the full clustered-CI and sensitivity tables (M5).
5. Run within-study and mixed-model seasonal analyses and report excluded records, then rewrite the mechanism paragraphs as hypotheses (M6).
6. Add a map and sampling-point provenance. Either include DoE/BWDB stations and a real objective, or rename the section "coverage of compiled studies" and drop "surveillance" and "prioritized" (M7).
7. Add pathway-appropriate benchmarks and clean up the ECR citation (M8).
8. Verify every reference (M9), then anonymize and archive.

After this round, expect Pb, the HPI headline and the As seasonal result to hold up best. I'd treat the spatial section and the river-level HPI claims as the most likely to be cut.


Fix them in dependency order: data integrity first, then one script that produces every number, then analyses, then spatial, then text, then references and repository. If you rewrite prose before the numbers are frozen, you'll rewrite it twice. Before you start, make two decisions: what a "record" is, and whether the spatial section stays in this paper (my recommendation is yes, but as a coverage analysis of your compiled sites only).

---

## Phase 1: Freeze and document the data (M4)

**1. Define the schema, one row per measurement:**

`record_id, study_id, river, site_id, lat, lon, geocode_quality, date, season_label, metal, conc_mgL, nd_flag, dl_mgL, value_type (sample/site_mean/median/range), fraction (dissolved/total/unspecified), method, qaqc, page_ref`

Everything else (exceedance, HPI, season, coverage) is derived from this table. If you can't fill `value_type` for a study, that tells you how reliable it is. Analyze `sample` and `site_mean` rows separately, or drop the means.

**2. Generate the audit log by diffing your two dataset versions.** You already hold the evidence:

```python
old, new = pd.read_csv("v1.csv"), pd.read_csv("v2.csv")
m = old.merge(new, on=["record_id","metal"], suffixes=("_old","_new"))
chg = m[~np.isclose(m.conc_old, m.conc_new, equal_nan=True)]
chg[["record_id","study_id_new","metal","conc_old","conc_new"]].to_csv("audit_log.csv")
```

Then add `reason` (unit_scale / sediment_mg_kg / transcription / season_date / duplicate) and `verifier` columns by hand. Report the totals in Methods: records corrected, by error type. Check whether the ~3 records that flipped from exceeding to non-exceeding share a study. If they do, audit *every* record from that study, and every study that uses the same units convention.

**3. Run automated plausibility checks on all 268 records**, not only extremes:
- Flag values above the 99th percentile per metal on the log scale.
- Flag values at least 100× the study's own median.
- Flag exact-round values (Ni = 0.1000, Zn = 0.5000) and values exactly equal to a guideline.
- Flag identical value vectors that appear in two different studies. Secondary reuse of data would double-count records.

**4. Second-extractor check.** Have a second person re-extract a random 20–30% and report agreement (within-tolerance match rate for concentrations, kappa for season and fraction). That backs up "rigorous audit."

**5. Fix the dates.** Either extend the window to include Mortuza (2024) and say "published 2010–2024" everywhere, or remove his records. Find the one dry-season record that changed status in the diff and document why.

**6. Search protocol.** Reconstruct what you can: databases, search string, date searched, screening counts, a PRISMA-style flow, and a five-item risk-of-bias checklist (filtration stated, DL stated, QA/QC, dated, coordinates). A starting string: `("heavy metal*" OR "trace metal*" OR arsenic OR lead OR cadmium OR chromium) AND (river OR "surface water") AND Bangladesh`. If you can't reconstruct it honestly, relabel the work a "non-systematic compilation" and drop "systematic" and "comprehensive."

**7. Supplement S1.** One table of the 28 studies: citation, river(s), year(s), records, value type, fraction, method, DL. Add k (number of studies) per metal to Table 1.

**8. Non-detects.** Flag each one. Don't count "<DL where DL exceeds the guideline" as an exceedance or a compliance. Treat it as undetermined and report how many there are per metal. For summaries, run DL/2 and DL substitution as bounds.

---

## Phase 2: One script produces every number (M1)

Write a `results.json` from the analysis, then generate LaTeX macros from it. Letters only in macro names (LaTeX rejects digits and underscores):

```python
import json, re
R = json.load(open("results.json"))   # e.g. {"ReachPctLen25": "88.1", ...}
with open("results_macros.tex", "w") as f:
    for k, v in R.items():
        assert re.fullmatch(r"[A-Za-z]+", k), k
        f.write(f"\\newcommand{{\\{k}}}{{{v}}}\n")
```

Use `\ReachPctLen25`-style names spelled out (`\ReachPctLenTwentyFive`). In the Abstract, Highlights, text and Conclusions write `\ReachPctLen`, never a typed number. Compute percentages by length and by count under different names so the two can't be confused. Add a CI check that greps the `.tex` files for digits typed outside macros in the Abstract and Highlights.

Also commit a **pre-analysis plan** in the repo before you re-run anything: panels, tests, direction, corrections, sensitivity sets.

---

## Phase 3: Analyses

### HPI (M2, M3)

Fix the panel and show sensitivity:

```python
WHO = {"As":.010,"Cd":.003,"Cr":.050,"Cu":2.0,"Ni":.070,"Pb":.010,"Zn":3.0}
def hpi(r, panel):
    w = {m: 1/WHO[m] for m in panel}
    return sum(w[m]*100*r[m]/WHO[m] for m in panel) / sum(w.values())

panels = {"core4":["As","Cd","Cr","Pb"], "core5":["As","Cd","Cr","Ni","Pb"], "all7":list(WHO)}
wide = df.pivot_table(index="record_id", columns="metal", values="conc_mgL")
for name, p in panels.items():
    sub = wide.dropna(subset=p)
    sub[name] = sub.apply(lambda r: hpi(r, p), axis=1)
    # report n, median, IQR, share > 100, per river
```

- Pick the primary panel by balancing N against comparability, and report all three plus your current "≥3 metals" as a reference. Report Spearman correlation between panels.
- Add a **contribution plot**: the share of ΣWᵢQᵢ from each metal, per river. This replaces "driven by weights."
- **Labels:** define one threshold. HPI > 100 is the critical limit (Prasad & Bose); say so everywhere. Either drop the 100–200 and >200 tiers, or call them "this study's tiers" with no "standard" claim.
- **HEI/MI:** HEI and MI have the same formula, so keep only HEI, or keep both with explicitly different benchmarks and state that. Compute them on the same fixed panel. Report the HPI–HEI Spearman correlation, and add a sentence explaining the discordance: HPI up-weights Cd, Pb and As, HEI weights all metals equally. Delete "corroborating."
- **Small N:** for rivers with fewer than about 10 records, show points, not a rank. Add studies per river. Delete "reflecting lower industrial metal loadings."

### Exceedance with clustering (M5)

A study-level cluster bootstrap is simple and defensible:

```python
rng = np.random.default_rng(42)
def cluster_ci(d, B=5000):
    by = {s: g.exceed.to_numpy() for s, g in d.groupby("study_id")}
    studies = list(by)
    est = [np.concatenate([by[s] for s in rng.choice(studies, len(studies))]).mean()
           for _ in range(B)]
    return np.percentile(est, [2.5, 97.5])
```

Run it for every metal × benchmark × subset in one loop: all records; excluding Buriganga, Turag and Shitalakhya; leave-one-river-out; confirmed-dissolved only; individual-sample rows only. Add a study-weighted estimate and, optionally, a random-effects pooled proportion in R (`metafor::rma.glmm` with `measure="PLO"`, or `meta::metaprop`). Output one master table, and report k studies and the largest single-study share per metal.

Then rewrite the sensitivity text from the actual table: report WHO *and* BD results for all metals, with CIs. Fix the Wilson wording (it's the plain Wilson interval, no continuity correction). Replace "national exceedance" with "pooled literature-wide exceedance."

### Seasonal analysis (M6)

1. **Date audit.** Classify every record as dry, wet, pre-monsoon (Apr–May), source-labeled season only, or undated. Report counts per metal and per study. Where a study gives only "winter" or "monsoon," use its label and document the rule. Also run a four-season scheme (winter Dec–Feb, pre-monsoon Mar–May, monsoon Jun–Sep, post-monsoon Oct–Nov, or whichever scheme the source studies use), and cite it.

2. **Within-study contrasts** (the cleanest test of a seasonal effect):

```python
rows = []
for (s, riv, m), g in df.groupby(["study_id","river","metal"]):
    d, w = g[g.season=="dry"].logc, g[g.season=="wet"].logc
    if len(d) >= 3 and len(w) >= 3:
        rows.append((s, riv, m, d.mean()-w.mean(),
                     d.var(ddof=1)/len(d) + w.var(ddof=1)/len(w)))
# per metal: statsmodels.stats.meta_analysis.combine_effects(effect, variance,
#   method_re="iterated") -> pooled log10 ratio, CI, tau2, I2, k
```

If k is under about 5 for a metal, say it's underpowered and don't interpret it.

3. **Mixed model on all dated records:**
```python
smf.mixedlm("logc ~ C(season) + year", d, groups="study_id",
            vc_formula={"river": "0 + C(river)"}).fit(reml=True)
```
Holm-adjust across metals. For serious censored handling, use R `brms` with `cens()` (or `NADA2`).

4. **Effect sizes.** Report Hodges–Lehmann shifts or log-ratios with study-bootstrap CIs. Keep Mann–Whitney only as descriptive.

5. **Discharge.** Match each sampling date to the nearest BWDB/FFWC gauge and plot log C against log Q. If you can't get that, call it "seasonal contrast" throughout and stop saying "dilution": rename 3.3 and the "Significant Seasonal Dilution for Arsenic" bullet.

6. **Rewrite the mechanism paragraphs** as hypotheses. Model text for As: "Higher dry-season As is consistent with reduced dilution, but also with a larger groundwater-fed baseflow or irrigation-return component in this arsenic-enriched basin, tidal/sorption effects, and between-study differences; these data cannot discriminate among them." Model text for Pb and Ni: "No seasonal contrast was detected; given the pooled design, low power and possible particulate-bound fractions, this should not be interpreted as evidence for any mechanism." Delete "compensatory non-point source wash-off" from the Conclusions, and replace "orders of magnitude" with a cited BWDB/FFWC discharge ratio, or delete it.

7. Highlights version: "Dry-season As was ~1.7× wet-season (pooled records; Holm p = 0.027)."

### Spatial coverage (M7)

**Rename the claim first.** Use "coverage of compiled sampling sites," "unsampled reaches," and "published sampling sites," and drop "surveillance," "monitoring stations" and "prioritized." Add a Limitations sentence saying DoE/BWDB stations are excluded and the gap is relative to a 28-study compilation. (A real surveillance claim needs the DoE/BWDB station list, which can be a follow-up paper.)

1. **Site provenance table:** unique sites, share with source-reported GPS vs geocoded from maps or place names, and an uncertainty class (≤1 km, ≤5 km, >5 km). Add a sensitivity run where each site's location is perturbed or its coverage radius shrunk or extended by its uncertainty.

2. **Along-network distance** from the HydroRIVERS attributes. Build the graph on all segments, snap sites to the nearest segment, and report coverage on the major ones:

```python
G = nx.Graph()
L = riv.set_index("HYRIV_ID").LENGTH_KM
for r in riv.itertuples():
    if r.NEXT_DOWN != 0:
        G.add_edge(r.HYRIV_ID, r.NEXT_DOWN, weight=(L[r.HYRIV_ID]+L[r.NEXT_DOWN])/2)
cov = nx.multi_source_dijkstra_path_length(G, snapped_ids, cutoff=25, weight="weight")
major_len = riv[riv.major].LENGTH_KM
covered_len = major_len[riv[riv.major].HYRIV_ID.isin(cov)].sum()
```
Report both Haversine and network results at 10/25/50 km, with length percentages computed once, in the script.

3. **A map**, a must-have: Bangladesh boundary, major rivers colored covered/uncovered, sampling sites sized by records, and any candidates (`geopandas` plus `matplotlib`, `riv.plot(column="covered")`).

4. **Candidates.** Either move Table 4 to the supplement as "largest unsampled reaches," or define an objective. For example, an importance score per segment from population within a buffer (WorldPop), industrial clusters, proximity to observed hotspots and intake locations, then greedy maximum coverage:

```python
chosen, covered = [], set()
for _ in range(15):
    c = max(cands, key=lambda c: sum(imp[s] for s in cover[c] - covered))
    chosen.append(c); covered |= cover[c]
```
Greedy gives a (1−1/e) guarantee for this submodular coverage problem. Drop Q as a ranking criterion; it's modeled and noisy (it rises upstream along the Jamuna in your table).

5. **Labels.** Delete the hand-typed names. Generate them with a spatial join against upazila or district polygons (`gpd.sjoin_nearest`) so each label is traceable. Verify the four mismatches I flagged.

---

## Phase 4: Benchmarks and pathways (M8)

- **Benchmark table:** WHO drinking guideline, ECR drinking, plus one pathway-matched benchmark per pathway you actually discuss. For irrigation, use FAO (Ayers & Westcot) long-term limits: as I recall, As 0.10, Cd 0.01, Cr 0.10, Cu 0.20, Ni 0.20, Pb 5.0, Zn 2.0 mg/L, but verify against the source. For aquatic life, pick one framework and cite it; hardness-dependent criteria need hardness data, so if you lack it say so. If you can't add a benchmark for a pathway, cut that pathway from Section 4.2.
- **ECR:** get the gazette and cite the number, date and schedule. If you can't confirm 2023 values, cite ECR 1997 Schedule 3 and drop "2023" from the legend.
- **Treated intakes:** verify from DWASA/CWASA documentation which surface sources feed treatment plants (I believe Saidabad draws from the Shitalakhya). Then write a paragraph stating that raw-water metals matter for treatability while your records are not at intakes. Cite or delete "groundwater is the majority" and "boro rice is heavily irrigated with river water."
- Change the Fig. 1 legend from "Health Benchmark" to "WHO guideline value," since Zn isn't health-based.

---

## Phase 5: References, repository, text (M9 and minor)

**Reference audit.** Check each DOI against Crossref, then check the claim each citation supports:

```python
r = requests.get(f"https://api.crossref.org/works/{doi}", timeout=20).json()["message"]
print(r["title"][0], r["issued"]["date-parts"][0][0], r.get("volume"), r.get("page"))
```

Specific repairs:
- GBM population claim: cite a demographic or hydrology source, not Datta & Subramanian (sediments).
- Literature-clustering claim: support it with your own per-river record table, and drop Hossain (2021) as the sole support.
- Li & Zhang (2018): confirm it exists as cited; replace it with Bangladesh or GBM evidence for the two claims it carries.
- Add a Discussion paragraph comparing results with prior Bangladeshi syntheses and other river systems. Search properly and cite what you find.

**Repository.** Release on Zenodo (DOI). During review use an anonymized mirror (anonymous.4open.science) and remove the personal handle. Include `requirements.txt` or `environment.yml`, fixed seeds, and a `make all` that regenerates every table and figure.

**Limitations rewrite**, covering: record independence/clustering; record definition; non-detect handling; unspecified fraction (and the direction of bias: it inflates exceedance); fixed-panel HPI and small per-river N; 34–47% of records absent from seasonal tests; temporal heterogeneity; no pH/TSS/salinity covariates; compilation ≠ full literature; DoE/BWDB excluded. Delete the instrument list unless S1 supports it.

**Find-and-replace list:**

| Search for | Replace with |
|---|---|
| "systematic" (Abstract) | "compiled" (or keep only if the protocol is documented) |
| "national exceedance(s)" | "pooled literature-wide exceedance" |
| "comprehensive synthesis" | "compilation" |
| "seasonal dilution" (as a finding) | "seasonal contrast" |
| "confirms" (Highlights) | "indicates (pooled records)" |
| "geodesic distance routing" | "great-circle and along-network distance" |
| "published monitoring stations" | "published sampling sites" |
| "surveillance gaps / deployments" | "unsampled reaches" |
| "audited maximum" | delete |
| "with continuity adjustment" | "Wilson score interval" |
| "critical" (HPI) | one consistent definition |

Also: redesign the graphical abstract as a small workflow (compiled dataset, exceedance with the Dhaka vs rest contrast, As seasonal contrast, coverage map) instead of a copy of Fig. 1. Rewrite the Highlights last, from the macros, and put the hotspot caveat in one of them. Consider dropping "Dissolved and" from the title and defining the fraction in Methods.

---

## Done-when checklist

1. Every number in the Abstract, Highlights and text traces to `results.json`.
2. Audit log, S1 study table and site provenance table exist, and the dataset has a DOI tag.
3. HPI uses a fixed panel, with one threshold definition.
4. Table 1 has clustered CIs, studies per metal, and a full sensitivity table.
5. Seasonal analysis includes within-study or mixed-model results, excluded-record counts, and "contrast" wording.
6. There is a map and a network-based coverage figure; "surveillance" language is gone, or the DoE/BWDB analysis is added.
7. Every reference is verified against its claim.
8. The repository is anonymized, archived and reproducible.

Expect numbers to move once the audit and clustering are done. Write the analysis plan first so you don't pick the version of the result you prefer.

If you want, I can write any of these as ready-to-run files: the plausibility and audit scripts, the results-to-LaTeX pipeline, the fixed-panel HPI plus clustered-CI plus seasonal meta-analysis script, or the rewritten Limitations, Highlights and Discussion paragraphs.