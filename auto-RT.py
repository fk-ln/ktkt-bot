import tweepy
from config import *
from add_list import check_list

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

search_results = api.search(q="#キタキタ北千住 -filter:retweets", count=10, result_type="mixed")
count = 0

print("")

for result in search_results:
    tweet_id = result.id
    screen_name = result.user.screen_name
    isWritten = check_list(screen_name)
    print('Date : ', result.created_at)   
    print("User_ID : "+result.user.name+"(@"+screen_name+")")
    print("not-RT : "+str(isWritten))
    try:
        if screen_name != 'ktfk_bot' and isWritten == False:
            api.retweet(tweet_id)  #RT
            count = count + 1
    except Exception as e:
        #print(e)
        print("This tweet is already retweeted.")
    print("")

print(count,"Tweets retweeted.")
print("")

