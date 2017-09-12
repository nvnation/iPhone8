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
import time
import os
import sys
import json




CONSUMER_KEY = 'NycLgBpMgLePdZbPl6oIN86ce'
CONSUMER_SECRET = 'fI6i38MhQOkWYqVYR2zjLCEvauZ2LilSCAEICvMutYjF70o3ld'
OAUTH_TOKEN = '831717276768309250-uj1WHYhUOQ6qU45vc1o2yqUvGYGozua'
OAUTH_TOKEN_SECRET = 'OdquemZymENTORJvwuJQHlWraEcOwJIVVqC8lc3ts7seR'
flag = True



class MyListener(StreamListener):

    def __init__(self, time_limit = 10):
        self.start_time = time.time()
        self.limit = time_limit
        self.saveFile = open('iphone.txt', 'a') 
        super(MyListener, self).__init__()
    
    def on_data(self,data):
        if(time.time() - self.start_time)<self.limit:     
            try:
                #print(data)                
                self.saveFile.write(data)
                self.saveFile.write('\n')
                return True
            except BaseException as e:
                print("error")
            return True
        else:
            self.saveFile.close()
 
            return False
    def on_error(self, status):
        print(status)
        #return True

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream = Stream(auth, MyListener())
stream.filter(track = ['#iPhone8', '#AppleEvent', '#iPhoneX'], async = True)
tweets = []


def parse_json():
    for line in open('iphone.txt'):
        try:
            tweets.append(json.loads(line))
        except:
            pass
parse_json() 

tweet = tweets[0]

print(tweet)

print('\n\n\n\n')

print(tweet.keys())

 

