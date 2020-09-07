
clean:
	rm -rf tmp nohup.out build dist *.egg-info
	mkdir tmp
	find . -name __pycache__ | xargs rm -rf

init: clean
	export PYTHONPATH=/home/dwalton/rubiks-cube/rubiks-cube-NxNxN-solver/:/home/dwalton/rubiks-cube/rubiks-cube-lookup-tables/
	rm -rf venv rubikscubelookuptables/builder-crunch-workq
	gcc -O3 -o rubikscubelookuptables/builder-crunch-workq rubikscubelookuptables/builder-crunch-workq.c rubikscubelookuptables/ida_search_core.c rubikscubelookuptables/rotate_xxx.c -lm
	python3 -m venv venv
	@./venv/bin/python3 -m pip install -U pip==20.2
	@./venv/bin/python3 -m pip install --use-feature=2020-resolver -r requirements.dev.txt
	@./venv/bin/python3 -m pip install --use-feature=2020-resolver -r requirements.txt
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
	./utils/builderui.py Build333Phase1
	./utils/builderui.py Build333Phase2
	./utils/builderui.py Build333Phase2Edges
	./utils/builderui.py Build333Phase2Corners
	./utils/builderui.py Build333Phase3
	./utils/builderui.py Build333Phase3Edges
	./utils/builderui.py Build333Phase3Corners
	./utils/builderui.py Build333Phase4
	./utils/builderui.py Build333Phase4Edges
	./utils/builderui.py Build333Phase4Corners

444-phase1: clean
	./utils/builderui.py Build444UDCentersStage
	./utils/build-ida-graph.py Build444UDCentersStage
	./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step11-UD-centers-stage.json
	./utils/builderui.py Build444LRCentersStage
	./utils/build-ida-graph.py Build444LRCentersStage
	./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step12-LR-centers-stage.json
	#./utils/builderui.py Build444FBCentersStage
	#./utils/build-ida-graph.py Build444FBCentersStage
	#./utils/json-to-binary.py lookup-tables/lookup-table-4x4x4-step13-FB-centers-stage.json

444-phase2: clean
	./utils/builderui.py Build444HighLowEdgesEdges
	./utils/builderui.py Build444HighLowEdgesCenters
	./utils/builderui.py Build444HighLowEdges --depth 6

444-phase3: clean
	./utils/builderui.py Build444Reduce333Centers
	./utils/convert-to-hashed-cost-only.py lookup-tables/lookup-table-4x4x4-step32-reduce333-centers.txt 58831 helper-tables/lookup-table-4x4x4-step32-reduce333-centers.txt.starting-states.compact
	./utils/builderui.py Build444Reduce333Edges
	./utils/convert-to-hashed-cost-only.py lookup-tables/lookup-table-4x4x4-step31-reduce333-edges.txt 239500847 helper-tables/lookup-table-4x4x4-step31-reduce333-edges.txt.starting-states.compact
	./utils/builderui.py Build444Reduce333 --depth 6

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

555-phase3: clean
	./utils/builderui.py Build555LRCenterStageEOInnerOrbit
	./utils/build-ida-graph.py Build555LRCenterStageEOInnerOrbit
	./utils/json-combine.py lookup-tables/lookup-table-5x5x5-step901-LR-center-stage-EO-inner-orbit.json-1000000 lookup-tables/lookup-table-5x5x5-step901-LR-center-stage-EO-inner-orbit.json-2000000 lookup-tables/lookup-table-5x5x5-step901-LR-center-stage-EO-inner-orbit.json-3000000 lookup-tables/lookup-table-5x5x5-step901-LR-center-stage-EO-inner-orbit.json-4000000 lookup-tables/lookup-table-5x5x5-step901-LR-center-stage-EO-inner-orbit.json-5000000 lookup-tables/lookup-table-5x5x5-step901-LR-center-stage-EO-inner-orbit.json-6000000 lookup-tables/lookup-table-5x5x5-step901-LR-center-stage-EO-inner-orbit.json-7000000 lookup-tables/lookup-table-5x5x5-step901-LR-center-stage-EO-inner-orbit.json-8000000 lookup-tables/lookup-table-5x5x5-step901-LR-center-stage-EO-inner-orbit.json-9000000 lookup-tables/lookup-table-5x5x5-step901-LR-center-stage-EO-inner-orbit.json-10000000 lookup-tables/lookup-table-5x5x5-step901-LR-center-stage-EO-inner-orbit.json
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step901-LR-center-stage-EO-inner-orbit.json
	./utils/builderui.py Build555EdgeOrientOuterOrbit
	./utils/build-ida-graph.py Build555EdgeOrientOuterOrbit
	./utils/json-combine.py lookup-tables/lookup-table-5x5x5-step902-EO-outer-orbit.json-1000000 lookup-tables/lookup-table-5x5x5-step902-EO-outer-orbit.json-2000000 lookup-tables/lookup-table-5x5x5-step902-EO-outer-orbit.json
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step902-EO-outer-orbit.json

555-phase4: clean
	./utils/builderui.py Build555Phase4 --depth 3

# There are other files to build for phase 5
555-phase5: clean
	./utils/builderui.py Build555Phase5Centers
	./utils/build-ida-graph.py Build555Phase5Centers
	./utils/json-combine.py lookup-tables/lookup-table-5x5x5-step51-phase5-centers.json-1000000 lookup-tables/lookup-table-5x5x5-step51-phase5-centers.json-2000000 lookup-tables/lookup-table-5x5x5-step51-phase5-centers.json
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step51-phase5-centers.json
	./utils/builderui.py Build555Phase5FBCenters
	./utils/build-ida-graph.py Build555Phase5FBCenters
	./utils/json-to-binary.py lookup-tables/lookup-table-5x5x5-step56-phase5-fb-centers.json

555: 555-phase1 555-phase2 555-phase3 555-phase4 555-phase5 555-phase6
