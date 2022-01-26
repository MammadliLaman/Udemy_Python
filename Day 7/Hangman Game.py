import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)
chosen_word = random.choice(word_list)

display = []
while len(chosen_word) > len(display):
    display.append("_")
print(display)

count = 0
lives = 6
while count < len(chosen_word):
    guess = input("Guess a letter: ").lower()
    found = False
    if guess in display:
        print(f"You have already guessed {guess}")
        continue
    for index in range(len(chosen_word)):
        if chosen_word[index] == guess and display[index] == '_':
            display[index] = chosen_word[index]
            count += 1
            found = True
    if not found:
        print(stages[lives])
        lives -= 1
    if lives < 0:
        print("You lose")
        break
    elif count == len(chosen_word):
        print(f"You won. The word is complete: {display}")

