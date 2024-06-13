# PROBLEM: CREATE A SIMPLE FAHRENHEIT TO CELSIUS CONVERTER.

# STEP ONE: 
# I would write out what I know about the conversion:

# > C equals (F - 32 ) / 1.8. 

# STEP TWO:
# I write comments describing what my code should do:

# > ask the user for F
# > convert it to a float()
# > C = (F - 32) / 1.8
# > print C to the user

# STEP THREE:
# "Fill the blanks" with pseudo code:

# ask the user for F
# f = input(?)

# convert it to a float()
# float(f)

# C = (F - 32) / 1.8
# result_in_celsius = (f - 32) / 1.8

# print C to the user
# print(f"Result = {result_in_celsius}")

# STEP FOUR:
# Converting the pseudo code to the correct Python:

# ask the user for F
fahrenheit_to_convert = input("Enter Fahrenheit value for converting to celsius: > ")

# convert it to a float()
fahrenheit_to_convert = float(fahrenheit_to_convert)

# C = (F - 32) / 1.8
result_in_celsius = (fahrenheit_to_convert - 32) / 1.8

# print C to the user
print(f"{fahrenheit_to_convert} fahrenheits converted are equal to {result_in_celsius} C.")

# STEP FIVE:
# Deleting the code and rewriting it, directly in Python.

def get_fahr_value_to_convert():
    return float(input("Enter Fahrenheit value to convert to celsius: > "))

def fahr_to_celsius_conversion(fahr):
    return (fahr - 32) / 1.8

def print_result(fahrenheits, result_to_print):
    print(f"{fahrenheits} fahrenheits are equal to {result_to_print} C.")

fahrenheits = get_fahr_value_to_convert()
converted_result = fahr_to_celsius_conversion(fahrenheits)

print_result(fahrenheits, converted_result)

# Zed Shaw's quotes that I wanted to include:

## I do use this process when I am stuck, or if I'm learning a new 
## language. If I don't know a language, but know what I want to do, 
## then I can usually write comments and slowly convert them to code, 
## which also teaches me that language. The only difference between 
## me and you is that I do it faster because of years of training.

## Rules for If-Statements:
## 1. Every if-statement must have an else.
## 2. If this else should never run because it doesn't make sense, 
##    then you must use a die function in the else that prints out 
##    an error message and dies, just like we did in the last exercise. 
##    This will find many errors.
## 3. The exception to rules #1 and #2 is in any for-loop or similar loop
##    that is scanning for items in lists, or in list comprehensions. Add 
##    the else anyway, and if it doesn't make sense there then remove it.
## 4. Try not to nest if-statements more than two deep and always try to 
##    do them one deep.
## 5. Treat if-statements like paragraphs, where each if-elif-else grouping
##    is like a set of sentences. Put blank lines before and after.
## 6. Your Boolean tests should be simple. If they are complex, move their 
##    calculations to variables earlier in your function and use a good name for the variable.