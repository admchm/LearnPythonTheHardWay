## Study Drill #2: 
## Find the Python documentation for dictionaries and try to do even 
## more things to them.

# Answer: https://docs.python.org/3/tutorial/datastructures.html

diction = {'jack': 4098, 'sape': 4139, 'guido': 4127}
del diction['sape']
print(diction)

print(sorted(diction))

if "sape" in diction:
    print("avail")
    
if "guido" in diction:
    print("avail")