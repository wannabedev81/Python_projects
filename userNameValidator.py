## This is a username validator to check the given username. 
## The following criterias are checked:
## - username cannot be longer than 8 characters
## - username cannot have spaces
## - username must be alphabetical
## User will be messaged if the username is correct or not. 
#  

while True:
    username = input("Please enter a username: ")

    if len(username) > 8:
        print("Username must be maximum 8 characters long.")
    elif not username.find(" ") == -1:
        print("Username cannot contain spaces.")
    elif not username.isalpha():
        print("Username must contain alphabetical characters.")
    else:
        print(f"Username {username} accepted.")
        break

