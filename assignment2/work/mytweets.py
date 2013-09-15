# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urllib.parse import parse_qs

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "n7jt1uMTwGCcIzDvey8g0A"
CONSUMER_SECRET = "0r6HUrVD36W4MULgWETKMxrQsCICNy1OFFNc2iW4o"

OAUTH_TOKEN = "528649269-SffJ0Rei5PzLYd2NSJPnnm28dP5nlAnt7E1gRGwo"
OAUTH_TOKEN_SECRET = "htrwXF09pS8tP8cMzFrxmMryavdPXd0zPiJHRnLs"


def setup_oauth():
    """Authorize your app via identifier."""
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
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print( "OAUTH_TOKEN: " + token )
        print( "OAUTH_TOKEN_SECRET: " + secret )
        print( )
    else:
        oauth = get_oauth()
        r = requests.get(url="https://api.twitter.com/1.1/statuses/mentions_timeline.json", auth=oauth)
        print( r.json() )
