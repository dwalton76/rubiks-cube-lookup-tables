rubiks-cube-lookup-tables is the python code that was used to build the
lookup-tables that are used by [rubiks-cube-NxNxN-solver](https://github.com/dwalton76/rubiks-cube-NxNxN-solver).
If you are asking yourself "What is a rubiks cube lookup-table?" read this
[blog post](http://programmablebrick.blogspot.com/2017/07/rubiks-cube-solver.html) that explains how the solver works, it covers lookup-tables.


All rubiks cube lookup tables that can be constructed by the code in this repo
have already been built and are available in the following repos. When you run
the rubiks-cube-NxNxN-solver solver the first time it will download these tables
automatically.
- https://github.com/dwalton76/rubiks-cube-lookup-tables-4x4x4
- https://github.com/dwalton76/rubiks-cube-lookup-tables-5x5x5
- https://github.com/dwalton76/rubiks-cube-lookup-tables-6x6x6
- https://github.com/dwalton76/rubiks-cube-lookup-tables-7x7x7

The following are all of the tables that can be built. NOTE that some of
these tables can take hours (or maybe even days) to build while others
are small and can build in a few minutes.
- Build444UDCentersStage
- Build444LRCentersStage
- Build444FBCentersStage
- Build444ULFRBDCentersStage
- Build444HighLowEdgesEdges
- Build444HighLowEdgesCenters
- Build444HighLowEdges
- Build444Reduce333Edges
- Build444Reduce333Centers
- Build444Reduce333
- Build555UDCenterStage
- Build555UDCenterStageTCenterOnly
- Build555UDCenterStageXCenterOnly
- Build555LRCenterStage
- Build555LRTCenterStage
- Build555LRXCenterStage
- Build555ULFRBDCenterSolveUnstaged
- Build555ULFRBDCenterSolve
- Build555ULCenterSolve
- Build555UFCenterSolve
- Build555LFCenterSolve
- Build555ULFRBDTCenterSolveTake
- Build555EdgesStageFirstFour
- Build555ULFRBDCenterSolveUnstagedEdgesStageSecondFour
- Build555EdgesStageSecondFour
- Build555EdgesSolveFirstFour
- Build555EdgesSolveSecondFour
- Build555ULFRBDCenterSolveUnstagedEdgesLastFourXPlane
- Build555EdgesLastFourXPlane
- Build666UDInnerXCentersStage
- Build666LRInnerXCentersObliqueEdgesStage
- Build666LRObliqueEdgesStage
- Build666LRInnerXCenterStage
- Build666Step50
- Build666LFRBInnerXCenterAndObliqueEdges
- Build666LRInnerXCenterAndObliqueEdges
- Build666FBInnerXCenterAndObliqueEdges
- Build777Step40
- Build777Step41
- Build777Step42
- Build777Step50
- Build777Step51
- Build777Step52
- Build777Step60
- Build777Step61
- Build777Step62


To build all states for the Build444UDCentersStage table do:
```
$ ./builderui.py Build444UDCentersStage
// go get coffee
$
```

To build all states up to 4-moves deep for the Build444UDCentersStage table do:
```
$ ./builderui.py Build444UDCentersStage --depth 4
// go get coffee
$
```


To delete any temporary files
```
$ make clean
```
