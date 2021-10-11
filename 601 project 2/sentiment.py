from Twitter_Module import Twitter_Module
from Google_Module import Google_Module
import pandas
from IPython.display import display

consumer_key = "Y2R2YyiGiXa8wD7KqvLOEht5C"
consumer_secret = "bmVpIHMybwu4eYHnasQ6kmJ7Zv5DRYO3VCUo9A82CBegR8gCc5"
access_key = "2824609167-xdYnMeHX4Tk5kvHZOUakiP4IRKZkePP10OwP5wj"
access_secret = "7ect2FUAHahrMPh44B2BnqLjFRJXAkHrf7oOtUq1D77wG"

callback_uri = 'oob'

sm_module = Twitter_Module(consumer_key, consumer_secret, access_key, access_secret, callback_uri)
nlp_module = Google_Module()
texts = sm_module.getText()
sentiments = nlp_module.getScore(texts)
d = {"Text": [], "Sentiment Score": [], "Magnitude": []}
for i in range(len(texts)):
    d["Text"].append(texts[i])
    d["Sentiment Score"].append(sentiments[i][0])
    d["Magnitude"].append(sentiments[i][1])
df = pandas.DataFrame(data=d)
display(df)
