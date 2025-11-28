## 1. Count uppercase and lowercase letters in a string. 

input_text = "ADDHddklsieSS"

uppercase = 0
lowercase = 0

for letter in input_text:
    if letter == letter.upper():
        uppercase += 1
    else:
        lowercase += 1

print(f"The text has {uppercase} uppercase letters and {lowercase} lowercase letters. ")


## 2. Reverse a string manually - no reverse no slicing


input_text = "ADDHddklsieSS"

reverse_text = ""

for i in range(len(input_text)-1, -1, -1):
    reverse_text += input_text[i]

print(input_text)
print(reverse_text)

## 3. Count how many times each digit appears in a number


input = "1123435332438"

output = {}

for digit in input: 
    if digit in output:
        output[digit] += 1
    else: 
        output[digit] = 1

print(output)

## 4. Remove all spaces from the string - without replace


input = "slnlhl ljé lj l "

reworked_input = ""

for letter in input: 
    if letter != " ":
        reworked_input += letter        
    else:
        continue

print(reworked_input)

## 5. Count how many pairs of equal numbers exist in the list


input = [1, 1, 2, 2, 3, 3, 4]

number_of_items = {}

total_of_pairs = 0

for number in input:
    if number in number_of_items: 
        number_of_items[number] += 1
    else:
        number_of_items[number] = 1

for (key, value) in number_of_items.items():
    if value // 2: 
        total_of_pairs += 1

print(f"Total of pairs is {total_of_pairs}. ")

## 6. Manually check if a list is sorted - without sort() or sorted()


input = "1234567"

def sorted_checker(input):

    for i in range(0, len(input)-1):
        if int(input[i]) < int(input[i+1]):
            is_sorted = True
        else:
            is_sorted = False
    
    return is_sorted

print(sorted_checker(input))

## 7. Return the index of the first vowel in a string:


input_text = "122s2ddaoiien"

vowels = "aeiouAEIOU"
found = ""

for i in range(0, len(input_text)):
    if input_text[i] in vowels:
        found += input_text[i]
        print(i)
        break  

## 8. Create a function that returns a factorial of a number


input = 5

factorial = 1

for i in range(input, 0, -1):
    factorial *= i

print(factorial)

## 9. Convert all digits into a string to their word form

word_forms = { "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten"}

input = "shhoen1lhl2jl6"

reworked_text = ""

def digit_lookup(dictionary, char):
    for key, value in dictionary.items():
        if key == char:
            return value
     

for character in input: 
    if character.isdigit():
        reworked_text += (digit_lookup(word_forms, character))
        
    else:
        reworked_text += character

print(reworked_text)

## 10. Menu with 3 functions
## 1. reverse a string 2. count vowels 3. Exit

is_running = True

print("Menu options: ")
print("1. Reversing a string: ")
print("2. Count vowels: ")
print("3. Quit")

while is_running:
    selection = int(input("What option would you select? "))

    if selection == 1:
        input_text = input("Please enter a text message: ")

        reverse_text = ""

        for i in range(len(input_text)-1, -1, -1):
            reverse_text += input_text[i]

        print(f"Your text in reverse is: {reverse_text}. ")

    elif selection == 2:
        string_input = input("Please enter a text: ")
        vowels = "aeiouAEIOU"
        number_of_vowels = 0

        for char in string_input:
            if char in vowels:
                number_of_vowels += 1
            else:
                continue
        
        print(f"Your text has {number_of_vowels} amount of vowels. ")
    
    elif selection == 3: 
        is_running = False