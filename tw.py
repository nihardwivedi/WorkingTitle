import tweepy
from tweepy.auth import OAuthHandler

consumer_key = 'k1'
consumer_secret = 'k2'
access_token = 'k3'
access_token_secret = 'k4'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

####################
#  find_user():
####################

file=open('users.txt','w')
game_player = []
if(api.verify_credentials):
  print("We successfully logged in.")

for tweet in tweepy.Cursor(api.search,q='Borderlands3').items(10):
  file.write('Tweet by: @' + tweet.user.screen_name+'\n')
  game_player.append(tweet.user.screen_name)

file.close()
print("ok")
print(game_player)

#########################
#get_user_tweet():
#########################
file=open('tweets.txt','w',encoding="utf-8")
i = 0 
for i in range(len(game_player)):
  public_tweets = api.user_timeline(game_player[i])
  file.write(game_player[i]+'::\n')

  for tweet in public_tweets:
    file.write(tweet.text+'\n')

  file.write('\n\n\n ********************************************\n')

file.close()
print("tweet collection, ok")
