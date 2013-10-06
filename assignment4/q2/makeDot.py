#!/usr/local/bin/python3

import sys
import os
import json

if __name__ == "__main__":
    searchdir = sys.argv[1]

    print("digraph linkForest {")

    for root, _, files in os.walk(searchdir):
        for filename in files:
            f = open( os.path.join( root, filename ) )
            data = f.read() 
            f.close()

            info = json.loads(data)

            (uri, links) = info.popitem()

            for link in links:
              
                link = link.replace('"', '%22')

                print(
                    '"' + uri + '" -> "' + link + '"' + 
                    ' [ label = "' + uri + ' links to ' + link + '" ];' 
                    )

    print("}")
