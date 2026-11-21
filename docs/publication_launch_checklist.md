# 🚀 Publication Launch Checklist

> [!IMPORTANT]
> All reviews in `review/paper_2/round_{1-6}/` are internal LLM peer reviews (Claude/ChatGPT/Gemini), not actual journal reviews. All 4 papers are **fresh original submissions**.

---

## Phase 0: Pre-Flight (Before Any Submission)

### Author Metadata — Do This First
Replace placeholders in **all 6 manuscript packages**:

| Placeholder | Replace With |
|---|---|
| `Author One` | Real first author name |
| `Author Two` | Real second author name |
| `Author Three` | Real third author name |
| `University Name` | Actual institution |
| `author.one@university.edu` | Corresponding author email |
| `sh.mazumder@example.edu` | Corresponding author email |
| ORCID fields | Real ORCID iDs |

**Files to update:**
- [ ] `manuscripts/paper_1_stoten/main.tex` (lines 50–65)
- [ ] `manuscripts/paper_1_stoten/cover_letter_stoten.md`
- [ ] `manuscripts/paper_2_environmental_pollution/main.tex` (lines 50–65)
- [ ] `manuscripts/paper_2_environmental_pollution/cover_letter_env_poll.md`
- [ ] `manuscripts/paper_3_systematic_review/main.tex` (lines 50–65)
- [ ] `manuscripts/paper_3_systematic_review/cover_letter_env_intl.md`
- [ ] `manuscripts/paper_4_data_descriptor/main.tex` (lines 50–58)
- [ ] `manuscripts/paper_4_data_descriptor/cover_letter_scientific_data.md`
- [ ] `.zenodo.json` (creators array)

After updating → recompile all PDFs:
```bash
for d in paper_1_stoten paper_2_environmental_pollution paper_3_systematic_review paper_4_data_descriptor conference_1_igarss conference_2_water; do
  (cd manuscripts/$d && ./build.sh)
done
```

---

## Phase 1: Zenodo DOI Reservation (DONE ✅)

- **Reserved DOI:** `10.5281/zenodo.24414976`
- **Deposit Archive:** [`zenodo_heavy_metal_database_v1.0.0.zip`](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/submissions/zenodo_heavy_metal_database_v1.0.0.zip) (7.6 MB)
- **Status:** Integrated into Paper 4 manuscript, LaTeX, and submission bundle.

> [!CAUTION]
> Keep deposit in "Draft" on Zenodo. Do NOT click "Publish" until Papers 1 & 2 are confirmed under journal review.

### Status of DOI Integration:
- [x] Inserted `10.5281/zenodo.24414976` into `manuscripts/paper_4_data_descriptor/main.tex`
- [x] Inserted `10.5281/zenodo.24414976` into `manuscripts/paper_4_data_descriptor/manuscript_paper_4.md`
- [x] Inserted `10.5281/zenodo.24414976` into `manuscripts/paper_4_data_descriptor/cover_letter_scientific_data.md`
- [x] Inserted `10.5281/zenodo.24414976` into `manuscripts/shared/submission_and_venue_guide.md`
- [x] Recompiled Paper 4 PDF (`8 pp`)
- [x] Regenerated `scientific_data_paper_4_submission.zip` (1.5 MB)
- [x] Pushed to GitHub `origin/main`

---

## Phase 2: Submit Papers 1 & 2 (Day 1–3)

### Paper 2 → Environmental Pollution (Submit First)

> [!IMPORTANT]
> Pivoted from Chemosphere (delisted by Clarivate from Web of Science) to **Environmental Pollution** (Elsevier, IF 8.9, Q1, 100% SCIE indexed, $0 APC subscription option).

**Portal:** [https://www.editorialmanager.com/envpol/](https://www.editorialmanager.com/envpol/)

- [ ] Create account / login on Editorial Manager
- [ ] Click **"Submit New Manuscript"**
- [ ] Article Type: `Research Paper`
- [ ] Enter title, abstract, keywords
- [ ] Upload files:
  - Cover Letter → [`cover_letter_env_poll.md`](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/paper_2_environmental_pollution/cover_letter_env_poll.md)
  - Graphical Abstract → [`graphical_abstract.png`](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/paper_2_environmental_pollution/graphical_abstract.png)
  - Manuscript → [`main.pdf`](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/paper_2_environmental_pollution/main.pdf)
  - Supplementary → [`supplementary_table_s1_audited_studies.md`](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/shared/supplementary_table_s1_audited_studies.md)
- [ ] Paste Highlights (5 bullets ≤ 85 chars):
  ```
  ECR 2023 potable limits increase river Pb exceedances from 34.9% to 85.6%.
  Confirmed 0.45 um filtered Pb median is 0.025 mg/L, exceeding WHO standards.
  HPI math dampens panel shifts: Cd and Pb command 77.1% of index scores.
  HKSJ seasonal dilution ratios cross 1.0; low-flow As peaks pre-monsoon.
  Academic sampling monitors only 16.5% of major Bangladesh river reaches.
  ```
- [ ] Category: `Environmental Chemistry`
- [ ] Suggested reviewers (3–4 names with emails)
- [ ] Publishing model: **Subscription ($0 APC)**
- [ ] Data availability: link to GitHub repo
- [ ] Build PDF, review, **Submit**

### Paper 1 → STOTEN (Submit Day 2–3)

**Portal:** [https://www.editorialmanager.com/stoten/](https://www.editorialmanager.com/stoten/)

- [ ] Create account / login on Editorial Manager
- [ ] Click **"Submit New Manuscript"**
- [ ] Article Type: `Research Article`
- [ ] Enter title, abstract, keywords
- [ ] Upload files:
  - Cover Letter → [`cover_letter_stoten.md`](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/paper_1_stoten/cover_letter_stoten.md)
  - Graphical Abstract → [`fig2_risk_map.png`](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/paper_1_stoten/fig2_risk_map.png)
  - Manuscript → [`main.pdf`](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/paper_1_stoten/main.pdf)
  - Supplementary → [`supplementary_table_s1_audited_studies.md`](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/shared/supplementary_table_s1_audited_studies.md)
- [ ] Paste Highlights (5 bullets)
- [ ] Category: `Environmental Monitoring` or `Contaminated Sediments`
- [ ] Suggested reviewers (3 names with emails)
- [ ] Publishing model: **Subscription ($0 APC)**
- [ ] Data availability: link to GitHub repo
- [ ] Build PDF, review, **Submit**

> [!NOTE]
> Papers 1 and 2 have zero matrix overlap (sediment vs water). Safe to submit simultaneously to different Elsevier journals.

---

## Phase 3: Submit Paper 4 (Day 5–7)

### Paper 4 → Nature Scientific Data

**Portal:** [https://mts-scidata.nature.com/](https://mts-scidata.nature.com/)

- [ ] Confirm Zenodo DOI is reserved and inserted into `main.tex`
- [ ] Create account on Springer Nature MTS
- [ ] Article Type: `Data Descriptor`
- [ ] Upload:
  - Cover Letter → [`cover_letter_scientific_data.md`](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/paper_4_data_descriptor/cover_letter_scientific_data.md)
  - Manuscript → [`main.pdf`](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/paper_4_data_descriptor/main.pdf)
- [ ] Data repository: Zenodo reserved DOI + GitHub URL
- [ ] Suggested reviewers (3 names)
- [ ] **Submit**

> [!WARNING]
> Nature Scientific Data is **Gold Open Access** — typical APC is ~$1,990. Check if your institution has a Springer Nature Read & Publish agreement for fee waiver. Alternative zero-APC venue: *Data in Brief* (Elsevier, IF 1.2).

---

## Phase 4: Submit Paper 3 (Week 3–4)

### Paper 3 → Environment International

**Portal:** [https://www.editorialmanager.com/envint/](https://www.editorialmanager.com/envint/)

- [ ] Submit after Papers 1 & 2 have confirmed "Under Review" status
- [ ] This paper synthesizes across both matrices — references Papers 1, 2, and 4 as companion studies
- [ ] Article Type: `Review Article` or `Systematic Review`
- [ ] Upload all files from [`env_intl_paper_3_submission.zip`](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/submissions/env_intl_paper_3_submission.zip)
- [ ] **Submit**

> [!TIP]
> Alternative venue if Env Intl declines: *Critical Reviews in Environmental Science and Technology* (CREST, IF 12.6, Taylor & Francis, hybrid $0 APC available).

---

## Phase 5: Conferences (Align with CFP Deadlines)

- [ ] Conference 1 (IEEE IGARSS): Check deadline at [igarss.org](https://www.igarss.org). Upload [`main.pdf`](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/conference_1_igarss/main.pdf).
- [ ] Conference 2 (IWA Water Congress): Check deadline at [iwa-network.org](https://iwa-network.org). Upload [`main.pdf`](file:///Users/rohansmac/Documents/projects/heavy-metal/manuscripts/conference_2_water/main.pdf).

---

## Phase 6: Post-Submission

- [ ] When Papers 1 & 2 confirmed "Under Review" → click **"Publish"** on Zenodo draft
- [ ] Update Paper 4 Zenodo DOI from reserved → live (if requested by reviewers)
- [ ] Track all submission IDs in a spreadsheet
- [ ] Respond to reviewer comments within 2–4 weeks of receipt
