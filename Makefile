
all:
	gcc -O3 -o builder-crunch-workq builder-crunch-workq.c ida_search_core.c rotate_xxx.c -lm

env:
	python3 -m venv venv
	@./venv/bin/python3 -m pip install -U pip==20.2
	@./venv/bin/python3 -m pip install setuptools==49.2.0 pyhashxx==0.1.3

gdb:
	ulimit -c unlimited
	gcc -o builder-crunch-workq builder-crunch-workq.c ida_search_core.c rotate_xxx.c -lm -ggdb

clean:
	rm -rf backup* tmp/.bsdsort* tmp/workq* tmp/* __pycache__  lookup-table.txt lookup-table.txt.diff lookup-table.txt.original *.pyc lookup-table.txt*.gz keepers.txt lookup-table.txt.tmp nohup.out

format:
	isort -rc *.py utils

222: clean
	./builderui.py Build222Ultimate

333: clean
	./builderui.py Build333Phase1
	./builderui.py Build333Phase2
	./builderui.py Build333Phase2Edges
	./builderui.py Build333Phase2Corners
	./builderui.py Build333Phase3
	./builderui.py Build333Phase3Edges
	./builderui.py Build333Phase3Corners
	./builderui.py Build333Phase4
	./builderui.py Build333Phase4Edges
	./builderui.py Build333Phase4Corners

444-phase1: clean
	./builderui.py Build444UDCentersStage
	./utils/build-ida-graph.py Build444UDCentersStage
	./utils/json-to-binary.py lookup-table-4x4x4-step11-UD-centers-stage.json
	./builderui.py Build444LRCentersStage
	./utils/build-ida-graph.py Build444LRCentersStage
	./utils/json-to-binary.py lookup-table-4x4x4-step12-LR-centers-stage.json
	./builderui.py Build444FBCentersStage
	./utils/build-ida-graph.py Build444FBCentersStage
	./utils/json-to-binary.py lookup-table-4x4x4-step13-FB-centers-stage.json

444-phase2: clean
	./builderui.py Build444HighLowEdgesEdges
	./builderui.py Build444HighLowEdgesCenters
	./builderui.py Build444HighLowEdges --depth 6

444-phase3: clean
	./builderui.py StartingStates444Reduce333Centers
	./builderui.py Build444Reduce333Centers
	./utils/convert-to-hashed-cost-only.py lookup-table-4x4x4-step32-reduce333-centers.txt 58831 lookup-table-4x4x4-step32-reduce333-centers.txt.starting-states.compact
	./builderui.py Build444Reduce333Edges
	./utils/convert-to-hashed-cost-only.py lookup-table-4x4x4-step31-reduce333-edges.txt 239500847 lookup-table-4x4x4-step31-reduce333-edges.txt.starting-states.compact
	./builderui.py Build444Reduce333 --depth 6

444: 444-phase1 444-phase2 444-phase3
