def main():
    # Main function
    running = True
    firstRun = True
    startMenuIndex = 1
    endMenuIndex = 6
    startMajorModuleIndex = 1
    endMajorModuleIndex = 3
    majorModuleResourceCount = {"Industry": 0, "Science": 0, "Food": 0}
    majorModuleResourceLevel = {"Industry": 0, "Science": 0, "Food": 0}
    resourceBaseAmounts = {"Industry": 5, "Science": 2, "Food": 4}
    mechanicPalAmount = 0

    # Create main program loop
    while running == True:
        print("Count")
        for x in majorModuleResourceCount:
            print(x)
            print(majorModuleResourceCount[x]) 
        print()
        
        print("Level")
        for x in majorModuleResourceLevel:
            print(x)
            print(majorModuleResourceLevel[x]) 
        print()
        
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

        # If we got out of the loop, check to see which user
        if userInput == 1:
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
            
        elif userInput == 2:
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
            
        elif userInput == 3:
            # Set mechanic pals count
            print("hi")
        elif userInput == 4:
            # Display the calculated values
            print("hi")
        elif userInput == 5:
            # Display all resource levels based on resource count
            print("hi")
        else:
            # End the program
            print("hi")


def displayMenu():
    print("1. Change Major Modules resource counts")
    print("2. Change Major Modules resource level")
    print("3. Set mechanic pals count")
    print("4. Display the calculated values")
    print("5. Display the calculated values using all resource levels")
    print("6. End program")
    print("> ", end='')

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
