# Create Rock, Paper, Scissors Game
import random
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_icons = [rock, paper, scissors]
print("My choice:")
print(game_icons[my_choice])
your_choice = random.randint(0, 2)
print("Your choice:")
print(game_icons[your_choice])
if my_choice == 0 and your_choice == 2:
    print("I Win")
elif my_choice == 1 and your_choice == 0:
    print("I Win")
elif my_choice == 2 and your_choice == 1:
    print("I Win")
elif my_choice == your_choice:
    print("It is a draw")
else:
    print("I lose")


