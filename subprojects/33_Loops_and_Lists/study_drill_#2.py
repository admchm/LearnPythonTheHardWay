## Study Drill #2: 
## Could you have avoided that for-loop entirely on line 22 and just 
## assigned range(0,6) directly to elements?

# Answer: of course, we could:
elements = []

for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

print("\n")    

# vs
elements = list(range(0, 6))
print(elements)