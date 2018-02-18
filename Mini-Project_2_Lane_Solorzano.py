import webbrowser
import sys

# Christopher Lane
# Valerie Solorzano

# Welcome
print("\t\tWelcome! this program will provide key recipe ingridents to \
make the following ")
print('')

# Chocolate Chip Cookies (for 42 cookies)
print("\t\t\t\t\tChcocolate Chip Cookies")

# Ask user to input cookie amount
print('')
print('')
online = input("Enter 'yes' or 'no' if you would like to view the recipe \
in a browser window: \n")

# Conditional loop asking the user to provide valid feedback
while online != 'yes' and online != 'no':
	print("You entered an invalid value!")
	print("Please only enter 'yes' or 'no'!")
	online = input("Enter 'yes' or 'no' if you would like to view the \
recipe in a browser window? \n")

# if / elif to respond to user input at previous while loop
if online == 'yes':
	webbrowser.open("https://www.bettycrocker.com/recipes/\
	buttery-chocolate-chip-cookies/ff0a3092-58bd-49ab-a1fa-6c7ec0bd13fa", \
	new = 1)
	print('')
elif online == 'no':
	print('')
	pass

# Ask user to enter amount of cookies she / he would like to bake
cookies_amount = int(input("Enter how many cookies you would like to make: "))

# Calculation for the amount of ingridients  needed based on user 
# entry amount 
cups_butter = float(cookies_amount * (1.5 / 42))
cups_granulated_sugar = float(cookies_amount * (1.25 / 42))
cups_brown_sugar = float(cookies_amount * (1.25 / 42))
cups_flour = float(cookies_amount * (4 / 42))
cups_chocolate_chips = float(cookies_amount * (4 / 42))
tbsp_vanilla = float(cookies_amount * (1 / 42))
tsp_baking_soda = float(cookies_amount * (2 / 42))
tsp_salt = float(cookies_amount * (1 / 42))
eggs_amount = int(cookies_amount /  (42 / 2))

# Formula used for per cookie ingridients:
# cookie amount user entry * (((price for store bought weight / 
# some integer to get .25 cup) * 6 to get base recipe amount) / 
# 42 to get per cookie amount)

# Butter per cookie calculation
# Butter store purchase price: 8 oz. for $2.88
cost_butter = float(cookies_amount * (((2.88 / 4) * 6) / 42))

# Granulated sugar per cookie calculation 
# Granulated sugar store purchase price: 64 oz. for $1.98
cost_granulated_sugar = float(cookies_amount * (((1.98 / 32) * 5) / 42))

# Brown sugar per cookie calculation
# Brown sugar store purchase price: 32 oz. for $1.98
cost_brown_sugar = float(cookies_amount * (((1.98 / 16) * 5) / 42))

# Flour per cookie calculation
# Flour store purchase price: 80 oz. for $2.56
cost_flour = float(cookies_amount * (((2.56 / 40) * 16) / 42))

# Chocolate chips per cookie calculation
# Chocolate chips store purchase price: 20 oz. for $5.68
cost_chocolate_chips = float(cookies_amount * ((5.68 / 10) * 16) / 42)

# Vanilla per cookie calculation
# Vanilla store purchase price: 2 oz. for $1.98
cost_vanilla = float(cookies_amount * (1.98 / 42))

# Baking soda per cookie calculation
# Baking soda store purchase price: 96 tsp. for $1.48
cost_baking_soda = float(cookies_amount * ((1.48 / 40) / 42))

# Salt per cookie calculation
# Salt store purchase price: 156 tsp. for $1.48
cost_salt = float(cookies_amount * ((1.48 / 156) / 42))

# Eggs per cookie calculation
# Eggs store purchase price: 18 pcs. for $3.98
cost_eggs = float((3.98 / 18) * eggs_amount)

# Total estimated cost
total_cost = cost_butter + cost_granulated_sugar + cost_brown_sugar + \
cost_flour + cost_chocolate_chips + cost_vanilla + cost_baking_soda + \
cost_salt + cost_eggs

# Display shoppinglist with price per ingridient needed based on 
# user input cookie amount
print('')
print('')
print("For " + str(cookies_amount) + " cookies you will need to buy: ")
print('')
print("\t\tIngidients" + "\t\t\tPrice")
print("\t\t----------" + "\t\t\t-----")
print("\t\tbutter \t\t\t\t$" + str(format(cost_butter, '.2f'))) 
print("\t\tgranulated sugar \t\t$" + str(format(cost_granulated_sugar, '.2f')))
print("\t\tbrown sugar \t\t\t$" + str(format(cost_brown_sugar, '.2f')))
print("\t\tflour \t\t\t\t$" + str(format(cost_flour, '.2f')))
print("\t\tchocolate Chips \t\t$" + str(format(cost_chocolate_chips, '.2f')))
print("\t\tvanilla \t\t\t$" + str(format(cost_vanilla, '.2f')))
print("\t\tbaking Soda \t\t\t$" + str(format(cost_baking_soda, '.2f')))
print("\t\tsalt \t\t\t\t$" + str(format(cost_salt, '.2f')))
print("\t\teggs \t\t\t\t$" + str(format(cost_eggs, '.2f')))
print("\t\t\t\t\t\t" + "______")
print("\t\t\t\tTotal Cost\t$" + str(format(total_cost, '.2f')))  

# Display recipe with ingridients, amount needed, and meassuring type 
print('')
print('')
print("For " + str(cookies_amount) + " cookies, you will need: ")
print('')
print("\tIngridients" + "\t\tMeassurement" + "\t\tType")
print("\t-----------" + "\t\t------------" + "\t\t----")
print("\tbutter \t\t\t" + str(format(cups_butter, '.2f')) + "\t\t\tcups")
print("\tgranulated sugar \t" + str(format(cups_granulated_sugar, '.2f')) + "\t\t\tcups")
print("\tbrown sugar \t\t" + str(format(cups_brown_sugar, '.2f')) + "\t\t\tcups")
print("\tflour \t\t\t" + str(format(cups_flour, '.2f')) + "\t\t\tcups")
print("\tchocolate chips \t" + str(format(cups_chocolate_chips, '.2f')) + "\t\t\tcups")
print("\tvanilla \t\t" + str(format(tbsp_vanilla, '.2f')) + "\t\t\ttablespoon")
print("\tbaking soda \t\t" + str(format(tsp_baking_soda, '.2f')) + "\t\t\tteaspoon")
print("\tsalt \t\t\t" + str(format(tsp_salt, '.2f')) + "\t\t\tteaspoon")
print("\teggs \t\t\t" + str(eggs_amount))

# Display baking instructions to user
print('')
print('')
print("\t\t\t\t\tBaking Instructions")
print('')
print("Step 1 \t Heat oven to 350ºF.")
print("Step 2 \t Mix butter, sugars, vanilla, and eggs in a large \
bowl with a spoon.")
print("Step 3 \t Stir in flour, baking soda and salt.")
print("Step 4 \t Stir in chocolate chips.")
print("Step 5 \t Drop dough rounded measuring tablespoonfuls about 2 \
inches apart onto ungreased cookie sheet.")
print("Step 6 \t Bake 12 to 15 minutes or until light brown.")
print("Step 7 \t Let the cookies cool slightly.")
print("Step 8 \t Remove from cookie sheet to wire rack; let them cool.")
print('')

# Display ordering informration 
print('')
print("For ordering prices see below: ")
print('')


# Variable for full ordering price of 12 (one dozen) cookies with a \
#profit margin of 50%
sales_price = 7.80 

# discount rates
discount_ten = 0.10
discount_fifteen = 0.15
discount_twenty = 0.20
discount_twenty_five = 0.25 

# Ask user to input number of dozen they would like to order
number_of_dozens = int(input("Enter the amount of cookies in dozens \
you would like to order: "))

# Price calculation for cookies based on amount of dozen ordered
if 10 <= number_of_dozens <= 19:
	print("You will receive a discount of " + \
		str(format(discount_ten, '.0%')))
	print("Your total cost on your purchase will be: $" + \
		str(format((sales_price * number_of_dozens) - \
		((sales_price * number_of_dozens) * discount_ten), ',.2f')))
elif 20 <= number_of_dozens <= 29:
	print("You will receive a discount of " + \
		str(format(discount_fifteen, '.0%')))
	print("Your total cost on your purchase will be: $" + \
		str(format((sales_price * number_of_dozens) - \
		((sales_price * number_of_dozens) * discount_fifteen), ',.2f'))) 
elif 30 <= number_of_dozens <= 39:
	print("You will receive a discount of " + \
		str(format(discount_twenty, '.0%')))
	print("Your total cost on your purchase will be: $" + \
		str(format((sales_price * number_of_dozens) - \
		((sales_price * number_of_dozens) * discount_twenty), ',.2f')))
elif 40 <= number_of_dozens:
	print("You will receive a discount of " + \
		str(format(discount_twenty_five, '.0%')))
	print("Your total cost on your purchase will be: $" + \
		str(format((sales_price * number_of_dozens) - \
		((sales_price * number_of_dozens) * discount_twenty_five), ',.2f')))
else:
	print("I am sorry but you do not qualify for a discount. \
	\nOur discounts start with the purchase of ten dozen or more.")
	print("The total on your purchase will be: $" + \
	str(format(sales_price * number_of_dozens, '.2f')))

print('')
print('')

close = input("Type exit to close the program! \n")

if close == 'exit':
	sys.exit()

