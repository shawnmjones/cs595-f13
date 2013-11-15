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

if __name__ == '__main__':

    ratingsfile = sys.argv[1]
    namesfile = sys.argv[2]
    correlation = sys.argv[3]

    ratingsdict = getRatingsFromFile(ratingsfile)

    raters = ratingsdict.keys()

    if correlation == 'agreed':
        reversesort = True
    else:
        reversesort = False

    comparedRaters = {}

    for i in range(0, len(raters)): # O(n)

        best = recommendations.topMatches(ratingsdict, raters[i], n=len(raters))

        best.sort(reverse=reversesort)

        if best[0][1] == raters[i]:
            best.pop()

        # remove dupes
        if (best[0][1], raters[i]) not in comparedRaters:
            comparedRaters[(raters[i], best[0][1])] = best[0][0]

    for item in sorted(
            comparedRaters, key=comparedRaters.get, reverse=reversesort
        ):
        print str(item[0]) + '\t' + str(item[1]) + '\t' + \
            str(comparedRaters[item])
