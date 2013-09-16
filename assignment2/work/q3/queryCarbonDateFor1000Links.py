#!/usr/local/bin/python3

import sys
import urllib.request
import json

def queryCarbonDate(cduri, uri):

    if cduri[-1] != '/':
        cduri += '/'

    sys.stderr.write("Using cduri = " + cduri + "\n")
    sys.stderr.write("Requesting " + cduri + uri + "\n")
    sys.stderr.flush()

    request = urllib.request.urlopen(cduri + uri)
    pagedata = request.readall().decode('utf-8')
    request.close()

    data = json.loads(pagedata)

    return data['Estimated Creation Date']

if __name__ == '__main__':
    cduri = sys.argv[1]
    urifile = sys.argv[2]
    
    f = open(urifile)
    
    for line in f:
        cdate = queryCarbonDate(cduri, line.strip())
        print(cdate + ":" + line.strip())
        sys.stdout.flush()
    
    f.close()
