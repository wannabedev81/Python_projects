## This program has 2 parts. First is a random number guesser program.
## Second part is the improved version showing the dice art as well after getting a random dice roll. 

import random

## Random number guesser

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)

guesses = 0
is_running = False

print("Welcome to the guessing game. ")
print(f"Please select a number between {lowest_num} and {highest_num}. ")

while is_running:
    guess = input("Please enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range. ")
            print(f"Please select a number between {lowest_num} and {highest_num}: ")
        elif guess < answer:
            print()
            print("Too low please guess again. ")
        elif guess > answer: 
            print()
            print("Too high, please try again. ")
        else:
            print("-------------------------")
            print("Congratulations")
            print(f"You guessed it right! The answer was: {answer}")
            print()
            print(f"The number of guesses is: {guesses}. ")
            is_running = False
    else:
        print("Invalid guess. ")
        print(f"Please select a number between {lowest_num} and {highest_num}: ")

## Dice roller with art

## unicode chars: ● ┌ ─ ┐ │ └ ┘


art_dictionary = {
    1: ("┌─────────┐", 
        "│         │", 
        "│    ●    │", 
        "│         │", 
        "└─────────┘"),
    2: ("┌─────────┐", 
        "│  ●      │", 
        "│         │", 
        "│      ●  │", 
        "└─────────┘"), 
    3: ("┌─────────┐", 
        "│  ●      │", 
        "│    ●    │", 
        "│      ●  │", 
        "└─────────┘"), 
    4: ("┌─────────┐", 
        "│ ●     ● │", 
        "│         │", 
        "│ ●     ● │", 
        "└─────────┘"), 
    5: ("┌─────────┐", 
        "│ ●     ● │", 
        "│    ●    │", 
        "│ ●     ● │", 
        "└─────────┘"), 
    6: ("┌─────────┐", 
        "│ ●     ● │", 
        "│ ●     ● │", 
        "│ ●     ● │", 
        "└─────────┘"),    
}

dice = []
total = 0
number_of_dice = int(input("How many dice you want to roll? "))

for die in range(number_of_dice):
    dice.append(random.randint(1, 6))

##for die in range(number_of_dice):
##    for line in art_dictionary.get(dice[die]):
##        print(line)

for line in range(5):
    for die in dice:
        print(art_dictionary.get(die)[line], end=" ")
    print()   

for die in dice:
    total += die
print(f"Total: {total}")

