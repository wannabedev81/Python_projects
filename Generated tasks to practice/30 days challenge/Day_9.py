## 1. Read a data file and count valid lines
import os

filename = "records.txt"

def file_reader(file):
    
    try:
        with open(file, "r") as f:
            lines = f.readlines()
            return lines
            
    except FileNotFoundError:
        print("Cannot find file.")
        return []


lines = file_reader(filename)

counter = 0

for line in lines:
    line = line.strip()
    if line: 
        counter += 1

print(f"Number of lines in the list: {counter}")

## 2. Create a function that asks the user for a valid integer. E.g: what is your age?

def age():
    isrunning = True

    while isrunning:
        age = input("what is your age? ")

        if age.isdigit():
            age = int(age)
            print(f"Your age is {age}.")
            isrunning = False

        else:
            print("Please enter a valid integer: ")
            
age()

## 3. Menu system with validation and exit:
## 1: count characters in text, 2: count words in text, 3. Exit

is_running = True 

print("Menu options: ") 
print("1. Counting characters in a text: ") 
print("2. Return the number of words from an input: ") 
print("3. Exit") 

while is_running: 
    selection = int(input("What option would you select? ")) 
    
    if selection == 1: 
        input_text = input("Please enter a text: ") 
        counter = 0
        
        for char in input_text: 
            counter += 1
                        
        print(f"Your text has {counter} amount of characters. ") 
        
    elif selection == 2: 
        string_input = input("Please enter a text: ") 
        
        words = string_input.split()
        
        print(f"Your text has {len(words)} amount of words. ") 
    
    elif selection == 3: 
        is_running = False

## 4. Create a login system. Username="admin", password="1234", max attempts 3
## Username cannot be empty, pw cannot be empty, after 3 failed tries lock out. 
## store credentials in a dictionary. 

attempts = 3
users = {}

def login():
    
    global attempts
    
    while attempts > 0:
        username = input("Please enter your username: ")
        if not username: 
            print("Username cannot be empty. ")
            continue

        password = input("Please enter your password: ")
        
        if not password:
            print("Nothing entered. Please enter your password. ")
            continue

        if username == "admin" and password == "1234":
                users[username] = password
                print("Login successful", users)
                return
    
        attempts -= 1
        print(f"You have {attempts} attempts left. ")
        
    print("Too many tries. You are locked out. ")
        
login()

## 5. Simple file based pw verifier. 


is_running = True

while is_running: 
    username = input("Username: ")

    password = input("Password: ")

    with open("users.txt", "r") as file:
        content = file.read().splitlines()
    
    if f"{username}:{password}" in content:
        print("Login OK")
        is_running = False
    else:
        print("Invalid credentials. ")    


## 6. Logging user actions into a file - write a log.txt
## example: user admin login success

def age():
    isrunning = True

    while isrunning:
        age = input("what is your age? ")

        if age.isdigit():
            age = int(age)
            print(f"Your age is {age}.")
            isrunning = False

        else:
            print("Please enter a valid integer: ")
            

def login_checker():
    action = ""

    is_running = True
    while is_running: 
        username = ""
        password = ""

        with open("users.txt", "r") as file:
            content = file.read()
        username = input("Please enter your username: ")
        if username not in content:
            print("User is not yet registered. ")
        else: 
            password = input("Please enter your password: ")

            if username + ":" + password in content:
                print("Login OK")            
                is_running = False
                with open("log.txt", "a") as log:
                    action = "User: " + username + " logged in."
                    log.write(action + "\n")
            else:
                print("Invalid credentials.")
                with open("log.txt", "w") as log:
                    action = "User: " + username + " failed to log in."
                    log.write(action + "\n")

age()
login_checker()
with open("log.txt", "r") as log:
    content = log.read()
    print(content)

## 7. Word frequency from file - read from a file how many times each word appears. 

file_text = ""

with open("records.txt", "r") as file:
    file_text = file.read()

words = file_text.split()
frequency = {}

for word in words:
    if word not in frequency:
        frequency[word] = 1
    else:
        frequency[word] += 1

print(frequency)

## 8, CSV like parsin. 


fileread = ""

with open("parsing.txt", "r") as file:
    fileread = file.read()

cleaned_text = fileread.replace(",", " ")


with open("reworked_parsing.txt", "w") as destination:
    destination.write(cleaned_text)


## 9. Create an input sanitizer function that validates empty inputs, numbers in names, and special characters in both. 

def input_sanitizer(text, name):

    unwanted_characters = "&@$ß!%+§"

    if not text.strip():
        print("The text must contain at least 1 character.")
    
    for char in name:
        if char.isdigit():
            print("Names cannot contain numbers. ")
    
    for char in text + name:
        if char in unwanted_characters:
            print("Given text or name cannot contain any special characters. ")
       

input_sanitizer(" ", "Ad4am@")