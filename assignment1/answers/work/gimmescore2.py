#!/usr/local/bin/python3

import sys
import time
import urllib.request
import re
from bs4 import BeautifulSoup

class GimmeScoreException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

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

    trs = soup.find_all('tr')

    for tr in trs:
        if school in tr.text:
            break

    if not tr.text:
        raise GimmeScoreException('School "' + school + '" not found in scores this week, maybe try again another day?')

    if '@' in tr.text:
        raise GimmeScoreException('School "' + school + '" found, but game has not started yet')

    # get rid of unnecessary whitespace
    structuredData = tr.text.strip()

    # insert commas for delimiting
    structuredData = structuredData.replace('\n\n\n', ',').replace('-', ',')

    # get rid of the unneded 'Final', if game is finished
    structuredData = structuredData.replace('\nFinal', '').strip()

    # get rid of the unneeded team ranking, if present
    structuredData = re.sub(r'\([0-9]+\)', '', structuredData).strip()

    # create a list of data
    structuredData = structuredData.split(',')

    # fill the game dictionary with the data
    game = {}
    game['school1'] = structuredData[0].strip()
    game['score1'] = structuredData[1].strip()
    game['score2'] = structuredData[2].strip()
    game['school2'] = structuredData[3].strip()

    return game

def main(args):

    try:
        school = args[1]
        refresh = int(args[2])
        uri = args[3]
    except (IndexError, e):
        usage()
        sys.exit(1)

    try:
        while(True):
            webpage = fetchCurrentScore(uri)
            game = getScoresFromPage(webpage, school)

            printCurrentScore(
                game['school1'], game['score1'], game['school2'], game['score2']
                )
            time.sleep(refresh)
    except GimmeScoreException as e:
        print(e.value)


if __name__ == '__main__':
    main(sys.argv)
