# importing module
from sys import argv

# script, first, second, third = argv
# print("The scripts is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)

# call in terminal:
# >python ex13.py first 2nd 3rd

## Study Drills
## 1. Try giving fewer than three arguments to your script. See that error you get? See if you can explain it.
# Answer:
# ValueError: not enough values to unpack (expected 4, got 1)
# This error means that not enough values were provided, so they cannot be assigned to first, second and third variables

## 2. Write a script that has fewer arguments and one that has more. Make sure you give the unpacked variables good names.
# Answer:
# print("How are you doing today?")
# script, answer = argv
# print(f"You wrote {answer}.")
# call in terminal:
# python ex13.py fine 

# print("Count to four:")
# script, one, two, three, four = argv
# print(f"First value: {one}")
# print(f"Second value: {two}")
# print(f"Third value: {three}")
# print(f"Fourth value: {four}")
# call in terminal
# python ex13.py one two three four


## 3. Combine input with argv to make a script that gets more input from a user. Don't overthink it. Just use argv to get something, 
## and input to get something else from the user. 4. Remember that modules give you features. Modules. Modules. Remember this because we'll need it later.
# Answer:
script, some_value = argv
print(f"You just pass {some_value}")
# call in temrinal 
# python ex13.py some_value
user_input = input("Could you repeat what you just have written? ")
#user_input = print("Could you repeat what you just have written?", input())
print(f"Thanks. Your answer is {user_input}")
