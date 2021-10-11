# Author: David Shi

import tweepy
from IPython.display import display
import pandas
from social_media_module import Social_Media_Module

consumer_key = "Y2R2YyiGiXa8wD7KqvLOEht5C"
consumer_secret = "bmVpIHMybwu4eYHnasQ6kmJ7Zv5DRYO3VCUo9A82CBegR8gCc5"
access_key = "2824609167-xdYnMeHX4Tk5kvHZOUakiP4IRKZkePP10OwP5wj"
access_secret = "7ect2FUAHahrMPh44B2BnqLjFRJXAkHrf7oOtUq1D77wG"

callback_uri = 'oob'

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
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)
        my_timeline = api.home_timeline()
        data = []
        for status in my_timeline:
            status_dict = dict(vars(status))
            data.append(status_dict["text"])
        return data