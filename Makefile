
222:
	make clean
	./builder.py --cores 4 --depth 20 --type 2x2x2-solve

444:
	make clean
	./builder.py --cores 4 --depth 20 --type 4x4x4-UD-centers-stage
	make clean
	./builder.py --cores 4 --depth 20 --type 4x4x4-LR-centers-stage
	make clean
	./builder.py --cores 4 --depth 20 --type 4x4x4-LFRB-centers-solve

# ./utils/print-moves.py builds steps-3x3x3-preserved-LFRB-depth-9.txt which is needed to build the slice-forward and slice-backward tables
555:
	./utils/print-moves.py
	make clean
	./builder.py --cores 4 --depth 8 --type 5x5x5-UD-centers-stage
	make clean
	./builder.py --cores 4 --depth 20 --type 5x5x5-UD-centers-stage-T-centers
	make clean
	./builder.py --cores 4 --depth 20 --type 5x5x5-UD-centers-stage-X-centers
	make clean
	./builder.py --cores 4 --depth 20 --type 5x5x5-LR-centers-stage
	make clean
	./builder.py --cores 4 --depth 8 --type 5x5x5-ULFRBD-centers-solve
	make clean
	./builder.py --cores 4 --depth 20 --type 5x5x5-UDLR-centers-solve

666:
	make clean
	./builder.py --cores 4 --depth 20 --type 6x6x6-UD-inner-x-centers-stage
	make clean
	./builder.py --cores 4 --depth 8 --type 6x6x6-UD-oblique-edge-pairing
	make clean
	./builder.py --cores 4 --depth 20 --type 6x6x6-UD-oblique-edge-pairing-left-only
	make clean
	./builder.py --cores 4 --depth 20 --type 6x6x6-UD-oblique-edge-pairing-right-only
	make clean
	./builder.py --cores 4 --depth 20 --type 6x6x6-LR-inner-x-centers-stage
	make clean
	./builder.py --cores 4 --depth 20 --type 6x6x6-LR-oblique-pairing
	make clean
	./builder.py --cores 4 --depth 20 --type 6x6x6-UD-centers-solve
	make clean
	./builder.py --cores 4 --depth 10 --type 6x6x6-LFRB-centers-solve
	make clean
	./builder.py --cores 4 --depth 20 --type 6x6x6-LR-centers-solve
	make clean
	./builder.py --cores 4 --depth 20 --type 6x6x6-FB-centers-solve

777:
	make clean
	./builder.py --cores 4 --depth 7 --type 7x7x7-UD-oblique-edge-pairing
	make clean
	./builder.py --cores 4 --depth 20 --type 7x7x7-UD-oblique-edge-pairing-middle-only
	make clean
	./builder.py --cores 4 --depth 20 --type 7x7x7-UD-oblique-edge-pairing-outside-only

clean:
	rm -rf backup* tmp/.bsdsort* tmp/workq* tmp/* __pycache__  lookup-table.txt lookup-table.txt.diff lookup-table.txt.original *.pyc lookup-table.txt*.gz keepers.txt lookup-table.txt.tmp
