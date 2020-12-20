import tweepy
import logging
import time
import random
import config
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Authenticate to Twitter
auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.token_secret)

# Create API object
api = tweepy.API(auth)
last_tweeted = datetime.now()-timedelta(hours=24)
randomquote = random.choice(open('quotes.txt').readlines())

#Main

def main():
    tweet_daily(api, last_tweeted, randomquote)
    print(config.api_key)

# Daily tweet
def tweet_daily(api, last_tweeted, randomtext):
    if last_tweeted < datetime.now()-timedelta(hours=24):
        api.update_status(randomtext)
        logger.info(f"Tweeted {randomtext} at {datetime.now().strftime('%m/%d/%Y at %H:%M:%S')}")
        return datetime.now()
    else:
        return last_tweeted


if __name__ == "__main__":
    main()
