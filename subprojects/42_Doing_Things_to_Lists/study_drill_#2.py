## Study Drill #2: 
## Translate these two ways to view the function calls in English. For example, 
## more_stuff.pop() reads as, "Call pop on more_stuff." Meanwhile, pop(more_stuff) 
## means, "Call pop with argument more_stuff." Understand how they are really the same thing.

# Answer: 

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')  # call split on ten things
more_stuff = ["Day", "Night", "Song", "Frisbee", 
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # call pop on more_stuff
    print("Adding: ", next_one)
    stuff.append(next_one)      # call append on stuff
    print(f"There are {len(stuff)} items now.")

print(stuff.pop())              # call pop on stuff
print(' '.join(stuff))          # call join with argument stuff
                             
print(stuff)

print('#'.join(stuff[3:5]))     #call join with argument stuff