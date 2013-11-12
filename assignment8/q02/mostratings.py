#!/usr/local/bin/python3

import sys
import codecs

def getRatingsFromFile(ratingsfile):
  
    ratingsdict = {}

    f = open(ratingsfile)

    for line in f:
        (user_id, item_id, rating, timestamp) = line.split('\t')

        # deal with new items
        if item_id not in ratingsdict:
            ratingsdict[item_id] = []

        ratingsdict[item_id].append(int(rating))

    f.close()

    return ratingsdict

def getMovieNames(namesfile):

    namesdict = {}

    f = codecs.open(namesfile, 'r', 'iso-8859-1')

    for line in f:
        (id, name) = line.split('|')[0:2]
        namesdict[id] = name

    f.close()

    return namesdict

def getRatingsCount(ratingsdict):

    countlist = []

    for key in ratingsdict:
        countlist.append( ( len(ratingsdict[key]), key ) )

    return sorted(countlist, reverse=True)

def getTopN(countlist, n):

    return countlist[0:n]

if __name__ == '__main__':
    topratingsCount = int(sys.argv[1])
    ratingsfile = sys.argv[2]
    namesfile = sys.argv[3]

    ratingsdict = getRatingsFromFile(ratingsfile)
    averagelist = getRatingsCount(ratingsdict)
    topN = getTopN(averagelist, topratingsCount)

    namesdict = getMovieNames(namesfile)

    for i in topN:
        print(namesdict[i[1]] + '\t' + str(i[0]))
    
