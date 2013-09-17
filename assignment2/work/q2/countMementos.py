#!/usr/local/bin/python3

import re
import sys
import urllib.request

MEMENTOPATTERN = re.compile(r'rel="[^"]*memento[^"]*"')

def getTimeMap(uri):
    
    urit = "http://mementoproxy.cs.odu.edu/aggr/timemap/link/" + uri

    try:
        request = urllib.request.urlopen(urit)

        if request.getcode() == 200:
            timemap = request.readall()
            request.close()
        else:
            timemap = None
            request.close()

    except urllib.error.HTTPError as e:
        timemap = None

    except urllib.error.URLError as e:
        timemap = None

    return timemap


def countMementos(uri):

    urit = getTimeMap(uri)

    if not urit:
        count = 0
    else:
        count = len(MEMENTOPATTERN.findall(str(urit)))

    return count
    

if __name__ == "__main__":
    inputfile = sys.argv[1]
    
    f = open(inputfile)

    for uri in f:

        mementoCount = countMementos(uri.strip())

        print(str(mementoCount) + "\t" + uri.strip())
        sys.stdout.flush()

    f.close()
