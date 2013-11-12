#!/usr/local/bin/python

import pprint
import sys

sys.path.insert(0, '../starter-code')

import recommendations

def getRatingsFromFile(ratingsfile):
  
    ratingsdict = {}

    f = open(ratingsfile)

    for line in f:
        (user_id, item_id, rating, timestamp) = line.split('\t')

        if user_id not in ratingsdict:
            ratingsdict[user_id] = {}

        ratingsdict[user_id][item_id] = float(rating)

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

if __name__ == '__main__':

    ratingsfile = sys.argv[1]
    namesfile = sys.argv[2]
    n = int(sys.argv[3])
    correlation = sys.argv[4]

    ratingsdict = getRatingsFromFile(ratingsfile)

    raters = ratingsdict.keys()

    # list of tuples
    comparedRaters = {}

    # this whole thing runs in O(n^3) time, which leads it to
    # take a minute with 100,000 on my quad-core MacBook Pro
    for i in range(0, len(raters)): # O(n)

        for j in range(0, len(raters)): # O(n)

            if i != j:
                # strip out dupes!!!
                if (raters[j], raters[i]) not in comparedRaters:
                    # it looks like sim_pearson runs in O(n)
                    r = recommendations.sim_pearson(
                        ratingsdict, raters[i], raters[j]
                        )
    
                    comparedRaters[(raters[i], raters[j])] = r

    if correlation == 'agreed':
        reversesort = True
    else:
        reversesort = False

    for item in sorted(
        comparedRaters, key=comparedRaters.get, reverse=reversesort)[0:n]:
        print(
            str(comparedRaters[item]) +
                '\t' + str(item[0]) + '\t' + str(item[1])
                )

#    pprint.pprint(comparedRaters)
