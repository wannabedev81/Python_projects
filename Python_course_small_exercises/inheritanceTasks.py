class Animal:
    alive = True

    def eat(self):
        print("This animal is eating.")
    
    
    def sleep(self):
        print("This animal is sleeping.")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running.")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming.")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying.")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
rabbit.run()
fish.swim()
hawk.fly()

#multi level inheritance

class Organism: 

    alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating.")

class Dog(Animal):
    def bark(self):
        print("This dog is barking.")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()

# multiple inheritance

class Prey:

    def flee(self):
        print("This animal is fleeing.")

class Predator: 
    
    def hunt(self):
        print("This animal is hunting.")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

fish.flee()
fish.hunt()

# method overriding. 

class Animal:
    
    def eat(self):
        print("This animal is eating.")
    

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot.")  ## This will be used because of the scope, first is always the local scope checked. Inherited
                                                    ## items will be checked later

rabbit = Rabbit()
rabbit.eat()
