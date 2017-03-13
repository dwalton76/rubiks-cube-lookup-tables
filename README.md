
First compile the `rotate` program
```
$ gcc -o rotate rotate.c rotate_xxx.c
```

Then there are many tables you can build
```
$ ./builder.py --help
usage: builder.py [-h] [--depth DEPTH] [--cores CORES] [--type TYPE]

optional arguments:
  -h, --help     show this help message and exit
  --depth DEPTH  The number of moves deep to explore
  --cores CORES  The number of CPU cores to use
  --type TYPE    The type of lookup table to build
$
$
$ ./builder.py --cores 4 --depth 30 --type FOOBAR
FOOBAR is an invalid --type, choices are
    2x2x2-solve
    4x4x4-FB-centers-solve
    4x4x4-LR-centers-solve
    4x4x4-LR-centers-stage
    4x4x4-UD-centers-solve
    4x4x4-UD-centers-stage
    4x4x4-ULFRBD-centers-solve
    4x4x4-ULFRBD-centers-solve-unstaged
    4x4x4-edges
    5x5x5-B-centers-solve-unstaged
    5x5x5-D-centers-solve-unstaged
    5x5x5-F-centers-solve-unstaged
    5x5x5-FB-centers-solve
    5x5x5-L-centers-solve-unstaged
    5x5x5-LR-centers-solve
    5x5x5-LR-centers-stage
    5x5x5-LR-centers-stage-t-center-only
    5x5x5-LR-centers-stage-x-center-only
    5x5x5-R-centers-solve-unstaged
    5x5x5-U-centers-solve-unstaged
    5x5x5-UD-centers-solve
    5x5x5-UD-centers-stage
    5x5x5-UD-centers-stage-T-centers
    5x5x5-UD-centers-stage-X-centers
    5x5x5-ULFRBD-centers-solve
    5x5x5-ULFRBD-centers-solve-unstaged
    6x6x6-FB-solve-inner-x-center-and-oblique-edges
    6x6x6-LFRB-solve-inner-x-center-and-oblique-edges
    6x6x6-LR-inner-x-centers-stage
    6x6x6-LR-oblique-edge-pairing
    6x6x6-LR-oblique-edge-pairing-left-only
    6x6x6-LR-oblique-edge-pairing-right-only
    6x6x6-LR-solve-inner-x-center-and-oblique-edges
    6x6x6-UD-inner-x-centers-stage
    6x6x6-UD-oblique-edge-pairing
    6x6x6-UD-oblique-edge-pairing-left-only
    6x6x6-UD-oblique-edge-pairing-right-only
    6x6x6-UD-solve-inner-x-center-and-oblique-edges
    7x7x7-FB-solve-inner-center-and-oblique-edges
    7x7x7-FB-solve-inner-x-center-t-center-and-middle-oblique-edges
    7x7x7-FB-solve-oblique-edges
    7x7x7-LFRB-solve-inner-center-and-oblique-edges
    7x7x7-LR-oblique-edge-pairing
    7x7x7-LR-oblique-edge-pairing-left-only
    7x7x7-LR-oblique-edge-pairing-middle-only
    7x7x7-LR-oblique-edge-pairing-right-only
    7x7x7-LR-solve-inner-center-and-oblique-edges
    7x7x7-LR-solve-inner-x-center-t-center-and-middle-oblique-edges
    7x7x7-LR-solve-oblique-edges
    7x7x7-UD-oblique-edge-pairing
    7x7x7-UD-oblique-edge-pairing-left-only
    7x7x7-UD-oblique-edge-pairing-middle-only
    7x7x7-UD-oblique-edge-pairing-right-only
    7x7x7-UD-solve-inner-center-and-oblique-edges
    7x7x7-UD-solve-inner-center-and-oblique-edges-center-only
    7x7x7-UD-solve-inner-center-and-oblique-edges-edges-only
```


Build one, --depth is how many moves deep you are willing to go
```
$ ./builder.py --cores 4 --depth 30 --type 4x4x4-UD-centers-stage
2017-06-27 06:50:46,674   builder.py     INFO: Level 0/29: cp lookup-table.txt lookup-table.txt.original
2017-06-27 06:50:46,674   builder.py     INFO: Level 0/29: begin gunzip workq.txt files
gzip: tmp/workq.txt*.gz: No such file or directory
2017-06-27 06:50:46,676   builder.py     INFO: Level 0/29: end   gunzip workq.txt files
2017-06-27 06:50:46,676   builder.py     INFO: 
2017-06-27 06:50:46,676   builder.py     INFO: Level 0/29: begin rotate
2017-06-27 06:50:46,676   builder.py     INFO: Level 0/29: ./rotate --input tmp/workq.txt1 --output tmp/workq-results.txt1 --type 4x4x4-UD-centers-stage
2017-06-27 06:50:46,677   builder.py     INFO: Level 0/29: ./rotate --input tmp/workq.txt2 --output tmp/workq-results.txt2 --type 4x4x4-UD-centers-stage
2017-06-27 06:50:46,678   builder.py     INFO: Level 0/29: ./rotate --input tmp/workq.txt3 --output tmp/workq-results.txt3 --type 4x4x4-UD-centers-stage
2017-06-27 06:50:46,678   builder.py     INFO: Level 0/29: ./rotate --input tmp/workq.txt4 --output tmp/workq-results.txt4 --type 4x4x4-UD-centers-stage
2017-06-27 06:50:46,680   builder.py     INFO: Level 0/29: rotate core 1: finished
2017-06-27 06:50:46,680   builder.py     INFO: Level 0/29: rotate core 2: finished
2017-06-27 06:50:46,680   builder.py     INFO: Level 0/29: rotate core 3: finished
2017-06-27 06:50:46,680   builder.py     INFO: Level 0/29: rotate core 4: finished
2017-06-27 06:50:46,680   builder.py     INFO: Level 0/29: end   rotate
```

To delete any temporary files
```
$ make clean
```

