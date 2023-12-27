
clean:
	rm -rf tmp nohup.out build dist *.egg-info
	mkdir tmp
	find . -name __pycache__ | xargs rm -rf

init: clean
	export PYTHONPATH=/storage/dwalton76/rubiks-cube-NxNxN-solver/:/storage/dwalton76/rubiks-cube-lookup-tables/
	rm -rf venv rubikscubelookuptables/builder-crunch-workq
	gcc -O3 -o rubikscubelookuptables/builder-crunch-workq rubikscubelookuptables/builder-crunch-workq.c rubikscubelookuptables/ida_search_core.c rubikscubelookuptables/rotate_xxx.c -lm
	python3 -m venv venv
	@./venv/bin/python3 -m pip install -U pip
	@./venv/bin/python3 -m pip install -r requirements.dev.txt -r requirements.txt
	@./venv/bin/python3 -m pip check

gdb:
	ulimit -c unlimited
	gcc -o rubikscubelookuptables/builder-crunch-workq rubikscubelookuptables/builder-crunch-workq.c rubikscubelookuptables/ida_search_core.c rubikscubelookuptables/rotate_xxx.c -lm --ggdb

format:
	@./venv/bin/isort rubikscubelookuptables/
	@./venv/bin/isort utils/
	@./venv/bin/python3 -m black --config=pyproject.toml .
	@./venv/bin/python3 -m flake8 --config=.flake8

wheel:
	@./venv/bin/python3 setup.py bdist_wheel

222: clean
	nice ./utils/builderui.py Build222Ultimate --cores 8

333: clean
	nice ./utils/builderui.py Build333MicroPythonPhase1
	nice ./utils/builderui.py Build333MicroPythonPhase2
	nice ./utils/builderui.py Build333MicroPythonPhase2Edges
	nice ./utils/builderui.py Build333MicroPythonPhase2Corners
	nice ./utils/builderui.py Build333MicroPythonPhase3
	nice ./utils/builderui.py Build333MicroPythonPhase3Edges
	nice ./utils/builderui.py Build333MicroPythonPhase3Corners
	nice ./utils/builderui.py Build333MicroPythonPhase4
	nice ./utils/builderui.py Build333MicroPythonPhase4Edges
	nice ./utils/builderui.py Build333MicroPythonPhase4Corners

444-phase1: clean
	nice ./utils/builderui.py Build444UDCentersStage
	nice ./utils/build-ida-graph.py Build444UDCentersStage
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step11-UD-centers-stage.json

	nice ./utils/builderui.py Build444LRCentersStage
	nice ./utils/build-ida-graph.py Build444LRCentersStage
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step12-LR-centers-stage.json

	nice ./utils/builderui.py Build444LCentersStage
	nice ./utils/build-ida-graph.py Build444LCentersStage
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step13-L-centers-stage.json

444-phase2: clean
	nice ./utils/builderui.py Build444HighLowEdgesEdges
	nice ./utils/build-ida-graph.py Build444HighLowEdgesEdges
	nice ./utils/json-combine.py lookup-tables/lookup-table-4x4x4-step21-highlow-edges-edges.json
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step21-highlow-edges-edges.json

	nice ./utils/builderui.py Build444HighLowEdgesCenters
	nice ./utils/build-ida-graph.py Build444HighLowEdgesCenters
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step22-highlow-edges-centers.json

444-phase3: clean
	nice ./utils/builderui.py Build444Reduce333FirstTwoCenters
	nice ./utils/build-ida-graph.py Build444Reduce333FirstTwoCenters
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step31-centers.json

	nice ./utils/builderui.py Build444Reduce333FirstFourEdges
	nice ./utils/build-ida-graph.py Build444Reduce333FirstFourEdges
	nice ./utils/json-combine.py lookup-tables/lookup-table-4x4x4-step32-first-four-edges.json
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step32-first-four-edges.json

	nice ./utils/builderui.py Build444Reduce333Centers
	nice ./utils/build-ida-graph.py Build444Reduce333Centers
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step41-centers.json

	nice ./utils/builderui.py Build444Reduce333LastEightEdges
	nice ./utils/build-ida-graph.py Build444Reduce333LastEightEdges
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step42-last-eight-edges.json

444: 444-phase1 444-phase2 444-phase3

555-phase1: clean
	nice ./utils/builderui.py Build555LRCenterStageTCenter
	nice ./utils/build-ida-graph.py Build555LRCenterStageTCenter
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step11-LR-centers-stage-t-center-only.json

	nice ./utils/builderui.py Build555LRCenterStageXCenter
	nice ./utils/build-ida-graph.py Build555LRCenterStageXCenter
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step12-LR-centers-stage-x-center-only.json

555-phase2: clean
	nice ./utils/builderui.py Build555FBTCenterStage
	nice ./utils/build-ida-graph.py Build555FBTCenterStage
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step21-FB-t-centers-stage.json

	nice ./utils/builderui.py Build555FBXCenterStage
	nice ./utils/build-ida-graph.py Build555FBXCenterStage
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step22-FB-x-centers-stage.json

	nice ./utils/builderui.py Build555Phase2LRCenterStage
	nice ./utils/build-ida-graph.py Build555Phase2LRCenterStage
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step23-LR-center-stage.json

555-phase3: clean
	nice ./utils/builderui.py Build555Phase3LRCenterStage
	nice ./utils/build-ida-graph.py Build555Phase3LRCenterStage
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step901-LR-center-stage.json

	# The json-to-binary.py steps take ~16G of RAM
	nice ./utils/builderui.py Build555EdgeOrientOuterOrbit
	nice ./utils/build-ida-graph.py Build555EdgeOrientOuterOrbit
	nice ./utils/json-combine.py lookup-tables/lookup-table-5x5x5-step902-EO-outer-orbit.json
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step902-EO-outer-orbit.json

	nice ./utils/builderui.py Build555EdgeOrientInnerOrbit
	nice ./utils/build-ida-graph.py Build555EdgeOrientInnerOrbit
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step903-EO-inner-orbit.json

555-phase4: clean
	nice ./utils/builderui.py Build555Phase4 --depth 3

555-phase5: clean
	# This takes a lot of RAM...run on an ec2 instance
	nice ./utils/builderui.py Build555Phase5Centers
	nice ./utils/build-ida-graph.py Build555Phase5Centers
	nice ./utils/json-combine.py lookup-tables/lookup-table-5x5x5-step51-phase5-centers.json
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step51-phase5-centers.json

	nice ./utils/builderui.py Build555Phase5HighEdgeMidge
	nice ./utils/build-ida-graph.py Build555Phase5HighEdgeMidge
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step53-phase5-high-edge-and-midge.json

	nice ./utils/builderui.py Build555Phase5LowEdgeMidge
	nice ./utils/build-ida-graph.py Build555Phase5LowEdgeMidge
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step54-phase5-low-edge-and-midge.json

	nice ./utils/builderui.py Build555Phase5FBCenters
	nice ./utils/build-ida-graph.py Build555Phase5FBCenters
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step56-phase5-fb-centers.json

555-phase6: clean
	nice ./utils/builderui.py Build555Phase6Centers
	nice ./utils/build-ida-graph.py Build555Phase6Centers
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step61-phase6-centers.json

	nice ./utils/builderui.py Build555Phase6HighEdgeMidge
	nice ./utils/build-ida-graph.py Build555Phase6HighEdgeMidge
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step62-phase6-high-edge-midge.json

	nice ./utils/builderui.py Build555Phase6LowEdgeMidge
	nice ./utils/build-ida-graph.py Build555Phase6LowEdgeMidge
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step63-phase6-low-edge-midge.json

555-solve-staged-centers: clean
	nice ./utils/builderui.py Build555UDCenterSolve
	nice ./utils/build-ida-graph.py Build555UDCenterSolve
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step34-UD-centers-solve.json

	nice ./utils/builderui.py Build555LRCenterSolve
	nice ./utils/build-ida-graph.py Build555LRCenterSolve
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step35-LR-centers-solve.json

	nice ./utils/builderui.py Build555FBCenterSolve
	nice ./utils/build-ida-graph.py Build555FBCenterSolve
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step36-FB-centers-solve.json

555: 555-phase1 555-phase2 555-phase3 555-phase4 555-phase5 555-phase6 555-solve-staged-centers

666-phase1: clean
	nice ./utils/builderui.py Build666LRInnerXCentersStage
	nice ./utils/build-ida-graph.py Build666LRInnerXCentersStage
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step00-inner-x-centers-stage.json

666-phase3: clean
	nice ./utils/builderui.py Build666UDInnerXCentersStage
	nice ./utils/build-ida-graph.py Build666UDInnerXCentersStage
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step11-UD-inner-x-centers-stage.json

	nice ./utils/builderui.py Build666UDXCentersStage
	nice ./utils/build-ida-graph.py Build666UDXCentersStage
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step12-UD-x-centers.json

	nice ./utils/builderui.py Build666UDLeftObliqueCentersStage
	nice ./utils/build-ida-graph.py Build666UDLeftObliqueCentersStage
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step13-UD-left-oblique-centers.json

	nice ./utils/builderui.py Build666UDRightObliqueCentersStage
	nice ./utils/build-ida-graph.py Build666UDRightObliqueCentersStage
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step14-UD-right-oblique-centers.json

	nice ./utils/builderui.py Build666UDObliqueCentersStage
	nice ./utils/build-perfect-hash.py lookup-tables/lookup-table-6x6x6-step15-UD-oblique-centers.txt

	nice ./utils/builderui.py Build666UDLeftObliqueInnerXCentersStage
	nice ./utils/build-perfect-hash.py lookup-tables/lookup-table-6x6x6-step16-UD-left-oblique-inner-x-centers.txt

	nice ./utils/builderui.py Build666UDRightObliqueInnerXCentersStage
	nice ./utils/build-perfect-hash.py lookup-tables/lookup-table-6x6x6-step17-UD-right-oblique-inner-x-centers.txt

666-phase5: clean
	nice ./utils/builderui.py Build666Step50LRCenters
	nice ./utils/build-ida-graph.py Build666Step50LRCenters
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step50-LR-solve-inner-x-center-and-oblique-edges.json

	nice ./utils/builderui.py Build666Step50HighLowEdges
	nice ./utils/build-ida-graph.py Build666Step50HighLowEdges
	nice ./utils/json-combine.py lookup-tables/lookup-table-6x6x6-step51-highlow-edges.json
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step51-highlow-edges.json

666-phase6: clean
	nice ./utils/builderui.py Build666UDInnerXCenterAndObliqueEdges
	nice ./utils/build-ida-graph.py Build666UDInnerXCenterAndObliqueEdges
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step61-UD-solve-inner-x-center-and-oblique-edges.json

	nice ./utils/builderui.py Build666FBInnerXCenterAndObliqueEdges
	nice ./utils/build-ida-graph.py Build666FBInnerXCenterAndObliqueEdges
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step62-FB-solve-inner-x-center-and-oblique-edges.json

	nice ./utils/builderui.py Build666LRObliqueEdges
	nice ./utils/build-ida-graph.py Build666LRObliqueEdges
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step63-LR-oblique-edges.json

666: 666-phase4 666-phase5 666-phase6

777-phase4: clean
	nice ./utils/builderui.py Build777Phase4TCenters
	nice ./utils/build-ida-graph.py Build777Phase4TCenters
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-phase4-t-centers.json

	nice ./utils/builderui.py Build777Phase4XCenters
	nice ./utils/build-ida-graph.py Build777Phase4XCenters
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-phase4-x-centers.json

	nice ./utils/builderui.py Build777Phase4Centers
	nice ./utils/build-perfect-hash.py lookup-tables/lookup-table-7x7x7-phase4-inner-centers.txt

	nice ./utils/builderui.py Build777Phase4LeftOblique
	nice ./utils/build-ida-graph.py Build777Phase4LeftOblique
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-phase4-left-oblique.json

	nice ./utils/builderui.py Build777Phase4RightOblique
	nice ./utils/build-ida-graph.py Build777Phase4RightOblique
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-phase4-right-oblique.json

	nice ./utils/builderui.py Build777Phase4MiddleOblique
	nice ./utils/build-ida-graph.py Build777Phase4MiddleOblique
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-phase4-middle-oblique.json

	nice ./utils/builderui.py Build777Phase4LeftRightOblique
	nice ./utils/build-perfect-hash.py lookup-tables/lookup-table-7x7x7-phase4-left-right-oblique.txt

	nice ./utils/builderui.py Build777Phase4LeftMiddleOblique
	nice ./utils/build-perfect-hash.py lookup-tables/lookup-table-7x7x7-phase4-left-middle-oblique.txt

777-phase5:
	nice ./utils/builderui.py Build777Phase5LeftOblique
	nice ./utils/build-ida-graph.py Build777Phase5LeftOblique
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-phase5-left-oblique.json

	nice ./utils/builderui.py Build777Phase5RightOblique
	nice ./utils/build-ida-graph.py Build777Phase5RightOblique
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-phase5-right-oblique.json

	nice ./utils/builderui.py Build777Phase5MiddleOblique
	nice ./utils/build-ida-graph.py Build777Phase5MiddleOblique
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-phase5-middle-oblique.json

	nice ./utils/builderui.py Build777Phase5LeftRightOblique
	nice ./utils/build-perfect-hash.py lookup-tables/lookup-table-7x7x7-phase5-left-right-oblique.txt

	nice ./utils/builderui.py Build777Phase5LeftMiddleOblique
	nice ./utils/build-perfect-hash.py lookup-tables/lookup-table-7x7x7-phase5-left-middle-oblique.txt

777-phase7: clean
	nice ./utils/builderui.py Build777Step41
	nice ./utils/build-ida-graph.py Build777Step41
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step41.json

	nice ./utils/builderui.py Build777Step42
	nice ./utils/build-ida-graph.py Build777Step42
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step42.json

	nice ./utils/builderui.py Build777Step43
	nice ./utils/build-ida-graph.py Build777Step43
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step43.json

	nice ./utils/builderui.py Build777Step44
	nice ./utils/build-ida-graph.py Build777Step44
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step44.json

777-phase8: clean
	nice ./utils/builderui.py Build777Step51
	nice ./utils/build-ida-graph.py Build777Step51
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step51.json

	nice ./utils/builderui.py Build777Step52
	nice ./utils/build-ida-graph.py Build777Step52
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step52.json

	nice ./utils/builderui.py Build777Step53
	nice ./utils/build-ida-graph.py Build777Step53
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step53.json

	nice ./utils/builderui.py Build777Step54
	nice ./utils/build-ida-graph.py Build777Step54
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step54.json

	nice ./utils/builderui.py Build777Step55
	nice ./utils/build-ida-graph.py Build777Step55
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step55.json

777-phase9: clean
	nice ./utils/builderui.py Build777Step61
	nice ./utils/build-ida-graph.py Build777Step61
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step61.json

	nice ./utils/builderui.py Build777Step62
	nice ./utils/build-ida-graph.py Build777Step62
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step62.json

	nice ./utils/builderui.py Build777Step65
	nice ./utils/build-ida-graph.py Build777Step65
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step65.json

	nice ./utils/builderui.py Build777Step66
	nice ./utils/build-ida-graph.py Build777Step66
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step66.json

777-phase-solve-t-centers: clean
	nice ./utils/builderui.py Build777Step71
	nice ./utils/build-ida-graph.py Build777Step71
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step71.json

	nice ./utils/builderui.py Build777Step72
	nice ./utils/build-ida-graph.py Build777Step72
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step72.json

	nice ./utils/builderui.py Build777Step75
	nice ./utils/build-ida-graph.py Build777Step75
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step75.json

	nice ./utils/builderui.py Build777Step76
	nice ./utils/build-ida-graph.py Build777Step76
	nice ./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step76.json

777: 777-phase7 777-phase8 777-phase9 777-phase-solve-t-centers
