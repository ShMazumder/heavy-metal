#!/usr/bin/env bash
set -e

echo "=== Repackaging all submission archives ==="

# 1. Paper 1 (STOTEN)
(
  cd manuscripts/paper_1_stoten
  zip -q -r ../submissions/stoten_paper_1_submission.zip \
    main.pdf main.tex references.bib elsarticle.cls elsarticle-harv.bst \
    fig1_shap.png fig2_risk_map.png cover_letter_stoten.md
)
echo "Updated stoten_paper_1_submission.zip"

# 2. Paper 2 (Environmental Pollution)
(
  cd manuscripts/paper_2_environmental_pollution
  zip -q -r ../submissions/env_poll_paper_2_submission.zip \
    main.pdf main.tex references.bib results_macros.tex \
    elsarticle.cls elsarticle-harv.bst \
    fig1_exceedance.png fig2_dilution.png fig3_spatial_coverage_map.png graphical_abstract.png \
    cover_letter_env_poll.md
)
echo "Updated env_poll_paper_2_submission.zip"

# 3. Paper 3 (Environment International)
(
  cd manuscripts/paper_3_systematic_review
  zip -q -r ../submissions/env_intl_paper_3_submission.zip \
    main.pdf main.tex references.bib \
    elsarticle.cls elsarticle-harv.bst \
    fig1_prisma.png fig2_forest.png fig3_spatial.png \
    cover_letter_env_intl.md
)
echo "Updated env_intl_paper_3_submission.zip"

# 4. Paper 4 (Scientific Data)
(
  cd manuscripts/paper_4_data_descriptor
  zip -q -r ../submissions/scientific_data_paper_4_submission.zip \
    main.pdf main.tex references.bib \
    fig1_spatial_coverage.png cover_letter_scientific_data.md
)
echo "Updated scientific_data_paper_4_submission.zip"

# 5. Zenodo deposit
./scripts/package_zenodo_deposit.sh

echo "All submission archives successfully repackaged!"
