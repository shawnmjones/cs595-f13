#!/usr/local/bin/python3

import sys

# this file performs the equivalent of cat <filenames> | sort | uniq

inputFilenames = sys.argv[1:]

urilist = []

# combine all of the entries from the given files together
for filename in inputFilenames:
    f = open(filename)
    urilist.extend(f.readlines())
    f.close()

# sort the list
urilist.sort()

# expensive, but agreed upon simplest way to "uniq" a list
urilist = list(set(urilist))

# sort the list again
urilist.sort()

# output!
for entry in urilist:
    print(entry.strip())
