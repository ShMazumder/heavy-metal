I'll start by reading the two review files, since only the manuscript PDF came through in my context.

I've read both reviews. Next I'll check the revised manuscript's numbers and figures myself instead of taking them on trust.

The legend does cover the upper confidence cap on the headline Pb bar. Now the external fact checks.

That settles the Saidabad claim. Next I'm checking the two citations that earlier reviewers flagged as load-bearing.

The Chowdhury and Ward entry is wrong on year, volume, pages and DOI. Now the other citation that carries two arguments.

I couldn't locate Li and Zhang 2018 as cited. One more check on novelty, since neither reviewer got a response on prior syntheses.

I'll check the Highlights lengths against Elsevier's limit before writing it up.

## Verdict: not ready for submission

This is a better manuscript than the Round 2 version. The statistics are cleaner and the writing is calmer. But the data foundation is still unverifiable, and the revision introduced new errors, including a factual one and a wrong citation. At a journal like Chemosphere I would expect rejection, or major revision at best.

I recomputed what I could from the PDF. The arithmetic is clean: Table 1 percentages, the Pb Wilson CIs, all seven Mann–Whitney p-values from the reported U and n, the Holm adjustments, Table 2's weighted mean HPI and 66/112 above 100, Table 4's percentages, and 162+106 = 268. The problems are design, provenance and framing, not arithmetic.

## What improved

- **Benchmarks:** FAO irrigation values are now included.
- **Intervals and tests:** cluster-bootstrap CIs and a *k* column were added, and the seasonal tests are now two-sided with Holm correction.
- **HPI:** it now uses a fixed panel with panel sensitivity runs and a single threshold.
- **Mechanisms:** the seasonal explanations are hedged, with the geogenic-baseflow alternative added.
- **Spatial:** the headline numbers now agree between Abstract and Table 4, and a map and along-network analysis were added.
- **Other fixes:** Cr(VI) and Zn caveats, a limitations section, and an anonymized repository link.

## Still unresolved from Rounds 1 and 2

| Item | Status |
|---|---|
| Search string, dates, screening counts, PRISMA, study table | Not addressed. Methods still say only "Boolean keywords". |
| Definition of "record" (sample vs site/season mean) | Not addressed |
| Non-detects and detection limits | Not addressed, only conceded in Limitations |
| Audit scope, number corrected, second extractor | Only two anecdotes |
| Full sensitivity table (all metals, N, *k*, CI) | Not addressed. It points to Table S2, which isn't in the PDF. |
| Graphical abstract | Still a copy of Fig. 1, third round running |
| "Prioritized", "surveillance", "monitoring reach" wording | Still in §2.5, the Table 5 caption and the Fig. 3 legend |
| Highlights | Regressed: 6 bullets (limit 3–5), and three exceed 85 characters (101, 100, 123) |
| Citations and prior literature | Not addressed, and new errors added (below) |

## Major problems

**1. The dataset description contradicts itself.**
- **Study count:** both earlier reviews describe a 28-study compilation. This version has 17 investigations (12 with metals), yet §2.4 still lists study IDs up to P28. The disappearance of about 11 studies is never explained.
- **Inclusion criteria:** criterion (ii) requires reported elemental concentrations, but 106 of the 268 records come from studies that report only pH, EC, DO and similar. The Abstract and Conclusions say 268 observations were screened against metal benchmarks, when only 162 could be.
- **Season counts:** the season partition (111/62/81/14) is also on all 268 records, not the 162 that were tested.
- **A filtered subset:** a 2025 review quotes Buriganga surface-water Cr up to about 167 mg/L (reaching up to 167,160 μg/L), while your compiled Cr maximum is 7.55 mg/L. So either the inclusion filter or your audit is doing a lot of undocumented work. Anyone in the field will also know that 12 river-metal studies over 2010–2024 is a small slice of the literature.
- **Undefined "record":** Kirtankhola (N = 30 from one study) and Korotoa (N = 40 from two) look like station × season means. If so, "% of records exceeding" describes study design, not water.
- **Audit scope:** a 100× error and a 1000× error were found in 2 of 12 studies, so the residual error rate is not zero. Methods still give no count of corrections and no second-extractor agreement. Describing your own data-entry slips ("reduced total compilation Pb mass by 56%", "spurious index blowouts") in Methods is out of place. A sum of concentrations is not a "mass".

**2. The concentrations look implausible for dissolved metals, and non-detects are unhandled.**
- **Reported medians:** Pb is about 29 µg/L, Cr 71, Ni 89, Cu 89, Cd 2.8 and As 15 µg/L.
- **Global comparison:** from memory (please check against Gaillardet et al. 2014), global-river dissolved averages for these metals are roughly 0.1–2 µg/L.
- **Detection limits:** typical flame-AAS detection limits run from about 1 to 50 µg/L depending on element and method, which brackets the WHO Pb and Cd guideline values.
- **Consequence:** the 85.6% Pb exceedance can't be interpreted until every record carries its detection limit and a non-detect flag. §4.4 admits studies "frequently reported zero or omitted substitution rules".
- **Rule to adopt:** a non-detect whose DL is above the guideline should count as undetermined, not as compliant or exceeding.
- **Fraction argument:** the stated direction of bias for unspecified fractions is one-sided. Guidelines apply to water as consumed, so filtered data would bias exceedance downward.
- **§4.3 tension:** it says Pb is "predominantly particulate-bound" (uncited), yet 10 of 12 studies filtered and still give a dissolved-Pb median of 29 µg/L.

**3. The sensitivity analysis is selective, and your own numbers contradict the message.**
- **Framing:** the Abstract and Highlights say excluding Dhaka rivers "confirms" strong hotspot clustering. The evidence quoted is the BD-standard drop for Pb (34.9→18.3%) and As (18.0→8.9%).
- **What §3.1 shows:** WHO Pb falls only from 85.6% to 82.6%, Cr from 60.6% to 47.8% and Ni from 54.8% to 43.1%. At the WHO level the result barely depends on Dhaka. That either means broad contamination or points back to problem 2.
- **Missing detail:** N, *k* and CIs for the non-urban subsets are not given. My inference from the percentages is about 115 non-urban Pb records, so about 31 Dhaka records, of which about 30 exceed the BD standard.
- **Table 1:** the header promises Wilson and cluster CIs per cell, but only the Pb row has Wilson intervals. "[0.0–0.0%]" for 0/146 and 0/79 is invalid (Wilson upper bounds are about 2.6% and 4.6%).
- **Few clusters:** percentile cluster bootstrap with 6–12 clusters under-covers. As (WHO) spans 18–85%, which says the pooled figure is not a meaningful single number. Show per-study proportions (a forest plot) and a random-effects estimate with a prediction interval, as both reviewers asked.

**4. The HPI/HEI section has structural problems.**
- **Coverage:** Core-4 (N = 112) comes from 5 rivers and 7 studies (Table 2). Turag and Shitalakhya, two of the three "Dhaka hotspot" rivers, have no Core-4 record, nor do Padma, Meghna, Surma, Paira or Old Brahmaputra. The Highlights omit this. Buriganga's median HPI of 1,977 is a single study (*k* = 1, N = 15). The pooled median is weighted by how many rows each river contributed.
- **Panel comparison:** Core-4 → Core-5 → All-7 uses different record subsets (112 → 62 → 35). The rise from 58.9% to 74.2% to 85.7% above 100 confounds panel with sample. Recompute Core-4 on the 62 and 35 subsets.
- **HEI "low risk":** HEI is a sum. On four metals, HEI < 10 allows a mean hazard quotient up to 2.5. A median HEI of 7.94 means the average metal is about twice its guideline, not "low risk". The "HPI vs HEI discordance" in §3.2 is therefore a threshold artefact, not evidence of HPI's weighting. Korotoa's 10.20 is also not "< 10".
- **Spearman correlation:** ρ = 0.976 (p < 10⁻¹⁵) between two indices built from the same four inputs, on pseudo-replicated rows, is close to trivial.
- **Possible copy error:** the Karnaphuli median HEI (7.94) equals the all-records median exactly. Check it.
- **Review history in the text:** §3.2 refers to "the 5,920 blowout in earlier reports" and "earlier index inflation". That is your own Round 2 version. Delete it.
- **Qi definition:** Mohan and Prasad–Bose define Qi with an ideal value Iᵢ. You use Mᵢ/Sᵢ × 100 (Iᵢ = 0) without saying so.
- **Reporting:** give Q1–Q3 instead of an IQR width, and drop the five-significant-figure medians (156.99).

**5. The seasonal analysis is over-interpreted.**
- **Test floor:** with *k* = 4 pairs, the smallest possible exact two-sided Wilcoxon p is 0.125. "Lacks power" is guaranteed by design. Yet L225–226 infers from the null that the pooled contrast reflects between-study composition. You can't claim both.
- **Direction:** all seven within-study ratios exceed 1 (1.06–1.25), and Pb (1.25×) is higher than As (1.21×). Saying Pb shows "no contrast across either framework" is unwarranted. A pooled random-effects log-ratio, as Round 2 asked, would handle this. A rank test on four points does not.
- **Headline p-value:** As padj = 0.0273 comes from an unclustered Mann–Whitney test, the kind you criticize elsewhere. With about 9 studies and dry and wet records likely from different ones, effective n is nearer the study count. Demote it from the Abstract and Highlights.
- **Opposite directions:** for Ni and Pb the U statistics sit above their null means (dry stochastically larger) while the ratios of medians are below 1. The ratio of medians is an unstable effect size, so report Hodges–Lehmann shifts.
- **Season definitions:** the Introduction says dry is Nov–Mar. Methods say Dec–Feb and call it "minimum baseflow". Mar–May is excluded as "pre-monsoon", yet the lowest Ganges/Padma flows typically fall in Mar–May. Please verify against BWDB/FFWC. If so, the "dilution" framing compares winter with monsoon, not low flow with high flow.
- **Dropped records:** 34–47% of records per metal are still excluded, unchanged since Round 2.
- **Unexplained pairing:** §2.4 lists ten studies with paired designs, but *k*_pair is only 3–5, even for Cr, which all 12 metal studies report.

**6. The spatial result is mostly arithmetic, and the figure is suspect.**
- **Site count and radius:** I count roughly 20 site markers in Fig. 3. Twenty 25-km discs cover at most about 39,000 km², roughly a quarter of the country, so a gap of 74% or more is expected from any ~20-site dataset. Nothing justifies 25 km hydrologically. The 88% figure measures the size of your compilation, not a gap in the literature. A single missed Jamuna or Teesta study would falsify a "no records" statement.
- **Border clip:** Fig. 3 draws many red river segments outside the Bangladesh outline (India), while §2.5 says "strictly within Bangladesh borders". Either the plot isn't the analysed network, or the clip failed and 8,369.5 km is inflated.
- **Site provenance:** the largest marker sits in the Meghna estuary south of Bhola (~90.65°E, 22.1°N), and I see no marker at Barishal on the Kirtankhola. Confirm the geocoding. The site provenance table requested in Round 2 is still missing.
- **Network method:** it doesn't say whether the graph is directed, how stations were snapped, or whether the filter is "and" or "or".
- **Site source:** Fig. 3 and Table 4 describe "water quality" sites, which seem to come from all 17 studies, while the Abstract speaks of "heavy metal records". State which.
- **Table 5:** it is still ranked by catchment area alone, then thinned to about 30-km spacing. That makes it a chain of points up the Meghna → Padma → Ganges → Jamuna → Brahmaputra, with nothing on contamination, population, intakes or the small industrial rivers in Table 2. Methods claim "catchment area and reach length", but only area appears. "Gazetteer-verified" has no method, and the labels are hand-typed. Move Table 5 to the supplement, or define an objective.

**7. Factual errors and citations.**
- **Saidabad:** §4.2 says Saidabad WTP (Phases I–III) draws from the Shitalakhya and Padma. The existing Saidabad plants take raw water from the Shitalakhya (Sitalakhya), and Phase III is intended to switch the source away from the polluted Sitalakhya. Padma water goes to a separate plant, the Padma–Jashaldia treatment plant, inaugurated in June 2019. The paragraph is also uncited.
- **Chowdhury & Ward:** you cite it as 2007, vol. 27, pp. 2009–2022, doi:10.1002/joc.1504. The paper I find is 2004, International Journal of Climatology 24(12), 1495–1508, doi:10.1002/joc.1076. It analyses rainfall and streamflow variability linked to climate patterns, so it can't support "170 million people" depending on the rivers.
- **Li & Zhang (2018):** I could not locate it under the cited title and venue. Round 2 flagged it too, and it carries two load-bearing claims. Verify it on Crossref (I couldn't run that check here).
- **Prior syntheses, no differentiation:** these are not cited:
  - A critical review of heavy metal and metalloid pollution of soil, water and foods in Bangladesh (2018).
  - A systematic review and meta-analysis of surface water quality in Bangladesh over two decades, which reports that most rivers exceed WHO limits for Zn, Cu, Pb, Cd, Ni, As and Cr.
  - A 2025 *Water* paper, a meta-analysis of metal(oid)s in Bangladeshi river surface water over 2007–2022 using HPI, MI and PCA. This overlaps your HPI/MI component directly.
  
  Without a positioning paragraph, the first reviewer question will be "what is new?", and items 1 and 6 weaken the honest answer.
- **ECR:** "1997/2023" remains ambiguous. The listed values match the 1997 schedule, and the 2023 reference is a generic "Technical Report".

## Presentation and compliance

- The Abstract has doubled brackets four times ("[[32.3–82.9%]]"), and the Highlights have "([70.6–94.1%])".
- In Fig. 1 and the graphical abstract, the legend covers the upper CI cap (94.1%) of the headline Pb bar.
- "Confirming" is used about five times for things the data don't confirm.
- Elsevier requires a generative-AI use disclosure if AI assisted the writing or analysis, so check the policy.

## Not verifiable from the PDF

Supplementary Tables S1 and S2, audit_log.csv, the repository (network access is off), the ECR 2023 gazette text, and whether the non-urban figures match S2.

## Minimum work before submitting

1. Freeze and document the dataset: a study table (S1) with value type, fraction, method and DL, a flag for each non-detect, the 28→17→12 reconciliation, and second-extractor agreement.
2. Rerun exceedance with the DL-aware rule. Add the full sensitivity table with N, *k* and CIs, plus a forest plot with random-effects pooling.
3. Fix HPI: same-subset panel comparison, an explicit statement that Core-4 covers 5 rivers, the HEI claim removed or re-thresholded, and the "earlier reports" language deleted.
4. Redo the seasonal analysis as a pooled within-study log-ratio or mixed model, demote the As p-value, and reconcile the season definitions.
5. Either cut Table 5 and "prioritized" language, or define an objective. Fix the border clip, add the site provenance table, and retitle the section as coverage of compiled sites.
6. Fix the three citations and the Saidabad statement, and add a prior-synthesis paragraph with a clear statement of novelty.
7. Fix the presentation items above.

If those hold up, this could be a modest, defensible descriptive synthesis. Even then, the novelty gap makes Chemosphere a stretch, and a regional or environmental-monitoring journal may fit better.

I can also make this a doc you can edit here, share, or download as Word or PDF, if you'd like.


The fixes depend on each other, so the order matters. Do the re-search and data audit first. Any change there moves every downstream number, and prose you edit before that point will need rewriting.

## Phase 0: Three decisions before touching anything

1. **Define "record."** Use one row per measurement, tagged `sample`, `site_mean` or `station×season_mean`. Analyze the types separately or drop the means. If you can't tell for a study, say so in the study table.
2. **Decide whether to re-run the literature search.** I recommend it. Your spatial claim ("no records on mainstem X") and your novelty claim both depend on completeness. If you can't re-search, relabel the work a "non-exhaustive compilation of N studies" and delete every "lacks published records" statement.
3. **Choose the spatial scope.** Either a descriptive coverage analysis of compiled sites (my recommendation), or a real monitoring-design paper with DoE/BWDB stations as a separate follow-up.

## Phase 1: Rebuild the data foundation (problems 1 and 2)

**Search and study table**
- Re-run the search and record the string, databases, date, counts at each screening stage, and reasons for exclusion. Start from `("heavy metal*" OR "trace metal*" OR arsenic OR lead OR cadmium OR chromium OR nickel) AND (river OR "surface water") AND Bangladesh`. Add BanglaJOL, and chase citations both ways.
- Seed the search from the three prior syntheses I found (the 2018 IJERPH review, the Bilal meta-analysis, the 2025 *Water* meta-analysis). Check their study lists against yours. Every study they include that you don't needs a documented exclusion reason.
- Reconcile 28 → 17 → 12 in a table that lists each dropped study and why.
- Keep the five physicochemical-only studies out of every metal count. If they feed the spatial analysis, say that explicitly, or drop them.
- Build Supplement S1: study, river, years, records, value type, fraction, method, DL, QA/QC reported, coordinates source.

**Audit**
- Re-verify all 162 metal records against the source tables, not just extremes. Twelve studies is feasible.
- Have a second person re-extract a random 25% and report agreement.
- Generate the audit log by diffing your dataset versions, then add `reason` (unit scale / transcription / season / duplicate) and `verifier` by hand. Report the totals in Methods.
- Move the P04 and P27 anecdotes into the audit table. Methods should read "X records corrected: a unit scale, b transcription".
- Run plausibility flags on every record: above the 99th percentile on the log scale, ≥100× the study's own median, exact-round values (Ni = 0.1000, Zn = 0.5000), and identical value vectors in two studies (double-counting).

**Non-detects and fraction**
- Add `dl_mgL` and `nd_flag` per record. Where a paper gives no DL, record "unknown" instead of guessing.
- Replace the single exceedance rate with a **bounded** one:

```python
lo = (~df.nd) & (df.conc > g)        # certain exceedances
undet = df.nd & (df.dl > g)          # DL above guideline: can't tell
hi = lo | undet
print(lo.mean(), hi.mean())          # report [lo, hi], also per study
```

- Report the share of undetermined records per metal. If Pb's interval is wide, that is your honest headline.
- Run the headline analyses on confirmed-0.45 µm records only.
- Rewrite the fraction paragraph to say that guidelines apply to water as consumed, so filtered data bias exceedance down and unfiltered data bias it up.
- Add a plausibility paragraph comparing your medians with global dissolved-metal baselines, cited properly. Say what your data show and don't hide the gap. Cut the uncited "Pb is predominantly particulate" sentence, or cite it and reconcile it with the filtered data.

## Phase 2: One script produces every number

Regenerate every figure in the Abstract, Highlights, text and Conclusions from a `results.json` fed into LaTeX macros. The Round 2 snippet still applies. After Phase 1 your numbers will move, and this is what stops a repeat of the stale-number problem.

## Phase 3: Analyses (problems 3, 4, 5)

**Exceedance**
- Build one master table: metal × benchmark × subset (all, non-Dhaka, leave-one-river-out, leave-one-study-out, confirmed-dissolved). Give N, *k*, estimate and CI in every cell. Zero cells get a Wilson or Clopper–Pearson upper bound (about 2.6% for 0/146), never [0–0].
- Add per-study proportions as a forest plot and a random-effects pooled estimate with a prediction interval:

```r
d <- escalc(measure="PLO", xi=n_exceed, ni=n_rec, data=studies)
m <- rma(yi, vi, data=d, method="REML")
predict(m, transf=transf.ilogit)   # pooled proportion, CI and prediction interval
```

- Keep the cluster bootstrap only as a sensitivity check. With 6–12 clusters it under-covers.
- Rewrite the Dhaka finding to match the data: "At the BD-standard level, exceedance falls by about half without Dhaka rivers. At the WHO level it remains high (Pb 82.6%), so the result is not driven by Dhaka alone, and its interpretation depends on detection-limit handling." Delete "confirming."

**HPI/HEI**
- Say in the Abstract and Highlights that Core-4 covers 5 rivers and 7 studies.
- Compute all three panels on the same rows (the N = 35 subset) so the panels are comparable. Report the larger-N Core-4 separately.
- Drop the pooled "all records" median, or weight it by study. Show per-river points rather than ranks where N < 10.
- For HEI, report the mean hazard quotient (HEI/n), which is interpretable: HEI 7.94 on four metals means about 2× the guideline. Delete the "HPI over-classifies" discordance claim. If you keep a classification, use thresholds scaled to the number of metals and cite that choice.
- State Iᵢ = 0 in the Qᵢ definition. Report Q1–Q3, round medians to 2–3 significant figures, check the Karnaphuli 7.94 duplicate, and delete "earlier reports" and "earlier index inflation" from §3.2.

**Seasonal**
- Drop the Wilcoxon test on four pairs. Compute per study × river × metal log₁₀(dry/wet), require at least 3 samples per season, and pool by random effects (as in the Round 2 snippet). Report the pooled ratio, CI, τ² and *k*. If *k* is below about 5, say "underpowered, not interpreted".
- Run a mixed model (`logc ~ season + year`, random study and river) as the secondary analysis. Holm-adjust across metals.
- Demote the pooled As p-value to a descriptive statement. The Abstract and Highlights should lead with the within-study result and its direction.
- Report the consistent sign across all seven metals as a descriptive pattern, without a test.
- Resolve the definitions: use the source label where given, document the rule, and align the Introduction with Methods. Add a sensitivity run with dry = Dec–May (check BWDB/FFWC for the actual minimum-flow months).
- Report how many records were excluded and why. Explain why *k*_pair is 3–5 when ten studies are listed. If you can get BWDB gauge data, plot log C against log Q. If not, say "seasonal contrast", never "dilution".

## Phase 4: Spatial (problem 6)

- **Border clip:** clip the network to the Bangladesh polygon, assert that every geometry lies inside, and draw Fig. 3 from the same GeoDataFrame used in the analysis. That removes any mismatch between figure and numbers.
- **Site provenance:** build a table of unique sites with the share from source GPS versus geocoded, an uncertainty class (≤1 km / ≤5 km / >5 km), and a re-run with each site's radius widened or shrunk by its uncertainty. Check the Kirtankhola and Bhola-estuary points specifically.
- **Method details:** state directed or undirected, the snapping tolerance, and whether the filter is Strahler "and" or "or" discharge.
- **Null model:** compare observed coverage against the coverage of the same number of randomly placed sites:

```python
obs = covered_km(sites, 25)
null = [covered_km(random_points(major_reaches, n=len(sites)), 25) for _ in range(1000)]
# also draw nulls restricted to the regions the real sites sit in
```

- Report whether your sites are more clustered than random. That is the real finding, and it replaces "88% lacks records".
- **Radius:** justify it with 10/25/50 km sensitivity and a stated rationale, such as travel time or a typical dilution scale.
- **Candidates:** either move Table 5 to the supplement as "largest unsampled reaches", or define an importance score (WorldPop population within a buffer, industrial clusters, observed hotspots, intake locations) and select by greedy maximum coverage. Use a spatial join against upazila polygons to generate the labels, so each is traceable.
- **Terminology:** remove "prioritized", "surveillance" and "monitoring reach" from §2.5, Table 5 and the Fig. 3 legend.
- **Site source:** say which studies' sites are plotted.

## Phase 5: Literature and factual fixes (problem 7)

- **Saidabad:** correct §4.2 to say Saidabad I–II draw from the Shitalakhya, Phase III is designed to take Meghna water, and Padma water is treated at the Padma–Jashaldia plant. Cite DWASA or lender documents. Tie it to your data: Shitalakhya has no Core-4 records.
- **Chowdhury & Ward:** replace with the correct 2004 entry for the hydrology claim, and cite a demographic source for "170 million people".
- **References:** check every DOI on Crossref, and check that each citation supports its claim. Replace Li & Zhang with Bangladesh or GBM evidence if you can't verify it.
- **ECR:** obtain the gazette. If you can't confirm the 2023 values, cite ECR 1997 Schedule 3 and drop "2023".
- **Novelty paragraph:** add one that names the three prior syntheses and states precisely what you add, such as clustering-aware exceedance, a documented audit and a coverage analysis. Compare your findings with them. If the 2025 meta-analysis reports MI and HPI for the same rivers, say how yours differ.

## Phase 6: Presentation

- **Abstract:** fix the doubled brackets and replace every "confirming" with "indicates" or "is consistent with".
- **Highlights:** write 3–5 bullets of 85 characters or fewer, last, from the final macros. For example:
  - "Pb exceeds WHO limit in X% of records; DL handling widens this to [a–b]%"
  - "Excluding Dhaka rivers lowers BD-standard, but not WHO-level, exceedance"
  - "Within-study dry/wet ratios exceed 1 for all seven metals (k = x)"
  - "Compiled sampling sites cover Y% of major river length, near random expectation"
- **Graphical abstract:** redesign it as a four-box workflow (compiled studies → exceedance with and without Dhaka → seasonal contrast → coverage map), not Fig. 1.
- **Fig. 1:** move the legend outside the axes (`bbox_to_anchor`) and set ylim to about 105, so the Pb error bar is visible.
- **Repository and journal rules:** deposit data and code on Zenodo with a DOI (keep the anonymized mirror for review), and add software versions and seeds. Check Elsevier's generative-AI disclosure requirement.

## If time is short

Cut in this order: Table 5 and "prioritized" language, river-level HPI ranking, the seasonal p-value headline, and the spatial "gap" framing (replace it with the null-model result). Protect the audit, DL handling, the full sensitivity table and the citation fixes, because those are what a reviewer will check first.

I can write any of these as runnable files: the audit and plausibility scripts, the DL-bounded exceedance table, the random-effects and mixed-model seasonal script, the same-subset HPI code, or the coverage null model. Once your numbers are frozen I can also rewrite the Abstract, Highlights and Limitations to match. Tell me which you'd like first.