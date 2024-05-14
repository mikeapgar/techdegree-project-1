"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
Mike Apgar 05-13-2024
--------------------------------
"""
# Set Range
RANGE = 10

# Import The Random Module
import random

# Begin Game And Pass In High Score
def start_game(score, count):

    # Provide A Welcome Message
    print("\n\n\n=============> WELCOME TO THE GUESSING GAME <=============\n")
    print("====================> BY MIKE APGAR <=====================")
    
    # Display High Score
    if count != 0:
        print("\n============> HIGH SCORE (least attempts): {} <============\n\n\n".format(score))
    else:
        print("\n\n")

    # Get Player Name
    player_name = input("Please enter your name to get started.   ")
    player_name = player_name.title()
    
    # Generate the Winning Number
    random_answer = random.randint(1, RANGE)
    
    # Continuous Guess Prompting Begins
    number_of_guesses = 0
    while True:
        
        # Get Initial Player Guess
        try:
            player_guess = int(input("\nHi {}, guess a number between 1 and {}.   ".format(player_name, RANGE)))
            number_of_guesses += 1 
        
        # Display Error Message For Invalid Input
        except ValueError:
            print("Invalid entry: Please enter an integar.")
            number_of_guesses += 1
        else:
            break

    # Provide Correct Feedback
    while True:
        try:
            
            # Continuously Get Player Guess
            while player_guess != random_answer:

                # Input Is Out Of Range, Guess Again
                if player_guess < 1 or player_guess > RANGE:
                    player_guess = int(input("\nSorry {}, the number is out of range. Please guess again.   ".format(player_name)))
                    number_of_guesses += 1 

                # Input Is Too Low, Guess Again   
                elif player_guess < random_answer:
                    player_guess = int(input("\nSorry {}, the number is higher. Please guess again.   ".format(player_name)))
                    number_of_guesses += 1 

                # Input Is Too High, Guess Again  
                elif player_guess > random_answer:
                    player_guess = int(input("\nSorry {}, the number is lower. Please guess again.   ".format(player_name))) 
                    number_of_guesses += 1
        
        # Display Error Message For Invalid Input
        except ValueError:
            print("Invalid entry: Please enter an integar.")
            number_of_guesses += 1
        else:
            break

    # Display Got It Message
    print("\nGot it {}, {} is the correct guess!".format(player_name, player_guess))

    # Display Number Of Attempts Message
    print("\nIt took you {} attempts to guess correctly.".format(number_of_guesses))

    # Display New High Score Message
    if number_of_guesses < score and count != 0:
        print("\nThat's a new high score!")

    # Display Option To Play Again
    while True:
        try:
            
            # Prompt User To Play Again
            play_again = input("\nDo you want to play again? (y/n)   ")
            if play_again.lower() == "n":

                # Provide a Goodbye Message
                print("\nThank you for playing The Guessing Game.\n")
            elif play_again.lower() == "y":

                # Set High Score And Play Again
                if number_of_guesses < score:
                    score = number_of_guesses
                count += 1
                start_game(score, count)
            else:

                # Raise Exception For Invalid Input
                raise Exception("Invalid entry: Please enter y or n.")
        except Exception as ex:
            print(ex)
        else:
            break


# Begin Game - Pass In High Score And Play Count
high_score = 100
play_count = 0
start_game(high_score, play_count)
