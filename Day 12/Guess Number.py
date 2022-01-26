#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo
print(logo)
level = input("Play 'easy' or 'hard' level by typing the level difficulty: ")

if level == "easy":
    def easy_level():
        number = random.randint(1, 101)
        guessed_num = int(input("Guess a number between 1-100: "))
        soul_easy = 10
        while soul_easy > 0:
            if guessed_num > number:
                print("Too High")
            elif guessed_num < number:
                print("Too Low")
            else:
                return f"You guessed the number and You have left {soul_easy} souls."
            soul_easy -= 1
            guessed_num = int(input("Guess a number between 1-100: "))
        return "You have not any soul. You lost"
    print(easy_level())

else:
    def hard_level():
        number = random.randint(1, 100)
        guessed_num = int(input("Guess a number between 1-100: "))
        soul_hard = 5
        while soul_hard > 0:
            if guessed_num > number:
                print("Too High")
            elif guessed_num < number:
                print("Too Low")
            else:
                return f"You guessed the number and You have left {soul_hard} souls."
            soul_hard -= 1
            guessed_num = int(input("Guess a number between 1-100: "))
        return "You have not any soul. You lost"
    print(hard_level())





# if level == "easy":
#     def easy_level():
#         number = random.randint(1, 101)
#         guessed_num = int(input("Guess a number between 1-100: "))
#         not_found = True
#         soul_easy = 10
#         while not_found:
#             if guessed_num > number:
#                 print("Too High")
#                 soul_easy -= 1
#                 guessed_num = int(input("Guess a number between 1-100: "))
#             elif guessed_num < number:
#                 print("Too Low")
#                 soul_easy -= 1
#                 guessed_num = int(input("Guess a number between 1-100: "))
#             else:
#                 print("You guessed the number")
#                 print(f"You have left {soul_easy} souls.")
#                 not_found = False
#
#     easy_level()
# else:
#     def hard_level():
#         number = random.randint(1, 101)
#         guessed_num = int(input("Guess a number between 1-100: "))
#         soul_hard = 5
#         not_found = True
#         while not_found:
#             if guessed_num > number:
#                 print("Too High")
#                 soul_hard -= 1
#                 guessed_num = int(input("Guess a number between 1-100: "))
#             elif guessed_num < number:
#                 print("Too Low")
#                 soul_hard -= 1
#                 guessed_num = int(input("Guess a number between 1-100: "))
#             else:
#                 print("You guessed the number")
#                 print(f"You have left {soul_hard} souls.")
#                 not_found = False
#     hard_level()