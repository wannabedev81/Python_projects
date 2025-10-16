## this program will ask the user to input a temperature. The program will ask the user if the given temperature
## is in F or C. Based on the asnwer the program will convert the temp to the alternative temperature (e.g.: C is given
## so the program will show the temp what it would be in F.).

temp_outside = float(input("What is the temperature outside? "))
question = input("Is the temperature in Fahrenheit or Celsius (F or C? ").upper()

if question == "F":
    temp_outside = round((temp_outside - 32) * 5 / 9, 1)
    print(f"The temperature is {temp_outside} in C.")

if question == "C": 
    temp_outside = round((temp_outside * 9) / 5 + 32, 1)
    print(f"The temperature is {temp_outside} in F.")

else: 
    print(f"The selected option {question}, is not valid selection.")

