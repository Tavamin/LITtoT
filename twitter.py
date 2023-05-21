import tweepy
from decouple import config





class Twitter:
    def __init__(self):
        self.consumer_key = config('CONSUMER_KEY')
        self.consumer_secret = config('CONSUMER_SECRET')
        self.access_token = config('ACCESS_TOKEN')
        self.access_token_secret = config('ACCESS_TOKEN_SECRET')
        self.bearer_token = config('BEARER_TOKEN')
        self.client = tweepy.Client(consumer_key=self.consumer_key, consumer_secret=self.consumer_secret,
                                    access_token=self.access_token,
                                    access_token_secret=self.access_token_secret, bearer_token=self.bearer_token)

    def write_tweet(self, text: str):
        try:
            self.client.create_tweet(text=text)
        except Exception as e:
            print(e)
        else:
            print("Tweeted successfully")


if __name__ == "__main__":
    twitter = Twitter()
    twitter.write_tweet("1234")
