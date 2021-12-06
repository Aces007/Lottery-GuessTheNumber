import random
YourChosenNumbers = [] 
Picks = 3

def YourPicks():
    while Picks > len(YourChosenNumbers):
        ThinkOfYourPick = int(input("Pick your lucky numbers: "))
        if 0 <= ThinkOfYourPick <= 9:
            YourChosenNumbers.append(ThinkOfYourPick)
        else:
            print ("Error!, it should be within the Min&Max range")
    
    SortEach = sorted(YourChosenNumbers)
    return SortEach


def TheWinningPicks():
    return sorted(random.sample(range(0, 9), Picks))
    


def DidYouWin():
    if YourNumbers == WinningNumbers:
        print ("Winner")
        print ("Your Numbers", YourNumbers, "Vs, The Winning Digits", WinningNumbers)        
    else:
        print ("You loss")
        print ("Your Numbers", YourNumbers, "Vs, The Winning Digits", WinningNumbers)        
        
    
YourNumbers = YourPicks()
WinningNumbers = TheWinningPicks()
Outcome = DidYouWin()