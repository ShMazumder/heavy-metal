I'll start with the new headline claim (ECR 2023 Schedule 2, S.R.O. 53) and the reference entries I flagged last round that are still unchanged.

Two of the three "prior review" entries are now confirmed mismatched. Last, I'll spot-check some of the newly listed primary studies.

I've got what I need from searching. Last, I'll re-check the new arithmetic: the HKSJ intervals, the "78.3%" weight claim, the filtered-subset medians, and the Pb counts.

## Verdict: not ready for submission

This version answers many earlier requests: a PRISMA string and counts, a defined record granularity, HKSJ intervals, a Monte Carlo null, a dissolved-only run, and a clipped network. Several of those answers created larger problems than they solved, and the reference list now has a serious integrity problem.

The arithmetic mostly holds. Table 2 means and HQs, Table 4 percentages, season totals summing to 162, 125/146 = 85.6%, and HQmean = HEI/4 all check. The HPI algebra (Eq. 2–3) is also correct. The problems are in what is built on top of these numbers.

## 1. Reference integrity (fix before anything else)

I checked several entries against publisher or database records, and the details do not match:

| Cited as | What I found |
|---|---|
| Hoque, Rahman & Islam 2025, *Water* 17, 385, doi:10.3390/w17030385 | The matching 2007–2022 meta-analysis of Bangladeshi river metals is *Water* 2025, 17(5), 630, doi:10.3390/w17050630, with Ram Proshad and Abubakr Idris among the authors and a different title. |
| Bilal, Hassan, Iqbal & Wang 2023, ESPR 30, 45120–45138, doi:…25410-z | Bilal, Li, Iqbal, Mu, Tulcan and Ghufran, ESPR 30(40):91710–91728, doi:10.1007/s11356-023-28879-x. |
| Islam et al. 2018, IJERPH 15, 1967, called a "review" | By its own title it is a health-risk study of one river system. The 2018 IJERPH piece that fits your sentence is the critical review of heavy metal and metalloid pollution of soil, water and foods in Bangladesh. |
| Proshad, Kormoker & Islam 2020, *Toxin Rev.* 40, 852–865, doi:…1780615 | That DOI appears in another paper's reference list as Proshad, Islam, Tusher, Zhang, Khadka, Gao and Kundu, *Toxin Rev.* 40, 803 (2021). |
| Hossain, Tanjin, Rahman, Yu, Hasan & Islam 2021, *SN Appl. Sci.* 3, 509 | The DOI matches, but the paper is Hossain, Rahaman, Hasan, Uddin, Khatun and Shamsuddin, "Comparative seasonal assessment…" of the Buriganga and Turag. This is the study behind your P04 "33.0 → 0.33" correction. |
| Baki et al. 2020, *Environ. Geochem. Health* | I could not locate it in my searches. That is not proof it doesn't exist. |

I could not check Islam 2021, Khatun 2021 or Hasan 2024. I can't tell how these mismatches arose, but a reviewer will read them as fabricated. Regenerate every entry from Crossref DOIs, and have a person open each source.

The citations also fail on content:
- **Datta & Subramanian 1998:** it is a sediment-geochemistry paper. It does not support "screening index of treatment burden" (Intro), and it is not the source for the "over one billion tonnes/yr" sediment flux (§4.2).
- **Harvey et al. 2002:** it concerns aquifer arsenic mobilization, not arsenic return flow into rivers.
- **Chattogram WASA, "Haria", Mohara plant, "over 170 million":** all uncited. As far as I know Mohara is fed from the Halda, and the 2022 Census gives about 169.8 million. Verify both.

## 2. The compilation contradicts your coverage claim

The Water 2025 meta-analysis compiled 648 samples from 24 rivers, including the Teesta, Brahmaputra, Dhaleshwari, Bangshi, Halda and Naf, and used HPI, HEI and MI. Your list has 12 rivers. At least 15 of those 24 are absent, and your candidate stations GAP_STN_14 and 15 sit on the Brahmaputra.

I also found studies that appear to meet your criteria but are not among your 13 citations:
- Bhuyan et al. 2017 (Meghna River water and sediment).
- Bashar et al. 2023 (Buriganga, 210 water samples, 16 metals).
- Akbor et al. 2020 (Buriganga, 13 metals).

So "published literature covers 16.5% of river length" is a statement about your 12-study subset, not the literature. Recompute coverage after reconciling against these reviews, or retitle the section as coverage of compiled sites. The Intro also claims earlier compilations suffered shifting-panel inflation and ignored non-detects. Neither claim is cited to any specific paper.

## 3. The new ECR 2023 headline

ECR 2023 is real: S.R.O. 53/Law/2023 of 5 March 2023, which repealed the 1997 rules. The problem is how you use it.

- **Wrong schedule logic.** The rules' Schedule 2 sets standards for different kinds of water, including lead limits for different types of surface water. Your own reference title says "drinking water and inland surface water". The statutory comparator for river water is therefore the surface-water class, not the potable table. Raw river water has no duty to meet potable limits, so "violation", "non-compliance" and "compliance audit" are wrong.
- **Anachronism.** Most records predate March 2023.
- **Repackaging.** For Pb, Cd and Cr the ECR 2023 exceedance is identical to your WHO column. Only Ni (0.050) and Cu (1.5) are new thresholds.
- **Vocabulary.** "Surge" and "jumps" (Graphical Abstract A, Highlight 2) imply pollution rose. Only the benchmark moved.
- **Unverified numbers.** I could not confirm the specific values (Pb 0.010, Cd 0.003, Ni 0.050, Cu 1.5). Quote them from the gazette with schedule and serial numbers.
- **Uncited claim.** "Earlier literature relied on an obsolete baseline" has no citation.

Reduce this to one table column and one sentence, using the surface-water classes if you want a statutory comparison.

## 4. The dissolved-phase "refutation" is not a test

- **Same data, nearly.** The filtered subset is 131–139 of 162 records (81–86%), so it cannot differ much from the full set. Moving from 85.6% to 84.0% shows only that.
- **Identical medians.** The "dissolved medians" in §4.2 (Pb 0.0286, Cr 0.0710, Ni 0.0888) equal the full-sample medians in Table 1 to three figures for all three metals. A real 131-record subset would not do that, so check that Table 1 was not reused.
- **Wrong concern.** The worry was detection limits and flame-AAS performance, not particulates. Stratify by instrument (ICP-MS and GF-AAS vs flame-AAS) and by DL relative to the guideline. If ICP-MS-only exceedance is still high, you have a real result.
- **Non-detects.** Only three non-detects are reported, while flame-AAS DLs go up to 0.050 mg/L. Report how many quantified values fall below their own study's DL, and whether "<DL" rows were dropped.
- **Missing outputs.** The [lo, hi] bounds and prediction intervals promised in Methods never appear. The random-effects pooled estimate is given for Pb only.
- **Overclaim.** "Refutes" is not defensible here.

## 5. Seasonal results: stories built on noise

- **Nothing is significant.** The HKSJ intervals include 1 for all seven metals (Pb [0.56–2.95], Cu [0.04–6.53]).
- **No Simpson's paradox.** The pooled Pb ratio (0.88) lies inside the within-study Pb interval, and so does the Ni ratio (0.73 inside [0.35–2.86]). The two estimates are indistinguishable. The explanation ("wet-season studies were concentrated in contaminated corridors") needs a study × season × river table. Korotoa is also not your most contaminated river.
- **Copper story.** "Wet-season Cu surge from copper oxychloride and antifouling paint" has no data or citation behind it.
- **Conclusions contradict Table 3.** "Consistent dry-season concentration across trace metals" is contradicted by Cu 0.54 and Ni 1.00.
- **Numbers moved.** Compared with the previous submission, Cu within-study went from 1.08 to 0.54, Ni from 1.14 to 1.00, and Cd from 1.21 to 1.41. The Pb DL interval became 2.6× wider (log₁₀ width 0.172 → 0.444) with the same *k* and unchanged pooled columns. Explain which run is right.
- **HKSJ implementation.** In all seven rows the HKSJ interval equals the DL interval scaled by exactly t/z, to rounding. That is what plain t-substitution gives. HKSJ also rescales the variance by Q/(k−1), so check the code (e.g. `metafor::rma(test="knha")`).
- **The "tripartite arsenic" paradox.** Some dry- and wet-season medians falling below the pooled median is arithmetic once a third, higher stratum exists. It is not a paradox. It rests on pooled medians, the estimator you dismiss as confounded two paragraphs earlier. There is no test, CI or within-study estimate for the pre-monsoon contrast.
- **Contradictory baseflow.** Methods call Nov–Feb "minimum baseflow", while §3.3 and §4.4 call Mar–May the annual minimum.
- **Season counts.** Mar–May moved from 48 to 41 and unclassified from 13 to 20, with the excluded total fixed at 61. The 41 equals the arsenic-specific count (57 + 23 + 41 = 121 of 122). So Methods may be mixing a metal-specific count into the all-record partition.
- **Mechanism as fact.** Boro-irrigation return flow producing a 30 µg/L median river As is asserted, with Harvey 2002 cited for it. It is the title of Graphical Abstract panel C. Show which studies supply the 41 records before invoking a mechanism.

## 6. The HPI critique is right, but mislabelled in the headline

- **Weights vs score.** The 60.2/18.1/18.1/3.6% are linear weight shares (1/S ÷ Σ1/S), not score shares. Graphical Abstract B labels the pie "Cd + Pb command 78.3% of score", and the Abstract and Highlight attribute it to quadratic scaling. At your own Table 1 medians, M/S² gives Cd 40%, Pb 37%, As 20%, Cr 4%. That matches your §3.2 contributions (41.3/35.8/19.9/3.0), not 60.2%.
- **"One million".** That ratio holds only at equal concentrations. At the Table 1 medians the Cd:Zn numerator ratio is about 7,000.
- **Contradiction.** §3.2 still says the panel result "proves… prior literature variations were driven entirely by geographic differences". §2.3 and §4.3 say it is an algebraic artifact. The "widespread misconception" in §4.3 is uncited.
- **Positioning.** The 1/S² property is an observation, so present it as a short note rather than a headline.

## 7. Spatial: the old flaws persist

- **Impossible p.** With 1,000 simulations the smallest attainable p is about 0.001, so "p < 0.0001" cannot be true.
- **Independence.** Your 23 coordinates sit in roughly 9–11 study areas, yet the null places 23 independent random reaches. Using your own null (38.1% at 23 sites, about 2.1% per site), about 9 independent sites give about 17%, which is what you observe. The "significant clustering" may be only study-level clustering.
- **Untested explanation.** "Proving… capital-adjacent industrial centers and accessible ports" is untested.
- **Table 5.** It is byte-identical to the previous version even though the network was re-clipped and re-run. The "prioritized surveillance" wording is back in the Fig. 3 legend, the title and the Conclusions.
- **Map and Methods.** The Fig. 3 title says "Heavy Metal" sites, but the legend says "Water Quality" sites. There is still no marker near Barishal for the Kirtankhola (30 Core-4 records, k = 1), and none at Sylhet for the Surma. Supplementary S2 is used for two different things. I believe HydroRIVERS derives from the 15-arcsecond HydroSHEDS layer, not 3-arcsecond; check the documentation.

## 8. Dataset accounting and reproducibility

- **PRISMA arithmetic.** 74 full texts → "28 meeting criteria", yet 11 are sediment-only and 5 are physicochemical-only, which fail your criterion (ii) as written. There is no flow diagram or exclusion reasons. You cite 13 papers for "exactly 12 studies".
- **"100% concordance".** On 41 records the 95% upper bound on the discordance rate is 8.6%. A second extraction done after the first audit is also not independent.
- **Unexplained changes.** Pb Dhaka N went from 31 to 37 and non-urban N from 115 to 109, while the percentages (82.6%, 18.3%) stayed identical to 0.1 point. Non-urban Cr changed (47.8% → 53.0%) and Ni (43.1% → 32.2%) was dropped, all without explanation.
- **Unseeded bootstrap.** The Pb WHO lower bound has been 70.6, 70.5 and 71.1% across three submissions for the same data.
- **Sensitivity table.** The full sensitivity table (all metals, N, *k*, CI) is still missing.

## 9. Scope and language

- **Aims vs results.** The aims still list the old four objectives, while the title and headlines are now regulatory discordance, HPI algebra and a seasonal arsenic peak.
- **Absolute verbs.** "Proves", "proving", "refutes" and "confirms" appear about eight times. "Hyper-polluted" is added.
- **Highlight 4.** It reports an estimate (Pb 1.28×) whose interval is 0.56–2.95.

## Minimum path to a submittable paper

1. Rebuild the reference list from Crossref and verify each claim-to-source link.
2. Reconcile your study list against the Water 2025 and ESPR 2023 reviews, and add the missing studies, or retitle and rescope the coverage claims.
3. Replace "compliance/violation" with benchmark exceedance, and use the ECR 2023 surface-water classes if you want a statutory comparison.
4. Stratify by instrument and DL and report [lo, hi], replacing the "refutation" with that analysis.
5. Rerun the seasonal analysis with seeded, documented code. Remove the causal stories, or add data that support them.
6. Fix the HPI shares in the Abstract, Highlights and Graphical Abstract, and delete the "prior literature… entirely geographic" sentence.
7. Redo the spatial null with study-level units and p ≥ 0.001, regenerate Table 5, and drop "prioritized/surveillance".

Items 1 and 2 decide whether this paper survives an editor's first read. I couldn't open your supplements or the repository, and my reference checks are spot-checks, not exhaustive.

I can also make this a doc you can edit here, share, or download as Word or PDF, if you'd like.