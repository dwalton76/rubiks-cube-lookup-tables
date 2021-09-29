
clean:
	rm -rf tmp nohup.out build dist *.egg-info
	mkdir tmp
	find . -name __pycache__ | xargs rm -rf

init: clean
	export PYTHONPATH=/home/dwalton/rubiks-cube/rubiks-cube-NxNxN-solver/:/home/dwalton/rubiks-cube/rubiks-cube-lookup-tables/
	rm -rf venv rubikscubelookuptables/builder-crunch-workq
	gcc -O3 -o rubikscubelookuptables/builder-crunch-workq rubikscubelookuptables/builder-crunch-workq.c rubikscubelookuptables/ida_search_core.c rubikscubelookuptables/rotate_xxx.c -lm
	python3 -m venv venv
	@./venv/bin/python3 -m pip install -U pip==20.3.1
	@./venv/bin/python3 -m pip install -r requirements.dev.txt
	@./venv/bin/python3 -m pip install -r requirements.txt
	@./venv/bin/python3 -m pre_commit install --install-hooks --overwrite
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
	./utils/builderui.py Build222Ultimate

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

444-phase1: clean
	./utils/builderui.py Build444UDCentersStage
	./utils/build-ida-graph.py Build444UDCentersStage
	./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step11-UD-centers-stage.json

	./utils/builderui.py Build444LRCentersStage
	./utils/build-ida-graph.py Build444LRCentersStage
	./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step12-LR-centers-stage.json

	./utils/builderui.py Build444LCentersStage
	./utils/build-ida-graph.py Build444LCentersStage
	./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step13-L-centers-stage.json

444-phase2: clean
	./utils/builderui.py Build444HighLowEdgesEdges
	./utils/build-ida-graph.py Build444HighLowEdgesEdges
	./utils/json-combine.py lookup-tables/lookup-table-4x4x4-step21-highlow-edges-edges.json-1000000 lookup-tables/lookup-table-4x4x4-step21-highlow-edges-edges.json-2000000 lookup-tables/lookup-table-4x4x4-step21-highlow-edges-edges.json
	./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step21-highlow-edges-edges.json

	./utils/builderui.py Build444HighLowEdgesCenters
	./utils/build-ida-graph.py Build444HighLowEdgesCenters
	./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step22-highlow-edges-centers.json

444-phase3: clean
	./utils/builderui.py Build444Reduce333FirstTwoCenters
	./utils/build-ida-graph.py Build444Reduce333FirstTwoCenters
	./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step31-centers.json

	./utils/builderui.py Build444Reduce333FirstFourEdges
	./utils/build-ida-graph.py Build444Reduce333FirstFourEdges
	./utils/json-combine.py lookup-tables/lookup-table-4x4x4-step32-first-four-edges.json-1000000 lookup-tables/lookup-table-4x4x4-step32-first-four-edges.json-2000000 lookup-tables/lookup-table-4x4x4-step32-first-four-edges.json-3000000 lookup-tables/lookup-table-4x4x4-step32-first-four-edges.json-4000000 lookup-tables/lookup-table-4x4x4-step32-first-four-edges.json-5000000 lookup-tables/lookup-table-4x4x4-step32-first-four-edges.json
	./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step32-first-four-edges.json

	./utils/builderui.py Build444Reduce333Centers
	./utils/build-ida-graph.py Build444Reduce333Centers
	./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step41-centers.json

	./utils/builderui.py Build444Reduce333LastEightEdges
	./utils/build-ida-graph.py Build444Reduce333LastEightEdges
	./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step42-last-eight-edges.json

444: 444-phase1 444-phase2 444-phase3

555-phase1: clean
	./utils/builderui.py Build555LRCenterStageTCenter
	./utils/build-ida-graph.py Build555LRCenterStageTCenter
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step11-LR-centers-stage-t-center-only.json

	./utils/builderui.py Build555LRCenterStageXCenter
	./utils/build-ida-graph.py Build555LRCenterStageXCenter
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step12-LR-centers-stage-x-center-only.json

555-phase2: clean
	./utils/builderui.py Build555FBTCenterStage
	./utils/build-ida-graph.py Build555FBTCenterStage
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step21-FB-t-centers-stage.json

	./utils/builderui.py Build555FBXCenterStage
	./utils/build-ida-graph.py Build555FBXCenterStage
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step22-FB-x-centers-stage.json

	./utils/builderui.py Build555Phase2LRCenterStage
	./utils/build-ida-graph.py Build555Phase2LRCenterStage
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step23-LR-center-stage.json

555-phase3: clean
	./utils/builderui.py Build555Phase3LRCenterStage
	./utils/build-ida-graph.py Build555Phase3LRCenterStage
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step901-LR-center-stage.json

	# This takes a lot of RAM...run on an ec2 instance
	./utils/builderui.py Build555EdgeOrientOuterOrbit
	./utils/build-ida-graph.py Build555EdgeOrientOuterOrbit
	./utils/json-combine.py lookup-tables/lookup-table-5x5x5-step902-EO-outer-orbit.json-1000000 lookup-tables/lookup-table-5x5x5-step902-EO-outer-orbit.json-2000000 lookup-tables/lookup-table-5x5x5-step902-EO-outer-orbit.json
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step902-EO-outer-orbit.json

	./utils/builderui.py Build555EdgeOrientInnerOrbit
	./utils/build-ida-graph.py Build555EdgeOrientInnerOrbit
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step903-EO-inner-orbit.json

555-phase4: clean
	./utils/builderui.py Build555Phase4 --depth 3

555-phase5: clean
	# This takes a lot of RAM...run on an ec2 instance
	./utils/builderui.py Build555Phase5Centers
	./utils/build-ida-graph.py Build555Phase5Centers
	./utils/json-combine.py lookup-tables/lookup-table-5x5x5-step51-phase5-centers.json-1000000 lookup-tables/lookup-table-5x5x5-step51-phase5-centers.json-2000000 lookup-tables/lookup-table-5x5x5-step51-phase5-centers.json
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step51-phase5-centers.json

	./utils/builderui.py Build555Phase5HighEdgeMidge
	./utils/build-ida-graph.py Build555Phase5HighEdgeMidge
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step53-phase5-high-edge-and-midge.json

	./utils/builderui.py Build555Phase5LowEdgeMidge
	./utils/build-ida-graph.py Build555Phase5LowEdgeMidge
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step54-phase5-low-edge-and-midge.json

	./utils/builderui.py Build555Phase5FBCenters
	./utils/build-ida-graph.py Build555Phase5FBCenters
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step56-phase5-fb-centers.json

555-phase6: clean
	./utils/builderui.py Build555Phase6Centers
	./utils/build-ida-graph.py Build555Phase6Centers
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step61-phase6-centers.json

	./utils/builderui.py Build555Phase6HighEdgeMidge
	./utils/build-ida-graph.py Build555Phase6HighEdgeMidge
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step62-phase6-high-edge-midge.json

	./utils/builderui.py Build555Phase6LowEdgeMidge
	./utils/build-ida-graph.py Build555Phase6LowEdgeMidge
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step63-phase6-low-edge-midge.json

555-solve-staged-centers: clean
	./utils/builderui.py Build555UDCenterSolve
	./utils/build-ida-graph.py Build555UDCenterSolve
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step34-UD-centers-solve.json

	./utils/builderui.py Build555LRCenterSolve
	./utils/build-ida-graph.py Build555LRCenterSolve
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step35-LR-centers-solve.json

	./utils/builderui.py Build555FBCenterSolve
	./utils/build-ida-graph.py Build555FBCenterSolve
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step36-FB-centers-solve.json

555: 555-phase1 555-phase2 555-phase3 555-phase4 555-phase5 555-phase6 555-solve-staged-centers

666-phase1: clean
	./utils/builderui.py Build666LRInnerXCentersStage
	./utils/build-ida-graph.py Build666LRInnerXCentersStage
	./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step00-inner-x-centers-stage.json

666-phase3: clean
	./utils/builderui.py Build666UDInnerXCentersStage
	./utils/build-ida-graph.py Build666UDInnerXCentersStage
	./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step11-UD-inner-x-centers-stage.json

	./utils/builderui.py Build666UDXCentersStage
	./utils/build-ida-graph.py Build666UDXCentersStage
	./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step12-UD-x-centers.json

	./utils/builderui.py Build666UDLeftObliqueCentersStage
	./utils/build-ida-graph.py Build666UDLeftObliqueCentersStage
	./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step13-UD-left-oblique-centers.json

	./utils/builderui.py Build666UDRightObliqueCentersStage
	./utils/build-ida-graph.py Build666UDRightObliqueCentersStage
	./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step14-UD-right-oblique-centers.json

666-phase5: clean
	./utils/builderui.py Build666Step50LRCenters
	./utils/build-ida-graph.py Build666Step50LRCenters
	./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step50-LR-solve-inner-x-center-and-oblique-edges.json

	./utils/builderui.py Build666Step50HighLowEdges
	./utils/build-ida-graph.py Build666Step50HighLowEdges
	./utils/json-combine.py lookup-tables/lookup-table-6x6x6-step51-highlow-edges.json-1000000 lookup-tables/lookup-table-6x6x6-step51-highlow-edges.json-2000000 lookup-tables/lookup-table-6x6x6-step51-highlow-edges.json
	./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step51-highlow-edges.json

666-phase6: clean
	./utils/builderui.py Build666UDInnerXCenterAndObliqueEdges
	./utils/build-ida-graph.py Build666UDInnerXCenterAndObliqueEdges
	./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step61-UD-solve-inner-x-center-and-oblique-edges.json

	./utils/builderui.py Build666FBInnerXCenterAndObliqueEdges
	./utils/build-ida-graph.py Build666FBInnerXCenterAndObliqueEdges
	./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step62-FB-solve-inner-x-center-and-oblique-edges.json

	./utils/builderui.py Build666LRObliqueEdges
	./utils/build-ida-graph.py Build666LRObliqueEdges
	./utils/json-to-binary.py lookup-tables/lookup-table-6x6x6-step63-LR-oblique-edges.json

666: 666-phase4 666-phase5 666-phase6

777-phase45: clean
	./utils/builderui.py Build777Phase45TCenters
	./utils/build-ida-graph.py Build777Phase45TCenters
	./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step11-phase45-t-centers.json

	./utils/builderui.py Build777Phase45XCenters
	./utils/build-ida-graph.py Build777Phase45XCenters
	./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step12-phase45-x-centers.json

	./utils/builderui.py Build777Phase45Centers
	./utils/build-perfect-hash.py lookup-tables/lookup-table-7x7x7-step13-inner-centers.txt

777-phase5:
	./utils/builderui.py Build777Phase5LeftRightOblique
	./utils/builderui.py Build777Phase5LeftMiddleOblique

777-phase7: clean
	./utils/builderui.py Build777Step41
	./utils/build-ida-graph.py Build777Step41
	./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step41.json

	./utils/builderui.py Build777Step42
	./utils/build-ida-graph.py Build777Step42
	./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step42.json

	./utils/builderui.py Build777Step43
	./utils/build-ida-graph.py Build777Step43
	./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step43.json

	./utils/builderui.py Build777Step44
	./utils/build-ida-graph.py Build777Step44
	./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step44.json

777-phase8: clean
	./utils/builderui.py Build777Step51
	./utils/build-ida-graph.py Build777Step51
	./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step51.json

	./utils/builderui.py Build777Step52
	./utils/build-ida-graph.py Build777Step52
	./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step52.json

	./utils/builderui.py Build777Step53
	./utils/build-ida-graph.py Build777Step53
	./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step53.json

	./utils/builderui.py Build777Step54
	./utils/build-ida-graph.py Build777Step54
	./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step54.json

	./utils/builderui.py Build777Step55
	./utils/build-ida-graph.py Build777Step55
	./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step55.json

777-phase9: clean
	./utils/builderui.py Build777Step61
	./utils/build-ida-graph.py Build777Step61
	./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step61.json

	./utils/builderui.py Build777Step62
	./utils/build-ida-graph.py Build777Step62
	./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step62.json

	./utils/builderui.py Build777Step65
	./utils/build-ida-graph.py Build777Step65
	./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step65.json

	./utils/builderui.py Build777Step66
	./utils/build-ida-graph.py Build777Step66
	./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step66.json

777-phase-solve-t-centers: clean
	./utils/builderui.py Build777Step71
	./utils/build-ida-graph.py Build777Step71
	./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step71.json

	./utils/builderui.py Build777Step72
	./utils/build-ida-graph.py Build777Step72
	./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step72.json

	./utils/builderui.py Build777Step75
	./utils/build-ida-graph.py Build777Step75
	./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step75.json

	./utils/builderui.py Build777Step76
	./utils/build-ida-graph.py Build777Step76
	./utils/json-to-binary.py lookup-tables/lookup-table-7x7x7-step76.json

777: 777-phase7 777-phase8 777-phase9 777-phase-solve-t-centers
