# Author: David Shi

import tweepy
from IPython.display import display
import pandas

consumer_key = "hwJEfbpDLJqmTjkb4WzV5oP0k"
consumer_secret = "qwNVMlzTHSdECS4BMndqcrwrnqzZcdimXeBImzhfs3tfnel2bX"
access_key = "2824609167-Ja1mO74Ou0DMT4SCvHXghj6u4PEFznkZxArJR1p"
access_secret = "hGAA6807zcCszrqcynWKl8BTzyo3D977QvmzWaacHqlsv"

callback_uri = 'oob'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
auth.set_access_token(access_key, access_secret)


api = tweepy.API(auth)


## Section 1: Upload tweets or images
# new_tweet = api.update_status("Test with twitter API")

# upload_media = api.media_upload("index.png")

# new_tweet_with_image = api.update_status("Test with twitter API", media_ids=[upload_media.media_id_string])

## Section 2: Show tweets' info in a timeline

my_timeline = api.home_timeline()

# print(my_timeline)

def timeline_dataframe(timeline):


    cols = set()
    type_filter = [str,int]
    data = []

    for status in timeline:
        #print(type(vars(status))
        status_dict = dict(vars(status))
        keys = status_dict.keys()
        single_tweet = {"user":status.user.screen_name, "author": status.author.screen_name}
        for k in keys:
            try:
                v_types = type(status_dict[k])
            except:
                v_types = None
            if v_types != None:
                if v_types in type_filter:
                    single_tweet[k] = status_dict[k]
                    cols.add(k)
        data.append(single_tweet)

    header_cols = list(cols)
    header_cols.append("user")
    header_cols.append("author")

    df = pandas.DataFrame(data,columns=header_cols)
    return df
df2 = timeline_dataframe(my_timeline)
df2.head()
display(df2)