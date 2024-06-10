# Final Challenge
# Your final challenge is to write out the Python code that writes out 
# the same song lyric from Exercise 23. Again, take it slow and try to 
# do it in your head before seeing whether you get it right. If you get 
# it wrong, take the time to understand why you got it wrong. For 
# comparison, I wrote out the lyrics in my head in one shot and didn't 
# get it wrong. I am also way more experienced than you are, so you will 
# probably make some mistakes and that is alright.

# expected lyrics:
# Little
# Red
# Corvette
# Baby
# UR
# Mush
# 2
# Fast

fruit = [
    {'kind': 'Apples',  'count': 12, 'rating': 'AAA'},
    {'kind': 'Oranges', 'count': 1,  'rating': 'B'},
    {'kind': 'Pears',   'count': 2,  'rating': 'A'},
    {'kind': 'Grapes',  'count': 14, 'rating': 'UR'}
];

cars = [
    {'type': 'Cadillac', 'color': 'Black',
     'size': 'Big', 'miles': 34500},
    {'type': 'Corvette', 'color': 'Red',
     'size': 'Little', 'miles': 1000000},
    {'type': 'Ford', 'color': 'Blue',
     'size': 'Medium', 'miles': 1234},
    {'type': 'BMW', 'color': 'White',
     'size': 'Baby', 'miles': 7890}
];

languages = [
    {'name': 'Python', 'speed': 'Slow',
     'opinion': ['Terrible', 'Mush']},
    {'name': 'JavaScript', 'speed': 'Moderate',
     'opinion': ['Alright', 'Bizarre']},
    {'name': 'Perl6', 'speed': 'Moderate',
     'opinion': ['Fun', 'Weird']},
    {'name': 'C', 'speed': 'Fast',
     'opinion': ['Annoying', 'Dangerous']},
    {'name': 'Forth', 'speed': 'Fast',
     'opinion': ['Fun', 'Difficult']},
];

print(cars[1]["size"])
print(cars[1]["color"])
print(cars[1]["type"])
print(cars[3]["size"])
print(fruit[3]["rating"])
print(languages[0]["opinion"][1])
print(fruit[2]["count"])
print(languages[3]["speed"])