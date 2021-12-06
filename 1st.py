YourChosenNumbers = []
reruns = 0

def NumbersOfTheDay():
    
    return 


def PickThree():
    for numbers in range(3):
        YourNumbers = int(input("Pick your three lucky numbrs: "))  
        if YourNumbers >= 0 or YourNumbers <= 9:
            YourChosenNumbers.append(YourNumbers)
        else:
            Invalid = print("You entered wrong numbers, try again (y/n)? ") 
            if Invalid == 'y':
                YourNumbers = int(input("Pick your three lucky numbrs: "))
                YourChosenNumbers.append(YourNumbers)
            else:
                print ("Thank you for playing...")    
    
    return sorted(YourNumbers)




