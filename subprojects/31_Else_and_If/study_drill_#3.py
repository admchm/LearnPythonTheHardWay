## Study Drill #3: 
## Try some more complex boolean expressions like cars > people or trucks < cars.

# Answer: 

people = 0
cars = 1
trucks = 2

if cars > people and cars > trucks:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.") # this
    
if trucks > cars or cars < people:
    print("That's too many trucks.") # this
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks and people != trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.") # this