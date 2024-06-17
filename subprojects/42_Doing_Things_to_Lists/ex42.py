ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", 
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")
    
print(stuff[1])             # Oranges
print(stuff[-1])            # Corn
                            # It retrieves parameters from the middle of the array and will subsequently move towards index [0]
print(stuff.pop())          # Corn
print(' '.join(stuff))      # Apples Oranges Crows Telephone Light Sugar 
                            # It takes all the elements in the stuff list and joins them into a single string separated by spaces. 
print(stuff)

print('#'.join(stuff[3:5])) # ???, Frisbee, Corn, Banana
                            # It takes elements from stuff from range 3:5 and returns single string separated by '#'

print("")
print(more_stuff[-1]) # Frisbee

three_things = "One Two Three"
print(' '.join(three_things))

# When to Use Lists
# You use a list whenever you have something that matches the list data structure's useful features:

# If you need to maintain order. Remember, this is listed order, not sorted order. Lists do not sort for you.
# If you need to access the contents randomly by a number. Remember, this is using cardinal numbers starting at 0.
# If you need to go through the contents linearly (first to last). Remember, that's what for-loops are for.