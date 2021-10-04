######## LEVEL THREE ########
# In level three, the computer's guesses are optimized to refine the range on the guesses based on whether they are too high or too low. Print how many guesses it takes the computer before it correctly guesses the number.

from random import choice

def play_level_3():
    player_number = int(input("Guess the computer's number (1-10): "))
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    guesses = 3
    correct = False


    while guesses > 0 and correct == False:
    
        computer_number = choice(num_list)
        print(computer_number)
        if computer_number == player_number:
            print("You have guess correctly")
            correct = True
        elif computer_number > player_number:
            print("The computer has guess too high")
            computer_num_index = num_list.index(computer_number)
            num_list = num_list[:computer_num_index]
            print(num_list)
        elif computer_number < player_number:
            print("The computer has guess too low")
            computer_num_index = num_list.index(computer_number)
            num_list = num_list[computer_num_index + 1:]
            print(num_list)
        guesses -= 1

    if guesses == 0 and correct == False:
        print("You have ran out of guesses")