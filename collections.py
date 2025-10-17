## This file contains a series of actions with collections. How to work with them.

cars = ["Toyota", "BMW", "Audi", "Hyundai", "Volkswagen"]

## print(dir(cars)) ---> prints out command options to do with the directory
## print(help(cars)) 

print(len(cars))
print("Toyota" in cars)

cars[0] = "Kia"
for car in cars: 
    print(car)

cars.append("Lexus")
print(cars)

cars.remove("Kia")
print(cars)

cars.insert(0, "Chevrolet")
print(cars)

cars.sort()
cars.reverse()
print(cars)

cars.remove("Hyundai")
cars.append("Toyota")
print(cars.index("Toyota"))

cars = {"Toyota", "BMW", "Audi", "Hyundai", "Volkswagen"}
## print(dir(cars)) ---> prints out command options to do with the directory
## print(help(cars))

print(len(cars))
print("Toyota" in cars)

cars.add("Lexus")
print(cars)

cars = ("Toyota", "BMW", "Audi", "Hyundai", "Volkswagen")
## print(dir(cars)) ---> prints out command options to do with the directory
## print(help(cars))

print(cars)
print(len(cars))
print(cars.index("Hyundai"))
print(cars.count("Lexus"))