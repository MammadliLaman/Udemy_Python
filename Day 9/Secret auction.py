from art import logo
print(logo)
import os
clear = lambda: os.system('cls')
dict = {}
while True:
    name = input("What's your name: ")
    bid_amount = int(input("What's is your bid: $ "))
    dict[name] = bid_amount
    adversary = input("Do there other competitor? Type 'Yes' or 'No': ")
    if adversary == "Yes":
        dict_new = {name: bid_amount}
        dict.update(dict_new)
        print(dict)
    else:
        print(dict)
        amount = 0
        person = ""
        for key in dict:
            value = dict[key]
            if value > amount:
                amount = value
                person = key
                print(f"{person} is winner of the auction.")
            else:
                continue
        break







