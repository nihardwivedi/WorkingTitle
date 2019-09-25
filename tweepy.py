import tweepy

consumer_key = ''
consumer_secret = '8dVzvKqzNMvyiimPmng5gOFMO0IfsmdjPvHSiuG2g0kboACrZM'
access_token = '1174917647948869632-Al3ZzX96GkItqBmEp6xQmEC3WTAz1V'
access_token_secret = '
 '
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

####################
#  find_user():
####################

file=open('users.txt','w')
apple_user = []
if(api.verify_credentials):
  print("We successfully logged in.")

for tweet in tweepy.Cursor(api.search,q='Borderlands3').items(20):
  file.write('Tweet by: @' + tweet.user.screen_name+'\n')
  apple_user.append(tweet.user.screen_name)

file.close()
print("ok")
print(game_player)

#########################
#get_user_tweet():
########################
file=open('tweets.txt','w')
i = 0 
for i in range(len(game_player)):
  public_tweets = api.user_timeline(game_player[i])
  file.write(game_player[i]+'::\n')

  for tweet in public_tweets:
    file.write(tweet.text+'\n')

  file.write('\n\n\n ********************************************\n')

file.close()
print("tweet collection, ok")
