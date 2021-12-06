import random

Guesses = 0
# RequiredGuesses = 20

MysteryDigit = random.randint(0, 100)


while Guesses < 20:
    print ("What number did I provide?")
    WhatIsIt = int(input("What's the number?: "))
    MakingSure = input("Are you certain about your answer? (Y/N): ")
    if MakingSure == 'Y':
        Guesses += 1
        if WhatIsIt < MysteryDigit:
            print ("Less than")

        elif WhatIsIt > MysteryDigit:
            print ("Greater than")        

        else:
            break

    else:
        WhatIsIt = int(input("What's the number?: "))
        if WhatIsIt < MysteryDigit:
            print ("Less than")

        elif WhatIsIt > MysteryDigit:
            print ("Greater than")        

        else:
            break

if WhatIsIt == MysteryDigit:
    print (f"{Guesses} times", "You figured it out!, Congratulations")

else:
    print (f"{MysteryDigit} was the number", "You were so close!, Better luck next time...") 




