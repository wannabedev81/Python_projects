## 1. Remove all duplicate characters from the string

textinput = "abracadabra"

reworked_text = ""

for char in textinput:
    if char in reworked_text:
        continue
    else:
        reworked_text += char

print(reworked_text)

## 2. Count how many words start with a vowel

input = "apple is on an orange table"

output = 0
vowels = "aeiouAEIOU"
word = ""
words = []

for char in input:
    if char == " ":
        words.append(word)
        word = ""
    else:
        word += char

words.append(word)

for item in words:
    if item[0] in vowels:
        output += 1

print(output)

## 3. Replacing a punctuation ("." "!" "?" " ")

textinput = "Not today!When the rain falls.Why not today?I just love it!"

punctuations = "?!.,"

reworked_text = ""

for char in textinput:
    if char in punctuations:
        reworked_text += " "
    else:
        reworked_text += char

print(reworked_text)

## 4. Finding the longest word in a sentence

sentence = "Today is not the best day for hiking because it is too cold outside."

word = ""
words = []
item_length = 0
longest_word = ""

for char in sentence:
    if char == " ":
        words.append(word)
        word = ""
    else:
        word += char

words.append(word)



for item in words:
    if len(item) > item_length:
        item_length = len(item)
        longest_word = item

print(f"The longest item has {item_length} characters and the word is {longest_word}. ")


## 5. Convert a list of words into a string with ; separator


words = ["apple", "pear", "banana"]

line_of_words = ""

for item in words:
    line_of_words += item + ";"

print(line_of_words)

## 6. Create a function that removes all empty strings from a list


list_of_items = ["hi", "", "hello", "", "greetings"]


def list_cleanup(list):
    result = []
    for item in list:
        if item != "":
            result.append(item)
    return result

print(list_cleanup(list_of_items))

## 7. Count how many times a word appears in a list


text = "red blue red green green blue blue red red red green"

color_apperance = {}
word = ""
words = []

for char in text:
    if char == " ":
        words.append(word)
        word = ""
    else:
        word += char

words.append(word)

for item in words:
    if item not in color_apperance:
        color_apperance[item] = 1
    else:
        color_apperance[item] += 1

print(color_apperance)

## 8. Extract only alphabetic characters from a string

input_text = "dsaél332k3né235l543,.!!??32klsda"

extract = ""

for char in input_text:
    if char.isalpha():
        extract += char
    else:
        continue

print(extract)


## 9. Create a simple login system: correct user name "user", correct pw "secret", max 3 attempts allowed
##  success: Login successful, 3 times wrong pw - Account locked



def login(): 
    username = ""
    password = ""
    attempts = 3

    while attempts > 0:
        username = input("Please enter your username: ")
        if username != "user":
            print("Wrong username.")
            attempts -= 1
        
        else:
            password = input("Please enter your password: ")
            if password != "secret":
                print("Wrong password. ")
                attempts -= 1
            else:
                print("Successful login. ")
                break
                
        if attempts == 0:
            print("You are locked out")
        

login()

## 10. Menu with 3 options: 1. Remove vowels from a string, 2. Return the number of words, 3. Exit

is_running = True 

print("Menu options: ") 
print("1. Removing vowels from a string: ") 
print("2. Return the number of words from an input: ") 
print("3. Exit") 

while is_running: 
    selection = int(input("What option would you select? ")) 
    
    if selection == 1: 
        input_text = input("Please enter a text message: ") 
        
        reworked_text = "" 
        vowels = "aeiouAEIOU" 
        
        for char in input_text: 
            if char not in vowels: 
                reworked_text += char 
                
        print(f"Your text without vowels is: {reworked_text}. ") 
        
    elif selection == 2: 
        string_input = input("Please enter a text: ") 
        
        counter = 0 
        word = "" 
        words = [] 
        
        for char in string_input: 
            if char == " ": 
                words.append(word) 
                word = ""
                
            else: word += char 
        
        words.append(word) 
        
        counter = len(words) 
        
        print(f"Your text has {counter} amount of words. ") 
    
    elif selection == 3: 
        is_running = False
