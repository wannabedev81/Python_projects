#abstract classes are kind of a template - ghost class
# children classes define the details of the abstract method
# all children class need to have their defined form of abstract method of parent class



from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Motorcycle(Vehicle):
    def go(self):
        print("You are riding a motorcycle")

    def stop(self):
        print("This motorcycle stopped.")

class Car(Vehicle):
    def go(self):
        print("You are driving a car.")

    def stop(self):
        print("This car is stopped")


car = Car()
motorcycle = Motorcycle()

motorcycle.go()
car.stop()
