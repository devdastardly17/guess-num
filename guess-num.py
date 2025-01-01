import random
import time
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

    #Checking if guess is correct
    attempt_num = 0
    start_time = time.time()
    
    for num in range(0,lives) :
        guess = int(input("Enter your guess: "))
        attempt_num += 1
        if guess == actual_num :
            playOn = False
            end_time = time.time()
            actual_time = round(end_time - start_time)
            print(f"Congratulations! You guessed the right number in {attempt_num} attempts in {actual_time} seconds")
            break
            
        else :
            lives -= 1
            print("You guessed wrong!")
            if guess > actual_num :
                print(f"Number is less than {guess}")
            else :
                print(f"Number is greater than {guess}")
            if lives == 0 :
               playAgain = input("Tsk Tsk!\nYou ran out of lives!\nYou might wanna try again. Would you like to? (Y/N)").lower()
               if playAgain == 'y' :
                   playOn = True
               else :
                   playOn = False
                   print("GaMe OvErRrRr")
