#classes have always capital beginning in their names

from Oop_car import Car

car_1 = Car("Chevrolet","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
print(car_2.make)
print(car_2.model)
print(car_2.color)
car_2.stop()

car_1.wheels = 2
print(car_1.wheels)
print(car_2.wheels)




