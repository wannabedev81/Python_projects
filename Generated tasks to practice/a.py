
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