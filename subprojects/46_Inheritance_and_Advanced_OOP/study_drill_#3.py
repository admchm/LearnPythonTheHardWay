## Study Drill #3: 
## Fill out the animals, fish, and people in this exercise with 
## functions that make them do things. See what happens when functions
## are in a "base class" like Animal versus in, say, Dog.

# Answer: 

class Animal(object):
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        
class Cat(Animal):
    def __init__(self, name):
        self.name = name
        
class Person(object):
    def __init__(self, name):
        self.name = name
        
        self.pet = None
    
    def sing(self):
        print("All you need is love!")
        
class Employee(Person):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
        super(Employee, self).__init__(name)
        self.salary = salary
        
    def favorite_sentence(self):
        print("Work, work!")
        
class Fish(object):
    pass

class Salomon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")
satan = Cat("Satan")
mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 11000)
frank.pet = rover

flipper = Fish()
crouse = Salomon()
harry = Halibut()

# additional methods
mary.sing()
print("\n")

frank.favorite_sentence()
frank.sing()