#Jose Zalapa and Josh Bettencourt
#Initial recipe
import math
bakingPowderTeaspoon=float(.5)
butterCups=float(1)
sugarCups=float(1.5)
eggs=int(1)
vanillaTeaspoon=float(1)

again='y'
print("\tSugar Cookie Order")
print("----------------------------------------")
#Start of math
while(again=='y'):
    cookieInput=int(input("Enter the total number of cookies wanted:"))
    print("Ingredients Required",'\t\t',"Prices")
    print("----------------------------------------")
#ingredient conversions
    request=(cookieInput/48)
    customBakingPowderTeaspoon=float(request*bakingPowderTeaspoon)
    customButterCups=float(request*butterCups)
    customSugarCups=float(request*sugarCups)
    customEggs=int(math.ceil(request*eggs))
    customVanillaTeaspoon=float(request*vanillaTeaspoon)
#base price    
    priceBakingPowder=float(.04)
    priceButter=float(.50)
    priceSugar=float(.33)
    priceEgg=float(.08)
    priceVanilla=float(.04)
#total price based on ingredient total    
    customPriceBakingPowder=(request*priceBakingPowder)
    customPriceButter=(request*priceButter)
    customPriceSugar=(request*priceSugar)
    customPriceEgg=(request*priceEgg)
    customPriceVanilla=(request*priceVanilla)
    totalPrice=0
    totalPrice=customPriceBakingPowder+customPriceButter+customPriceSugar+customPriceEgg+customPriceVanilla

#Print Statements for ingredients and prices
    print("Baking Powder:",format(customBakingPowderTeaspoon,".2f")," tsps",'\t',"Cost $",format(customPriceBakingPowder,".2f"))
    print("Butter:",format(customButterCups,".2f"),"cups",'\t\t',"Cost $",format(customPriceButter,".2f"))
    print("Sugar:",format(customSugarCups,'.2f'),"cups",'\t\t',"Cost $",format(customPriceSugar,'.2f'))
    print("Eggs:",customEggs,"egg(s)",'\t\t\t',"Cost $",format(customPriceEgg,".2f"))
    print("Vanilla:",format(customVanillaTeaspoon,".2f"),"tsps",'\t\t',"Cost $",format(customPriceVanilla,".2f"))
    print("----------------------------------------")
    print("Total cost $",format(totalPrice,".2f"),sep='')
    print("")
    print("If you no longer have order requests enter a 0")
    again=input("otherwise enter 'y' to continue: ")
print("")
print("Please rate how helpful this was to you!")
score=int(input('Please enter a score between 1 and 10: '))
if(score<1 or score>10):
    while(score<1 or score>10):
        print("Error: invalid score!")
        score=int(input('Please enter a score between 1 and 10: '))
if(score<=10 and score>=8):
    print("Excellent help!!")
elif(score<=7 and score>=5):
    print("Somewhat helpful")
elif(score<5):
    print("We will let out techs know...=(")
print("")            
print("If you need any further information please visit these sites.")
print("http://allrecipes.com/recipe/9870/easy-sugar-cookies/")
print("https://www.extension.iastate.edu/sioux/sites/www.extension.iastate.edu/files/sioux/Baking%20ingredients%20price%20list.pdf")
