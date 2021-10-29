from Twitter_Module import Twitter_Module
import tweepy
import time

def test_twitter():
    # Insert your  correct credentials here
    consumer_key = ""
    consumer_secret = ""
    access_key = ""
    access_secret = ""


    callback_uri = 'oob'

    sm_module = Twitter_Module(consumer_key, consumer_secret, access_key, access_secret, callback_uri)

    errorHandle = False
    start_time = time.time()
    try:
        texts = sm_module.getText()
        end_time = time.time()
    except Exception:
        errorHandle = True
    assert not errorHandle
    assert end_time-start_time < 1

    consumer_key = "Y2R2YyiGiXa8wD7KqvLOEht5C"
    consumer_secret = "bmVpIHMybwu4eYHnasQ6kmJ7Zv5DRYO3VCUo9A82CBegR8gCc5"
    access_key = "2824609167-xdYnMeHX4Tk5kvHZOUakiP4IRKZkePP10OwP5wj"
    access_secret = "7ect2FUAHahrMPh44B2BnqLjFRJXAkHrf7oOtUq1D77wG"
    sm_module = Twitter_Module(consumer_key, consumer_secret, access_key, access_secret, callback_uri)
    try:
        texts = sm_module.getText()
    except Exception:
        errorHandle = True
    assert errorHandle

