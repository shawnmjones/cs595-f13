#!/usr/local/bin/python3

import sys
import json
import networkx
from networkx.readwrite import json_graph


if __name__ == "__main__":
    inputfile = sys.argv[1]

    f = open(inputfile)
    inputdata = json.load(f)
    f.close()

    club = json_graph.node_link_graph(inputdata)

    # 4. repeat until we have 2 clusters
    while (networkx.number_connected_components(club) < 2):
        # 1. calculate edge-betweenness for all edges
        # 3. recalculate betweenness
        eb = networkx.edge_betweenness_centrality(club, weight='weight')
    
        # 2. remove the edge with highest betweenness
        # Thanks Stack Overflow:
        # http://stackoverflow.com/questions/16772071/sort-dict-by-value-python
        edge2remove = sorted(eb.items(), key=lambda x:x[1], reverse=True)[0][0]
    
        club.remove_edge(*edge2remove)

    # club should be split, sadly... :(

    outputdata = json_graph.node_link_data(club)

    print(json.dumps(outputdata, indent=4))
