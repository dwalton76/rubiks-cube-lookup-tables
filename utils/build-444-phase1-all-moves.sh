#!/bin/bash
set -euo pipefail
cd /home/dwalton/rubiks-cube/rubiks-cube-lookup-tables
export PYTHONPATH=/home/dwalton/rubiks-cube/rubiks-cube-NxNxN-solver:/home/dwalton/rubiks-cube/rubiks-cube-lookup-tables
SOLVER_TABLES=/home/dwalton/rubiks-cube/rubiks-cube-NxNxN-solver/lookup-tables

echo "START $(date -Is)"
./utils/builderui.py Build444AllCentersStageSymmetryRanked --cores 22
./utils/builderui.py Build444LRCentersStageRanked --cores 22
./utils/builderui.py Build444HighLowEdgesEdgesAllMoves --cores 22

cp -v lookup-tables/lookup-table-4x4x4-step12-all-centers-stage-symmetry.cost-only.bin* "$SOLVER_TABLES/"
cp -v lookup-tables/lookup-table-4x4x4-step14-LR-centers-stage.cost-only.bin* "$SOLVER_TABLES/"
cp -v lookup-tables/lookup-table-4x4x4-step23-highlow-edges-edges.cost-only.bin* "$SOLVER_TABLES/"
echo "DONE $(date -Is)"
