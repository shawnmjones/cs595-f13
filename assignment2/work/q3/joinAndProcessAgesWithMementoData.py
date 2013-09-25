#!/usr/local/bin/python3

import sys

mementoDataFile = sys.argv[1]
ageDataFile = sys.argv[2]

mementoData = {}
ageData = {}

f = open(mementoDataFile)

for line in f:
    line = line.strip()
    (mementoCount, uri) = line.split('\t')

    if int(mementoCount) > 0:
        mementoData[uri] = mementoCount

f.close()

f = open(ageDataFile)

for line in f:
    line = line.strip()
    (age, uri) = line.split('\t')

    ageData[uri] = age

f.close()

for key in mementoData:

    print(key + '\t' + mementoData[key] + '\t' + ageData[key])


