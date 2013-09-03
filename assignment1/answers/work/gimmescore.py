#!/usr/local/bin/python3

import sys
import time
import urllib.request
import re
from bs4 import BeautifulSoup

def usage():
    print("")
    print("Usage:  " + sys.argv[0] + " <school name> <refresh> <uri>")
    print("  where:")
    print("    school name - name of school from which to display scores")
    print("    refresh - number of seconds to refresh the score")
    print("    uri - URI to use for score lookup")
    print("")

def printCurrentScore(school1, score1, school2, score2):

    print(school1 + " " + score1 + ", " + school2 + " " + score2)

def fetchCurrentScore(uri):

    pagehandle = urllib.request.urlopen(uri)
    pagedata = pagehandle.readall()
    pagehandle.close()
    return pagedata
    

def getScoresFromPage(webpage, school):

    soup = BeautifulSoup(webpage)

    scripts = soup.find_all('script')

    # the HTML is buried in some JavaScript
    for script in scripts:
        if school in script.text:
            break

    # strip out all of the weird backslash JavaScript stuff
    htmlish = script.text.replace("\\n", '').replace('\\', '')
    soup = BeautifulSoup(htmlish)
    rows = soup.find_all('tr')

    for row in rows:
        if school in row.text:
            break

    structuredData = row.text.replace('Final', '')
    structuredData = re.sub(r'\([0-9]+\)', '', structuredData)
    structuredData = re.sub(r'[ ]{2,}', ',', structuredData)
    structuredData = structuredData.strip(',')
    structuredData = structuredData.replace(' - ', ',')
    structuredData = structuredData.split(',')

    game = {}
    game['school1'] = structuredData[0]
    game['score1'] = structuredData[1]
    game['score2'] = structuredData[2]
    game['school2'] = structuredData[3]

    return game

def main(args):

    try:
        school = args[1]
        refresh = int(args[2])
        uri = args[3]
    except (IndexError, e):
        usage()
        sys.exit(1)

    while(True):
        webpage = fetchCurrentScore(uri)
        game = getScoresFromPage(webpage, school)

        printCurrentScore(
            game['school1'], game['score1'], game['school2'], game['score2']
            )
        time.sleep(refresh)


if __name__ == '__main__':
    main(sys.argv)
