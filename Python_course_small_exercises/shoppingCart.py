## This program will be a shopping cart simulator. 
## It will ask for items purchased, their prices and will return
## a list of items with their prices and the total. 

foods = []
prices = []
total_price = 0

while True:
    food = input("What food you would like to buy? (or q to quit) ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Please enter the price of the {food}: EUR "))
        foods.append(food)
        prices.append(price)

print("------Your shopping cart items------")

for food in foods:
    print(food, end=" ")

for price in prices:
    total_price += price

print()
print(f"Your total is EUR {total_price}. ")

    