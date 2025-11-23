#Zip function aggregates elements from 2 iterables

usernames = ["Joe", "Brian", "Peter"]
passwords = ("Pword", "1234", "12ab34cd")

users = dict(zip(usernames, passwords))

print(type(users))

for (key,value) in users.items():
    print(key + " : " + value)

#adding another iterable. 

usernames = ["Joe", "Brian", "Peter"]
passwords = ("Pword", "1234", "12ab34cd")
login_date = ["1/02/21", "11/02/21", "28/01/21"]

users = zip(usernames, passwords, login_date)

for i in users:
    print(i)

