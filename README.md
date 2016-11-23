# Incremental-Subgraph-Feature Selection for Graph Classification

There are two main entries in this codes:

1. _featureGeneration.py: Python programs to generate the training features and testing features.

help: _featureGeneration.py <upperbound | lowerbound | lable_threshold | t | support>
	
	[upperbound]: Option, select cascades whose length is more than upperbound
	[lowerbound]: Option, select cascades whose length is less than lowerbound
	[lable_threshold]: Option, classification bound, the lable of cascade whose length is more than lable_threshold is "1", otherwise is "-1"
	[t]: Option, select part cascade whose time delay is less than t in each cascade
	[support]: Option, support threshold for sequetial pattern mining

	Example: python _featureGeneration.py 400 100 300 363250 70

2. mainEntry.m: The matlab programs which include optimazation part and classification part.

The results will be wrote to SSF.dat, OSF.dat, MSF.data and RSF.dat respectively.

Example: (using the exampleData.dat)
1. python _featureGeneration.py 35 15 36 5 12
2. run mainEntry.m
