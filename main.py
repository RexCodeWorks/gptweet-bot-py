
from api import twitter_api
from api import openai_api


        

def post_tweet(request):

    counter = 0

    while(counter < 5):
        tweet = openai_api.get_tweet("tips")
        print(len(tweet))

        if(len(tweet) < 280):
            print("Find good one!")
            twitter_api.post_tweet(tweet)
            break
        else:
            counter=+1
            print(counter)
            if (counter == 5):
                tweet = openai_api.get_tweet("quote")
                if (len(tweet) < 280):
                    print("Find good qoute!")
                    twitter_api.post_tweet(tweet)
    return "Done!"


# def hello_world(request):
#     post_tweet()










