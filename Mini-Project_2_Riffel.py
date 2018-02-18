batchOfCookies = 48

cupsOfSugarPer48Cookies = 1.3
costOfSugarPer48Cookies = .64

sticksOfButterPer48Cookies = 4
costOfButterPer48Cookies = 3.99

cupsOfFlourPer48Cookies = 1
costOfFlourPer48Cookies = .50

numberOfCookies = float( input( "Enter amount of cookies you want to make: "))

expectedCupsOfSugar = ( numberOfCookies / batchOfCookies ) * cupsOfSugarPer48Cookies
approximateCostOfSugar = ( numberOfCookies / batchOfCookies ) * costOfSugarPer48Cookies

expectedSticksOfButter = ( numberOfCookies / batchOfCookies ) * sticksOfButterPer48Cookies
approximateCostOfButter = ( numberOfCookies / batchOfCookies ) * costOfButterPer48Cookies

expectedCupsOfFlour = ( numberOfCookies / batchOfCookies ) * cupsOfFlourPer48Cookies
approximateCostOfFlour = ( numberOfCookies / batchOfCookies ) * costOfFlourPer48Cookies

totalCost = approximateCostOfSugar + approximateCostOfButter + approximateCostOfFlour

print( "To make " + str(numberOfCookies ) + " cookies you need " +\
       format( expectedCupsOfSugar, ".2f" ) + " cups of sugar, " +\
       "which costs approximately: $" + format( approximateCostOfSugar,",.2f" )+"\n" "and "+\
       format( expectedSticksOfButter, ".2f" ) + " sticks of butter, " +\
       "which costs approximately: $" + format( approximateCostOfButter,",.2f" )+"\n" "and "+\
       format( expectedCupsOfFlour, ".2f" ) + " cups of flour, " +\
       "which costs approximately: $" + format( approximateCostOfFlour,",.2f" )+"\n" +\
       "the total cost is approximately: $" + format ( totalCost,",.2f" ))

Recipe = input( "If you would like to see the recipe, press 'y'." )
if Recipe.lower() == 'y':
    print( "Step 1 - \nPreheat oven to 325°. \n" \
           "Step 2 - \nUse an electric mixer to cream the sugar and butter, whipping the two " \
           "until the butter is almost white and the mixture is light and fluffy, almost like " \
           "a slightly gritty frosting, then stir in flour. \n" \
           "Step 3 - \nForm the cookies into 1 balls, placing them about 2 inches apart on a baking sheet." \
           "If using sprinkles, flatten cookies into a disc shape and top with sprinkles. " \
           "Bake for 15 to 17 minutes, or until the edges of the cookies are lightly golden." )
else:
    print( "Have a nice day!" )
    



















           

