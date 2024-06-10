# Final Challenge
# You now have to figure out what this code spells out:

fruit = [
    ['Apples', 12, 'AAA'], ['Oranges', 1, 'B'],
    ['Pears', 2, 'A'], ['Grapes', 14, 'UR']
]

cars = [
    ['Cadillac', ['Black', 'Big', 34500]],
    ['Corvette', ['Red', 'Little', 1000000]],
    ['Ford', ['Blue', 'Medium', 1234]],
    ['BMW', ['White', 'Baby', 7890]]
]

languages = [
    ['Python', ['Slow', ['Terrible', 'Mush']]],
    ['JavaSCript', ['Moderate', ['Alright', 'Bizarre']]],
    ['Perl6', ['Moderate', ['Fun', 'Weird']]],
    ['C', ['Fast', ['Annoying', 'Dangerous']]],
    ['Forth', ['Fast', ['Fun', 'Difficult']]],
]

print(cars[1][1][1])            # Answer: Little
print(cars[1][1][0])            # Answer: Red
print(cars[1][0])               # Answer: Corvette
print(cars[3][1][1])            # Answer: Baby
print(fruit[3][2])              # Answer: UR
print(languages[0][1][1][1])    # Answer: Mush
print(fruit[2][1])              # Answer: 2
print(languages[3][1][0])       # Answer: Fast
# Don't attempt to run this in Jupyter first. Instead, try to work out manually what each line will spell out, then test it in Jupyter.