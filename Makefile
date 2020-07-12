
all:
	gcc -O3 -o builder-crunch-workq builder-crunch-workq.c ida_search_core.c rotate_xxx.c -lm

clean:
	rm -rf backup* tmp/.bsdsort* tmp/workq* tmp/* __pycache__  lookup-table.txt lookup-table.txt.diff lookup-table.txt.original *.pyc lookup-table.txt*.gz keepers.txt lookup-table.txt.tmp nohup.out

