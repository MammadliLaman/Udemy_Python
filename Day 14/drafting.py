import random
from art import logo, vs
from game_data import data

print(logo)


def first_round():
    """Returns a random data from the game_data."""
    dice = random.choice(data)
    return dice


print(first_round())


def compare(a, b):
    score = 0
    if a > b:
        new_score = score + 1
        print(f"You are right! Current score: {score}")
    score = new_score
    else:
        print(f"Sorry, that is wrong. Final score: {score}")


def play_game():
    is_game_over = False
    list_a = []
    list_b = []
    list_a.append(first_round())
    list_b.append(first_round())

    while not is_game_over:
        print(compare(list_a, list_b))




# print(f"Compare A: {list(dice.values)[0]}, a {list(dice.values)[2]}, from {list(dice.values)[3]}")
