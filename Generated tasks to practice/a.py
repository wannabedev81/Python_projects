word_forms = { "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine", "10": "ten"}

input = "shhoen1lhl2jl6"

reworked_text = ""

def digit_lookup(dictionary, char):
    for key, value in dictionary.items():
        if key == char:
            return value
     

for character in input: 
    if character.isdigit():
        reworked_text += (digit_lookup(word_forms, character))
        
    else:
        reworked_text += character

print(reworked_text)