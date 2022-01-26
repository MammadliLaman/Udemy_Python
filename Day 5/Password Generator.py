# Create Password Generator
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

import random
print("Welcome to the PyPassword Generator!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters = int(input("How many letters would you like in your password?\n"))
password_chars = list()
for letter in range(0, nr_letters):
    password_chars.append(random.choice(letters))
nr_symbols = int(input(f"How many symbols would you like?\n"))
for symbol in range(0, nr_symbols):
    password_chars.append(random.choice(symbols))
nr_numbers = int(input(f"How many numbers would you like?\n"))
for number in range(0, nr_numbers):
    password_chars.append(random.choice(numbers))

# Easy Solution
password = ''
for char in password_chars:
    password += char
print(password)

# Hard Solution
random.shuffle(password_chars)
shuffled_password = ''
for char in password_chars:
    shuffled_password += char
print(shuffled_password)












