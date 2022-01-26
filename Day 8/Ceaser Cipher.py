alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar() -> str:
    cipher_text = " "
    for letter in text:
        if letter == ' ':
            cipher_text += letter
        if letter in alphabet:
            cipher_text += alphabet[get_index(letter)]

    return cipher_text


def get_index(letter: chr) -> int:
    letter_index = alphabet.index(letter)
    length = len(alphabet)
    if direction == "encode":
        return (letter_index + shift) % length if letter_index + shift < length else (letter_index + shift + 1) % length
    else:
        index = alphabet.index(letter)
        return index - shift if index - shift > 0 else index - shift - 1


print(f"The {direction}d text is {caesar()}")

# def encrypt(text, shift):
#     ciphered_text = ""
#     for letter in text:
#         if letter in alphabet:
#             if (alphabet.index(letter) + shift) < len(alphabet):
#                 cipher_text_index = (alphabet.index(letter) + shift) % len(alphabet)
#                 ciphered_letter = alphabet[cipher_text_index]
#                 ciphered_text += ciphered_letter
#             else:
#                 cipher_text_index = (alphabet.index(letter) + shift + 1) % len(alphabet)
#                 ciphered_letter = alphabet[cipher_text_index]
#                 ciphered_text += ciphered_letter
#         elif letter == ' ':
#             ciphered_text += letter
#
#     print(f"The encoded text is {ciphered_text}")
#
#
# encrypt(text, shift)
#
#
# def decrypt(text, shift):
#     deciphered_text = ""
#     for letter in text:
#         if letter in alphabet:
#             if (alphabet.index(letter) - shift) > 0:
#                 decipher_text_index = (alphabet.index(letter) - shift)
#                 deciphered_letter = alphabet[decipher_text_index]
#                 deciphered_text += deciphered_letter
#             else:
#                 decipher_text_index = (alphabet.index(letter) - shift - 1)
#                 deciphered_letter = alphabet[decipher_text_index]
#                 deciphered_text += deciphered_letter
#         elif letter == ' ':
#             deciphered_text += letter
#
#     print(f"The decoded text is {deciphered_text}")
#
#
# decrypt(text, shift)
