## Study Drill #2: 
## Use your Person class to make 1000 people in a loop and store them 
## in a list.

# Answer:

class Person(object):
    
    def __init__(self, name, age, eyes):
        self.name = name
        self.age = age
        self.eyes = eyes
    
    def talk(self, words):
        print(f"I am {self.name} and {words}")

becky = Person("Becky", 39, "green")
becky.talk("I am talking here!")

people_list = []

for i in range(1000):
    people_list.append(Person("Becky", i, "green"))
    
print(f"people_list contains {len(people_list)} records")