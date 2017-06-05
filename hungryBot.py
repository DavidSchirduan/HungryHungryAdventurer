#import tweepy
import random
import time

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
#api = tweepy.API(auth)

'''
A simple food-generation twitter bot.
Designed by Thomas Novosel
Written by David Schirduan

bfastfoodtype
bfastplantspecifier
breakfastdrinktype
dinnerdrinktype
dinnerfoodtype
dinnerplantspecifier
drinkamount
drinkspecifier
excuse
foodamount
greeting
junk
monster
planttype
travelingplantspecifier
travellingdrinktype
travellingfoodtype
'''

#this is a totally random choosing
def pickFromList(listName):
    listFile = open("./Lists/" + listName + ".txt")
    lines = listFile.read().splitlines()
    theLine = random.choice(lines)
    return theLine






