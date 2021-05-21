#RTの対象外にするやつ
import tweepy
from config import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

stop_results = api.search(q="@ktfk_bot STOP-RT", count=10, result_type="mixed")
resume_results = api.search(q="@ktfk_bot RESUME-RT", count=10, result_type="mixed")

def check_list(id):
    bool0 = False
    f = open("exc-RT.txt", "r")
    lines = f.read().splitlines()
    bool0 = id in lines
    f.close()
    return bool0


def add_list(search_results):
    print("")
    for result in search_results:
        screen_name = result.user.screen_name
        isWritten = check_list(screen_name)
        print('Date : ', result.created_at)   
        print("User_ID : "+result.user.name+"(@"+screen_name+")")
        print("not-RT : "+str(isWritten))
        try:
            if (screen_name != 'ktfk_bot'):
                isWritten = check_list(screen_name)
                #print(isWritten)
                if isWritten == False:
                    with open("exc-RT.txt", mode="a") as f:
                        f.write(screen_name + "\n")
                        #print(user_id)
                    print("Status changed : not-RT False -> True")
            print("")
        except Exception as e:
            print(e)
            print("")

if __name__ == "__main__":
    add_list(resume_results)
            




