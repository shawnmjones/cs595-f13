#!/usr/local/bin/python3

# I realized that I didn't want to spend time waiting for more than 1000 links,
# so this script gives a random sample

import random
import sys

inputfile = sys.argv[1]

f = open(inputfile)
links = f.readlines()
f.close()

target = 1000

for i in range(0, target):
    # grab a random entry from the list
    print(links[random.randint(0, len(links))].strip())
