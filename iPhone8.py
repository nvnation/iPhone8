

#cd Desktop/iPhone8.py
#py iPhone8.py

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



CONSUMER_KEY = 'IxSX9lgYrsVNcD6B0B8eqVf7u'
CONSUMER_SECRET = 'ZmnsPVrpn8YVSjfchVKBlhHhh3Mrs46L0REwP5MMO85AbFLrkC'
OAUTH_TOKEN = '907790285219930112-argnKa8QSYMdHVxfZRZrw9kziT3pGM5'
OAUTH_TOKEN_SECRET = 'V1r0j7YoZKG787FhZAjDDVvUAHWmhFZmvZr3sS8hc79ab'
#flag = True

'''

class MyListener(StreamListener):

    def __init__(self, time_limit = 30):
        self.start_time = time.time()
        self.limit = time_limit
        self.saveFile = open('iphone.json', 'a')
        super(MyListener, self).__init__()

    def on_data(self,data):
        if(time.time() - self.start_time)<self.limit:
            try:
                #print(data)
                decoded = json.loads(data)
                if not decoded['text'].startswith('RT'):
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
        #print(status)
        return False

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream = Stream(auth, MyListener())
stream.filter(track = ['#iPhone8', '#AppleEvent', '#iPhoneX'], async = True, languages = 'en')
tweets = []


def parse_json():
    for line in open('iphone.json'):
        try:
            tweets.append(json.loads(line))
        except:
            pass
parse_json()

#tweet = tweets[0]

#print(tweet)

#print('\n\n\n\n')

#print(tweet.keys())

#print('\n\n\n\n')s
#print(tweet['text'])
#status = []
#for tweet in tweets:
    #status.append(tweet['text'])

#for i in status:
#    print(i)
'''


class MyListener(StreamListener):

    def __init__(self, time_limit = 10000):
        self.start_time = time.time()
        self.limit = time_limit
        self.saveFile = open('iphone.json', 'a')
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
stream.filter(track = ['#iPhone8', '#AppleEvent', '#iPhoneX'])
tweets = []

#
#def parse_json():
#    for line in open('iphone.json'):
#        try:
#            tweets.append(json.loads(line))
#        except:
#            pass
#parse_json()
#
'''
try:
    tweet = tweets[0]

    #print(tweet['text'])
    status = []


    for tweet in tweets:
            status.append(tweet['text'])
            print(tweet['text'])

except:
    print("No json file yet, run again")

#print(tweet.keys())
'''
