#!/usr/bin/env bash
set -e
echo "Building Paper 2 (Chemosphere) LaTeX..."
pdflatex -interaction=nonstopmode main.tex
bibtex main || true
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
echo "Successfully built manuscripts/paper_2_chemosphere/main.pdf"
