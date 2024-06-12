## Study Drill #2: 
## Change the numbers of cars, people, and trucks, and then trace through each if-statement to see what will be printed.

# Answer: 

people = 0
cars = 1
trucks = 2

if cars > people:
    print("We should take the cars.")   # this
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
    
if trucks > cars:
    print("That's too many trucks.")    # this
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.") # this