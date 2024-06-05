## Study Drill #3: 
## Once you have the formula worked out for the puzzle, get in there and see what happens when you modify the parts
## of the functions. Try to change it on purpose to make another value.

# Answer: All of the values, especially "what" value, will be altered

def add(a, b, c):
    print(f"ADDING {a} + {b} + {c}")
    return a + b + c

def substract(a, b, c):
    print(f"SUBSTRACTING {a} - {b} - {c}")
    return a - b - c

def multiply(a, b, c):
    print(f"MULTIPLYING {a} * {b} * {c}")
    return a * b * c

def divide(a, b, c):
    print(f"DIVIDING {a} / {b}")
    return a / b / c

print("Let's do some math with just functions!")

age = add(30, 5, 1)
height = substract(78, 4, 7)
weight = multiply(90, 2, 99)
iq = divide(100, 2, 5)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here's a puzzle")

what = add(age, 3, substract(height, 2, multiply(weight, 5, divide(iq, 2, 3))))

print("That becomes: ", what, "Can you do it by hand?")