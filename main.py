from random import randint

######## LEVEL ONE ########
# In level one, the computer generates a random number between 1 and 10 and the user has 3 guesses to pick the correct number. The computer will tell you if you are too high or too low.



# computer_number = randint(1, 10)
# guesses = 3
# correct = False

# while guesses > 0 and correct == False:
#     player_number = input("Guess the computer's number (1-10): ")
#     if computer_number == int(player_number):
#         print("You have guess correctly")
#         correct = True
#     else:
#         print("You have not guess correctly")
#     guesses -= 1

# if guesses == 0 and correct == False:
#     print("You have ran out of guesses")



######## LEVEL TWO ########
# In level two, the game is reversed and the user picks a number and the computer then has 3 guesses to select the correct answer.

# player_number = input("Please choose a number 1-10: ")
# guesses = 3 
# correct = False

# while guesses > 0 and correct == False:
#     computer_number = randint(1,10)
#     print(f"The computer has guessed {computer_number}")
#     if computer_number == int(player_number):
#         print("The computer has guessed correctly")
#         correct = True
#     else:
#         print("The computer has not guessed correctly")
#     guesses -= 1

# if guesses == 0 and correct == False:
#     print("You have ran out of guesses")

######## LEVEL THREE ########
# In level three, the computer's guesses are optimized to refine the range on the guesses based on whether they are too high or too low. Print how many guesses it takes the computer before it correctly guesses the number.

