## Study Drill #1: 
## Find out what a "flow chart" is and draw a few.

# Answer: 

# +-----------------------+
# | Start                 |
# +-----------------------+
#             |
#             v
# +-----------------------+
# | Input a number        |
# +-----------------------+
#             |
#             v
# +-----------------------+
# | Is the number         |
# | divisible by 2?       |
# +-----------------------+
#       /     \
#      v       v
# +--------+ +--------+
# | Yes    | | No     |
# +--------+ +--------+
#       |       |
#       v       v
# +-----------------------+   +-----------------------+
# | Print "The number     |   | Print "The number     |
# | is even"              |   | is odd"               |
# +-----------------------+   +-----------------------+
#             |                       |
#             v                       v
# +-----------------------+
# | End                   |
# +-----------------------+


number = int(input("Enter a number: "))

if number % 2 == 0:  # Is the number divisible by 2?
    print("The number is even")
else:
    print("The number is odd")
