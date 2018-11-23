import tweepy
from tweepy import StreamListener

consumerKey = "6RscnZoLmUABrNgZf01XUhaeb"
consumerSecret = "84D66eoyiDm3BLAumIsMZ44ioWQ7695tPLrlSS2TfiGQ7TUlkQ"
accessToken = "634822279-MYkXgUoICcgPLZt8lk2xGTzCgCxZPxDPD8nmimM9"
accessTokenSecret = "pVFT2qwlDwQyBnubaSsqlGO7btVFG8dR55zL1HdD1RLOj"

# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

class StdOutListener(StreamListener):

    def __init__(self):
        super().__init__()
        self.c = 0
        self.l = 10

    def on_data(self, data):
        #print(data)
        try:
            f.write(str(data) + "\n")
            if (self.c >= self.l):
                self.l *= 5/4
                print(self.c)
            self.c += 1
        except Exception:
            pass
        return True

    def on_error(self, status):
        print(status)
    def on_exception(self, exception):
        print(exception)


f = open("twitter.txt", "a")
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)
myStreamListener = MyStreamListener()
myStreamListener2 = StdOutListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener2)
# myStream = tweepy.Stream(auth, myStreamListener2)
try:
    #myStream.filter(track=["trump", "twitter", "trending", "summer", "travel", "love", "photography", "music",
                           #"fintech", "TuesdayThoughts", "birtain", "august", "instagram", "vote"], languages=["en"])
    myStream.filter(track=["iran", "usa", "mit", "tech", "tesla", "space", "nasa", "spacex", "electric", "solar", "mars", "intel",
                           "lenovo", "apple", "microsoft", "iphone", "yoga", "data", "information", "hadoop", "bitcoin"
                           ,"sport", "love", "life", "linux", "mac", "ycombinator", "china","edtech"], languages=["en"])
except Exception:
    pass
