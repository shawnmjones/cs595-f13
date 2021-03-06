#!/usr/local/bin/python3

import json

f = open("zachary.dat")
inputlines = f.readlines()
f.close()

outputDict = { "nodes" : [], "links" : [] }

nodeCounter = 0

# skip the unnecessary lines
# the header information (lines 0 - 6) isn't useful to us
# the matrix from lines 7 to 34 is just the mapping of
# connections, with no weights
for row in inputlines[7 + 34:]:
    name = nodeCounter + 1

    newNode = { 'id' : str(name) }

    outputDict['nodes'].append( newNode )

    columns = row.split()

    for j in range(len(columns)):

        if columns[j] != "0":
            
            weight = int(columns[j])
            source = nodeCounter
            target = j

            newLink = \
                { "source" : source, "target" : target, "weight" : weight }

            outputDict['links'].append( newLink )

    nodeCounter += 1

print(json.dumps(outputDict))
