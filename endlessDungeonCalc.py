import math

def main():
    # Main function
    running = True
    firstRun = True
    startMenuIndex = 1
    endMenuIndex = 6
    startMajorModuleIndex = 1
    endMajorModuleIndex = 3
    startMechanicalPalIndex = 1
    endMechanicalPalIndex = 2
    majorModuleResourceCount = {"Industry": 0, "Science": 0, "Food": 0}
    majorModuleResourceLevel = {"Industry": 1, "Science": 1, "Food": 1}
    majorModuleResourceLevelList = {1: 3, 2: 4, 3: 5, 4: 6}
    resourceBaseAmounts = {"Industry": 5, "Science": 2, "Food": 4}
    mechanicalPalLevelList = {1: 1, 2: 1.5, 3: 2, 4: 2.5}
    mechanicalPalLevel = 1
    mechanicPalAmount = 0
    playerAmount = 1

    # Create main program loop
    while running == True:
        
        if firstRun == True:
            displayMenu()
            firstRun = False
        else:
            print()
            displayMenu()
        userInput = int(input())
   
        while userInput < startMenuIndex or userInput > endMenuIndex:
            # Ask the user to reinput their value
            print("Please reinput a value between 1 - 6")
            print("> ", end='')
            userInput = int(input())

        # If we got out of the loop, check to see which userInput we got
        if userInput == 1:
            # Change Player Amount
            print("How many players are in the game? (Range of 1-4)")
            userInput = int(input())
            while userInput < 1 or userInput > 4:
                # Ask the user to reinput their value
                print("Please reinput a value between 1 - 4")
                print("> ", end='')
                userInput = int(input())
            playerAmount = userInput
            
        elif userInput == 2:
            # Change Major Modules resource counts
            print()
            print("Which one would you like to change?")
            print("1. Industry")
            print("2. Science")
            print("3. Food")
            print("> ", end='')
            userInput = int(input())

            while userInput < startMajorModuleIndex or userInput > endMajorModuleIndex:
                # Ask the user to reinput their value
                print("Please reinput a value between 1 - 3")
                print("> ", end='')
                userInput = int(input())
            defineResourceModuleTotals(majorModuleResourceCount, userInput); 
            
        elif userInput == 3:
            # Change Major Modules resource level
            print()
            print("Which one would you like to change?")
            print("1. Industry")
            print("2. Science")
            print("3. Food")
            print("> ", end='')
            userInput = int(input())

            while userInput < startMajorModuleIndex or userInput > endMajorModuleIndex:
                # Ask the user to reinput their value
                print("Please reinput a value between 1 - 3")
                print("> ", end='')
                userInput = int(input())
            defineResourceModuleLevel(majorModuleResourceLevel, userInput);
            
        elif userInput == 4:
            # Set mechanic pals count
            print()
            print("Which one would you like to change?")
            print("1. Set Levels")
            print("2. Set Count")
            print("> ", end='')
            userInput = int(input()) 
            
            while userInput < startMechanicalPalIndex or userInput > endMechanicalPalIndex:
                # Ask the user to reinput their value
                print("Please reinput a value between 1 - 2")
                print("> ", end='')
                userInput = int(input())
            
            if userInput == 1:
                # Level
                print("What level would you like to set it to? (Range of 1-4)")
                userInput = int(input())
                while userInput < 1 or userInput > 4:
                    # Ask the user to reinput their value
                    print("Please reinput a value between 1 - 4")
                    print("> ", end='')
                    userInput = int(input())
                mechanicalPalLevel = mechanicalPalLevelList[userInput]
            else:
                # Count
                print("How many total Mechanical Pals of do you have?")
                userInput = int(input())
                while userInput < 0:
                    # Ask the user to reinput their value
                    print("Cannot have a negative amount of Mechanical Pals?")
                    print("Please input a positive value")
                    print("> ", end='')
                    userInput = int(input())
                mechanicPalAmount = userInput
                
        elif userInput == 5:
            # Display the calculated values
            
            #Displays the resource values for only one player, with mechanical pal amounts and rounding
            if playerAmount == 1:
                
                mechPalValue = math.floor(returnMechanicalPalTotal(mechanicPalAmount, mechanicalPalLevel, mechanicalPalLevelList))
                print()
                print("Player Amount: " + str(playerAmount))
                print("MECHPAL: count/level/amount")
                print()
                print("  TYPE  |  LEVEL  |  COUNT  |  MECHPAL  |  TOTAL  |")
                print("---------------------------------------------------")
                
                # Industry
                totalResources = int(resourceBaseAmounts["Industry"] + mechPalValue + 
                (majorModuleResourceCount["Industry"] * majorModuleResourceLevelList[majorModuleResourceLevel["Industry"]]))
                
                print("Industry {0:5d} {1:9d} {2:8d}/{3:0d}/{4:0d} {5:8d}".format(majorModuleResourceLevel["Industry"], majorModuleResourceCount["Industry"], mechanicPalAmount, mechanicalPalLevel, mechPalValue, totalResources), end='')
                print()
                
                # Science
                totalResources = int(resourceBaseAmounts["Science"] + mechPalValue + 
                (majorModuleResourceCount["Science"] * majorModuleResourceLevelList[majorModuleResourceLevel["Science"]]))
                
                print("Science {0:6d} {1:9d} {2:8d}/{3:0d}/{4:0d} {5:8d}".format(majorModuleResourceLevel["Science"], majorModuleResourceCount["Science"], mechanicPalAmount, mechanicalPalLevel, mechPalValue, totalResources), end='')
                print()
                
                # Food
                totalResources = int(resourceBaseAmounts["Food"] + mechPalValue + 
                (majorModuleResourceCount["Food"] * majorModuleResourceLevelList[majorModuleResourceLevel["Food"]]))
                
                print("Food {0:9d} {1:9d} {2:8d}/{3:0d}/{4:0d} {5:8d}".format(majorModuleResourceLevel["Food"], majorModuleResourceCount["Food"], mechanicPalAmount, mechanicalPalLevel, mechPalValue, totalResources), end='')
                print()
                
            else:
                # If player amount is greater than 1, we need to implement a rounding system to make it fair for the players as based within the game.
                # For example if you have three players with 0 Industry generators, you will have 5(base) / 3 which doesn't divide nice evenly, so the game
                # will round to the next value divisible by 3 which is 6 in this case. 
                totalResources = (resourceBaseAmounts["Industry"] + returnMechanicalPalTotal(mechanicPalAmount, mechanicalPalLevel, mechanicalPalLevelList) + 
                (majorModuleResourceCount["Industry"] * majorModuleResourceLevelList[majorModuleResourceLevel["Industry"]]))
                
                totalSplitResources = (resourceBaseAmounts["Industry"] + returnMechanicalPalTotal(mechanicPalAmount, mechanicalPalLevel, mechanicalPalLevelList) + 
                (majorModuleResourceCount["Industry"] * majorModuleResourceLevelList[majorModuleResourceLevel["Industry"]])) / playerAmount
                
                print("Industry Level: %d\nIndustry Count: %d\nTotal Industry Per Player: %d\nTotal Industry: %d" % 
                (majorModuleResourceLevel["Industry"], majorModuleResourceCount["Industry"], totalSplitResources, totalResources))
                print()
                
                # Science
                totalResources = (resourceBaseAmounts["Science"] + returnMechanicalPalTotal(mechanicPalAmount, mechanicalPalLevel, mechanicalPalLevelList) + 
                (majorModuleResourceCount["Science"] * majorModuleResourceLevelList[majorModuleResourceLevel["Science"]]))
                
                totalSplitResources = (resourceBaseAmounts["Science"] + returnMechanicalPalTotal(mechanicPalAmount, mechanicalPalLevel, mechanicalPalLevelList) + 
                (majorModuleResourceCount["Science"] * majorModuleResourceLevelList[majorModuleResourceLevel["Science"]])) / playerAmount
                
                print("Science Level: %d\nScience Count: %d\nTotal Science Per Player: %d\nTotal Science: %d" % 
                (majorModuleResourceLevel["Science"], majorModuleResourceCount["Science"], totalSplitResources, totalResources))
                print()
                
                # Food
                totalResources = (resourceBaseAmounts["Food"] + returnMechanicalPalTotal(mechanicPalAmount, mechanicalPalLevel, mechanicalPalLevelList) + 
                (majorModuleResourceCount["Food"] * majorModuleResourceLevelList[majorModuleResourceLevel["Food"]]))
                
                totalSplitResources = (resourceBaseAmounts["Food"] + returnMechanicalPalTotal(mechanicPalAmount, mechanicalPalLevel, mechanicalPalLevelList) + 
                (majorModuleResourceCount["Food"] * majorModuleResourceLevelList[majorModuleResourceLevel["Food"]])) / playerAmount
                
                print("Food Level: %d\nFood Count: %d\nTotal Food Per Player: %d\nTotal Food: %d" % 
                (majorModuleResourceLevel["Food"], majorModuleResourceCount["Food"], totalSplitResources, totalResources))
                print()
        elif userInput == 6:
            # Display all resource levels based on resource count
            print("hi")
        else:
            # End the program
            print("hi")


def displayMenu():
    print("1. Change Player Amount")
    print("2. Change Major Modules resource counts")
    print("3. Change Major Modules resource level")
    print("4. Change Mechanic Pals")
    print("5. Display the calculated values")
    print("6. Display the calculated values using all resource levels")
    print("7. End program")
    print("> ", end='')

def returnMechanicalPalTotal(mpAmount, mpLevel, mpLevelList): 
    if(mpAmount == 0):
        return 0
    else:
        return ((mpAmount * mpLevelList[mpLevel]) / 2)

def defineResourceModuleLevel(majorModuleResourceLevelList, userMenuChoice):
    if userMenuChoice == 1:
        # Industry
        print("What level is your Industry Modules?")
        print("> ", end='')
        userInput = int(input())
        
        while userInput < 0:
            # Ask the user to reinput their value
            print("Cannot have a negative amount of Industry level?")
            print("Please input a positive value")
            print("> ", end='')
            userInput = int(input())
            
        # Assign the value to the right spot
        majorModuleResourceLevelList["Industry"] = userInput
        
    elif userMenuChoice == 2:
        # Science
        print("What level is your Science Modules?")
        print("> ", end='')
        userInput = int(input())
        
        while userInput < 0:
            # Ask the user to reinput their value
            print("Cannot have a negative amount of Science level")
            print("Please input a positive value")
            print("> ", end='')
            userInput = int(input())
            
        # Assign the value to the right spot
        majorModuleResourceLevelList["Science"] = userInput

    else:
        # Food
        print("What level is your Food Modules?")
        print("> ", end='')
        userInput = int(input())
        
        while userInput < 0:
            # Ask the user to reinput their value
            print("Cannot have a negative amount of Food level")
            print("Please input a positive value")
            print("> ", end='')
            userInput = int(input())
        
        # Assign the value to the right spot
        majorModuleResourceLevelList["Food"] = userInput

def defineResourceModuleTotals(majorModulesResourceCountList, userMenuChoice):
    if userMenuChoice == 1:
        # Industry
        print("How many total Industry modules of do you have?")
        print("> ", end='')
        userInput = int(input())
        
        while userInput < 0:
            # Ask the user to reinput their value
            print("Cannot have a negative amount of Industry modules")
            print("Please input a positive value")
            print("> ", end='')
            userInput = int(input())
            
        # Assign the value to the right spot
        majorModulesResourceCountList["Industry"] = userInput
        
    elif userMenuChoice == 2:
        # Science
        print("How many total Science modules of do you have?")
        print("> ", end='')
        userInput = int(input())
        
        while userInput < 0:
            # Ask the user to reinput their value
            print("Cannot have a negative amount of Science modules")
            print("Please input a positive value")
            print("> ", end='')
            userInput = int(input())
            
        # Assign the value to the right spot
        majorModulesResourceCountList["Science"] = userInput

    else:
        # Food
        print("How many total Food modules of do you have?")
        print("> ", end='')
        userInput = int(input())
        
        while userInput < 0:
            # Ask the user to reinput their value
            print("Cannot have a negative amount of Food modules")
            print("Please input a positive value")
            print("> ", end='')
            userInput = int(input())
        
        # Assign the value to the right spot
        majorModulesResourceCountList["Food"] = userInput


__name__ = "__main__"
# Run the main function to the program
if __name__ == "__main__":
    main()
