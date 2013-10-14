#!/usr/local/bin/python3

import sys
from xml.dom.minidom import parseString

def getFriendInfo(xml):

    dom = parseString(xml)
    countDict = {}

    for element in dom.getElementsByTagName("data"):
        if (element.attributes['key'].value == 'name'):
            name = element.childNodes[0].data 

        if (element.attributes['key'].value == 'friend_count'):
            count = element.childNodes[0].data

            countDict[name] = count
            name = ''
            count = ''

    return countDict

def getFriendCount(xml):

    dom = parseString(xml)
    return len(dom.getElementsByTagName("node"))


if __name__ == "__main__":

    graphmlFile = sys.argv[1] 

    f = open(graphmlFile)
    xml = f.read()
    f.close()

    myFriendCount = getFriendCount(xml)
    friendInfo = getFriendInfo(xml)

    print("Name,Friend Count")
    print('ME,' + str(myFriendCount))

    for friend in friendInfo:
        print(friend + ',' + friendInfo[friend])

