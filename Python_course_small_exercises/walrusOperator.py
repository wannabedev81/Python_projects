#assignment expression
#assign values to variables 

#happy = True
#print(happy)

#print(happy := True)

#foods = list()

#while True:
#    food = input("What do you like: ")
#    if food == "quit":
#        break
#    foods.append(food)

#rewrite with walrus

foods = list()

while food := input("What food do you like: ") != "quit":
    foods.append(food)

