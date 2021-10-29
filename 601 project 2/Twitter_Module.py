# Author: David Shi

import tweepy
from IPython.display import display
import pandas
from social_media_module import Social_Media_Module

class Twitter_Module(Social_Media_Module):
    c_key = None
    c_secret = None
    a_key = None
    a_secret = None
    uri = None


    def __init__(self, consumer_key,  consumer_secret, access_key, access_secret, callback_uri):
        self.c_key = consumer_key
        self.c_secret = consumer_secret
        self.a_key = access_key
        self.a_secret = access_secret
        self.uri = callback_uri

    def getText(self):
        auth = tweepy.OAuthHandler(self.c_key, self.c_secret, self.uri)
        auth.set_access_token(self.a_key, self.a_secret)
        api = tweepy.API(auth)
        my_timeline = api.home_timeline()
        data = []
        for status in my_timeline:
            status_dict = dict(vars(status))
            data.append(status_dict["text"])
        return data
