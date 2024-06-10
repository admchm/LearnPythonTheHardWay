# languages challenge
# You need to get all of these elements out of the languages variable:

languages = [
    ['Python', ['Slow', ['Terrible', 'Mush']]],
    ['JavaScript', ['Moderate', ['Alright', 'Bizarre']]],
    ['Perl6', ['Moderate', ['Fun', 'Weird']]],
    ['C', ['Fast', ['Annoying', 'Dangerous']]],
    ['Forth', ['Fast', ['Fun', 'Difficult']]],
]

# 'Slow'
print(languages[0][1][0])

# 'Alright'
print(languages[1][1][1][0])

# 'Dangerous'
print(languages[3][1][1][1])

# 'Fast'
print(languages[4][1][0])

# 'Difficult'
print(languages[4][1][1][1])

# 'Fun'
print(languages[4][1][1][0])

# 'Annoying'
print(languages[3][1][1][0])

# 'Weird'
print(languages[2][1][1][1])

# 'Moderate'
print(languages[2][1][0])