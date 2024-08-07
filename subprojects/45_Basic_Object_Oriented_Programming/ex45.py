class Person(object):
    
    def __init__(self, name, age, eyes):
        self.name = name
        self.age = age
        self.eyes = eyes
    
    def talk(self, words):
        print(f"I am {self.name} and {words}")

becky = Person("Becky", 39, "green")
becky.talk("I am talking here!")

# dict contains all of the attributes we set in __init__
print(becky.__dict__)

# the class that becky comes from
print(becky.__class__)

# the contents of a class
print(becky.__class__.__dict__)

# a list of strings for everything
print(dir(becky))

# these two do the same thing
print(becky.talk)
print(getattr(becky, "talk"))

# this is the class's version of talk
print(becky.__class__.__dict__["talk"])