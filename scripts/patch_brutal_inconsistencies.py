import re

print("=== 1. PATCHING PAPER 4 ===")
with open("manuscripts/paper_4_data_descriptor/main.tex") as f:
    t4 = f.read()

# Replace Table 2
t2_start = t4.find("\\label{tab:summary}")
t2_end = t4.find("\\end{table}", t2_start) + len("\\end{table}")
old_t2 = t4[t2_start:t2_end]

new_t2 = r"""\label{tab:summary}
\resizebox{\textwidth}{!}{%
\begin{tabular}{lcccccccc}
\toprule
Element & Medium & Unit & $N$ & Median & Mean & IQR & Min & Max \\
\midrule
\textbf{Lead (Pb)} & Water & mg/L & 146 & 0.0286 & 0.0818 & 0.0849 & 0.0044 & 0.7000 \\
& Sediment & mg/kg dw & 289 & 30.62 & 104.05 & 42.68 & 0.34 & 3312.00 \\
\textbf{Chromium (Cr)} & Water & mg/L & 160 & 0.0710 & 0.3131 & 0.0724 & 0.0047 & 7.5500 \\
& Sediment & mg/kg dw & 274 & 46.27 & 156.05 & 62.88 & 4.74 & 1884.00 \\
\textbf{Cadmium (Cd)} & Water & mg/L & 132 & 0.0028 & 0.0130 & 0.0100 & 0.0000 & 0.1230 \\
& Sediment & mg/kg dw & 269 & 1.77 & 5.57 & 3.83 & 0.01 & 65.47 \\
\textbf{Arsenic (As)} & Water & mg/L & 122 & 0.0152 & 0.0351 & 0.0278 & 0.0000 & 0.3520 \\
& Sediment & mg/kg dw & 228 & 10.16 & 13.57 & 13.25 & 0.01 & 67.00 \\
\textbf{Nickel (Ni)} & Water & mg/L & 104 & 0.0888 & 0.3467 & 0.1803 & 0.0006 & 2.8880 \\
& Sediment & mg/kg dw & 235 & 40.62 & 67.61 & 57.15 & 2.16 & 539.00 \\
\textbf{Copper (Cu)} & Water & mg/L & 105 & 0.0888 & 0.2649 & 0.1720 & 0.0050 & 2.1790 \\
& Sediment & mg/kg dw & 235 & 49.00 & 73.44 & 62.78 & 0.25 & 712.00 \\
\textbf{Zinc (Zn)} & Water & mg/L & 79 & 0.4000 & 0.5767 & 0.8244 & 0.0079 & 3.2000 \\
& Sediment & mg/kg dw & 88 & 28.31 & 43.06 & 52.67 & 0.02 & 298.04 \\
\bottomrule
\end{tabular}%
}
\end{table}"""

t4 = t4[:t2_start] + new_t2 + t4[t2_end:]

# Replace Table 3
t3_start = t4.find("\\label{tab:instrument}")
t3_end = t4.find("\\end{table}", t3_start) + len("\\end{table}")

new_t3 = r"""\label{tab:instrument}
\resizebox{\textwidth}{!}{%
\begin{tabular}{lcccccc}
\toprule
Element & High-Sens Median & High-Sens Exceed (\%) & Flame-AAS Median & Flame-AAS Exceed (\%) & Mann-Whitney $U$ & $p$-value \\
\midrule
\textbf{Lead (Pb)} & 0.0171 mg/L & 79.2\% & 0.1100 mg/L & 92.8\% & 4725.0 & $<0.001$ \\
\textbf{Chromium (Cr)} & 0.0461 mg/L & 46.8\% & 0.0910 mg/L & 73.5\% & 4649.0 & $<0.001$ \\
\textbf{Cadmium (Cd)} & 0.0015 mg/L & 44.2\% & 0.0030 mg/L & 45.5\% & 2654.5 & 0.013 \\
\textbf{Arsenic (As)} & 0.0133 mg/L & 50.6\% & 0.0177 mg/L & 62.2\% & 2000.0 & 0.157 \\
\bottomrule
\end{tabular}%
}
\end{table}"""

t4 = t4[:t3_start] + new_t3 + t4[t3_end:]

with open("manuscripts/paper_4_data_descriptor/main.tex", "w") as f:
    f.write(t4)
print("Paper 4 main.tex updated successfully.")

print("=== 2. PATCHING PAPER 1 ===")
with open("manuscripts/paper_1_stoten/main.tex") as f:
    t1 = f.read()

# Update abstract
old_p1_abs = "A standardized, harmonized database of 289 sediment records spanning 12 major river systems was established from 28 peer-reviewed studies (2010--2022)."
new_p1_abs = "A standardized, harmonized database of 289 sediment records spanning 10 major river systems was established from 17 peer-reviewed studies (within a wider 28-study, 12-river national database spanning 2010--2024, with field sampling spanning 2010--2022)."
assert old_p1_abs in t1, "P1 abstract phrase not found"
t1 = t1.replace(old_p1_abs, new_p1_abs)

# Update literature search
old_p1_lit = "covering peer-reviewed studies published between 2010 and 2022 on river sediment contamination in Bangladesh."
new_p1_lit = "covering peer-reviewed studies published between 2010 and 2024 on river sediment contamination in Bangladesh."
assert old_p1_lit in t1, "P1 lit phrase not found"
t1 = t1.replace(old_p1_lit, new_p1_lit)

# Update records audit
old_p1_rec = "Raw spreadsheet records ($N=557$) were audited against original PDF source texts from 28 peer-reviewed publications spanning 2010--2022 \\citep{Ahmad2010,Bhuiyan2015,Islam2015,Ali2016,Islam2017,Islam2018,Ali2021,Acharjee2022}. Missing river attributes for 149 records were resolved by tracing typographical fill-down omissions in source tables and fully mapped to verified river systems: Paira \\citep{Islam2017}, Kirtankhola, and Korotoa. Medium separation segregated sediment assays ($N=289$) into milligrams per kilogram dry weight ($\\text{mg/kg dw}$)."
new_p1_rec = "Raw spreadsheet records ($N=557$) were audited against original PDF source texts from 28 peer-reviewed publications spanning 2010--2024 \\citep{Ahmad2010,Bhuiyan2015,Islam2015,Ali2016,Islam2017,Islam2018,Ali2021,Acharjee2022}. Missing river attributes for 149 records were resolved by tracing typographical fill-down omissions in source tables and fully mapped to verified river systems: Paira \\citep{Islam2017}, Kirtankhola, and Korotoa. Medium separation segregated sediment assays ($N=289$ across 17 studies and 10 river systems; 12 across combined water and sediment media) into milligrams per kilogram dry weight ($\\text{mg/kg dw}$)."
assert old_p1_rec in t1, "P1 rec phrase not found"
t1 = t1.replace(old_p1_rec, new_p1_rec)

# Update 12 river systems in line 98
old_p1_riv = "map to 133 unique georeferenced spatial station centroids across the 12 river systems."
new_p1_riv = "map to 133 unique georeferenced spatial station centroids across the 10 monitored sediment river systems."
assert old_p1_riv in t1, "P1 riv phrase not found"
t1 = t1.replace(old_p1_riv, new_p1_riv)

# Update limitation
old_p1_lim = "The training dataset synthesizes published studies spanning 2010--2022."
new_p1_lim = "The training dataset synthesizes published studies spanning 2010--2024 (field sampling 2010--2022)."
if old_p1_lim in t1:
    t1 = t1.replace(old_p1_lim, new_p1_lim)

with open("manuscripts/paper_1_stoten/main.tex", "w") as f:
    f.write(t1)
print("Paper 1 main.tex updated successfully.")

print("=== 3. PATCHING CONF 1 ===")
with open("manuscripts/conference_1_igarss/main.tex") as f:
    tc1 = f.read()

old_c1 = "A comprehensive database of 289 sediment records across 12 river systems was curated from 28 peer-reviewed studies (2010--2022)."
new_c1 = "A comprehensive database of 289 sediment records across 10 river systems was curated from 17 peer-reviewed studies (within a wider 28-study, 12-river national database spanning 2010--2024, with field sampling spanning 2010--2022)."
assert old_c1 in tc1, "C1 phrase not found"
tc1 = tc1.replace(old_c1, new_c1)

with open("manuscripts/conference_1_igarss/main.tex", "w") as f:
    f.write(tc1)
print("Conf 1 main.tex updated successfully.")

print("=== 4. PATCHING CONF 2 ===")
with open("manuscripts/conference_2_water/main.tex") as f:
    tc2 = f.read()

old_c2 = r"A harmonized database of \TotalWaterRecords\ surface water records across 12 major rivers was synthesized from peer-reviewed literature published between \StudyWindowYears."
new_c2 = r"A harmonized database of \TotalWaterRecords\ surface water records across 10 major river systems (12 across combined water and sediment media) was synthesized from peer-reviewed literature published between \StudyWindowYears."
assert old_c2 in tc2, "C2 phrase not found"
tc2 = tc2.replace(old_c2, new_c2)

with open("manuscripts/conference_2_water/main.tex", "w") as f:
    f.write(tc2)
print("Conf 2 main.tex updated successfully.")

print("ALL TE-X FILES PATCHED SUCCESSFULLY!")
