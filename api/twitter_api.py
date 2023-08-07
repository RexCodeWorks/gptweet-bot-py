import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_APP_SECRET= os.getenv("TWITTER_APP_SECRET")
TWITTER_ACCESS_TOKEN= os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET= os.getenv("TWITTER_ACCESS_SECRET")

def post_tweet(tweet):
    client = tweepy.Client(consumer_key=TWITTER_API_KEY, consumer_secret=TWITTER_APP_SECRET,access_token=TWITTER_ACCESS_TOKEN, access_token_secret=TWITTER_ACCESS_SECRET)

    # new_tweet = 'Hello'
    client.create_tweet(text=tweet)
