## This program will ask for input from the user to calculate 
## compound interest amount. 
## The user need to add: initial investment amount, rate and the time of investment.

starting_amount = 0 
rate = 0
time = 0

while starting_amount <= 0: 
    starting_amount = float(input("Please enter an amount you would like to invest? "))
    if starting_amount <= 0:
        print("The to be invested amount can not be 0 or negative. ")

while rate <= 0:
    rate = float(input("Please enter the rate? "))
    if rate <= 0:
        print("The rate can not be less than 0 or equal to 0. ")      

while time < 1:
    time = int(input("How long would the investment be (in years)? "))
    if time < 1:
        print("Time can not be less that 1 year. ")      

result_of_investment = starting_amount * pow(1 + rate / 100, time)
print(f"The expected amount at the end of your investment time, {time} year(s), is {result_of_investment: .2f}. ")

