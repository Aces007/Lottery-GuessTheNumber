# This is the function that will initialize genereating random numbers for you to guess.
import random
# Then this variable will record the number of guesses you have already provided.
Guesses = 0
# RequiredGuesses = 20

MysteryDigit = random.randint(0, 100)

# Now the program starts, it will begin with this while loop that will prompt you to enter your answer in accordance with the recommended 
# guesses you can provide, though you can exceed with the RequiredGuesses, it would be impressive if you guess the number within or less than
# 20 guesses. 
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

# Then, after number of tries and frustrations lol, this will execute if you figured out the number we provided secretly. 
if WhatIsIt == MysteryDigit:
    print (f"{Guesses} times", "You figured it out!, Congratulations")

# But, on the event of failure to guess on the required tries, we will reveal the answer to you immediately. 
else:
    print (f"{MysteryDigit} was the number", "You were so close!, Better luck next time...") 




