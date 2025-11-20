#ducktyping : class of an object is less important than the method or attributes of it

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking.")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking.")

class Person:

    def catch_duck(self, duck):
        duck.walk()
        duck.talk()
        print("You cought the critter. ")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch_duck(duck)

person.catch_duck(chicken)
