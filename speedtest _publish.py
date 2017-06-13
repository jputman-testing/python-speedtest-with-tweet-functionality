import pyspeedtest
import tweepy
from tweepy import OAuthHandler

#running speed tests
speed = pyspeedtest.SpeedTest()
download = speed.download()
#taken from the pyspeedtest source code
#formats speedtest into something easily readable
def pretty_speed(speed):
    units = ['bps', 'Kbps', 'Mbps', 'Gbps']
    unit = 0
    while speed >= 1024:
        speed /= 1024
        unit += 1
    return '%0.2f %s' % (speed, units[unit])
#format my speed into something easy to read
formattedDown = pretty_speed(download)
#print is just used to verify everything working
print(formattedDown)

#code adapted from marcobonzanini.com
consumer_key = 'PUT YOUR KEY HERE'
consumer_secret = 'PUT YOUR KEY HERE'
access_token = 'PUT YOUR KEY HERE'
access_secret = 'PUT YOUR KEY HERE'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
#tweet is the text you want to tweet
tweet = "My Current internet speed is " + formattedDown
status = api.update_status(status=tweet)
#for some reason, Twitter's API calls a tweet a status.
#printing the output just so that I can get the mail from the crontab \
print(tweet)
