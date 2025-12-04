## 1. Find the first character that does not repeat in a string
## without dictionaries or counting helper

input = "aabbcccddeeegfff"


for char in input:
    counter = 0

    for character in input:
        if char == character:
            counter += 1
    
    if counter == 1:
        print(f"The character that only appears once is: {char}. ")


## 2. Manually check if a string is a palindrome

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

## 3. Create a split logic to split the sentence into words

input = "This is an example sentence"


def word_slicer(text):
    word = ""
    words = []

    for char in text:
        if char == " ":
            words.append(word)
            word = ""
        else:
            word += char
    
    words.append(word)

    return words

print(word_slicer(input))

## 4. Find the second largest number in a list

numbers = [52, 23, 83, 13, 31]

largest = float("-inf")
second_largest = float("-inf")

for n in numbers: 
    if n > largest:
        second_largest = largest
        largest = n
    
    elif n > second_largest and n != largest:
        second_largest = n
    
print(second_largest)

## 5. Compress a string using run-length encoding

input = "aaadddddffggggghhj"


for char in input:
    counter = 0

    for character in input:
        if char == character:
            counter += 1
    print(f"{char}: {counter}")
    
