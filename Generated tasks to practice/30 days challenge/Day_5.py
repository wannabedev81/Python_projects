## 1. Check if two strings are anagrams

text1 = input("amor")
text2 = input("roma")

def anagram_examiner(text1, text2):

    is_anagram = False

    converted_text1 = list(text1)
    converted_text2 = list(text2)

    converted_text1.sort()
    converted_text2.sort()

    text1_returned = ""
    text2_returned = ""

    for letter in converted_text1:
        text1_returned += letter
    
    for letter in converted_text2:
        text2_returned += letter

    if text1_returned == text2_returned:
        is_anagram = True
    else:
        is_anagram = False
    
    return is_anagram

anagram_examiner(text1, text2)

## 2. MAnually remove all vowels from a string

text = "Hangos a harang ma"

restructured_text = ""
vowels = "AEIOUaeiou"

for letter in text:
    if letter not in vowels:
        restructured_text += letter
    else:
        continue

print(restructured_text)

## 3. Count how many unique numbers are in a string - removing duplicates

input = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 5]

output = []
counter = 0

for num in input:
    if num in output:
        continue
    else:
        output.append(num)
        counter += 1

print(output)
print(counter)

## 4. Manually find the third smallest number

numbers = [5, 2, 8, 1, 3]

smallest = float("inf")
second_smallest = float("inf")
third_smallest = float("inf")

for n in numbers: 
    if n < smallest:
        second_smallest = smallest
        third_smallest = second_smallest
        smallest = n
        print(smallest, second_smallest, third_smallest)

    elif n < second_smallest and n != smallest:
        second_smallest = n
    elif n > second_smallest and n != smallest:
        third_smallest = n

print(smallest, second_smallest, third_smallest)

## 5. Replace every second character in a string with "*"

textinput = "abcdefghij"

reformed_text = ""

for i in range(0, len(textinput)):
    if i % 2 == 0:
        reformed_text += textinput[i]
    else:
        reformed_text += '*'
 
print(reformed_text)

## 6. Count how many digits, letters and others are in a string: 

input = "dkli122&@#"

digits = 0
letters = 0
others = 0

for char in input:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        others += 1

print(f"The text has: {digits} digits, {letters} letters, and {others} other characters. ")

## 7. Multiply all even numbers in a list

example_input = [2, 3, 4, 5, 6]

result = 1

for i in range(0, len(example_input)):
    if example_input[i] % 2 == 0:
        result *= example_input[i]

    else:
        continue

print(result)

## 8. Check if a number is Armstrong

import math

number = "153"

def Armstrong_checker(number):
    
    is_Armstrong = False
    
    a = number[0]
    b = number[1]
    c = number[2]

    Armstrong = math.pow(int(a), 3) + math.pow(int(b), 3) + math.pow(int(c), 3)


    if Armstrong == int(number):
        is_Armstrong = True

    else:
        is_Armstrong = False
    
    return is_Armstrong

print(Armstrong_checker(number))

## 9. Create a function that asks the user for N number of numbers and returns the sum of only the even numbers

def even_number_summarizer(n):
    
    number = 0
    result = 0
    
    while n > 0: 
        number = int(input("Please enter the number: "))
        if number % 2 == 0:
            result += number
            n -= 1
        else:
            n -=1
    
    return result

print(even_number_summarizer(5))
        

## 10. While loop menu with options
## menu options: 1. Greet, 2. Add two numbers , 3. Quit

is_running = True

print("Menu options: ")
print("1. Greet")
print("2. Multiply two numbers")
print("3. Quit")

while is_running:
    selection = int(input("What option would you select? "))

    if selection == 1:
        print("Hi there")

    elif selection == 2:
        number1 = int(input("Please enter a number: "))
        number2 = int(input("Please enter a second number: "))
        result = number1 + number2
        print(result)
    
    elif selection == 3: 
        is_running = False