# Make your own "Choose Your Own Adventure" game. Use conditionals such as if, else, and elif statements to lay out the logic and the story's path in your program.

# Text Snippets from my example

#     'You're at a crossroad. Where do you want to go? Type "left" or "right"'
#     'You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
#     "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
#     "It's a room full of fire. Game Over."
#     "You found the treasure! You Win!"
#     "You enter a room of beasts. Game Over."
#     "You chose a door that doesn't exist. Game Over."
#     "You get attacked by an angry trout. Game Over."
#     "You fell into a hole. Game Over."


print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

i1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right").lower()

if i1 == "left":
    i2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()
    if i2 == "wait":
        i3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
        if i3 == "yellow":
            print("Congratulations! You win!")
        elif i3 == "red":
            print("You got burnt by fire! Game over!")
        elif i3 == "blue":
            print("You were eaten by beasts. Game over!")
        else:
            print("Oops! That's not acceptable. Game over!")
    else: 
        print("You got attacked by a trout. Game over!")
else:
    print("You fell into a hole. Game Over!")