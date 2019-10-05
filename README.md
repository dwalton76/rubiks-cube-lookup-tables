rubiks-cube-lookup-tables is the python code that was used to build the
lookup-tables that are used by [rubiks-cube-NxNxN-solver](https://github.com/dwalton76/rubiks-cube-NxNxN-solver).
If you are asking yourself "What is a rubiks cube lookup-table?" read this
[blog post](http://programmablebrick.blogspot.com/2017/07/rubiks-cube-solver.html) that explains how the solver works, it covers lookup-tables.

All rubiks cube lookup tables that can be constructed by the code in this repo
have already been built and are stored in an Amazon S3 bucket. It took hundreds
of hours to build these tables, you should never build them. When you run
the rubiks-cube-NxNxN-solver solver the first time it will download these tables
automatically.
