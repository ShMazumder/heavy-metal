#!/bin/bash
# Package data files for Zenodo upload
set -e
OUTDIR="manuscripts/submissions/zenodo_deposit"
mkdir -p "$OUTDIR"

echo "Packaging Zenodo deposit..."

# Core database
cp data/processed/heavy_metal.db        "$OUTDIR/"
cp data/processed/water_data.csv        "$OUTDIR/"
cp data/processed/sediment_data.csv     "$OUTDIR/"
cp data/processed/stations.csv          "$OUTDIR/"
cp data/processed/studies.csv           "$OUTDIR/"
cp data/processed/master_harmonized.csv "$OUTDIR/"
cp data/processed/station_hydrorivers_matched.csv "$OUTDIR/"

# GIS layers
cp data/raw/hydrorivers_bangladesh.gpkg "$OUTDIR/"
cp data/raw/bangladesh_boundary.geojson "$OUTDIR/"

# Metadata
cp .zenodo.json "$OUTDIR/"

# Create README for the deposit
cat > "$OUTDIR/README.txt" << 'EOF'
==============================================================================
Heavy Metal Geospatial Database — Bangladesh Rivers (2010–2024)
==============================================================================

CONTENTS:
  heavy_metal.db                  Master SQLite relational database (4 tables)
  water_data.csv                  Surface water assays (268 rows × 49 cols)
  sediment_data.csv               Bed sediment assays (289 rows × 32 cols)
  stations.csv                    Observation stations (426 rows × 14 cols)
  studies.csv                     Study metadata & instrumentation (28 rows)
  master_harmonized.csv           Denormalized master table (557 rows × 59 cols)
  station_hydrorivers_matched.csv Topological reach join table (213 unique stations)
  hydrorivers_bangladesh.gpkg     HydroSHEDS HydroRIVERS clipped network
  bangladesh_boundary.geojson     National boundary polygon (WGS84)

COORDINATE SYSTEM: EPSG:4326 (WGS84)
LICENSE: CC-BY 4.0
CODE: https://github.com/ShMazumder/heavy-metal
EOF

# Create ZIP archive
(cd "$OUTDIR" && zip -r ../zenodo_heavy_metal_database_v1.0.0.zip ./)

echo ""
echo "Done. Upload this file to Zenodo:"
echo "  manuscripts/submissions/zenodo_heavy_metal_database_v1.0.0.zip"
echo ""
ls -lh manuscripts/submissions/zenodo_heavy_metal_database_v1.0.0.zip
