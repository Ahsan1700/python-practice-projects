import random
from choice_module import list_choices

player = int(input("Rock, Paper or Scissors? [0 / 1 / 2]\n"))
computer = random.randint(0,2)

print(list_choices[player])

print(f"COM chose: {computer}")
print(list_choices[computer])

if player >= 3 or player < 0:
    print("Invalid Input, You Lose!")

if computer == player:
    print("Tie!")
else:
    if (computer + 1) % 3 == player:
        print("You Win!")
    else:
        print("You Lose!")