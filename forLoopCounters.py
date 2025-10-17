## This is just a list of for loop exercises. 
import time


## Simple listing the numbers from a certain range
for number in range(1, 11):
    print(number)
print("You have reached the top.")


## Listing a input sign to form a triangle starting from the triangle base.
## Basically counting backwards. 

sign_input = input("Please select a sign? (*, @, &, +, -, $) ")

triangle_base = int(input("How many items the triangle base should have? "))

for step in reversed(range(1, triangle_base+1)):
    print(sign_input * step)

## Timer, which counts back the time remaining. 
## Time is a user input.


starting_time = int(input("Please input starting time in seconds: "))

for sec in range(starting_time, 0, -1):
    seconds = sec % 60
    minutes = int(sec / 60) % 60
    hours = int(sec / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time is up!")



