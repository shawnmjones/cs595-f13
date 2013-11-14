#!/usr/local/bin/python

import sys
import pprint

sys.path.insert(0, '../starter-code')

import recommendations

if __name__ == '__main__':

    film = sys.argv[1]
    n = int(sys.argv[2])

    prefs = recommendations.loadMovieLens('../data')

    result = recommendations.calculateSimilarItems(prefs, n=n)

    print "Movie most like '" + film + "': '" + result[film][0][1]
    print "Movie least like '" + film + "': '" + result[film][-1][1]
