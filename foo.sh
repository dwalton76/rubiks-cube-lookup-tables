#!/bin/bash

./utils/expand-state-with-centers-solved.py --centers-filename centers_solutions_555.txt --lookup-table-filename lookup-table-5x5x5-step100-stage-first-six-edges.txt --start 0 --end 50000 &
./utils/expand-state-with-centers-solved.py --centers-filename centers_solutions_555.txt --lookup-table-filename lookup-table-5x5x5-step100-stage-first-six-edges.txt --start 50001 --end 100000 &
./utils/expand-state-with-centers-solved.py --centers-filename centers_solutions_555.txt --lookup-table-filename lookup-table-5x5x5-step100-stage-first-six-edges.txt --start 100001 --end 150000 &
./utils/expand-state-with-centers-solved.py --centers-filename centers_solutions_555.txt --lookup-table-filename lookup-table-5x5x5-step100-stage-first-six-edges.txt --start 150001 --end 200000 &

#./utils/expand-state-with-centers-solved.py --centers-filename horse_shoe_centers_solutions_555.txt --lookup-table-filename lookup-table-5x5x5-step100-solve-first-six-edges.txt --start 0 --end 2300000 --specific-depth 17 &
#./utils/expand-state-with-centers-solved.py --centers-filename horse_shoe_centers_solutions_555.txt --lookup-table-filename lookup-table-5x5x5-step100-solve-first-six-edges.txt --start 2300001 --end 4600000 --specific-depth 17 &
#./utils/expand-state-with-centers-solved.py --centers-filename horse_shoe_centers_solutions_555.txt --lookup-table-filename lookup-table-5x5x5-step100-solve-first-six-edges.txt --start 4600001 --end 6900000 --specific-depth 17 &
#./utils/expand-state-with-centers-solved.py --centers-filename horse_shoe_centers_solutions_555.txt --lookup-table-filename lookup-table-5x5x5-step100-solve-first-six-edges.txt --start 6900001 --end 9200000 --specific-depth 17 &
#./utils/expand-state-with-centers-solved.py --centers-filename horse_shoe_centers_solutions_555.txt --lookup-table-filename lookup-table-5x5x5-step100-solve-first-six-edges.txt --start 9200001 --end 11500000 --specific-depth 17 &
#./utils/expand-state-with-centers-solved.py --centers-filename horse_shoe_centers_solutions_555.txt --lookup-table-filename lookup-table-5x5x5-step100-solve-first-six-edges.txt --start 11500001 --end 14000000 --specific-depth 17 &


#./utils/expand-state-with-centers-solved-no-pickle.py --centers-filename horse_shoe_centers_solutions_555.txt --lookup-table-filename lookup-table-5x5x5-step100-solve-first-six-edges.txt --specific-depth 17
