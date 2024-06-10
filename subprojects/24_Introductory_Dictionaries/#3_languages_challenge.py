# languages challenge
# You need to get all of these elements out of the languages variable:

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

# 'Slow'
print(languages[0]["speed"])

# 'Alright'
print(languages[1]["opinion"][0])

# 'Dangerous'
print(languages[3]["opinion"][1])

# 'Fast'
print(languages[4]["speed"])

# 'Difficult'
print(languages[4]["opinion"][1])

# 'Fun'
print(languages[4]["opinion"][0])

# 'Annoying'
print(languages[3]["opinion"][0])

# 'Weird'
print(languages[2]["opinion"][1])

# 'Moderate'
print(languages[1]["speed"])