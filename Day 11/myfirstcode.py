import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand_list = []
dealer_hand_list = []


def initial_hands():
    for _ in range(0, 2):
        initial_card_dealer = cards[random.randint(0, 12)]
        dealer_hand_list.append(initial_card_dealer)
        initial_card_player = (cards[random.randint(0, 12)])
        player_hand_list.append(initial_card_player)
    temporary = dealer_hand_list[1]
    dealer_hand_list[1] = "*"
    print(player_hand_list, dealer_hand_list)
    dealer_hand_list[1] = temporary


def lets_play_again():
    print(logo)
    initial_hands()
    black_jack()


def black_jack():
    player_hand_sum = player_hand_list[0] + player_hand_list[1]
    print(f"Player's initial hand is {player_hand_sum}")
    if player_hand_sum == 21:
        print("Black Jack. Player won")
        player_hand_list.clear()
        dealer_hand_list.clear()
        lets_play_again()
    dealer_hand_sum = dealer_hand_list[0] + dealer_hand_list[1]

    def compare_final_results():
        if dealer_hand_sum < player_hand_sum <= 21:
            print("Player Wins")
            player_hand_list.clear()
            dealer_hand_list.clear()
        elif player_hand_sum < dealer_hand_sum <= 21:
            print("Dealer Wins")
            player_hand_list.clear()
            dealer_hand_list.clear()
        else:
            print("Draw")
            player_hand_list.clear()
            dealer_hand_list.clear()
        lets_play_again()

    player_hit = True
    while player_hit:
        if player_hand_sum > 21:
            print(f"Dealer's initial hand is {dealer_hand_sum}")
            print("Player loses")
            break
        if player_hand_sum != 21:
            choice = input("Player, do you like 'Hit' or 'Stand': ")
            if choice == "Hit":
                random_card = cards[random.randint(0, 12)]
                another_hit = player_hand_sum + random_card
                player_hand_sum = another_hit
                if player_hand_sum > 21 and random_card == cards[0]:
                    player_hand_sum -= 10
                print(f"Player's hand is {player_hand_sum} now")
                if player_hand_sum == 21:
                    print("Player Wins")
                    player_hand_list.clear()
                    dealer_hand_list.clear()
                    lets_play_again()
            elif choice == "Stand":
                print(f"Player's final hand is {player_hand_sum}")
                print(f"Dealer's initial hand is {dealer_hand_sum}")
                if dealer_hand_sum == 21:
                    print("Black Jack. Dealer won")
                    player_hand_list.clear()
                    dealer_hand_list.clear()
                    lets_play_again()
                elif player_hand_sum < dealer_hand_sum:
                    print(compare_final_results())
                else:
                    while dealer_hand_sum < 17:
                        after_hit1 = dealer_hand_sum + cards[random.randint(0, 12)]
                        dealer_hand_sum = after_hit1
                        print(f"Dealer's hand is {dealer_hand_sum}")
                        if dealer_hand_sum >= 17:
                            if dealer_hand_sum > 21:
                                print("Dealer loses")
                                break
                            else:
                                print(f"Dealer's final hand is {dealer_hand_sum}")
                                print(compare_final_results())
                                player_hit = False
                                player_hand_list.clear()
                                dealer_hand_list.clear()
                                lets_play_again()


lets_play_again()