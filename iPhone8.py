'''
import twitter
import io
import json

import pandas as pd


CONSUMER_KEY = 'NycLgBpMgLePdZbPl6oIN86ce'
CONSUMER_SECRET = 'fI6i38MhQOkWYqVYR2zjLCEvauZ2LilSCAEICvMutYjF70o3ld'
OAUTH_TOKEN = '831717276768309250-uj1WHYhUOQ6qU45vc1o2yqUvGYGozua'
OAUTH_TOKEN_SECRET = 'OdquemZymENTORJvwuJQHlWraEcOwJIVVqC8lc3ts7seR'

QUERY = 'iPhone8'

OUT_FILE = QUERY + ".json"

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = twitter.TwitterStream(auth=auth)

#print("Filtering the public timeline for {0}").format(QUERY)
stream = twitter_stream.statuses.filter(track = QUERY)
counter = 25
#write information to json file
with io.open(OUT_FILE, 'w', encoding = 'utf-8', buffering=1) as f:
    for tweet in stream:
        f.write(str(u'{0}\n'.format(json.dumps(tweet, ensure_ascii=False))))
        print(tweet['text'])
        x=0
        x +=1
        if(x==25):
            stream.stop()



DATA_FILE = "tmp/iPhone8.json"

data = [{0}].format(",".join([l for l in open(DATA_FILE).readlines()]))

df = pd.read_json(data, orient = 'records')

print("Successfully imported", len(df),"tweets")
'''




import re
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import datetime as dt
import os
import sys
import json




CONSUMER_KEY = 'NycLgBpMgLePdZbPl6oIN86ce'
CONSUMER_SECRET = 'fI6i38MhQOkWYqVYR2zjLCEvauZ2LilSCAEICvMutYjF70o3ld'
OAUTH_TOKEN = '831717276768309250-uj1WHYhUOQ6qU45vc1o2yqUvGYGozua'
OAUTH_TOKEN_SECRET = 'OdquemZymENTORJvwuJQHlWraEcOwJIVVqC8lc3ts7seR'

class MyListener(StreamListener):
    def on_data(self,data):
        try:
            print(data)
            with open('iphone.json', 'a') as f:
               f.write(data)
            return True
        except BaseException as e:
            print("error")
        return True
    def on_error(self, status):
        print(status)
        #return True

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream = Stream(auth, MyListener())
stream.filter(track = ['#iPhone8', '#AppleEvent', '#iPhoneX'])
