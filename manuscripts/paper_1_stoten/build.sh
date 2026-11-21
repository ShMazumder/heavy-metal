#!/usr/bin/env bash
set -e
echo "Building Paper 1 (STOTEN) LaTeX..."
pdflatex -interaction=nonstopmode main.tex
bibtex main || true
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
echo "Successfully built manuscripts/paper_1_stoten/main.pdf"
