## Study Drill #4: 
## Do the inverse. Write a simple formula and use the functions in the same way to calculate it.

# Answer: I'm going to do a formula for 4 + (2 * 10) - 1 

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def substract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Here's the formula to calculate by using functions")

what = substract(add(4, multiply(2, 10)), 1)
print("That becomes: ", what)