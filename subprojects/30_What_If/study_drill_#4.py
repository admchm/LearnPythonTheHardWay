## Study Drill #4: 
## Can you put other boolean expressions from Exercise 28 in the if-statement? Try it.

# Answer: 

people = 20
cats = 30
dogs = 15

if people <= cats:
    print("Too many cats! The world is doomed!")
    
if people >= cats:
    print("Not many cats! The world is saved!")
    
if people != dogs:
    print("The world is drooled on!")
    
if people and dogs:
    print("The world is dry!")
    
dogs += 50

if people and not dogs:
    print("People are greater than or equal to dogs.")
    
if people == dogs:
    print("People are less than or equal to dogs.")
    
if people != dogs:
    print("People are dogs.")