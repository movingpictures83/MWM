# MWM
# Language: Python
# Input: CSV (network)
# Output: Screen (list of edges)
# Tested with: PluMA 1.1, Python 3.6
# Dependency: numpy==1.16.0

PluMA plugin that runs the Maximum Weighted Matching algorithm (Galil, 1986)
to help discover central edges in a network.

The idea is to compute the maximum weighted matching once for the original network,
and then for each edge, remove it and recompute the maximum weighted matching.
Those that when were removed caused the biggest change in overall weight of the maximum
matching, the plugin outputs as central edges.

The plugin expects as input a network in CSV format, where rows and columns represent
nodes and internal entries the edge weights, for example if A(i, j) = k then there
is an edge from node i to node j with weight k.  Zero weights equate to no edge.

Original Python implementation of Maximum Weighted Matching can be found here:
https://github.com/mlbright/Assignment-Problem/blob/master/mwmatching.py


