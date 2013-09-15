#!/usr/local/bin/python3

# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urllib.parse import parse_qs
import json
import time
import sys

# ugly, but necessary, globals; saw no need to change this
# strategy from the example
REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "n7jt1uMTwGCcIzDvey8g0A"
CONSUMER_SECRET = "0r6HUrVD36W4MULgWETKMxrQsCICNy1OFFNc2iW4o"

OAUTH_TOKEN = "528649269-SffJ0Rei5PzLYd2NSJPnnm28dP5nlAnt7E1gRGwo"
OAUTH_TOKEN_SECRET = "htrwXF09pS8tP8cMzFrxmMryavdPXd0zPiJHRnLs"

class APIError(Exception):
    """
        If something goes wrong with the API, throw one of these.
        (avoids sys.exit in the middle of the program)
    """

    def __init__(self, value):
        self.value = value 

    def __str__(self):
        return repr(self.value)

def setup_oauth():
    """
        Authorize your app via identifier.
        Code inspired by:  
        http://thomassileo.com/blog/2013/01/25/using-twitter-rest-api-v1-dot-1-with-python/
    """

    # Request token
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)

    credentials = parse_qs(r.content)

    resource_owner_key = credentials[b'oauth_token'][0].decode(encoding='UTF-8')
    resource_owner_secret = credentials[b'oauth_token_secret'][0].decode(encoding='UTF-8')
    
    # Authorize
    authorize_url = AUTHORIZE_URL + resource_owner_key
    print('Please go here and authorize: ' + authorize_url)
    
    verifier = input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    # Finally, Obtain the Access Token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token = credentials[b'oauth_token'][0].decode(encoding='UTF-8')
    secret = credentials[b'oauth_token_secret'][0].decode(encoding='UTF-8')

    return token, secret


def get_oauth():
    """
        Code inspired by:  
        http://thomassileo.com/blog/2013/01/25/using-twitter-rest-api-v1-dot-1-with-python/
    """
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth


def call_api(ident, oauth, count, screenName):
    #url = \
    #    "https://api.twitter.com/1.1/statuses/home_timeline.json?max_id=" + \
    #    str(ident) + "&count=" + str(count)
    url = \
        "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=" + \
        screenName + "&count=" + str(count) + "&max_id=" + str(ident)
        
    r = requests.get( url, auth=oauth )
    
    if 'errors' in r:
        raise APIError(
            json.dumps(
                r.json(), sort_keys=True, indent=4, separators=(',', ': ' ))
                )

    return r

def print_tweets_with_ids(
    startingid, oauth, tweetCountPerCall, numberOfCalls, screenName):
    """
        Make the API call, print the tweets returned.
    """

    ident = startingid

    for i in range(0, numberOfCalls):
   
        response = call_api(ident, oauth, tweetCountPerCall, screenName)

        tweetListSize = len(response.json())

        print(tweetListSize)

        if tweetListSize == 1:
            raise APIError("Ran out of tweets?")

        for i in range(0, tweetListSize):
            tweet = response.json()[i]
            ident = str(tweet['id'])
            text = tweet['text']
            print( str(ident) + ":" + str(text) )
    
        time.sleep(1)

def usage():

    print("Usage: " + sys.argv[0] +
        " <startingid> <tweetCountPerCall> <apiCalls> <screenName>")


if __name__ == "__main__":

    #startingid = "400000000000000000"
    try:
        startingId = sys.argv[1]
        tweetCountPerCall = int(sys.argv[2])
        apiCalls = int(sys.argv[3])
        screenName = sys.argv[4]
    except IndexError as e:
        usage()
        sys.exit(1)

    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print( "OAUTH_TOKEN: " + token )
        print( "OAUTH_TOKEN_SECRET: " + secret )
        print( )
    else:
        oauth = get_oauth()

        try:
            print_tweets_with_ids(
                startingId, oauth, tweetCountPerCall, apiCalls, screenName)
        except APIError as e:
            sys.stderr.write(e.value)
            sys.exit(254)
