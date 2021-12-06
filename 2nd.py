import random

Guesses = 0


MysteryDigit = random.randint(0, 100)


while Guesses == 0:
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

if WhatIsIt == MysteryDigit:
    print (Guesses, "You figured it out!, Congratulations")

else:
    print (MysteryDigit, "You were so close!, Better luck next time...") 




