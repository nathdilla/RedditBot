import praw
import tweepy
import time
import random
from datetime import datetime

CONSUMER_KEY = 'vEmMF92BZ0MsMQeWcIdPN50Qf'
CONSUMER_SECRET = '5Rt8zszTqCyZOUJKO5WeRdH5WoJCcqWVpbxRKqhUNUZOUNANiy'
ACCESS_KEY = '805165928845426688-gCeGBihWdqW3Ucnf8xXPrvyeeZsQs5e'
ACCESS_SECRET = 'vteIGYV5zOSlRAir8JRgRvrFynxCGErVj97EQ2ON2YvRO'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
twitter = tweepy.API(auth)

reddit = praw.Reddit(client_id='mrdTgh0xCGlO7A',
                     client_secret='0jfFMVEX6bAGFtQ8_WcPbn6XDdo',
                     user_agent='my user agent')


def filter_string(string):
    omitted = ["asshole", "fuck", "shit", "penis", "cock", "anus", "vagina", "dick", "fucking", "horny", "sex", "retard", "gay",
               "faggot", "cum", "fuckin", "bastard", "porn", "porno", "cocksucker", "motherfucker", "motherfuckin", "tits",
               "ass", "nigger", "nigga", "coochie", "chink", "tit", "blowjob", "handjob", "rimjob", "anal", "taint",
               "trib", "tribbing", "jackass", "dumbass"]
    output = string

    for nono_word in omitted:
        replace = "****"
        if nono_word == "asshole":
            replace = "jerk"
        output = output.replace(nono_word, replace)
    return output


def get_tweet():
    posts = []

    for submission in reddit.subreddit('ShowerThoughts').top(time_filter='day'):
        posts.append(submission.title)

    tweet = posts[random.randint(0, 10)]
    tweet = filter_string(tweet)

    try:
        twitter.update_status(status=tweet)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Tweeted: " + tweet + " - @" + current_time)
    except:
        print("Tweet invalid. Trying again...")
        get_tweet()


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("DATE EXECUTED: " + current_time)

while 1:
    get_tweet()
    for n in range(86400):
        time.sleep(1)
        print("daily tick: " + str(n))



