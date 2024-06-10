# I will give you a list name and a piece of data in the list. Your job is to 
# figure out what indexes you need to get that information. For example, if I 
# tell you fruit 'AAA' then your answer is fruit[0][2]. You should attempt to 
# do this in your head by looking at the code, then test your guess in the Jupyter.

# fruit challenge
# You need to get all of these elements out of the fruit variable:

fruit = [
    ['Apples', 12, 'AAA'], ['Oranges', 1, 'B'],
    ['Pears', 2, 'A'], ['Grapes', 14, 'UR']
]

# 12
print(fruit[0][1])

# 'AAA'
print(fruit[0][2])

# 2
print(fruit[2][1])

# 'Oranges'
print(fruit[1][0])

# 'Grapes'
print(fruit[3][0])

# 14
print(fruit[3][1])

# 'Apples'
print(fruit[0][0])



