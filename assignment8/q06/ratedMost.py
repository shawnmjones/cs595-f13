#!/usr/local/bin/python3

import sys
import pprint

def getRatingsFromFile(ratingsfile):

    f = open(ratingsfile)

    userlist = []

    for line in f:
        (user_id, item_id, rating, timestamp) = line.split('\t')

        userlist.append(user_id)

    return userlist


if __name__ == '__main__':

    ratingsFile = sys.argv[1]
    n = int(sys.argv[2])

    userlist = getRatingsFromFile(ratingsFile)

    users = set(userlist)

    countdict = {}

    for user in users:
        countdict[user] = userlist.count(user)

    for user in sorted(countdict, key=countdict.get, reverse=True)[0:n]:
        print(user + '\t' + str(countdict[user]))
