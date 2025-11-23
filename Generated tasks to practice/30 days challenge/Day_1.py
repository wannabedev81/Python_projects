## 1. Ask the user for their name and print a personalized greeting

def personalized_greeting():
    name = input("what is your name? ")
    print(f"Hello {name}! Welcome to Python!" )

personalized_greeting()

## 2. Simple calculator - Ask the user for 2 numbers and print their sum

number_one = int(input("Please enter the first number: "))
number_two = int(input("Please enter the second number: "))

sum = number_one + number_two

print(f"The sum of {number_one} and {number_two} is: {sum}. ")

## 3. odd even checker - Ask the user for input and print whether it is odd or even

number = int(input("Please input a number: "))

if number % 2 == 0:
    print(f"The number {number} is even.")

else:
    print("The number is odd.")

## 4. word lenght counter - Ask the user to enter a word and count its characters

word = input("Please enter a word: ")

word_length = len(word)

print(f"The word {word} contains {word_length} amount of characters. ")

## 5. Temperature converter - ask the user for a celsius temperature and convert it to Fahrenheit. 

celsius = float(input("Please enter a Celsius degree: "))

fahrenheit = (celsius) * (9 / 5) + 32

print(f"The temperature {celsius} is {fahrenheit} in Fahrenheit. ")

## 6. Countdown - Ask the user for input and print a countdown to zero - for or while loop

start = int(input("Please enter where to start the countdown: "))

for number in range(start, 0, -1):
    print(number)

## 7. List of favourite food - create a list of min 5 foods and print each one on a separate line

list_of_food = []
counter = 0

while counter < 6:

    favourite_food = input("what is your favourite food: ")
    list_of_food.append(favourite_food)
    counter += 1

for food in list_of_food:
    print(food)


## 8. Find the largest of three numbers - Ask the user for 3 numbers and print the largest

first = int(input("Please enter the first number: "))
second = int(input("Please enter the second number: "))
third = int(input("Please enter the third number: "))

if third < first > second:
    print(f"The largest number is {first}. ")
elif third < second > first:
    print(f"The largest number is {second}. ")
else:
    print(f"The largest number is {third}. ")

## 9. Simple pw validator - Ask the user to input a pw and print: Access granted if the pw is "python123"
## otherwise print "wrong password"

password = input("Please input the password: ")

if password == "python123":
    print("Access granted")
else:
    print("Wrong password")

## 10. Replace vowel in a string - ask the user to type a sentence and replace vowels with * and print

text = input("Please enter a sentence: ")

vowels = "AEIOUaeiou"

modified_text = ""

for letter in text: 
    if letter in vowels:
        modified_text += "*"
    else:
        modified_text += letter

print(modified_text) 