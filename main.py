
game_selection = input("Type '1' for Level One,  '2' for Level Two, and '3' for Level Three: ")

import level_1
import level_2
import level_3

if game_selection == '1': 
    level_1.play_level_1()
if game_selection == '2': 
    level_2.play_level_2()
else:
    level_3.play_level_3()

