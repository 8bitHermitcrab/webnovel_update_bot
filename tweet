##tweet.py

import tweepy
#from config import your_key, your_secret, your_token, your_token_secret

CONSUMER_KEY = "개인키"
CONSUMER_SECRET = "개인 시크릿키"
ACCESS_KEY = "액세스키"
ACCESS_SECRET = "액세스 시크릿키"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)  #tweepy api 기능 불러오기
api.update_status(status = '트윗 테스트 시작')    #내용 트윗하기(post)
