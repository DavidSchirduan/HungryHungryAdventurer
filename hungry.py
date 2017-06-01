import tweepy
import json
import urllib
import random
import time

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = '-2PKbfbrp2hNcwLgzeOSHkR73zhz58WC'
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

randomEntry = {"title" : "test","href" : "test","author" : "David Schirduan"}

def pickRandomEntry(randE):

    url = urllib.urlopen("https://200wordrpg.github.io/allposts.json")
    data = json.loads(url.read())
    
    num = random.randrange(0, len(data))
    randE = data[num]
    return randE

def tweetOut(randomE):
    while (randomE['author'] == "David Schirduan"):
        randomE = pickRandomEntry(randomE);

    twit = '"' + randomE['title'] + "\" \nby " + randomE['author'] + " \nis the 200 Word RPG Entry of the Day!\nhttps://200wordrpg.github.io" + randomE['href']

    print(twit)
    api.update_status(twit.encode('utf-8').strip())


while(True):
	tweetOut(randomEntry)
	time.sleep(86400)





