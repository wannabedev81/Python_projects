## 1. Count the number of words in a sentence without .split()

sentence = input("Please enter a sentence: ")

count_of_words = 1

for char in sentence: 
    if char == " ":
        count_of_words += 1

print(f"Your sentence has {count_of_words} words. ")

## 2. Find the smallest number in a list - without the use of .sorted()

numbers = [14, 1, 99, 27, 100, 12]

smallest = numbers[0]

for i in range(len(numbers)):
    if smallest > numbers[i]:
        smallest = numbers[i]

    print(f"{numbers[i]} and {numbers[i+1]}")
    print(smallest)


print(smallest)

## 3. Create a function that returns both the min and max of a list - without sorting

trial_list = [111, 23, 42, 1, 56, 34, 7]

def retunt_smallest_and_largest(list):

    smallest = list[0]
    largest = list[0]

    for item in list: 
        if item > largest: 
            largest = item
        elif item < smallest: 
            smallest = item
    
    return smallest, largest

print(retunt_smallest_and_largest(trial_list))

## 4. Count how many vowels appear in a sentence

def vowel_counter(text):
    list_of_vowels = "aeiouAEIOU"

    count_of_vowels = 0

    for char in text:
        if char in list_of_vowels:
            count_of_vowels += 1

    return count_of_vowels

print(vowel_counter(input("Please enter a text to check: ")))  

## 5. Merge two lists manually - without the use of "+" or .extend()

list1 = [1, 2, 3]
list2 = [4, 5, 6]

def list_merger(list1, list2):

    merged_list = []

    for item in list1:
        merged_list.append(item)
    
    for item in list2:
        merged_list.append(item)


    return merged_list

print(list_merger(list1, list2))

## 6. check if the number is prime - without math module

number = input("Please enter a number: ")

for num in range(len(number)):
    if number % num == number:
        print("The number is prime")
    else:
        print("The number is not prime")

 

## 7. Remove all vowels from a word

def remove_vowels(text):

    modified_text = ""
    vowels = "aeiouAEIOU"

    for char in text:
        if char not in vowels:
            modified_text += char
        else:
            continue

    return modified_text

print(remove_vowels(input("Please enter a word: ")))

## 8. Create a function that returns only the sum of only the odd numbers from a list

numbers = [10, 3, 7, 2, 9, 11]


def odd_numbers_total(list):
    
    total_of_odd_numbers = 0
    
    for num in list:
        if num % 2 != 0:
            total_of_odd_numbers += num

        else:
            continue
    
    return total_of_odd_numbers

print(odd_numbers_total(numbers))

## 9. Ask the user for 3 words and store them in a list - and print the list
list_of_words = []

for step in range(0, 3):
    word = input("please enter a word: ")

    list_of_words.append(word)

print(list_of_words)

## 10. Create a menu function that asks the user to choose an option
## functions: 1. Say hello 2. Multiply two numbers 3. Exit
## Ask user for choice and execute the option

is_running = True

print("Menu options: ")
print("1. Say hello")
print("2. Multiply two numbers")
print("3. Exit")

while is_running:
    selection = int(input("What option would you select? "))

    if selection == 1:
        print("Hello")

    elif selection == 2:
        number1 = int(input("Please enter a number: "))
        number2 = int(input("Please enter a second number: "))
        result = number1 * number2
        print(result)
    
    elif selection == 3: 
        is_running = False



