"""
Single Source of Truth for Water & Sediment Quality Benchmarks.
Standards:
  - WHO Guidelines for Drinking-water Quality (4th ed. incorporating 2022 addenda)
  - Bangladesh Environmental Conservation Rules (ECR 1997 Schedule 3)
  - Bangladesh Environmental Conservation Rules (ECR 2023 Schedule 2, S.R.O. 53-Law/2023)
  - FAO Irrigation Criteria (Paper 29, 1985)
  - Geochemical Baselines (Wedepohl 1995 Upper Continental Crust, UCC)
"""

WATER_BENCHMARKS = {
    'As': {
        'name': 'Arsenic',
        'who': 0.010,
        'bd_1997': 0.050,
        'bd_2023': 0.050,
        'fao': 0.100,
        'unit': 'mg/L'
    },
    'Cd': {
        'name': 'Cadmium',
        'who': 0.003,
        'bd_1997': 0.005,
        'bd_2023': 0.003,
        'fao': 0.010,
        'unit': 'mg/L'
    },
    'Cr': {
        'name': 'Chromium',
        'who': 0.050,
        'bd_1997': 0.050,
        'bd_2023': 0.050,
        'fao': 0.100,
        'unit': 'mg/L'
    },
    'Cu': {
        'name': 'Copper',
        'who': 2.000,
        'bd_1997': 1.000,
        'bd_2023': 1.500,
        'fao': 0.200,
        'unit': 'mg/L'
    },
    'Ni': {
        'name': 'Nickel',
        'who': 0.070,
        'bd_1997': 0.100,
        'bd_2023': 0.050,
        'fao': 0.200,
        'unit': 'mg/L'
    },
    'Pb': {
        'name': 'Lead',
        'who': 0.010,
        'bd_1997': 0.050,
        'bd_2023': 0.010,
        'fao': 5.000,
        'unit': 'mg/L'
    },
    'Zn': {
        'name': 'Zinc',
        'who': 3.000,      # Aesthetic guideline
        'bd_1997': 5.000,
        'bd_2023': 5.000,
        'fao': 2.000,
        'unit': 'mg/L'
    }
}

# Alias for backward compatibility
for el in WATER_BENCHMARKS:
    WATER_BENCHMARKS[el]['bd'] = WATER_BENCHMARKS[el]['bd_1997']

SEDIMENT_UCC_BASELINES = {
    'Cr': 35.0,   # mg/kg dw (Wedepohl 1995)
    'Pb': 20.0,
    'Cd': 0.1,
    'Cu': 25.0,
    'Ni': 20.0,
    'As': 1.5
}

# Hakanson (1980) Toxic Biological Response Factors
HAKANSON_TR = {
    'Cd': 30,
    'As': 10,
    'Pb': 5,
    'Cu': 5,
    'Ni': 5,
    'Cr': 2
}
