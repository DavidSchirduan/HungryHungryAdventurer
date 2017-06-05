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

foodItem1 = ""
fooditem2 = ""
drinkItem = ""

def ran(num):
    return random.randint(1, num)

#this is a totally random choosing
def pickFromList(listName):
    listFile = open("./Lists/" + listName + ".txt")
    lines = listFile.read().splitlines()
    theLine = random.choice(lines)
    return theLine


def CreateMeal(meal):
    if(ran(2) == 1):
        foodItem1 = monsterFood(meal)
    else:
        foodItem1 = plantFood(meal)
        
    if(ran(2) == 1):
        foodItem2 = monsterFood(meal)
    else:
        foodItem2 = plantFood(meal)

    drinkItem = drink(meal)

    greeting1 = greeting();

    Tmsg3 = greeting1 + " " + foodItem1 + " and " + foodItem2 + " with a " + drinkItem
    Tmsg2 = greeting1 + " " + foodItem1 + " with a " + drinkItem
    Tmsg1 = greeting1 + " a " + drinkItem

    if (tweetSafe(Tmsg)):
        return Tmsg3
    elif (tweetSafe(Tmsg)):
        return Tmsg2
    else:
        return Tmsg1
    

def monsterFood(whichMeal):
    

def plantFood(whichMeal):
    

def drink(whichMeal):
    

def greeting():
    

#if over 140 chars, remove second food item. If still, remove both food items
def tweetSafe(msg):
    return(len(msg) <= 140)
        

print(CreateMeal("bfast"))



