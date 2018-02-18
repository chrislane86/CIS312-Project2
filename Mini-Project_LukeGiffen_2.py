#define variables
standardCookieBatch= 12.0
standardCupsOfSugar= .33
standardCupsOfButter= .50
standardCupsOfFlour= 1.00
standardCostofSugar=.10
standardCostofButter=.25
standardCostofFlour=.10

#prompt user for input
userNumberOfCookies=float(input("How many cookies do you want to make?: "))
#calculation variables
modifiedAmountOfSugar=(userNumberOfCookies/standardCookieBatch)*standardCupsOfSugar
modifiedAmountOfButter=(userNumberOfCookies/standardCookieBatch)*standardCupsOfButter
modifiedAmountOfFlour=(userNumberOfCookies/standardCookieBatch)*standardCupsOfFlour
modifiedCostofSugar=(userNumberOfCookies/standardCookieBatch)*standardCostofSugar
modifiedCostofButter=(userNumberOfCookies/standardCookieBatch)*standardCostofButter
modifiedCostofFlour=(userNumberOfCookies/standardCookieBatch)*standardCostofFlour
totalCost=modifiedCostofSugar + modifiedCostofButter + modifiedCostofFlour

#prints the amount and cost of each portion of the recipe, and the total cost
print("For " + format(userNumberOfCookies, ".0f") + " sugar cookies " + "you need " '\n'
      + format(modifiedAmountOfSugar, ".2f") + " cups of sugar " + '\n'
      "at a cost of $" + format(modifiedCostofSugar, ".2f") + '\n'
      "and " + format(modifiedAmountOfButter, ".2f") + " cups of butter " '\n'
      "at a cost of $" + format(modifiedCostofButter, ".2f") + '\n'
     "and "  + format(modifiedAmountOfFlour, ".2f") + " cups of flour " + '\n'
      "at a cost of $" + format(modifiedCostofFlour, ".2f") + '\n'
       "your total cost will be $" + format(totalCost, ".2f") )
#this prints space between two sections
print('''
''')
#prints recipe link url
print("For detailed recipe instructions go to" + '\n'
"http://www.delish.com/cooking/recipe-ideas/recipes/a45306/3-ingredient-sugar-cookies/")
#prints space between sections
print('''
''')
#if else statement that prints a funny message regarding the users feelings about cookies
if userNumberOfCookies >= 96.0:
    print("You must really love cookies like even more than unicorns!")
elif userNumberOfCookies >= 48.0:
    print("You must love cookies like alot!")
elif userNumberOfCookies >= 24.0:
    print("You must at least enojoy cookies somewhat.")
elif userNumberOfCookies >= 12.0:
    print("You must feel somewhat nuetral regarding cookies.")
else:
    print("You hate cookies.")


