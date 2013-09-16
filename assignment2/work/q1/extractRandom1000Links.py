#!/usr/local/bin/python3

# I realized that I didn't want to spend time waiting for more than 1000 links,
# so this script gives a random sample

import random
import sys

inputfile = sys.argv[1]

f = open(inputfile)
links = f.readlines()
f.close()

count = 1000

selectedLinks = []

while count > 0:
    # grab a random entry from the list
    index = random.randint(0, len(links) - 1)
    newlink = links[index].strip()

    if newlink not in selectedLinks:
        selectedLinks.append(newlink)
    else:
        count -= 1

for link in sorted(selectedLinks):
    print(link)
