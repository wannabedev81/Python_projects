## In this file I have gathered some examples for how to interact with 2d collections. 

## First one is to create a numpad, like the ones on the old phones. 

numpad_items = ((1, 2, 3), 
                (4, 5, 6), 
                (7, 8, 9), 
                ("*", 0, "#"))

for row in numpad_items:
    for number in row:
        print(number, end=" ")
    print()

## Second to create a quiz game.

questions = ("Which planet is known as the red planet? ",
             "What is the chemical symbol for water? ",
             "How many sides a triangle have? ",
             "What is the largest land animal? ", 
             "What famous landmark is located in Paris, France? ")

options = (("A. Jupiter", "B. Venus", "C. Mars", "D. Saturn"), 
           ("A. H2O", "B. CO2", "C. N", "D. O"), 
           ("A. Four", "B. Two", "C. Five", "D. Three"), 
           ("A. Blue Whale", "B. African Bush Elephant", "C. Rhinoceros", "D. Giraffe"), 
           ("A. Big Ben", "B. Statue of Liberty", "C. Eiffel Tower", "D. Colosseum"))

answers = ("C", "A", "D", "B", "C")

guesses = []
score = 0
question_number = 0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_number]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("Right answer.")
    else:
        print("Incorrect")
        print(f"{answers[question_number]} is the correct answer. ")

    question_number +=1

print(f"""--------Result-----------
    Congratulations!
Your score is: {score} points""")



