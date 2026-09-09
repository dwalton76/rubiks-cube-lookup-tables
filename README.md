rubiks-cube-lookup-tables is the python code that was used to build the
lookup-tables that are used by [rubiks-cube-NxNxN-solver](https://github.com/dwalton76/rubiks-cube-NxNxN-solver).
If you are asking yourself "What is a rubiks cube lookup-table?" read this
[blog post](http://programmablebrick.blogspot.com/2017/07/rubiks-cube-solver.html) that explains how the solver works, it covers lookup-tables.

rubiks-cube-NxNxN-solver installs this repo as a Python module. From that repo,
`make 333-tables`, `make 444-tables`, `make 555-tables`, `make 666-tables`, and
`make 777-tables` build every table for that cube size into the solver's
`lookup-tables/` directory. A solve that needs a missing table prints the
matching target and exits.

```
sudo apt-get update
sudo apt install build-essential make python3-venv python3-dev
make init
source venv/bin/activate
```
