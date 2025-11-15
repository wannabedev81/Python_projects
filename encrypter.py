## this app will ask the user for a text input which will be encrypted and then shown the encrypted text
## it is possible to decrypt the text 

import random
import string

characters = " " + string.punctuation + string.digits + string.ascii_letters

characters = list(characters)

key = characters.copy()

random.shuffle(key)

#encryption

text = input("Enter a message to encrypt: ")

ciphertext = ""

for letter in text:
    index = characters.index(letter)
    ciphertext += key[index]

print(f"original message: {text}")
print(f"ciphered message: {ciphertext}")

#decryption

ciphertext = input("Enter a message to decrypt: ")
text = ""

for letter in ciphertext:
    index = key.index(letter)
    text += characters[index]

print(f"encripted text: {ciphertext}")
print(f"decrypted message: {text}")