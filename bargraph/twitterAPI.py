import tweepy  #Library for accessing Twitter API
from textblob import TextBlob  #Library for Text Processing 

#Setting up API credentials
#The credentials can be obtained by setting up your account at https://apps.twitter.com/

consumer_key = 'EhO3iJ6xUlCxLaVFsKZTbPy0H'
consumer_secret = 'MGNc2vzQtYYLJsLyZFeROJR36hiTc31GlAukwD6sR6XwXO12ZM'
access_token = '1102083971842682881-bkZs6TodQ31GAKOKaVNREEaBVJURE8'
access_token_secret = 'Q8iNkIInrFGa1JGzgFHoPKUegq5O3UST9WN8mbfBITSN6'
        
#Twitter API authentication
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth) #API instance

#Printing random tweets and using them for some purpose! 
public_tweets=api.search('#Demonetisation')

for tweet in public_tweets:
	text=tweet.text
	analysis=TextBlob(text)
	print(text)
	print(analysis.sentiment)
