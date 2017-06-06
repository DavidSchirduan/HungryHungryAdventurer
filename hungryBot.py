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
        
    foodItem2 = plantFood(meal)

    drinkItem = drink(meal)

    greeting1 = pickFromList("greeting");

    fullMsg = greeting1 + " " + foodItem1 + " and " + foodItem2 + " with a " + drinkItem
    halfMsg = greeting1 + " " + foodItem1 + " with a " + drinkItem
    shortMsg = greeting1 + " a " + drinkItem

    #make sure it's not too long for twitter
    if (len(fullMsg) < 140):
        return fullMsg
    elif (len(halfMsg) < 140):
        return halfMsg
    else:
        return shortMsg
    
def monsterFood(whichMeal):
    m = pickFromList("monster");
    f = pickFromList(whichMeal + "foodtype");
    return m + " " + f
    
def plantFood(whichMeal):
    pt = pickFromList("planttype");
    ps = pickFromList(whichMeal + "plantspecifier");
    m = pickFromList("monster");

    if(ran(2) == 1):
        return ps + " " + pt
    else:
        return pt + m    

def drink(whichMeal):
    ds = pickFromList("drinkspecifier");
    dt = pickFromList(whichMeal + "drinktype")
    
    return ds + " " + dt
        

print(CreateMeal("bfast"))
print(CreateMeal("dinner"))
print(CreateMeal("travelling"))
