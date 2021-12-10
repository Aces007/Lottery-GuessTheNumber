# This variable will initialize the while loop for the user to retry or play the game again... 
Rerun = True

# And we begin with the program, this while loop will initialize
while Rerun:
    import random
    YourChosenNumbers = []; LotteryDigits = []
    Min = 0; Max = 9; LuckyDigits = random.randint(Min, Max)





    for digits in range(3):
        ThinkOfYourPick = int(input("Pick your lucky numbers: "))
        if 0 <= ThinkOfYourPick <= 9:
            YourChosenNumbers.append(ThinkOfYourPick)
        else:
            print ("Error!, it should be within the Min&Max range")
            ThinkOfYourPick = int(input("Pick your lucky numbers: "))
            YourChosenNumbers.append(ThinkOfYourPick)
        SortEach = sorted(YourChosenNumbers)
        

    for luckydigits in range(3):
        while LuckyDigits in LotteryDigits:
            LuckyDigits = random.randint(Min, Max)
        LotteryDigits.append(LuckyDigits)
        

    if ThinkOfYourPick in YourChosenNumbers == LotteryDigits:
        print ("Winner")
        print ("Your Numbers", YourChosenNumbers, "Vs, The Winning Digits", LotteryDigits)        
    else:
        print ("You loss")
        print ("Your Numbers", YourChosenNumbers, "Vs, The Winning Digits", LotteryDigits)        

        
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