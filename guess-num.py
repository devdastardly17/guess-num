import random
playOn = True
while playOn:
    print(
    """
    _______  ______________        ___        _  ____  ____  ______  _______ 
    / ___/ / / / __/ __/ __/       / _ |      / |/ / / / /  |/  / _ )/ __/ _ \\\\
    / (_ / /_/ / _/_\ \_\ \        / __ |     /    / /_/ / /|_/ / _  / _// , _/
    \___/\____/___/___/___/       /_/ |_|    /_/|_/\____/_/  /_/____/___/_/|_| 
    ===========================================================================
    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    """
    )
    # Picking a difficulty level.
    difficulty = int(input("""
    Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
                        
    Enter your choice:
    """))
    lives = 0
    if difficulty == 1 :
        lives += 10
        print("Great! You have selected the Easy level.\nLet's start the game!")
    elif difficulty == 2 :
        lives += 5
        print("Great! You have selected the Medium level.\nLet's start the game!")
    elif difficulty == 3 :
        lives += 3
        print("Great! You have selected the Hard level.\nLet's start the game!")

    # Computer guesses random number between 1 and 100
    actual_num = random.randint(1,100)
    #print(actual_num)

    #Checking if guess is accurate ans 
    for num in range(0,lives) :
        guess = int(input("Enter your guess: "))

        if guess == actual_num :
            print("Congratualtions! You guessed the right number")
        else :
            lives -= 1
            print("You guessed wrong!")
            if lives == 0 :
                print("Tsk Tsk!\nYou ran out of lives!\nYou might wanna try again")
                playOn = False

