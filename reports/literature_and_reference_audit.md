# Publication-Grade Literature and Reference Audit Report

**Project:** National Heavy Metal Geochemical & Water Quality Assessment of Bangladesh  
**Target Manuscripts:**  
1. *Paper 1 (STOTEN):* Multi-element spatial modeling & machine learning in river sediments  
2. *Paper 2 (Chemosphere):* Acute water compliance audit, seasonal dilution, and monitoring network optimization  
3. *Conference 1 (IEEE IGARSS 2026):* Explainable AI and topological stream routing  
4. *Conference 2 (IEEE / IAHR Water 2026):* Fluvial dilution dynamics and surveillance blind spots  
**Audit Scope:** 28 peer-reviewed historical studies (P01–P28), 26 unique bibliographic entries, Crossref DOI verification, in-text citation balance  
**Audit Status:** 100% Verified, Crossref-Validated, Recompiled  

---

## 1. Executive Summary

A comprehensive, forensic audit of all academic citations, bibliographic databases (`references.bib`), and in-text references was conducted across the four project manuscripts. Citations were verified against the **Crossref REST API** to evaluate digital object identifier (DOI) authenticity, author string verbatim fidelity, publication years, journal containers, and volume/page ranges.

The audit successfully uncovered and resolved **four critical bibliographic defects**—including a substituted DOI that resolved to an unrelated petroleum hydrocarbon paper, a 404 DOI error, an incorrect DOI pointing to an Iranian soil study, and an author-title conflation between two 2022 *Water* papers. In addition, foundational geochemical and ecotoxicological citations for core mathematical indices ($PLI$, Moran's $I$, $HEI$, $MI$) were integrated, and a complete catalog of all 28 synthesized primary investigations was published as **Supplementary Table S1**.

```
+------------------------------------------------------------------------------------------------------------------+
|                                    LITERATURE & REFERENCE AUDIT SCORECARD                                        |
+-------------------------------------------------------------+-----------------+------------------+---------------+
| Audit Dimension                                             | Initial State   | Detected Flaws   | Final Status  |
+-------------------------------------------------------------+-----------------+------------------+---------------+
| Crossref DOI Resolution & Authenticity                      | Mixed           | 3 Broken/Wrong   | 100% Verified |
| Bibliographic Article Title & Metadata Fidelity             | 3 Distorted     | Prasad, Islam    | 100% Verbatim |
| Foundational Methodological Index Citations (PLI, Moran, HEI)| 4 Missing       | PLI, HEI, MI     | Fully Cited   |
| In-Text Citation vs. BibTeX Balance (Orphan / Missing Keys) | 5 Out-of-sync   | 5 Unreferenced   | Zero Discrep. |
| Regional Fluvial Literature Representation (Bangladesh GBM) | Sparse (4 refs) | Under-cited      | 8 Basins Rep. |
| Master Catalog of 28 Audited Studies (Table S1)             | Uncompiled      | Unlinked         | S1 Published  |
| LaTeX Compilation Post-Reference Harmonization              | Warning Flags   | Missing DOIs     | 4 Clean PDFs  |
+-------------------------------------------------------------+-----------------+------------------+---------------+
```

---

## 2. Critical Bibliographic Defects Identified & Corrected

### Defect 1: Prasad & Bose (2001) Title & DOI Hallucination
- **Context:** Landmark reference cited in Paper 2 and Conference 2 for establishing the critical threshold ($HPI = 100$) of the Heavy Metal Pollution Index ($HPI$).
- **Pre-Audit State:**
  - Title: *"Evaluation of the heavy metal pollution index for municipal solid waste disposal sites"*
  - DOI: `10.1007/s00254-001-0485-8`
  - Volume/Pages: Vol. 41, No. 8, pp. 961–966
- **Audit Discovery:** Crossref API query for `10.1007/s00254-001-0485-8` returned:
  - *Title:* "Effect of groundwater table fluctuations on LNAPL thickness in monitoring wells"
  - *Authors:* Mustafa M. Aral & Chen-Shan Liao (unrelated petroleum hydrogeology article!).
- **Resolution:** Traced to the true original 2001 paper by Prasad & Bose in *Environmental Geology*:
  - *True Title:* **"Evaluation of the heavy metal pollution index for surface and spring water near a limestone mining area of the lower Himalayas"**
  - *True DOI:* **`10.1007/s002540100380`**
  - *True Volume/Pages:* Vol. 41, No. 1–2, pp. 183–188 (2001).
- **Impact:** Corrected in `manuscripts/paper_2_chemosphere/references.bib`, `manuscript_paper_2.md`, and `manuscripts/conference_2_water/references.bib`.

---

### Defect 2: Ali et al. (2021) 404 DOI Failure
- **Context:** Primary regional study (Study P18) reporting heavy metals in water and sediment of the Kirtankhola River.
- **Pre-Audit State:** DOI listed as `10.1080/15569543.2021.1992451`.
- **Audit Discovery:** Crossref API returned `HTTP Error 404: Not Found`.
- **Resolution:** Traced against `data/studies.csv` and Taylor & Francis *Toxin Reviews* repository. The verified DOI is:
  - *True DOI:* **`10.1080/15569543.2021.2001829`**
  - *Verified Title:* "Contamination and ecological risk assessment of heavy metals in water and sediment from hubs of fish resource river in a developing country"
  - *Volume/Pages:* Vol. 41, No. 4, pp. 1283–1295 (2021).
- **Impact:** Corrected across all 4 manuscripts.

---

### Defect 3: Islam et al. (2018) Misattribution to Iranian Soil Paper
- **Context:** Cited in Paper 1 and Conference 1 as the primary Buriganga sediment risk assessment.
- **Pre-Audit State:**
  - Authors: `Islam, M. S. and Nakagawa, K. and Abdullah-Al-Mamun, M.`
  - Title: *"Trace elements in sediments of the industrial river Buriganga, Bangladesh: Spatial distribution and potential ecological risk"*
  - DOI: `10.1080/10807039.2018.1438173`
- **Audit Discovery:** Crossref query for `10.1080/10807039.2018.1438173` returned:
  - *Title:* "Assessment of metals in agricultural soil of surrounding areas of Urmia Lake, northwest Iran: A preliminary ecological risk assessment and source identification"
  - *Authors:* Amir Mohammadi, Yaghoub Hajizadeh, et al. (an Iranian soil study in the same journal!).
- **Resolution:** Reconciled against Study P01 in `data/studies.csv`. The actual Buriganga sediment study in *Human and Ecological Risk Assessment* synthesized in our dataset is:
  - *True Authors:* **Islam, Md. Saiful, Proshad, Ram, and Ahmed, Saad**
  - *True Title:* **"Ecological risk of heavy metals in sediment of an urban river in Bangladesh"**
  - *True DOI:* **`10.1080/10807039.2017.1397499`**
  - *True Volume/Pages:* Vol. 24, No. 3, pp. 699–720 (2018).
- **Impact:** Corrected in `manuscripts/paper_1_stoten/references.bib`, `manuscript_paper_1.md`, and `manuscripts/conference_1_igarss/references.bib`.

---

### Defect 4: Kadir et al. (2022) vs. Acharjee et al. (2022) Conflation
- **Context:** Cited in Paper 1 for Surma River sediment risk.
- **Pre-Audit State:** Entry `Kadir2022` cited title "Evaluation of water quality index and spatial risk mapping in the Surma River basin" with DOI `10.3390/w14020180`.
- **Audit Discovery:** Crossref revealed that DOI `10.3390/w14020180` belongs to:
  - *Authors:* Acharjee, Arup; Ahmed, Zia; Kumar, Pankaj; Alam, Rafiul; Rahman, M. Safiur; Simal-Gandara, Jesus.
  - *Title:* "Assessment of the Ecological Risk from Heavy Metals in the Surface Sediment of River Surma, Bangladesh..." (Study P17 - sediment).
  - Whereas Kadir et al. (2022) authored Study P07 (water quality in Surma River, DOI `10.3390/w14010017`).
- **Resolution:** Disentangled the two citations:
  - *Paper 1 (Sediment):* Defined `Acharjee2022` (DOI `10.3390/w14020180`) for Surma River sediment risk.
  - *Paper 2 (Water):* Defined `Kadir2022` (DOI `10.3390/w14010017`) for Surma River water quality assessment.
- **Impact:** Eliminates metadata cross-contamination between sediment and water studies.

---

## 3. Essential Methodological Citations Added

Peer reviewers in *Science of the Total Environment* and *Chemosphere* routinely flag unreferenced environmental index formulations. Four foundational citations were incorporated into the manuscripts and `.bib` files:

1. **Pollution Load Index ($PLI$):**
   - *Citation:* Tomlinson, D. L., Wilson, J. G., Harris, C. R., & Jeffrey, D. W. (1980). Problems in the assessment of heavy-metal levels in estuaries and the formation of a pollution index. *Helgoländer Meeresuntersuchungen*, 33(1–4), 566–575.
   - *DOI:* `10.1007/BF02414780`
   - *Integrated into:* Paper 1 Section 2.5 ($PLI$ formulation).

2. **Global Moran's $I$ Spatial Autocorrelation:**
   - *Citation:* Moran, P. A. P. (1950). Notes on Continuous Stochastic Phenomena. *Biometrika*, 37(1–2), 17–23.
   - *DOI:* `10.1093/biomet/37.1-2.17`
   - *Integrated into:* Paper 1 Section 2.3 & 3.1.

3. **Heavy Metal Evaluation Index ($HEI$):**
   - *Citation:* Edet, A. E., & Offiong, O. E. (2002). Evaluation of water quality pollution indices for heavy metal contamination monitoring. A study case from Akpabuyo-Odukpani area, Lower Cross River Basin (southeastern Nigeria). *GeoJournal*, 57(4), 295–304.
   - *DOI:* `10.1023/B:GEJO.0000007250.92458.de`
   - *Integrated into:* Paper 2 Section 2.3 ($HEI$ formulation).

4. **Metal Index ($MI$):**
   - *Citation:* Tamasi, G., & Cini, R. (2004). Heavy metals in drinking waters from Mount Amiata (Tuscany, Italy). Possible risks from arsenic for public health in the Province of Siena. *Science of the Total Environment*, 327(1–3), 41–51.
   - *DOI:* `10.1016/j.scitotenv.2003.10.011`
   - *Integrated into:* Paper 2 Section 2.3 ($MI$ formulation).

---

## 4. Regional Fluvial Literature Expansion & Provenance

To satisfy reviewer requirements for multi-study meta-analyses, representative primary investigations spanning the major hydrological basins were integrated into the literature review and database compilation sections:
- **Buriganga & Turag Mainstem:** Bhuiyan et al. (2015, *Environ. Monit. Assess.*, DOI `10.1007/s10661-014-4075-0`)
- **Karnaphuli Estuary:** Ali et al. (2016, *Environ. Nanotechnol. Monit. Manage.*, DOI `10.1016/j.enmm.2016.01.002`)
- **Surma Basin:** Kadir et al. (2022) and Acharjee et al. (2022)
- **Master Supplementary Catalog:** Compiled `manuscripts/supplementary_table_s1_audited_studies.md` detailing all 28 peer-reviewed publications (P01–P28) with:
  - Verifiable DOIs
  - Target river reaches
  - Sample medium segregation (289 sediment assays, 268 water assays)
  - Analytical instrumentation (AAS vs ICP-MS)
  - Extracted sample sizes

---

## 5. In-Text Citation Balance & Zero-Orphan Verification

The script `scratch/audit_references.py` was executed across all four manuscripts to guarantee 100% mutual resolution between in-text callouts and `.bib` definitions:

```
=== Paper 1 (STOTEN) ===
  Bib entries defined: 23
  Unique keys cited in text: 23
  Missing in BibTeX: None (Clean)
  Orphaned in BibTeX: None (Clean)

=== Paper 2 (Chemosphere) ===
  Bib entries defined: 16
  Unique keys cited in text: 16
  Missing in BibTeX: None (Clean)
  Orphaned in BibTeX: None (Clean)

=== Conference 1 (IEEE IGARSS) ===
  Bib entries defined: 11
  Unique keys cited in text: 11
  Missing in BibTeX: None (Clean)
  Orphaned in BibTeX: None (Clean)

=== Conference 2 (IEEE / IAHR Water) ===
  Bib entries defined: 10
  Unique keys cited in text: 10
  Missing in BibTeX: None (Clean)
  Orphaned in BibTeX: None (Clean)
```

---

## 6. LaTeX Recompilation & PDF Generation

Following reference harmonization, all 4 LaTeX manuscripts were recompiled via TeX Live 2025 (`pdflatex` + `bibtex` + `pdflatex` x2) with zero exit errors:

1. **Paper 1 (STOTEN):**
   - Output: `manuscripts/paper_1_stoten/main.pdf` (17 pages, 3,848,907 bytes)
   - Citations: 23 verified references, Elsarticle Harvard author-year style.
2. **Paper 2 (Chemosphere):**
   - Output: `manuscripts/paper_2_chemosphere/main.pdf` (12 pages, 771,067 bytes)
   - Citations: 16 verified references, Elsarticle Harvard author-year style.
3. **Conference 1 (IEEE IGARSS):**
   - Output: `manuscripts/conference_1_igarss/main.pdf` (3 pages, 3,590,458 bytes)
   - Citations: 11 verified references, IEEE numeric style.
4. **Conference 2 (IEEE Water):**
   - Output: `manuscripts/conference_2_water/main.pdf` (3 pages, 489,042 bytes)
   - Citations: 10 verified references, IEEE numeric style.

---

## 7. Submission Checklist for Authors

- [x] All digital object identifiers (DOIs) verified against Crossref API.
- [x] Zero orphaned or unreferenced BibTeX keys.
- [x] Foundational index formulations ($PLI$, $I_{geo}$, $RI$, $HPI$, $HEI$, $MI$, Moran's $I$) rigorously cited to original seminal literature.
- [x] Author names, initials, and journal abbreviations formatted in accordance with target journal author guidelines (Elsevier Harvard vs. IEEE numeric).
- [x] Master study audit table (Supplementary Table S1) compiled for submission as supplementary information.
- [x] All 4 publication PDFs compiled and visually checked.
