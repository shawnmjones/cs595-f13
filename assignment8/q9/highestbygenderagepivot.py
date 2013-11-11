#!/usr/local/bin/python3

import sys
import numpy
import codecs

def getUsersByGender(userfile, selectedGender):
    
    f = open(userfile)

    userdict = {}

    for line in f:
        (userid, age, gender) = line.split('|')[0:3]

        if gender == selectedGender:
            userdict[userid] = int(age)

    f.close()

    return userdict

def getUsersByAgeRange(userdict, pivot, direction):

    newuserdict = {}

    for user in userdict:

        if direction == 'less':
            # add to new dict because they're < pivot
            if userdict[user] < pivot:
                newuserdict[user] = userdict[user] 
        
        if direction == 'greater':
            # add to new dict because they're > pivot
            if userdict[user] > pivot:
                newuserdict[user] = userdict[user] 
 
    return newuserdict
                

def getRatingsFromFileForUsers(ratingsfile, userlist):
  
    ratingsdict = {}

    f = open(ratingsfile)

    for line in f:
        (user_id, item_id, rating, timestamp) = line.split('\t')

        if user_id in userlist:
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

def getAverageRatings(ratingsdict):

    averagelist = []

    for key in ratingsdict:
        averagelist.append( ( numpy.mean(ratingsdict[key]), key ) )

    return sorted(averagelist, reverse=True)

def getTopN(averagelist, n):

    return averagelist[0:n]

if __name__ == '__main__':
    topratingsCount = int(sys.argv[1])
    ratingsfile = sys.argv[2]
    namesfile = sys.argv[3]
    userfile = sys.argv[4]
    gender = sys.argv[5]
    agepivot = int(sys.argv[6])
    agedirection = sys.argv[7]

    userdict = getUsersByGender(userfile, gender)
    userdict = getUsersByAgeRange(userdict, agepivot, agedirection)
    ratingsdict = getRatingsFromFileForUsers(ratingsfile, userdict)
    averagelist = getAverageRatings(ratingsdict)
    topN = getTopN(averagelist, topratingsCount)

    namesdict = getMovieNames(namesfile)

    for i in topN:
        print(namesdict[i[1]] + '\t' + str(i[0]))
    
