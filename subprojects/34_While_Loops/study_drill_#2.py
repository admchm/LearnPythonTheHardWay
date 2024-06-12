## Study Drill #2: 
## Use this function to rewrite the script to try different numbers.

# Answer:

i = 1 
limit = 14
numbers = []

while i < limit:
    print(f"At the top i is {i}")
    numbers.append(i)
    
    i = i + 2
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")
    
print("The numbers: ")

for num in numbers:
    print(num)