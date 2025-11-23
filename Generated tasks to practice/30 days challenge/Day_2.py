## 1. Reverse a string manually - without the use of the step function in dictionaries or without the reverse() function

def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]

print(reverse("Alma"))


## 2. Count letter frequency - Return a dictionary for "banana"

def count_letter_frequency(text):
    counted_letters = {}

    for char in text:
        number_of_characters = text.count(char)
        counted_letters.update({char: number_of_characters})

    return counted_letters

print(count_letter_frequency("banana"))

##### A better soltuion to it:

def count_letter_frequency(text):
    counted_letters = {}

    for char in text:
        if char not in counted_letters:
            counted_letters[char] = 1
        else:
            counted_letters[char] += 1

    return counted_letters

print(count_letter_frequency("banana"))




## 3. Ask the user for 5 numbers and return the average

numbers = []
total = 0
average = 0

for i in range(0, 5): 
    
    number = int(input("Please enter a number"))
    numbers.append(number)
    total += number
    
average = total / len(numbers)


print(average)

### Alternative solution

numbers = []
total = 0
average = 0

for i in range(5):
    numbers.append(int(input("Please enter a number: ")))

average = total(numbers) / len(numbers)

print(average)


## 4. Find the second largest number in a list - without sorted()

list_of_numbers = [125, 45, 32, 64, 23]

greater = 0
lesser = 0

for step in range(len(list_of_numbers)-1):
    if list_of_numbers[step] > greater:
        greater = list_of_numbers[step]

for step in range(len(list_of_numbers)-1):
    if list_of_numbers[step] > lesser and list_of_numbers[step] != greater:
        lesser = list_of_numbers[step]
   
print("-------------------------")     
print(greater)
print(lesser) 

## 5. Check if a word is a palindrome

def palindrome_check(word):

    reverse_word = ""
    counter = len(word)-1

    for step in range(counter, -1, -1):
        reverse_word += word[step]

    if reverse_word == word:
        return True
    else:
        return False

print(palindrome_check("racecar"))
print(palindrome_check("apple"))

## 6. Sum all even numbers from 1 to N

def sum_even_numbers():

    number = int(input("Please enter a number until all even numbers should be summed: "))

    sum = 0

    for num in range(1, number +1):
        if num % 2 == 0:
            sum += num
        else:
            continue
        
    return sum

print(sum_even_numbers())

## Alternative solution without input calls in function: 

def sum_even_numbers(n):

    total = 0

    for num in range(2, n+1, +2):
        if num % 2 == 0:
            total += num
        else:
            continue
        
    return total

print(sum_even_numbers(int(input("Please enter a number until all even numbers should be summed: "))))


## 7. Print each word in a new line - "Hello world this is Python"


def print_words(sentence):
    
    sentence = sentence.replace(" ", "\n")

    return sentence


print(print_words("Hello world this is Python"))

## 8. Converting a list to a "," separated string

original_list = ['a', 'b', 'c']



def converting_list(list):
    stringlist = ""

    for item in list:
        stringlist += item + ", "
    
    return stringlist

print(converting_list(original_list))

## 9. Replacing spaces with hyphens and uppercase

def format_stringtext(text):

    formatted_text = ""

    for letter in text: 
        if letter.isalpha():
            formatted_text += letter.upper()
        elif letter == " ":
            formatted_text += letter.replace(" ", "-")
    return formatted_text

print(format_stringtext("hello world"))

## 10. Ask for number until input == done - Return the total and the average

total = 0
average = float(0)

counter = 1

while counter >= 0:

    number = input("Please input a nother number or write 'done' to quit: ")
    
    if number.lower() == "done":
        break
    
    else:
        number = int(number)
        total += number
        average = total / counter
        counter += 1

print(total)
print(average)



