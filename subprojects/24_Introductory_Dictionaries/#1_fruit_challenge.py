# The Challenge
# I will give you the exact same set of data elements for you to get. Your job is to figure out what indexing you need to get that information. For example, if I tell you fruit 'AAA', then your answer is fruit[0]['rating']. You should attempt to do this in your head by looking at the code, then test your guess in the python shell.

# fruit challenge
# You need to get all of these elements out of the fruit variable:

fruit = [
    {'kind': 'Apples',  'count': 12, 'rating': 'AAA'},
    {'kind': 'Oranges', 'count': 1,  'rating': 'B'},
    {'kind': 'Pears',   'count': 2,  'rating': 'A'},
    {'kind': 'Grapes',  'count': 14, 'rating': 'UR'}
];

# 12
print(fruit[0]["count"])

# 'AAA'
print(fruit[0]["rating"])

# 2
print(fruit[2]["count"])

# 'Oranges'
print(fruit[1]["kind"])

# 'Grapes'
print(fruit[3]["kind"])

# 14
print(fruit[3]["count"])

# 'Apples'
print(fruit[0]["kind"])