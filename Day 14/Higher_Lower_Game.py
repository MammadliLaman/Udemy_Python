import random
from art import logo, vs
from game_data import data


def random_account():
    """Generate a random account from the game data."""
    return random.choice(data)


def data_account(account):
    """Format account data into printable format."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name} a {description} from {country}"


def check_answers(guess, a_follower, b_follower):
    """Check if user is correct."""
    """Get follower count."""
    """If Statement"""
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"


def failed():
    play_again = input("Do you play again? Type 'Yes' or 'No':")
    if play_again == "Yes":
        game()
    else:
        return "Goodbye"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = random_account()
    account_b = random_account()

    while game_should_continue:
        account_a = account_b
        account_b = random_account()

        while account_a == account_b:
            account_b = random_account()

        print(f"Compare A: {data_account(account_a)}")
        print(vs)
        print(f"Compare B: {data_account(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answers(guess, a_follower_count, b_follower_count)

        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
            return failed()


game()










