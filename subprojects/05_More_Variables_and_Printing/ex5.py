my_name = 'Adam'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"Actually, that's not too heavy.")
print(f"He's got {my_eyes} and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight}, I get {total}.")

## Study drills:
## 1. Change all the variables so there is no my_ in front of each one. Make sure you change the name everywhere, not just where you used = to set them.
print("\nStudy drill #1:")
name = 'Adam'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually, that's not too heavy.")
print(f"He's got {eyes} and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

## 2. Try to write some variables that convert the inches and pounds to centimeters and kilograms. Do not just type in the measurements. Work out the math in Python.
# I used here "," instead of ".", which gave me odd results. "," is used for separating values
print("\nStudy drill #2:")
two_pounds_to_kilograms = 2 * 0.45359237
two_inches_to_centimeters = 2 * 2.54
print(f"Two pounds converted to kilograms are: {two_pounds_to_kilograms}")
print(f"Two inches converted to centimeters are: {two_inches_to_centimeters}")

## Common Student Questions
print("\nSection - Common Student Questions:")
floating_point_number = 3423423.4234234
print(f"Floating point number {floating_point_number} after calling a round() function with this value will provide {round(floating_point_number)}")

