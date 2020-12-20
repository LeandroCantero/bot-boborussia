import tweepy
import logging
import time
import random
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Authenticate to Twitter
auth = tweepy.OAuthHandler("lqHgUYzMJUXW3tjoQUZqhUe5P", "cto3v6CKRcX3mjxSygQe35XFRk4JWCRZJA5TpqT3NxWJLBC2gw")
auth.set_access_token("1340452358485123072-iC2xVPaSdvl8QZbgjBHVqIf81axLsM", "Y1H3Er72nIbzuzfW1tEbKcqiC3mzcLcfESV8yo8a2mVbB")

# Create API object
api = tweepy.API(auth)
last_tweeted = datetime.now()-timedelta(hours=24)
randomquote = random.choice(open('quotes.txt').readlines())

#Main

def main():
    tweet_daily(api, last_tweeted, randomquote)

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
