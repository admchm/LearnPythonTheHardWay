## Study Drill #3: 
## Add another variable to the function arguments that you can pass 
## in that lets you change the + 1 on line 8 so you can change how much it increments by.

# Answer: 

print("Give the number to set as a step")
step = int(input("> "))

i = 0 
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    
    i += step
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")
    
print("The numbers: ")

for num in numbers:
    print(num)