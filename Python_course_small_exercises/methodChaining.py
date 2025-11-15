class Car:

    def turn_on(self):
        print("You start the engine.")
        return self

    def drive(self):
        print("You drive the car.")
        return self

    def brake(self):
        print("You breake the car.")
        return self

    def turn_off(self):
        print("You turned the car off.")
        return self

car = Car()

#car.turn_on().drive()

#car.brake().turn_off()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()

# the sign \ is needed to continue with the line
