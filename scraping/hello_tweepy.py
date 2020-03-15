import tweepy


creds = {
    "ACCESS_KEY": "740559384380604417-SLDNlS5cjZMhBzbEFsKTKKaISdehZGL",
    "ACCESS_SECRET": "Iy1MbQwla7mebPV3kPAo417xfP7acsNOxR0g7XydHMzLa",
    "CONSUMER_KEY": "X6eRSFIzQ7A8GX8EKS6pjNsVF",
    "CONSUMER_SECRET": "UcpNwe39JqQ83zdigXA7fLqSfFAFlc4k15eCRW2vL7upuAdhLX"
}

auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_KEY'], creds['ACCESS_SECRET'])

api = tweepy.API(auth)

def hello_world():
    public_tweets = api.home_timeline()

    for tweet in public_tweets:
        print(tweet.text)


