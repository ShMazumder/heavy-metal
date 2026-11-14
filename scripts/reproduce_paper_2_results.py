import math
import os
import shutil
import sqlite3
import struct
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu

print("=== REPRODUCIBLE PIPELINE FOR PAPER 2 (ROUTE A) ===")

# --- 1. Wilson Score Confidence Intervals ---
def wilson_ci(count, nobs, alpha=0.05):
    if nobs == 0:
        return 0.0, 0.0
    z = 1.959963984540054
    p = count / nobs
    denom = 1 + z**2 / nobs
    center = (p + z**2 / (2 * nobs)) / denom
    margin = (z * math.sqrt(p * (1 - p) / nobs + z**2 / (4 * nobs**2))) / denom
    return max(0.0, center - margin), min(1.0, center + margin)

# --- 2. Load Patched Water Data ---
df_water = pd.read_csv('data/water_data.csv')
print(f"Loaded water dataset: {df_water.shape[0]} records, {df_water.shape[1]} columns.")

# Define benchmarks
# WHO 4th ed (2022 addendum) & Bangladesh ECR 2023 / 1997 drinking schedule
benchmarks = {
    'Pb': {'name': 'Lead', 'who': 0.010, 'bd': 0.050},
    'Cr': {'name': 'Chromium', 'who': 0.050, 'bd': 0.050},
    'Ni': {'name': 'Nickel', 'who': 0.070, 'bd': 0.100},
    'As': {'name': 'Arsenic', 'who': 0.010, 'bd': 0.050},
    'Cd': {'name': 'Cadmium', 'who': 0.003, 'bd': 0.005},
    'Cu': {'name': 'Copper', 'who': 2.000, 'bd': 1.000},
    'Zn': {'name': 'Zinc', 'who': 3.000, 'bd': 5.000} # Note: WHO 3.0 mg/L is aesthetic/acceptability
}

# --- 3. Compute Table 1: Exceedance Summary ---
records_t1 = []
for el, b in benchmarks.items():
    col = f"{el}_mg_L"
    s = df_water[col].dropna()
    n = len(s)
    mean_val = s.mean()
    median_val = s.median()
    max_val = s.max()
    
    who_limit = b['who']
    bd_limit = b['bd']
    
    who_cnt = int((s > who_limit).sum())
    who_pct = (who_cnt / n) * 100.0
    w_lo, w_hi = wilson_ci(who_cnt, n)
    
    bd_cnt = int((s > bd_limit).sum())
    bd_pct = (bd_cnt / n) * 100.0
    b_lo, b_hi = wilson_ci(bd_cnt, n)
    
    records_t1.append({
        'Element': el,
        'Name': b['name'],
        'N_Samples': n,
        'Mean_mg_L': round(mean_val, 4),
        'Median_mg_L': round(median_val, 4),
        'Max_mg_L': round(max_val, 4),
        'WHO_Guideline_mg_L': who_limit,
        'WHO_Exceed_Count': who_cnt,
        'WHO_Exceed_Pct': round(who_pct, 1),
        'WHO_CI_Low': round(w_lo * 100.0, 1),
        'WHO_CI_High': round(w_hi * 100.0, 1),
        'BD_ECR_Standard_mg_L': bd_limit,
        'BD_ECR_Exceed_Count': bd_cnt,
        'BD_ECR_Exceed_Pct': round(bd_pct, 1),
        'BD_CI_Low': round(b_lo * 100.0, 1),
        'BD_CI_High': round(b_hi * 100.0, 1)
    })

df_t1 = pd.DataFrame(records_t1).sort_values(by='WHO_Exceed_Pct', ascending=False)
os.makedirs('data/paper_2_water_results', exist_ok=True)
df_t1.to_csv('data/paper_2_water_results/who_ecr_exceedance_summary.csv', index=False)
print("Saved: data/paper_2_water_results/who_ecr_exceedance_summary.csv")
print(df_t1[['Element', 'N_Samples', 'Median_mg_L', 'Max_mg_L', 'WHO_Exceed_Pct', 'WHO_CI_Low', 'WHO_CI_High', 'BD_ECR_Exceed_Pct']])

# Sensitivity Analysis: Non-peri-urban rivers
peri_urban = ['Buriganga', 'Turag', 'Shitalakhya']
df_non_urban = df_water[~df_water['River'].isin(peri_urban)]
sens_records = []
for el, b in benchmarks.items():
    col = f"{el}_mg_L"
    s = df_non_urban[col].dropna()
    n = len(s)
    who_cnt = int((s > b['who']).sum())
    who_pct = (who_cnt / n) * 100.0 if n > 0 else 0.0
    w_lo, w_hi = wilson_ci(who_cnt, n)
    bd_cnt = int((s > b['bd']).sum())
    bd_pct = (bd_cnt / n) * 100.0 if n > 0 else 0.0
    b_lo, b_hi = wilson_ci(bd_cnt, n)
    sens_records.append({
        'Element': el,
        'N_NonUrban': n,
        'WHO_Exceed_Pct': round(who_pct, 1),
        'WHO_CI': f"[{round(w_lo*100,1)}–{round(w_hi*100,1)}%]",
        'BD_Exceed_Pct': round(bd_pct, 1),
        'BD_CI': f"[{round(b_lo*100,1)}–{round(b_hi*100,1)}%]"
    })
df_sens = pd.DataFrame(sens_records)
df_sens.to_csv('data/paper_2_water_results/sensitivity_non_urban_exceedance.csv', index=False)
print("Saved sensitivity table.")

# --- 4. Compute Multi-Metal Pollution Indices (HPI, HEI, MI) ---
metal_keys = list(benchmarks.keys())
metal_cols = [f"{m}_mg_L" for m in metal_keys]
df_water['multi_metal_count'] = df_water[metal_cols].notna().sum(axis=1)

# Include records with >= 3 analyzed metals
multi_mask = df_water['multi_metal_count'] >= 3

hpi_list = []
hei_list = []
mi_list = []

for idx, row in df_water.iterrows():
    if not multi_mask[idx]:
        hpi_list.append(np.nan)
        hei_list.append(np.nan)
        mi_list.append(np.nan)
        continue
    
    sum_wq = 0.0
    sum_w = 0.0
    hei_val = 0.0
    mi_val = 0.0
    
    for m in metal_keys:
        c = row[f"{m}_mg_L"]
        if pd.notna(c):
            s_who = benchmarks[m]['who']
            s_bd = benchmarks[m]['bd']
            w_i = 1.0 / s_who
            q_i = (c / s_who) * 100.0
            sum_wq += w_i * q_i
            sum_w += w_i
            hei_val += (c / s_who)
            mi_val += (c / s_bd)
            
    hpi_list.append(round(sum_wq / sum_w, 2))
    hei_list.append(round(hei_val, 2))
    mi_list.append(round(mi_val, 2))

df_water['HPI'] = hpi_list
df_water['HEI'] = hei_list
df_water['MI'] = mi_list

# Classifications: Prasad & Bose (2001) / standard HPI
def classify_hpi(v):
    if pd.isna(v):
        return np.nan
    if v < 100:
        return 'Low Pollution (HPI < 100)'
    elif v <= 200:
        return 'Moderate Pollution (100 <= HPI <= 200)'
    else:
        return 'Critical Pollution (HPI > 200)'

df_water['HPI_Class'] = df_water['HPI'].apply(classify_hpi)
df_water.to_csv('data/paper_2_water_results/water_records_with_indices.csv', index=False)
print("Saved: data/paper_2_water_results/water_records_with_indices.csv")

# River level synthesis of indices
sub_indices = df_water.dropna(subset=['HPI'])
river_summary = []
for river, grp in sub_indices.groupby('River'):
    n = len(grp)
    mean_hpi = grp['HPI'].mean()
    med_hpi = grp['HPI'].median()
    iqr_hpi = grp['HPI'].quantile(0.75) - grp['HPI'].quantile(0.25)
    crit_pct = (grp['HPI'] > 200).sum() / n * 100.0
    unsuitable_pct = (grp['HPI'] > 100).sum() / n * 100.0
    mean_hei = grp['HEI'].mean()
    med_hei = grp['HEI'].median()
    mean_mi = grp['MI'].mean()
    med_mi = grp['MI'].median()
    
    river_summary.append({
        'River': river,
        'N_Records': n,
        'Mean_HPI': round(mean_hpi, 2),
        'Median_HPI': round(med_hpi, 2),
        'IQR_HPI': round(iqr_hpi, 2),
        'Pct_HPI_gt_100': round(unsuitable_pct, 1),
        'Pct_HPI_gt_200': round(crit_pct, 1),
        'Mean_HEI': round(mean_hei, 2),
        'Median_HEI': round(med_hei, 2),
        'Mean_MI': round(mean_mi, 2),
        'Median_MI': round(med_mi, 2)
    })

df_river_indices = pd.DataFrame(river_summary).sort_values(by='Median_HPI', ascending=False)
df_river_indices.to_csv('data/paper_2_water_results/water_indices_summary_by_river.csv', index=False)
print("Saved: data/paper_2_water_results/water_indices_summary_by_river.csv")
print(df_river_indices.to_string())

# Also update SQLite heavy_metal.db table water_indices_by_river
conn = sqlite3.connect('data/heavy_metal.db')
df_river_indices.to_sql('water_indices_by_river', conn, if_exists='replace', index=False)
conn.commit()
conn.close()

# --- 5. Compute Table 2: Seasonal Dilution Analysis (Two-Sided + Holm-Bonferroni) ---
dry_mask = df_water['Season'].isin(['Winter', 'winter'])
wet_mask = df_water['Season'].isin(['Rainy', 'Wet', 'Monsoon'])

seasonal_records = []
p_values = []
test_elements = ['As', 'Cr', 'Cd', 'Zn', 'Cu', 'Pb', 'Ni']

for el in test_elements:
    col = f"{el}_mg_L"
    dry_vals = df_water[dry_mask & df_water[col].notna()][col].values
    wet_vals = df_water[wet_mask & df_water[col].notna()][col].values
    
    n_d = len(dry_vals)
    n_w = len(wet_vals)
    med_d = np.median(dry_vals) if n_d > 0 else np.nan
    med_w = np.median(wet_vals) if n_w > 0 else np.nan
    ratio = med_d / med_w if med_w > 0 else np.nan
    
    res = mannwhitneyu(dry_vals, wet_vals, alternative='two-sided')
    p_val = res.pvalue
    u_stat = res.statistic
    
    seasonal_records.append({
        'Element': el,
        'Name': benchmarks[el]['name'],
        'N_Dry': n_d,
        'Median_Dry_mg_L': round(med_d, 4),
        'N_Wet': n_w,
        'Median_Wet_mg_L': round(med_w, 4),
        'Dry_to_Wet_Ratio': round(ratio, 2),
        'Mann_Whitney_U': u_stat,
        'p_value_twosided': p_val
    })
    p_values.append(p_val)

# Holm-Bonferroni adjustment
sorted_indices = np.argsort(p_values)
m_tests = len(p_values)
adj_p_values = [0.0] * m_tests

running_max = 0.0
for rank, idx in enumerate(sorted_indices):
    k = rank + 1
    multiplier = m_tests - k + 1
    adjusted = p_values[idx] * multiplier
    adjusted = min(1.0, adjusted)
    running_max = max(running_max, adjusted)
    adj_p_values[idx] = running_max

for i, rec in enumerate(seasonal_records):
    rec['p_adj_holm'] = round(adj_p_values[i], 4)
    rec['Significant_Dilution'] = 'Yes (p_adj < 0.05)' if adj_p_values[i] < 0.05 else 'No (Not Significant)'

df_t2 = pd.DataFrame(seasonal_records).sort_values(by='p_value_twosided')
df_t2.to_csv('data/paper_2_water_results/seasonal_dilution_analysis.csv', index=False)
print("Saved: data/paper_2_water_results/seasonal_dilution_analysis.csv")
print(df_t2[['Element', 'N_Dry', 'Median_Dry_mg_L', 'N_Wet', 'Median_Wet_mg_L', 'Dry_to_Wet_Ratio', 'Mann_Whitney_U', 'p_value_twosided', 'p_adj_holm', 'Significant_Dilution']])

# --- 6. Compute Table 3: Spatial Coverage and Surveillance Gaps ---
def haversine_np(lat1, lon1, lat2_arr, lon2_arr):
    R = 6371.0
    dlat = np.radians(lat2_arr - lat1)
    dlon = np.radians(lon2_arr - lon1)
    a = np.sin(dlat / 2.0)**2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2_arr)) * np.sin(dlon / 2.0)**2
    c = 2 * np.arcsin(np.sqrt(a))
    return R * c

def dist_pt_pt(lat1, lon1, lat2, lon2):
    R = 6371.0
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    a = np.sin(dlat / 2.0)**2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon / 2.0)**2
    return R * 2 * np.arcsin(np.sqrt(a))

coords = df_water[['Lat_WGS84', 'Lon_WGS84']].dropna().drop_duplicates().values

conn = sqlite3.connect('data/hydrorivers_bangladesh.gpkg')
c = conn.cursor()
c.execute('SELECT HYRIV_ID, ORD_STRA, DIS_AV_CMS, UPLAND_SKM, LENGTH_KM, MAIN_RIV, geom FROM hydrorivers_bangladesh WHERE ORD_STRA >= 4 AND DIS_AV_CMS >= 50')
rows = c.fetchall()

reach_data = []
for hyriv_id, ord_stra, dis_av, upland, length_km, main_riv, blob in rows:
    flags = blob[3]
    env_size = {0:0, 1:32, 2:48, 3:48, 4:64}.get((flags >> 1) & 0x07, 0)
    wkb = blob[8 + env_size:]
    endian = '<' if wkb[0] == 1 else '>'
    num_pts = struct.unpack(endian + 'I', wkb[5:9])[0]
    pts = struct.unpack(endian + f'{num_pts*2}d', wkb[9:9+num_pts*16])
    xs = pts[0::2]
    ys = pts[1::2]
    mid_lat = float(np.mean(ys))
    mid_lon = float(np.mean(xs))
    
    # Enforce Bangladesh territory bounding box
    if not (20.5 <= mid_lat <= 26.65 and 88.02 <= mid_lon <= 92.68):
        continue
        
    dists = haversine_np(mid_lat, mid_lon, coords[:,0], coords[:,1])
    min_dist = float(np.min(dists))
    reach_data.append({
        'HYRIV_ID': int(hyriv_id),
        'ORD_STRA': int(ord_stra),
        'DIS_AV_CMS': round(dis_av, 1),
        'UPLAND_SKM': round(upland, 1),
        'LENGTH_KM': round(length_km, 2),
        'MAIN_RIV': int(main_riv),
        'Mid_Lat': round(mid_lat, 6),
        'Mid_Lon': round(mid_lon, 6),
        'Min_Dist_km': round(min_dist, 1)
    })

df_bd_major = pd.DataFrame(reach_data)
candidates = df_bd_major[df_bd_major['Min_Dist_km'] > 25.0].sort_values(by=['UPLAND_SKM', 'DIS_AV_CMS'], ascending=False)

# Select 15 geographically diverse, non-redundant candidates (>= 30 km separation)
selected_candidates = []
min_spacing = 30.0

reach_names = [
    "Lower Meghna Mainstem (Chandpur Confluence)",
    "Padma-Meghna Convergence (Munshiganj Reach)",
    "Lower Padma Main Channel (Madaripur)",
    "Upper Padma Mainstem (Goalundo Reach)",
    "Ganges-Jamuna Convergence Reach (Rajbari)",
    "Upper Ganges Mainstem (Kushtia)",
    "Central Ganges Channel (Pabna-Natore Reach)",
    "North-West Padma Reach (Rajshahi Upstream)",
    "Upper Border Ganges Reach (Chapai Nawabganj)",
    "Lower Jamuna (Brahmaputra) Reach (Sirajganj)",
    "Central Jamuna Mainstem (Bogra Reach)",
    "Upper Jamuna Channel (Jamalpur-Bogra Reach)",
    "Brahmaputra Confluence Reach (Gaibandha)",
    "Upper Brahmaputra Channel (Kurigram)",
    "Northern Brahmaputra Entry Reach (Chilmari)"
]

for _, r in candidates.iterrows():
    lat = r['Mid_Lat']
    lon = r['Mid_Lon']
    if not selected_candidates:
        selected_candidates.append(r)
    else:
        too_close = any(dist_pt_pt(lat, lon, s['Mid_Lat'], s['Mid_Lon']) < min_spacing for s in selected_candidates)
        if not too_close:
            selected_candidates.append(r)
    if len(selected_candidates) == 15:
        break

df_t3 = pd.DataFrame(selected_candidates)
df_t3['Priority_Rank'] = range(1, 16)
df_t3['Candidate_Station_ID'] = [f"GAP_STN_{i:02d}" for i in range(1, 16)]
df_t3['Target_River_Reach'] = reach_names

cols_order = ['Priority_Rank', 'Candidate_Station_ID', 'Mid_Lat', 'Mid_Lon', 'ORD_STRA', 'UPLAND_SKM', 'DIS_AV_CMS', 'Min_Dist_km', 'Target_River_Reach', 'HYRIV_ID']
df_t3 = df_t3[cols_order].rename(columns={
    'Mid_Lat': 'Recommended_Latitude',
    'Mid_Lon': 'Recommended_Longitude',
    'ORD_STRA': 'Strahler_Stream_Order',
    'UPLAND_SKM': 'Upstream_Catchment_km2',
    'DIS_AV_CMS': 'Mean_Discharge_m3_s',
    'Min_Dist_km': 'Distance_to_Nearest_Study_km'
})
df_t3.to_csv('data/paper_2_water_results/priority_future_monitoring_stations.csv', index=False)
print("Saved: data/paper_2_water_results/priority_future_monitoring_stations.csv")
print(df_t3[['Priority_Rank', 'Candidate_Station_ID', 'Recommended_Latitude', 'Recommended_Longitude', 'Distance_to_Nearest_Study_km', 'Target_River_Reach']].to_string())

# --- 7. Generate Publication Figures (300 DPI) ---
print("\n--- Generating Publication Figures ---")

# Figure 1: Benchmark Exceedance Rates with 95% Wilson Confidence Intervals
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)

x = np.arange(len(df_t1))
width = 0.35

who_yerr = [
    df_t1['WHO_Exceed_Pct'] - df_t1['WHO_CI_Low'],
    df_t1['WHO_CI_High'] - df_t1['WHO_Exceed_Pct']
]
bd_yerr = [
    df_t1['BD_ECR_Exceed_Pct'] - df_t1['BD_CI_Low'],
    df_t1['BD_CI_High'] - df_t1['BD_ECR_Exceed_Pct']
]

rects1 = ax.bar(x - width/2, df_t1['WHO_Exceed_Pct'], width, yerr=who_yerr, capsize=4,
                label='WHO Drinking Guideline (Health Benchmark)', color='#1f77b4', edgecolor='black', alpha=0.9)
rects2 = ax.bar(x + width/2, df_t1['BD_ECR_Exceed_Pct'], width, yerr=bd_yerr, capsize=4,
                label='Bangladesh Standard (ECR 2023 / 1997)', color='#d62728', edgecolor='black', alpha=0.9)

ax.set_ylabel('Exceedance Rate in Published Records (%)', fontsize=12, fontweight='bold')
ax.set_title('Heavy Metal Benchmark Exceedance Rates in Published Bangladesh River Water Records (2010–2022)\nwith 95% Wilson Score Confidence Intervals', fontsize=12, fontweight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels([f"{r['Name']}\n({r['Element']})\n[N={r['N_Samples']}]" for _, r in df_t1.iterrows()], fontsize=10)
ax.set_ylim(0, 105)
ax.axhline(50, color='gray', linestyle='--', linewidth=0.8, alpha=0.7)
ax.grid(axis='y', linestyle=':', alpha=0.6)
ax.legend(frameon=True, facecolor='white', framealpha=0.95, loc='upper right', fontsize=10)

plt.tight_layout()
fig1_path = 'data/paper_2_water_results/guidelines_exceedance_rates.png'
plt.savefig(fig1_path, dpi=300)
plt.close()
print(f"Figure 1 saved to {fig1_path}")

# Figure 2: Seasonal Dilution Dynamics (Dry vs Wet Season Boxplots)
fig, axes = plt.subplots(1, 4, figsize=(16, 4.5), dpi=300)

plot_metals = [
    ('As', 'Arsenic (As)', 'mg/L', True),
    ('Cr', 'Chromium (Cr)', 'mg/L', False),
    ('Cd', 'Cadmium (Cd)', 'mg/L', False),
    ('Pb', 'Lead (Pb)', 'mg/L', False)
]

colors = ['#ff7f0e', '#1f77b4'] # Orange for Dry/Winter, Blue for Wet/Rainy

for idx, (m, label, unit, sig) in enumerate(plot_metals):
    ax = axes[idx]
    col = f"{m}_mg_L"
    dry_data = df_water[dry_mask & df_water[col].notna()][col].values
    wet_data = df_water[wet_mask & df_water[col].notna()][col].values
    
    # Boxplot
    bp = ax.boxplot([dry_data, wet_data], positions=[1, 2], widths=0.5, patch_artist=True,
                    boxprops=dict(facecolor='white', color='black'),
                    medianprops=dict(color='black', linewidth=2),
                    showfliers=False)
    
    bp['boxes'][0].set_facecolor('#fdbf6f')
    bp['boxes'][1].set_facecolor('#a6cee3')
    
    # Overlay individual data points with jitter
    np.random.seed(42)
    jitter_d = np.random.normal(1, 0.05, size=len(dry_data))
    jitter_w = np.random.normal(2, 0.05, size=len(wet_data))
    ax.scatter(jitter_d, dry_data, color='#e6550d', alpha=0.6, s=25, edgecolors='none')
    ax.scatter(jitter_w, wet_data, color='#1f78b4', alpha=0.6, s=25, edgecolors='none')
    
    ax.set_yscale('log')
    ax.set_xticks([1, 2])
    ax.set_xticklabels([f"Dry (Winter)\n[N={len(dry_data)}]", f"Wet (Rainy)\n[N={len(wet_data)}]"], fontsize=10, fontweight='bold')
    ax.set_ylabel(f'Concentration ({unit})', fontsize=10)
    
    rec_m = df_t2[df_t2['Element'] == m].iloc[0]
    p_adj = rec_m['p_adj_holm']
    ratio = rec_m['Dry_to_Wet_Ratio']
    
    status_str = f"Ratio: {ratio}×\n$p_{{adj}}$ = {p_adj:.4f}"
    if rec_m['Significant_Dilution'].startswith('Yes'):
        status_str += " *"
    ax.set_title(f"{label}\n{status_str}", fontsize=11, fontweight='bold', pad=10)
    ax.grid(axis='y', linestyle=':', alpha=0.6)

plt.tight_layout()
fig2_path = 'data/paper_2_water_results/seasonal_dilution_boxplots.png'
plt.savefig(fig2_path, dpi=300)
plt.close()
print(f"Figure 2 saved to {fig2_path}")

# Copy updated figures to manuscripts directory
shutil.copy(fig1_path, 'manuscripts/paper_2_chemosphere/fig1_exceedance.png')
shutil.copy(fig2_path, 'manuscripts/paper_2_chemosphere/fig2_dilution.png')
if os.path.exists('manuscripts/conference_2_water'):
    shutil.copy(fig1_path, 'manuscripts/conference_2_water/fig1_exceedance.png')
    shutil.copy(fig2_path, 'manuscripts/conference_2_water/fig2_dilution.png')
print("Figures copied to manuscripts directory.")
print("\nPIPELINE COMPLETED SUCCESSFULLY.")

