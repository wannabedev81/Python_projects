## this application is a game where the user guesses letters of a text
## there is maximum 6 guesses allowed.
## by each good guess a letter is shown from the text.
## by each wrong guess a portion of a hangmans picture will be drawn.
## if the picture is completed the user lost the game
## if the text is guessed the user won the game. 
import random

words = ("orange", "coconut", "banana", "apple")

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_guesses):
    print("***************")
    for line in hangman_art[wrong_guesses]:
        
        print(line)
    print("***************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    
    wrong_guesses = 0
    guessed_letters = set()

    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input.")
            continue

        if guess in guessed_letters:
            print(f"The letter is already been guessed. ")
            continue
        
        if guess in answer:
            for character in range(len(answer)):
                if answer[character] == guess:
                    hint[character] = guess
        else:
            wrong_guesses += 1
            



if __name__ == '__main__':
    main()

