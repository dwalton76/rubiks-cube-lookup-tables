#!/bin/bash

#./utils/expand-state-with-centers-solved.py --centers-filename centers_solutions_555.txt --lookup-table-filename lookup-table-5x5x5-step100-stage-first-six-edges.txt --start 0 --end 800 &
#./utils/expand-state-with-centers-solved.py --centers-filename centers_solutions_555.txt --lookup-table-filename lookup-table-5x5x5-step100-stage-first-six-edges.txt --start 801 --end 1600 &
#./utils/expand-state-with-centers-solved.py --centers-filename centers_solutions_555.txt --lookup-table-filename lookup-table-5x5x5-step100-stage-first-six-edges.txt --start 1601 --end 2400 &
#./utils/expand-state-with-centers-solved.py --centers-filename centers_solutions_555.txt --lookup-table-filename lookup-table-5x5x5-step100-stage-first-six-edges.txt --start 2401 --end 3200 &

./utils/expand-state-with-centers-solved.py --centers-filename horse_shoe_centers_solutions_555.txt --lookup-table-filename lookup-table-5x5x5-step100-solve-first-six-edges.txt --start 0 --end 800 &
./utils/expand-state-with-centers-solved.py --centers-filename horse_shoe_centers_solutions_555.txt --lookup-table-filename lookup-table-5x5x5-step100-solve-first-six-edges.txt --start 801 --end 1600 &
./utils/expand-state-with-centers-solved.py --centers-filename horse_shoe_centers_solutions_555.txt --lookup-table-filename lookup-table-5x5x5-step100-solve-first-six-edges.txt --start 1601 --end 2400 &
./utils/expand-state-with-centers-solved.py --centers-filename horse_shoe_centers_solutions_555.txt --lookup-table-filename lookup-table-5x5x5-step100-solve-first-six-edges.txt --start 2401 --end 3200 &

