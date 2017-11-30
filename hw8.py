# Import statements
import unittest
import sqlite3
import requests
import json
import re
import tweepy


consumer_key = "tSSmjXj2wUuJfFqneE1UylDfo"
consumer_secret = "Nalv8aGz8Hx4m5gzb25jx4xl8nDQcbll8EClfAz5LJXi5ri98K"
access_token = "464846788-UlDBvt3WK7bjxbRyhjDjG6Prw6eMxFxEIRnGTAFj"
access_token_secret = "7ZboZQwEpqJbJ5XfmW9wJ696m22zYLq0Oa8EsWkG5Xh1R"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Set up library to grab stuff from twitter with your authentication, and return it in a JSON format
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# And we've provided the setup for your cache. But we haven't written any functions for you, so you have to be sure that any function that gets data from the internet relies on caching.
CACHE_FNAME = "twitter_cache.json"
try:
    cache_file = open(CACHE_FNAME,'r')
    cache_contents = cache_file.read()
    cache_file.close()
    cache_dic = json.loads(cache_contents)
except:
    cache_dic = {}

## [PART 1]

# Here, define a function called get_tweets that searches for all tweets referring to or by "umsi"
# Your function must cache data it retrieves and rely on a cache file!


def get_tweets():
    if cache_dic == {}:
        var1 = api.home_timeline()
        for x in var1:
            words = x['text'].split(' ')
            if 'umsi' in words or 'UMSI' in words:
                cache_dic[x['id']] = [x['user']['screen_name'], x['created_at'], x['text'], x['retweet_count']]
        var2 = api.user_timeline('umsi')
        for y in var2:
            cache_dic[tweet['id']] = [y['user']['screen_name'], y['created_at'], y['text'], y['retweet_count']]
        file = open(CACHE_FNAME, "w")
        file.write(json.dumps(cache_dic))
        file.close()
        return cache_dic
    else:
        return cache_dic



## [PART 2]
# Create a database: tweets.sqlite,
# And then load all of those tweets you got from Twitter into a database table called Tweets, with the following columns in each row:
## tweet_id - containing the unique id that belongs to each tweet
## author - containing the screen name of the user who posted the tweet (note that even for RT'd tweets, it will be the person whose timeline it is)
## time_posted - containing the date/time value that represents when the tweet was posted (note that this should be a TIMESTAMP column data type!)
## tweet_text - containing the text that goes with that tweet
## retweets - containing the number that represents how many times the tweet has been retweeted

# Below we have provided interim outline suggestions for what to do, sequentially, in comments.

# 1 - Make a connection to a new database tweets.sqlite, and create a variable to hold the database cursor.


conn = sqlite3.connect('tweets.sqlite')
cur = conn.cursor()


# 2 - Write code to drop the Tweets table if it exists, and create the table (so you can run the program over and over), with the correct (4) column names and appropriate types for each.
# HINT: Remember that the time_posted column should be the TIMESTAMP data type!

cur.execute('DROP TABLE IF EXISTS Tweets')
cur.execute("CREATE TABLE IF NOT EXISTS Tweets(tweet_id INTEGER, author VARCHAR(128), time_posted TIMESTAMP, tweet_text VARCHAR(128), retweets INTEGER)")


# 3 - Invoke the function you defined above to get a list that represents a bunch of tweets from the UMSI timeline. Save those tweets in a variable called umsi_tweets.

umsi_tweets = get_tweets();

# 4 - Use a for loop, the cursor you defined above to execute INSERT statements, that insert the data from each of the tweets in umsi_tweets into the correct columns in each row of the Tweets database table.

for x in umsi_tweets:
    cur.execute('INSERT INTO Tweets(tweet_id, author, time_posted, tweet_text, retweets) VALUES(?, ?, ?, ?, ?)', (x, umsi_tweets[x][0], umsi_tweets[x][1], umsi_tweets[x][2], umsi_tweets[x][3]))

#  5- Use the database connection to commit the changes to the database

conn.commit()

# You can check out whether it worked in the SQLite browser! (And with the tests.)

## [PART 3] - SQL statements
# Select all of the tweets (the full rows/tuples of information) from umsi_tweets and display the date and message of each tweet in the form:
    # Mon Oct 09 16:02:03 +0000 2017 - #MondayMotivation https://t.co/vLbZpH390b
    #
    # Mon Oct 09 15:45:45 +0000 2017 - RT @MikeRothCom: Beautiful morning at @UMich - It’s easy to forget to
    # take in the view while running from place to place @umichDLHS  @umich…
# Include the blank line between each tweet.

cur.execute('SELECT tweet_text, time_posted from Tweets')
for x in cur:
    print (x[1], '-', x[0], '\n')

# Select the author of all of the tweets (the full rows/tuples of information) that have been retweeted MORE
# than 2 times, and fetch them into the variable more_than_2_rts.
# Print the results

cur.execute('SELECT author from Tweets WHERE retweets>2')
more_than_2_rts = []
for x in cur:
    more_than_2_rts.append(x)
print (more_than_2_rts)

if __name__ == "__main__":
    unittest.main(verbosity=2)