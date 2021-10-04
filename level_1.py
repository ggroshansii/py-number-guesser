
######## LEVEL ONE ########
# In level one, the computer generates a random number between 1 and 10 and the user has 3 guesses to pick the correct number. The computer will tell you if you are too high or too low.


computer_number = randint(1, 10)
guesses = 3
correct = False

while guesses > 0 and correct == False:
    player_number = input("Guess the computer's number (1-10): ")
    if computer_number == int(player_number):
        print("You have guess correctly")
        correct = True
    else:
        print("You have not guess correctly")
    guesses -= 1

if guesses == 0 and correct == False:
    print("You have ran out of guesses")
