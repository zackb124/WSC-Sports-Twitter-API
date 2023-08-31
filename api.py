import tweepy
import pandas as pd
from datetime import datetime


# Set API keys
consumer_key = "MkfhJwrkGv3WZhya8Xi592jy2" #API key
consumer_secret = "DjbyucK6e6ssMY4VZ669qsLWuf06xndLAg6alyQ8qVfWSxP30U" #API key secret
access_token = "4407044007-M7gb0jn9s14qny0wwaLvRUxq9ahtvXkDO1Owzpf"
access_token_secret = "RERi7Vo9rOE3BUNJkREGnMPeH8i33OMKqMd51qp3jkxqv"

# Create a Twitter API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get the Twitter user object for the page
user = api.get_user(screen_name = "WSC_Sports")

# Get the number of followers and total tweets
followers_count = user.followers_count
total_tweets = user.statuses_count

current_date = datetime.now().date()




# engagements = api.get_user_engagements(screen_name="WSC_Sports")

# tweets = api.user_timeline(screen_name="WSC_Sports", count=200)
# # Iterate through the tweets and get the number of engagements
# total_engagements = 0
# for tweet in tweets:
#     likes = tweet.likes
#     retweets = tweet.retweets
#     quote_count = tweet.quote_count
#     reply_count = tweet.reply_count
#     total_engagements += likes + retweets + quote_count + reply_count

# Print the total engagements
# print(total_engagements)

#df = pd.DataFrame(followers_count,total_engagements,date)