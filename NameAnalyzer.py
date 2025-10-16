def nameAnalyzer():
    fname = input("Please enter your firstname: ").capitalize()
    lname = input("Please enter your lastname: ").capitalize()
    name = fname + " " + lname
    print(f"Your full name is {name}. ")
    
    return name

yourname = nameAnalyzer()

length = len(yourname)
print(f"Your name is {length} character long.")

character_only = yourname.isalpha()
if character_only:
    print("Your name indeed contain only alphabetical characters.")