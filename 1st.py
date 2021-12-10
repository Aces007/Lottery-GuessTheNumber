# This variable will initialize the while loop for the user to retry or play the game again... 
Rerun = True

# And we begin with the program, this while loop will initialize the lottery program. 
while Rerun:
    import random
    # These will store the values of the randomly generated lottery digits done with the import random function above, and the chosen numbers 
    # or "lucky" numbers you have chosen for yourself.
    YourChosenNumbers = []; LotteryDigits = []
    Min = 0; Max = 9; LuckyDigits = random.randint(Min, Max)




# This will ask you for your lucky numbers should I call it and it will record it in preperation of comparing it with the lottery digits...
    for digits in range(3):
        ThinkOfYourPick = int(input("Pick your lucky numbers: "))
        if 0 <= ThinkOfYourPick <= 9:
            YourChosenNumbers.append(ThinkOfYourPick)
        else:
            print ("Error!, it should be within the Min&Max range")
            ThinkOfYourPick = int(input("Pick your lucky numbers: "))
            YourChosenNumbers.append(ThinkOfYourPick)
        # One additional information is this else statement executes if you pick numbers which are more than or less than the Min and Max
        # numbers indicated for the lottery digits.
        
# After entering your chosen lucky digits the program will now initialize the lottery digits that will be in comparison with your numbers......
    for luckydigits in range(3):
        while LuckyDigits in LotteryDigits:
            LuckyDigits = random.randint(Min, Max)
        LotteryDigits.append(LuckyDigits)
        
# Then, this if else statements will evaluate the results on whether you won or lost.
    if ThinkOfYourPick in YourChosenNumbers == LotteryDigits:
        print ("Winner")
        print ("Your Numbers", YourChosenNumbers, "Vs, The Winning Digits", LotteryDigits)        
        break
    else:
        print ("You loss")
        print ("Your Numbers", YourChosenNumbers, "Vs, The Winning Digits", LotteryDigits)        

# In the event of a loss, this will initialize and asks you if you would want to give another run with the game.
    InitializeRerun = input("Would you like to play again?: ")
    if InitializeRerun == 'Yes':
        print ("Here we go again")
        Rerun = True
    elif InitializeRerun == 'No':
        Rerun = False
        print ("Well, Thanks for playing with us, Better luck next time!")
        break
    else:
        Rerun = False
        print ("Thank you for trying, Better luck next time around!")            
        break