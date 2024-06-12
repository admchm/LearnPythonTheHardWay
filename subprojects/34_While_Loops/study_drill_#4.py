## Study Drill #4: 
## Write it to use for-loops and range. Do you need the incrementor in 
## the middle anymore? What happens if you do not get rid of it?

# Answer: We don't need the incrementor anymore. We are providing the
#         'stop' argument at 6, so it will be working correctly.

numbers = []

for i in range(6):
    print(f"At the top i is {i}")
    numbers.append(i)
    
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")
    
print("The numbers: ")

for num in numbers:
    print(num)