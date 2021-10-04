######## LEVEL TWO ########
# In level two, the game is reversed and the user picks a number and the computer then has 3 guesses to select the correct answer.

player_number = input("Please choose a number 1-10: ")
guesses = 3 
correct = False

while guesses > 0 and correct == False:
    computer_number = randint(1,10)
    print(f"The computer has guessed {computer_number}")
    if computer_number == int(player_number):
        print("The computer has guessed correctly")
        correct = True
    else:
        print("The computer has not guessed correctly")
    guesses -= 1

if guesses == 0 and correct == False:
    print("You have ran out of guesses")