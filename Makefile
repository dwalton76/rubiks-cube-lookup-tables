
all:
	gcc -O3 -o builder-crunch-workq builder-crunch-workq.c ida_search_core.c rotate_xxx.c -lm

gdb:
	ulimit -c unlimited
	gcc -o builder-crunch-workq builder-crunch-workq.c ida_search_core.c rotate_xxx.c -lm -ggdb

clean:
	rm -rf backup* tmp/.bsdsort* tmp/workq* tmp/* __pycache__  lookup-table.txt lookup-table.txt.diff lookup-table.txt.original *.pyc lookup-table.txt*.gz keepers.txt lookup-table.txt.tmp nohup.out

222:
	./builderui.py Build222Ultimate

333:
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

444:
	./builderui.py Build444UDCentersStage
	./utils/build-ida-graph.py Build444UDCentersStage
	./builderui.py Build444LRCentersStage
	./builderui.py Build444FBCentersStage
