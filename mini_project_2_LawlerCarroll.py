#Importing the math module allows us to do some rounding that will come in handy later.
import math

#Explains recipe and objective.
print("My family has a peanut butter cookie recipe that has been passed down for generations. The original \
recipe calls for 1 cup of white sugar, 1 cup of brown sugar, 1 cup of shortening, 2 eggs, 1/2 tsp salt, \
1 tsp vanilla, 1 tsp baking soda, 1/2 tsp baking powder, 2/3 cup of peanut butter, and 3 cups of flour to \
to make 40 cookies. This program will allow you to input the number of cookies desired and will output the \
ingredients required, projected cost and even whether it is more cost effective to shop at the grocery store \
or in bulk.")

#Space
print()

#Prompts user to input number of cookies they wish to make.
cookies=input('Enter number of cookies to be made: ')

#Space
print()

#Introduces total cost variable and sets to zero.
totalCost = 0

#Sets user input cookies as variable x as an integer.
x=(int(cookies))

#Based on original recipe, calculates amount necessary of each ingredient based on user input.
whiteSugar=(x/40)*1
brownSugar=(x/40)*1
short=(x/40)*1
eggs=(x/40)*2
salt=(x/40)*(0.5)
vanilla=(x/40)*1
bakingSoda=(x/40)*1
bakingPowder=(x/40)*(0.5)
peanutButter=(x/40)*(2/3)
flour=(x/40)*3

#The math.ceil function allows us to always round up, whereas Python's round feature rounds up/down. \
#This does not work for us as we can have more than the required amount of an ingredient and use less but \
#not vice versa, for example, if we need to use 2 1/4 teaspoon it is more reasonable to say we need 2.5 tsp \
#and use less rather than round down and say we need only 2. The 4's you see make it so each value is rounded \
#to the nearest 1/4, and can be changed, fof example changing the 4's to 2's would round to the nearest 0.5. \
#Notice eggs are rounded to the nearest whole number as you cannot really have 1/2 egg.
whiteSugar=math.ceil(whiteSugar*4)/4
brownSugar=math.ceil(brownSugar*4)/4
short=math.ceil(short*4)/4
eggs=math.ceil(eggs)
salt=math.ceil(salt*4)/4
vanilla=math.ceil(vanilla*4)/4
bakingSoda=math.ceil(bakingSoda*4)/4
bakingPowder=math.ceil(bakingPowder*4)/4
peanutButter=math.ceil(peanutButter*4)/4
flour=math.ceil(flour*4)/4

#This section calculates the approximate price of each ingredient based on prices and quanitities from the \
#local grocery store. Price is calculated by the packages you need; for example, you cannot generally by 13 \
#eggs, you would buy 2 dozen, which is reflected here. Price of 13 eggs and 23 is the same as both are \
#contained in two dozen. math.ceil comes in handy here as it takes whatever fraction of a container we would \
#use, like 2.23 bags of flour and rounds it up to the nearest whole number. This amount is then multiplied \
#by prices from a local grocer.
groceryWhiteSugar = math.ceil(whiteSugar/2)*(1.5)
groceryBrownSugar = math.ceil(brownSugar/2.5)*(1.5)
groceryShort = math.ceil(short/2)*3
groceryEggs = math.ceil(eggs/12)*2
grocerySalt = math.ceil(salt/160)*1
groceryVanilla = math.ceil(vanilla/15)*5
groceryBakingSoda = math.ceil(bakingSoda/48)*(0.75)
groceryBakingPowder = math.ceil(bakingPowder/96)*(1.5)
groceryFlour = math.ceil(flour/(20/3))*(2.5)
groceryPeanutButter = math.ceil(peanutButter/(7.5))*4

#This section does the same as above but calculates based on the price and quantity of purchasing in bulk. \
#We got these amounts from WebRestaurant.com as an example.
bulkWhiteSugar = math.ceil(whiteSugar/100)*(22)
bulkBrownSugar = math.ceil(brownSugar/62.5)*(15)
bulkShort = math.ceil(short/100)*(32.50)
bulkEggs = math.ceil(eggs/60)*4
bulkSalt = math.ceil(salt/8000)*17
bulkVanilla = math.ceil(vanilla/768)*5.50
bulkBakingSoda = math.ceil(bakingSoda/2400)*(0.75)
bulkBakingPowder = math.ceil(bakingPowder/960)*(1.5)
bulkFlour = math.ceil(flour/(200/3))*10
bulkPeanutButter = math.ceil(peanutButter/(118.125))*42

#Calculates total cost of ingredients from the grocery store and bulk to be compared in next section.
totalGrocery =(groceryWhiteSugar + groceryBrownSugar + groceryShort + \
               groceryEggs + grocerySalt + groceryVanilla + groceryBakingSoda + \
               groceryBakingPowder + groceryFlour + groceryPeanutButter)

totalBulk = (bulkWhiteSugar + bulkBrownSugar + bulkShort + bulkEggs + \
             bulkSalt + bulkVanilla + bulkBakingSoda + bulkBakingPowder + \
             bulkFlour + bulkPeanutButter)

#Uses if/else to determine cheapest place to shop based on cookies needed. Sets variables for cost based on \
#corresponding prices and displays appropriate message to end user.
if totalGrocery < totalBulk:
    costOfWhiteSugar = groceryWhiteSugar
    costOfBrownSugar = groceryBrownSugar
    costOfShort = groceryShort
    costOfEggs = groceryEggs
    costOfSalt = grocerySalt
    costOfVanilla = groceryVanilla
    costOfBakingSoda = groceryBakingSoda
    costOfBakingPowder = groceryBakingPowder
    costOfFlour = groceryFlour
    costOfPeanutButter = groceryPeanutButter
    totalCost = totalGrocery
    print("It will be most cost effective to shop at your local grocer rather than buy in bulk.")
    
else:
    costOfWhiteSugar = bulkWhiteSugar
    costOfBrownSugar = bulkBrownSugar
    costOfShort = bulkShort
    costOfEggs = bulkEggs
    costOfSalt = bulkSalt
    costOfVanilla = bulkVanilla
    costOfBakingSoda = bulkBakingSoda
    costOfBakingPowder = bulkBakingPowder
    costOfFlour = bulkFlour
    costOfPeanutButter = bulkPeanutButter
    totalCost = totalBulk
    print("It will be most cost effective to buy in bulk rather than at your grocer. Try WebRestaurant.com.")

#Space    
print()

#Lists quantity needed of each item as well as individual and total costs. Format .2f is used to abbreviate to \
#two decimal places for dollar amounts. Remaining directions for recipe follow.
print("You will need: " "\n"
      +str(whiteSugar) + " cups of white sugar, which will cost" + " $"+str(format(costOfWhiteSugar,".2f"))+ "\n"
      +str(brownSugar) + " cups of brown sugar, which will cost" + " $"+str(format(costOfBrownSugar,".2f")) + "\n"
      +str(short) + " cups of shortening, which will cost" + " $"+str(format(costOfShort,".2f")) + "\n"
      +str(eggs) + " eggs, which will cost" + " $"+str(format(costOfEggs,".2f") + "\n"
      +str(salt) + " teaspoons of salt, which will cost" + " $"+str(format(costOfSalt, ".2f")) + "\n"
      +str(vanilla) + " teaspoons of vanilla, which will cost" + " $"+str(format(costOfVanilla, ".2f")) + "\n"
      +str(bakingSoda) + " teaspoons of baking soda, which will cost" + " $"+str(format(costOfBakingSoda, ".2f")) + "\n"
      +str(bakingPowder) + " teaspoons of baking powder, which will cost" + " $"+str(format(costOfBakingPowder,".2f")) + "\n"
      +str(peanutButter) + " cups of peanut butter, which will cost" + " $"+str(format(costOfPeanutButter,".2f")) + "\n"
      +str(flour) + " cups of flour, which will cost " + " $"+str(format(costOfFlour,".2f")) + "\n"
      +"For a grand total of:" + " $"+str(format(totalCost,".2f")) + "\n"
      + "\n"                                                 
      +"Mix wet and dry ingredients separately. Combine and form into roughly 1.5 tbsp balls."+ "\n"
      +"Turn oven on to 350 and bake for 12 minutes. Transfer to plate. Happy baking!"))
      
