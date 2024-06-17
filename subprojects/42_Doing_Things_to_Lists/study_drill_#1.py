## Study Drill #1: 
## Take each function that is called, and go through the steps for function 
## calls to translate them to what Python does. For example, more_stuff.pop() is pop(more_stuff).

# Answer:

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')   # split(ten_things)
more_stuff = ["Day", "Night", "Song", "Frisbee", 
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # pop(more_stuff)
    print("Adding: ", next_one)
    stuff.append(next_one)      # append(next_one)
    print(f"There are {len(stuff)} items now.")

print(stuff.pop())              # pop(stuff)
print(' '.join(stuff))
                             
print(stuff)

print('#'.join(stuff[3:5])) 