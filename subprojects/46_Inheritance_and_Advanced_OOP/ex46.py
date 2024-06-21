# In Python 3 you do not need to add the (object) after the name of 
# the class, but the Python community believes in "explicit is better than implicit"
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
        
class Employee(Person):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
        super(Employee, self).__init__(name)
        self.salary = salary
        
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