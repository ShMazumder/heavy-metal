#!/usr/bin/env bash
set -e
echo "Building Conference 2 (Water) LaTeX..."
pdflatex -interaction=nonstopmode main.tex
bibtex main || true
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
echo "Successfully built manuscripts/conference_2_water/main.pdf"
