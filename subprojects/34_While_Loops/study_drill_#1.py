## Study Drill #1: 
## Convert this while-loop to a function that you can call, and replace 
## 6 in the test (i < 6) with a variable.

# Answer: 

i = 0 
limit = 6
numbers = []

while i < limit:
    print(f"At the top i is {i}")
    numbers.append(i)
    
    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")
    
print("The numbers: ")

for num in numbers:
    print(num)