def main():

    # Main function
    running = True
    startMenuIndex = 1
    endMenuIndex = 6
    startMajorModuleIndex = 1
    endMajorModuleIndex = 3
    majorModuleResourceCount = {"Industry": 0, "Science": 0, "Food": 0}
    majorModuleResourceLevel = {"Industry": 0, "Science": 0, "Food": 0}
    resourceBaseAmounts = {"Industry": 5, "Science": 2, "Food": 4}
    mechanicPalAmount = 0

    # Create main program loop
    while running:
        displayMenu()
        userInput = input()

        while userInput < startMenuIndex or userInput > endMenuIndex:
            # Ask the user to reinput their value
            print("Please reinput a value between 1 - 6")
            userInput = input()

        # If we got out of the loop, check to see which user
        if userInput == 1:
            # Change Major Modules resource counts
            print("Which one would you like to change?")
            print("1. Industry")
            print("2. Science")
            print("3. Food")
            print("> ")
            userInput = input()

            while userInput < startMajorModuleIndex or 
                userInput > endMajorModuleIndex:
                # Ask the user to reinput their value
                print("Please reinput a value between 1 - 3")
                userInput = input()
            defineResourceModuleTotals(majorModuleResourceCount, userInput); 
            
        elif userInput == 2:
            # Change Major Modules resource level
            print("hi")
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
    print("5. Display all resource levels based on resource count")
    print("6. End program")
    print("> ")


def defineResourceModuleTotals(majorModulesResourceCountList, userMenuChoice):
    if userMenuChoice == 1:
        # Industry
        print("How many total Industry modules of do you have?")
        userInput = input()
        
        while userInput < 0:
            # Ask the user to reinput their value
            print("Cannot have a negative amount of Industry modules")
            userInput = input()
            
        # Assign the value to the right spot
        majorModulesResourceCountList["Industry"] = "a"
        
    elif userMenuChoice == 2:
        # Science
        print("How many total Science modules of do you have?")
        userInput = input()
        
        while userInput < 0:
            # Ask the user to reinput their value
            print("Cannot have a negative amount of Science modules")
            userInput = input()
            
        # Assign the value to the right spot
        majorModulesResourceCountList["Science"] = userInput

    else:
        # Food
        print("How many total Food modules of do you have?")
        userInput = input()
        
        while userInput < 0:
            # Ask the user to reinput their value
            print("Cannot have a negative amount of Food modules")
            userInput = input()
        
        # Assign the value to the right spot
        majorModulesResourceCountList["Food"] = userInput


__name__ = "__main__"
# Run the main function to the program
if __name__ == "__main__":
    main()