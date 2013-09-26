#!/usr/local/bin/python3

import sys
import time
import datetime

cdlistfile = sys.argv[1]

f = open(cdlistfile)

for line in f:
    try:
        line = line.strip()
        (cdate, uri) = line.split('\t')
        ct = time.strptime(cdate, "%Y-%m-%dT%H:%M:%S")
        # Thanks http://stackoverflow.com/questions/1697815/how-do-you-convert-a-python-time-struct-time-object-into-a-datetime-object
        cdt = datetime.datetime.fromtimestamp(time.mktime(ct))
        now = datetime.datetime.now()
        days = (now - cdt).days
        print(str(days) + '\t' + uri)
    except ValueError:
        # skip over those items without carbon dates
        pass

f.close()
