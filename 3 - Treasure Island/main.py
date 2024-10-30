print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're at a cross road. Where do you want to go?")
direction = input("\tGo Left or Right? [left / right]: ").lower()
if direction == 'right':
    print("You've come to a lake. There is an island in the middle of the lake.")
    action = input("\tWait for a Boat or Swim Across? [wait / swim]: ").lower()
    if action == 'wait':
        print("You arrive at the island unharmed. There is a house with 3 colored doors.")
        door = input("\tWhich colour will you choose? [red / green / blue]: ").lower()
        if door == 'red':
            print("You find a lighter and accidentally light yourself on fire!\n*Game Over*")
        elif door == 'green':
            print("You find a note that says 'Map to the One Piece'!\n***You Win***")
        elif door == 'blue':
            print("You fall into a hole that leads to the lake, you drown!\n*Game Over*")
        else:
            print("You walk headfirst into the wall and knock yourself out!\n*Game Over*")
    else:
        print("You run into the lak and realize you cant swim, you drown!\n*Game Over*")
else:
    print("That's not 'right', You fall into a hole!\n*Game Over*")