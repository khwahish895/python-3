import tweepy

API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

auth = tweepy.OAuth1User Handler(consumer_key=API_KEY, consumer_secret=API_SECRET_KEY,
                                access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def post_tweet(status):
    api.update_status(status)
