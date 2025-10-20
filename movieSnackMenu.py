## This program will ask from the user what he/she wants to select from the snack menu. 
## Then based on the selection it will grab information from a preset dictionary and
## show the user the selected items and relevant prices as well as the total. 

snack_menu = {"nachos": 23.50,
              "hotdog": 12.40,
              "popcorn": 10.50,
              "chocolate bar": 5.00,
              "pizzaslice": 7.00,
              "coke": 3.00,
              }

user_cart = []
total = 0

print("----------------------------")
print("-----Movie Snackbar Menu----")
for key, value in snack_menu.items():
    print(f"{key:15}: EUR {value:.2f}")
print("----------------------------")

while True:
    snack = input("Select an item (q to quit): ").lower()
    if snack == 'q':
        break
    elif snack_menu.get(snack) is not None:
        user_cart.append(snack)

print()
print("Your order is:")
print("-------------------------")
for snack in user_cart:
    total += snack_menu.get(snack)
    print(snack, end=" ")

print()
print("-------------------------")
print(f"Your total is: EUR {total:.2f} ")