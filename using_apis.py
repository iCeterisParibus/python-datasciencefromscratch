# Data Science From Scratch example using APIs

import json

serialized = """{"title" : "Data Science Book",
                 "author" : "Joel Grus",
                 "publicationYear" : 2014,
                 "topics" : ["data", "science", "data science"]}"""

deserialized = json.loads(serialized)
if "data science" in deserialized["topics"]:
    print deserialized

# Using an Unauthenticated APIs

import requests

end_points = "http://api.github.com/users/joelgrus/repos"

repos = json.loads(requests.get(end_points).text)

from dateutil.parser import parse
from collections import Counter

dates = [parse(repo["created_at"]) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)

last_5_repositories = sorted(repos,
                             key = lambda r: r["created_at"],
                             reverse=True)[:5]

last_5_languages = [repo["language"]
                    for repo in last_5_repositories]

# Getting Credentials

# 1. go to https://apps.twitter.com/
# 2. Sign in with twitter account information
# 3. Click create New app
# 4. Give it a name (such as "Data Science") and a description and put any URL as website (doesn't matter which one)
# 5. Agree to the Terms of Service and click Create
# 6. Take note of Consumer Key and Consumer Secret
# 7. Click create my access token
# 8. Take note of the access token and access token secret (you may have to refresh the page)

from twython import Twython

CONSUMER_KEY = 'Twitter Consumer Key' # Will need to replace with personal credentials
ONSUMER_SECRET = 'Twitter Consumer Secret' # Will need to replace with personal credentials

ACCESS_TOKEN = 'Twitter Token' # Will need to replace with personal credentials
ACCESS_TOKEN_SECRET = 'Twitter Token Secret' # Will need to replace with personal credentials

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)

for status in twitter.search(q='"data science"')["statuses"]:
    user = status["user"]["screen_name"].encode('utf-8')
    text = status["text"].encode('utf-8')
    print user, ":", text
    print

from twython import TwythonStreamer

tweets = []

class MyStreamer(TwythonStreamer):
    """our own subclass of TwythonStreamer that specifies
    how to interact with the stream"""

    def on_success(self, data):
        """what to do when twitter sends us data?
        here data will be a Python dict representating a tweet"""

        # only want to collect English-language tweets
        if data['lang'] == 'en':
            tweets.append(data)
            print "received tweet #", len(tweets)

        # stop when we've collected enough
        if len(tweets) >= 1000:
            self.disconnect()

    def on_error(self, status_code, data):
        print status_code, data
        self.disconnect

stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET,
                    ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# starts consuming public statuses that contain the key word 'data'
stream.statuses.filter(track='data')

# if instead we wanted to start consuming a sample of *all* public statuses
# stream.statuses.sample()

from collections import Counter

top_hashtags = Counter(hashtag['text'].lower()
                       for tweet in tweets
                       for hashtag in tweet["entities"]["hashtags"])

print top_hashtags.most_common(10)
