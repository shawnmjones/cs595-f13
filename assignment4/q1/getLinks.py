#!/usr/local/bin/python3

import sys
import os
import os.path
import shutil
import json
from urllib.parse import urlparse

from bs4 import BeautifulSoup

def processLinks(uri, links):
    """
        Rules:
            * If it doesn't start with http[s]://, then:
                * if it starts with #, then replace with uri
                * if it starts with 'javascript:', we don't know where it goes,
                    throw it out, as mentioned in class
                * if it starts with /, prepend the scheme and netloc from
                    urlparse to it
            * If it contains ?, strip out everything after ? <-- not done
    """

    fixedLinks = []

    mainpr = urlparse(uri)
    mainscheme = mainpr[0]
    mainnetloc = mainpr[1]
    mainpath = '/' if not mainpr[2] else mainpr[2]
    mainparams = mainpr[3]
    mainquery = mainpr[4]
    mainfrag = mainpr[5]

    for link in links:

        linkpr = urlparse(link)
        scheme = mainscheme if not linkpr[0] else linkpr[0]
        netloc = mainnetloc if not linkpr[1] else linkpr[1]
        path = '/' if not linkpr[2] else linkpr[2]
        params = linkpr[3]
        query = linkpr[4]
        frag = linkpr[5]

        if scheme != 'javascript':
            if path:
                if path[0] != '/':
                    path = mainpath + path 

            fixedLink = scheme + '://' + netloc + path + params

            if query:
                fixedLink = fixedLink + '?' + query

            fixedLinks.append(fixedLink)

    # we only care about the set of links, not how many
    fixedLinks = list(set(fixedLinks))

    return fixedLinks
        

def extractLinks(data):
    soup = BeautifulSoup(data)
    links = []

    for a in soup.find_all('a', href=True):
        links.append(a['href']) 

    return links

if __name__ == "__main__":
    urilist = sys.argv[1]
    searchdir = sys.argv[2]
    outputdir = sys.argv[3]

    if os.path.exists(outputdir):
        if os.path.isdir(outputdir):
            shutil.rmtree(outputdir)
        else:
            sys.stderr.write('cannot remove ' + outputdir)
            sys.exit(212)

    os.mkdir(outputdir)

    f = open(urilist)

    filelist = {}

    for line in f:
        (uri, checksum) = line.split()
        fname = checksum + '.raw'
        filelist[fname] = uri

    f.close()

    for root, _, files in os.walk(searchdir):
        for filename in files:
            if filename in filelist:
                f = open( os.path.join(root, filename) )
                data = f.read()
                f.close()

                linkDict = {}

                uri = filelist[filename]

                links = extractLinks(data)
                links = processLinks(uri, links)
                linkDict[uri] = links 

                outputfile = filename.replace('.raw', '.links.json')
                o = open( os.path.join(outputdir, outputfile), 'w' )
                o.write(
                    json.dumps(linkDict, sort_keys=True, 
                    indent =4, separators=(',', ': ') )
                    )
                o.close()
