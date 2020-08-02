
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
	isort rubikscubelookuptables utils
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
	./utils/json-to-utilsary.py lookup-table-4x4x4-step11-UD-centers-stage.json
	./utils/builderui.py Build444LRCentersStage
	./utils/build-ida-graph.py Build444LRCentersStage
	./utils/json-to-utilsary.py lookup-table-4x4x4-step12-LR-centers-stage.json
	./utils/builderui.py Build444FBCentersStage
	./utils/build-ida-graph.py Build444FBCentersStage
	./utils/json-to-utilsary.py lookup-table-4x4x4-step13-FB-centers-stage.json

444-phase2: clean
	./utils/builderui.py Build444HighLowEdgesEdges
	./utils/builderui.py Build444HighLowEdgesCenters
	./utils/builderui.py Build444HighLowEdges --depth 6

444-phase3: clean
	./utils/builderui.py Build444Reduce333Centers
	./utils/convert-to-hashed-cost-only.py lookup-table-4x4x4-step32-reduce333-centers.txt 58831 helper-tables/lookup-table-4x4x4-step32-reduce333-centers.txt.starting-states.compact
	./utils/builderui.py Build444Reduce333Edges
	./utils/convert-to-hashed-cost-only.py lookup-table-4x4x4-step31-reduce333-edges.txt 239500847 helper-tables/lookup-table-4x4x4-step31-reduce333-edges.txt.starting-states.compact
	./utils/builderui.py Build444Reduce333 --depth 6

444: 444-phase1 444-phase2 444-phase3
