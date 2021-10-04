

game_selection = input("Press 1 if you would like to guess the computer's number. Press 2 if you would like to have the computer guess your number: ")

import level_1
import level_3

if game_selection == 1: 
    level_1.play_level_1()
else:
    level_3.play_level_3()

