
clean:
	rm -rf tmp nohup.out build dist *.egg-info
	mkdir tmp
	find . -name __pycache__ | xargs rm -rf

init: clean
	export PYTHONPATH=/home/dwalton/rubiks-cube/rubiks-cube-NxNxN-solver/:/home/dwalton/rubiks-cube/rubiks-cube-lookup-tables/
	rm -rf venv rubikscubelookuptables/builder-crunch-workq rubikscubelookuptables/compact-center-symmetry-cost rubikscubelookuptables/compact-center-symmetry-777 rubikscubelookuptables/builder-find-new-states utils/pad-lines
	gcc -O3 -o rubikscubelookuptables/builder-crunch-workq rubikscubelookuptables/builder-crunch-workq.c rubikscubelookuptables/ida_search_core.c rubikscubelookuptables/rotate_xxx.c -lm
	gcc -O3 -o rubikscubelookuptables/compact-center-symmetry-cost rubikscubelookuptables/compact-center-symmetry-cost.c
	gcc -O3 -pthread -o rubikscubelookuptables/compact-center-symmetry-777 rubikscubelookuptables/compact-center-symmetry-777.c
	gcc -O3 -o rubikscubelookuptables/builder-find-new-states rubikscubelookuptables/builder-find-new-states.c
	gcc -O3 -o utils/pad-lines utils/pad-lines.c
	python3 -m venv venv
	@./venv/bin/python3 -m pip install -U pip==26.2.1
	@./venv/bin/python3 -m pip install -r requirements.dev.txt
	@./venv/bin/python3 -m pip install -r requirements.txt
	@./venv/bin/python3 -m pip check

gdb:
	ulimit -c unlimited
	gcc -o rubikscubelookuptables/builder-crunch-workq rubikscubelookuptables/builder-crunch-workq.c rubikscubelookuptables/ida_search_core.c rubikscubelookuptables/rotate_xxx.c -lm --ggdb

# Every python file git knows about: tracked, plus new files that are not ignored.
# This honors .gitignore at every level, which keeps the generated modules named in
# rubikscubelookuptables/.gitignore (builder555ss.py is 61MB) away from the formatters.
FORMAT_FILES = $(shell git ls-files --cached --others --exclude-standard -- '*.py' '*.pyi')

format:
	@./venv/bin/isort $(FORMAT_FILES)
	@./venv/bin/python3 -m black --config=pyproject.toml $(FORMAT_FILES)
	@./venv/bin/python3 -m flake8 --config=.flake8 $(FORMAT_FILES)

# The builder tests all stage intermediate files in ./tmp, so they have to run one
# at a time. Do not add -n/xdist here. Test builds write tables under
# tmp/test-lookup-tables and do not append histogram.txt.
test:
	RUBIKS_LOOKUP_TABLE_DIR=tmp/test-lookup-tables RUBIKS_SKIP_HISTOGRAM=1 ./venv/bin/python3 -m pytest -vv tests/

test-lite:
	RUBIKS_LOOKUP_TABLE_DIR=tmp/test-lookup-tables RUBIKS_SKIP_HISTOGRAM=1 ./venv/bin/python3 -m pytest -vv tests/ -k "not test_build_" --ignore=tests/test_builder_determinism.py

wheel:
	@./venv/bin/python3 setup.py bdist_wheel

333: clean
	./utils/builderui.py Build333MicroPythonPhase1
	./utils/builderui.py Build333MicroPythonPhase2
	./utils/builderui.py Build333MicroPythonPhase2Edges
	./utils/builderui.py Build333MicroPythonPhase2Corners
	./utils/builderui.py Build333MicroPythonPhase3
	./utils/builderui.py Build333MicroPythonPhase3Edges
	./utils/builderui.py Build333MicroPythonPhase3Corners
	./utils/builderui.py Build333MicroPythonPhase4
	./utils/builderui.py Build333MicroPythonPhase4Edges
	./utils/builderui.py Build333MicroPythonPhase4Corners

444-phase1-ranked: clean
	./utils/builderui.py Build444AllCentersStageSymmetryRanked --cores 22
	./utils/builderui.py Build444LRCentersStageRanked --cores 22
	./utils/builderui.py Build444HighLowEdgesEdgesAllMoves --cores 22

444-centers: clean
	./utils/builderui.py Build444Reduce333Centers --cores 22

444-pair-all-edges: clean
	./utils/builderui.py Build444PairAllEdges

444: 444-phase1-ranked 444-centers 444-pair-all-edges

555-phase1: clean
	./utils/builderui.py Build555LRCenterStageTCenter

	./utils/builderui.py Build555LRCenterStageXCenter

555-phase2: clean
	./utils/builderui.py Build555FBTCenterStage

	./utils/builderui.py Build555FBXCenterStage

555-phase3: clean
	./utils/builderui.py Build555Phase3LRCenterStage
	./utils/builderui.py Build555EdgeOrientOuterOrbit
	./utils/builderui.py Build555EdgeOrientInnerOrbit

555-phase4: clean
	./utils/builderui.py Build555Phase4 --depth 7 --cores 10

555-phase5: clean
	# Combo tables are 576,240,000-byte ranked cost arrays; centers is 24,010,000.
	./utils/builderui.py Build555Phase5Centers --cores 10
	./utils/builderui.py Build555Phase5FBCentersHighEdgeMidge --cores 10
	./utils/builderui.py Build555Phase5FBCentersLowEdgeMidge --cores 10

555-phase6: clean
	# Combo table used only to build a perfect-hash file for IDA (~813 million states).
	./utils/builderui.py Build555PairLastEightEdgesEdgesOnly
	./utils/build-perfect-hash.py lookup-tables/lookup-table-5x5x5-step501-pair-last-eight-edges-edges-only.txt

	./utils/builderui.py Build555Phase6Centers
	./utils/build-ida-graph.py Build555Phase6Centers
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step61-phase6-centers.json

	./utils/builderui.py Build555Phase6HighEdgeMidge
	./utils/build-ida-graph.py Build555Phase6HighEdgeMidge
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step62-phase6-high-edge-midge.json

	./utils/builderui.py Build555Phase6LowEdgeMidge
	./utils/build-ida-graph.py Build555Phase6LowEdgeMidge
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step63-phase6-low-edge-midge.json

555: 555-phase1 555-phase2 555-phase3 555-phase4 555-phase5 555-phase6

666-phase1:
	./utils/builderui.py Build666Phase1LRInnerXCentersStageBinary --cores 10

666-phase2:
	./utils/builderui.py Build666Phase2UDInnerXCentersStageBinary --cores 10

666-phase3-preserve-inner-x: clean
	./utils/builderui.py Build666Phase3UDLeftRightObliqueCentersStage
	./utils/builderui.py Build666Phase3UDLeftObliqueOuterXCentersStage
	./utils/builderui.py Build666Phase3UDRightObliqueOuterXCentersStage

666-phase5:
	./utils/builderui.py Build666DaisyAllInnerXPlusUDObliquesCenters --cores 22
	./utils/builderui.py Build666DaisyAllInnerXPlusLRObliquesCenters --cores 22
	./utils/builderui.py Build666DaisyAllInnerXPlusFBObliquesCenters --cores 22

666: 666-phase1 666-phase2 666-phase3-preserve-inner-x 666-phase5

777-phase2: clean
	./utils/builderui.py Build777Phase2UDInnerCentersStage

777-phase5-6-ranked: clean
	./utils/builderui.py Build777Phase56UDLeftRightObliqueCentersStage --cores 22
	./utils/builderui.py Build777Phase56UDLeftMiddleObliqueCentersStage --cores 22
	./utils/builderui.py Build777Phase56UDLeftObliqueOuterXCentersStage --cores 22
	./utils/builderui.py Build777Phase56UDMiddleRightObliqueCentersStage --cores 22
	./utils/builderui.py Build777Phase56UDRightObliqueOuterXCentersStage --cores 22
	./utils/builderui.py Build777Phase56UDMiddleObliqueOuterXCentersStage --cores 22

777-daisy-ranked: clean
	./utils/builderui.py Build777DaisyUDWithoutLeftObliqueCenters --cores 22
	./utils/builderui.py Build777DaisyUDWithoutMiddleObliqueCenters --cores 22
	./utils/builderui.py Build777DaisyUDWithoutRightObliqueCenters --cores 22
	./utils/builderui.py Build777DaisyUDWithoutInnerTCenters --cores 22
	./utils/builderui.py Build777DaisyUDWithoutInnerXCenters --cores 22
	./utils/builderui.py Build777DaisyLRWithoutLeftObliqueCenters --cores 22
	./utils/builderui.py Build777DaisyLRWithoutMiddleObliqueCenters --cores 22
	./utils/builderui.py Build777DaisyLRWithoutRightObliqueCenters --cores 22
	./utils/builderui.py Build777DaisyLRWithoutInnerTCenters --cores 22
	./utils/builderui.py Build777DaisyLRWithoutInnerXCenters --cores 22
	./utils/builderui.py Build777DaisyFBWithoutLeftObliqueCenters --cores 22
	./utils/builderui.py Build777DaisyFBWithoutMiddleObliqueCenters --cores 22
	./utils/builderui.py Build777DaisyFBWithoutRightObliqueCenters --cores 22
	./utils/builderui.py Build777DaisyFBWithoutInnerTCenters --cores 22
	./utils/builderui.py Build777DaisyFBWithoutInnerXCenters --cores 22

# Optional fallback, built only if the 70^4 search is too slow. The BFS needs 70^5
# bytes of scratch but publishes a 314 MiB cost table plus symmetry index, shared
# by all three axes.
777-daisy-perfect: rubikscubelookuptables/compact-center-symmetry-777
	./utils/builderui.py Build777DaisyPerfectCenters --cores 22

# Native-goal twin of 777-daisy-perfect, used by 9x9x9 and larger.
777-solve-perfect: rubikscubelookuptables/compact-center-symmetry-777
	./utils/builderui.py Build777SolvePerfectCenters --cores 22

777: 777-phase2 777-phase5-6-ranked
