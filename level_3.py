######## LEVEL THREE ########
# In level three, the computer's guesses are optimized to refine the range on the guesses based on whether they are too high or too low. Print how many guesses it takes the computer before it correctly guesses the number.

from random import choice

def play_level_3():

    print(" ")
    print(" ")
    print(" ")
    print("Welcome to Level 3")
    print(" ")
    print("--")
    print(" ")
    print("In level three, the computer's guesses are optimized to refine the range on the guesses based on whether they are too high or too low. Print how many guesses it takes the computer before it correctly guesses the number.")
    print(" ")
    print("--")
    print(" ")


    player_number = int(input("Pick a number for the computer to guess (1-10): "))
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    num_guesses = 0
    correct = False


    while correct == False:
    
        computer_number = choice(num_list)
        print("Computer's Guess:", computer_number)
        if computer_number == player_number:
            print("The computer picked the correct number")
            correct = True
            print(f"It took the computer {num_guesses} guesses")
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
        num_guesses += 1
