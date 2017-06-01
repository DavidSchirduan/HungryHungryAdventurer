*Basic Rules*

Never more than 3 items.

One item is always a drink.

Never more than one MonsterFood.

If there is a MonsterFood it always is the first item written.

Any number of PlantFoods.

Each MonsterFood is made up of [(monster) (foodtype)] in that order.

Each PlantFoods is made up of [(plantspecifier) (planttype)] or [(planttype) (monster)].

Each drink is made up of [(drinkspecifier) (drinktype)].

If total form generated is longer than 140 characters, regenerate an a part until it is 140 characters or less. So regenerate greeting first, if still over 140 characters, regenerate fooditem1, if still over, regenerate fooditem2, if still over regenerate drink, if still over regenerate greeting again.

When someone tweets at HungryHungryAdventurer, bot scans tweet for "breakfast", "dinner", or "traveling".

Uses whichever is found first, if "breakfast" use breakfast lists instead of other lists.

Monsterfood Lists: monster, breakfastfoodtype, dinnerfoodtype, travellingfoodtype

PlantFoods Lists: breakfastplantspecifier, dinnerplantspecifier, travelingplantspecifier, planttype, monster (same list as monsterfood)

Drink Lists: drinkspecifier, breakfastdrinktype, dinnerdrinktype, travellingdrinktype

Other Lists: greeting

When the bot responds the form of the response is: "(greeting), (fooditem1) and (fooditem2) with (drinkitem)"
