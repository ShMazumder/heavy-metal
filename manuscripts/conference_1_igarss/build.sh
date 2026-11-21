#!/usr/bin/env bash
set -e
echo "Building Conference 1 (IGARSS) LaTeX..."
pdflatex -interaction=nonstopmode main.tex
bibtex main || true
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
echo "Successfully built manuscripts/conference_1_igarss/main.pdf"
