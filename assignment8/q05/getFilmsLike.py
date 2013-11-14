#!/usr/local/bin/python

import sys
import pprint

sys.path.insert(0, '../starter-code')

import recommendations

if __name__ == '__main__':

    film = sys.argv[1]
    threshold = int(sys.argv[2])
    direction = sys.argv[3]

    prefs = recommendations.loadMovieLens('../data')

    result = recommendations.calculateSimilarItems(prefs, n=1682)

    if direction == 'most':
        print "Movies most like '" + film + "': '"
        for i in range(0, threshold):
            print result[film][i][1] + ' (' + str(result[film][i][0]) + ')'
    else:
        print "Movies least like '" + film + "': '"
        for i in range(1, threshold):
            print result[film][-i][1] + ' (' + str(result[film][-i][0]) + ')'
