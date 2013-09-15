#!/usr/local/bin/python3

import sys
import re
import urllib.request

# for IRI support, thank you evitan for your 0-point answer that was helpful:
# http://stackoverflow.com/questions/4389572/how-to-fetch-a-non-ascii-url-with-python-urlopen
import httplib2 

URLPATTERN = re.compile("http://[\S]*")

def extractURIsFromLine(line):
    """
        Attempts to extract the URIs from the string given.

        Unfortunately, it requires the global URLPATTERN for performance.
    """

    return URLPATTERN.findall(line)

    

def extractRealSupportedURI(uri):
    """
        Returns "real" URI if it survives redirects and returns a 200.

        Returns None otherwise.
    """

    realURI = None

    try:
        # this function follows the URI, resolving all redirects,
        # and detects redirect loops
        # iri2uri is needed for IRIs
        request = urllib.request.urlopen(httplib2.iri2uri(uri))
        
        if request.getcode() == 200:
            realURI = request.geturl()

    except urllib.error.HTTPError as e:
        # something went wrong, we don't care what
        realURI = None

    except urllib.error.URLError as e:
        # something went wrong, we don't care what
        realURI = None

    except UnicodeError as e:
        # something went very wrong with the IRI decoding
        realURI = None

    return realURI

if __name__ == "__main__":

    filenames = sys.argv[1:]

    for filename in filenames:
        f = open(filename)
    
        for line in f:
            sys.stderr.write("Working on: " + line + '\n') 
            uris = extractURIsFromLine(line)
    
            for uri in uris:
                sys.stderr.write("Trying URI: [" + uri + ']\n')
                goodURI = extractRealSupportedURI(uri)
    
                if goodURI:
                    print(goodURI)
       
        f.close()
