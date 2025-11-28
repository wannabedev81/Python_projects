## 1. Count how many times each digit appears in a number
## input must be a string, no .count(), output: dictionary with digit - how many times it appeared { '1': 2 }

#### Cannot solve

## Solution received:

number = input("Please enter a number: ")

digit_counter = {}

for digit in number:
    if digit in digit_counter:
        digit_counter[digit] += 1
    else:
        digit_counter[digit] = 1

print(digit_counter)

## 2. Remove all duplicates from a list manually - no set() no list(dict.fromkeys())

input = [ 1, 2, 4, 5, 4, 6, 7, 5, 6]

output = []
counter = 0

for num in input:
    if num in output:
        continue
    else:
        output.append(num)
    

print(output) 

## 3. Reverse the order of words in a sentence without split
## loop over characters 

### Cannot really solve
# solution received: 

input = "Hello world python"

word = ""
words = []

for character in input:
    if character == " ":
        words.append(word)
        word = ""
    else:
        word += character

#appending last word
words.append(word)

#reverse the order
reversed_input = ""

for w in range(len(words)-1, -1, -1):
    reversed_input += words[w]
    if w != 0:
        reversed_input += " "

print(reversed_input)

## 4. Find second smallest number in a list - with a single loop

##### Cannot solve
# solution given: 

numbers = [5, 2, 8, 1, 3]

smallest = float("inf")
second_smallest = float("inf")

for n in numbers: 
    if n < smallest:
        second_smallest = smallest
        smallest = n
    elif n < second_smallest and n != smallest:
        second_smallest = n

print(second_smallest)

## 5. Convert digits to #

input = "hello 123 wordl 9"

output = ""

for char in input:
    if char.isdigit():
        output += "#"
    else:
        output += char

print(output)


## 6. Count consonants - ignoring non-letters

input = "Python 3.9"

output = 0
vowels = "aeiouAEIOU"

for char in input:
    if char not in vowels and char.isalpha():
        output += 1

print(output)  

## 7. Multiply all numbers in a list

input = [ 2, 3, 4]

output = 1

for i in range(len(input)):
    output *= input[i]
    print(output)
    
print(output)

## 8. Check if a number is perfect the sum of its proper divisors equals the number

input = 6

divisors = 0

for num in range(1, input):
    if input % num == 0:
        divisors += num

if divisors == n:
    print("Perfect number")
else:
    print("Not perfect")

print(divisors)


## 9. Create a function that asks the user for N number of numbers and returns positive ones. 


def return_of_positives(numbers):
    positive_numbers = []

    is_running = True

    counter = numbers

    while is_running:
        number_to_add = int(input("please enter the number to the list: "))
        counter -= 1
        if number_to_add > 0:
            positive_numbers.append(number_to_add)
        else:
            continue
        if counter == 0:
            is_running = False
    return positive_numbers

print(return_of_positives(int(input("how many numbers would you like to input: "))))


## 10. Create a while loop password menu
## Ask user for pw, right pw is "letmein", wrong pw -> ask again. Max 3 attempts after 3 --> locked out. 

is_running = True
attempts = 3

while is_running:
    password = input("Please enter the password: ")
    if password != "letmein":
        print("Wrong password. ")
        attempts -= 1
        print(f"You have {attempts} left. ")
    else:
        print("Access granted. ")
        is_running = False

    if attempts == 0:
        print("Too many attempts you are locked out. ")
        is_running = False


    