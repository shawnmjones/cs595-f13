#!/usr/local/bin/python3

import sys
import os
import os.path
import feedparser
import urllib.request
import time
from bs4 import BeautifulSoup

def dereferenceUri(uri):

    pagehandle = urllib.request.urlopen(uri)
    pagedata = pagehandle.readall()
    pagehandle.close()

    return pagedata

def getAtomFeedUri(html):

    soup = BeautifulSoup(html) 

    atomLinks = soup.find_all('link',
        attrs = { 'rel' : 'alternate', 'type' : 'application/atom+xml' })

    # we assume there is only one atom link
    atomURI = atomLinks[0].attrs['href']

    return atomURI

def meetsCriteria(feedText):

    parsedData = feedparser.parse(feedText)

    # assume we're good to go by default (fail optimistic?)
    goodToGo = True

    if (len(parsedData.entries) < 25):
        goodToGo = False        

    return goodToGo

def saveFeed(feedText, outputDir):

    feedData = feedparser.parse(feedText)

    o = open(outputDir + '/' + feedData.feed.title, 'wb')
    o.write(feedText)
    o.close()

def getNextUri():

    uri = "http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117"

    pagehandle = urllib.request.urlopen(uri)
    nexturi = pagehandle.geturl()
    pagehandle.close() 

    return nexturi


if __name__ == "__main__":

    seedUri = sys.argv[1]
    outputDir = sys.argv[2]

    # make directory for storage of atom feeds
    if not os.path.exists(outputDir):
        os.mkdir(outputDir)

    uri = seedUri

    # TODO: change to stop when we have 100 saved files?
    while (len(os.listdir(outputDir)) < 100):

        try:
            # dereference the uri and get text
            html = dereferenceUri(uri)
        except urllib.error.HTTPError as e:
            print("failed to dereference " + uri + ", delaying 5 seconds")
            time.sleep(5)
        else:
            # fetch the atom feed URI
            feedURI = getAtomFeedUri(html)
   
            try:
                # get the atom feed text
                feedText = dereferenceUri(feedURI)
            except urllib.error.HTTPError as e:
                print("failed to dereference " + feedURI + ", delaying 5 seconds")
                time.sleep(5)
            else:
                # if it meets the criteria, save the file
                if meetsCriteria(feedText):
                    print("Saving blog feed to " + outputDir)
                    saveFeed(feedText, outputDir)
    
                # Tried these steps, but realized I would have to parse JavaScript
                # * look for the iframe containing the next button
                #       <iframe name='navbar-iframe'...
                # iframeURI = getIframeUri(html)
                # * dereference the link from that iframe
                # iframeText = getIframeText(iframeURI)
                # * extract the uri form <a class="b-link" href="...">Next Blog</a>
                # uri = getNextUri(iframeText)
    
                # be nice to the site
                time.sleep(1)

        try:
            uri = getNextUri()
        except urllib.error.HTTPError as e:
            print("failed to acquire next uri, delaying 5 seconds")
            time.sleep(5)
            uri = getNextUri()
