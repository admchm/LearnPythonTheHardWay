# Rule #1: Everything is a sequence of instructions
x = 10
y = 20
z = x + y

# output for a function listed below:

#LOAD_CONST   0 (10) # load the number 10
#STORE_NAME   0 (x)  # store that in x

#LOAD_CONST   1 (20) # load the number 20
#STORE_NAME   1 (y)  # store that in y

#LOAD_NAME    0 (x)  # loads x (which is 10)
#LOAD_NAME    1 (y)  # loads y (which is 20)
#BINARY_ADD          # adds those
#STORE_NAME   2 (z)  # store the result in z

# import the dis function which is used for disassemble
from dis import dis

dis('''
x = 10
y = 20
z = x + y
''')

print("================")

# bytes are stored in a directory named __pycache__

# Rule #2: Jumps make the sequence non-linear

#   1     >>    2 LOAD_CONST               1 (10)
#               4 STORE_NAME               0 (x)
#               6 JUMP_BACKWARD            3 (to 2)

x = 0
while x < 5:
    x += 1
    
dis("while True: x = 10")

print("================")

# Rule #3: Tests control jumps

#   2           2 LOAD_CONST               0 (1)    # load 1
#               4 STORE_NAME               0 (x)    # x = 1

#   3           6 LOAD_NAME                0 (x)    # load x
#               8 LOAD_CONST               1 (0)    # load 0
#              10 COMPARE_OP              68 (>)    # compare x > 0
#              14 POP_JUMP_IF_FALSE        3 (to 22)# jump if false

#   4          16 LOAD_CONST               2 (10)   # not false, load 10
#              18 STORE_NAME               1 (y)    # y = 10
#              20 RETURN_CONST             3 (None) # done, load None

#   3     >>   22 RETURN_CONST             3 (None) # exit

if x > 0:
    y = 10
    
dis('''
x = 1 
if x > 0:
    y = 10
''')

print("================")

# Rule 4: Storage controls tests
x = 10
y = 20
z = x + y

if 1 < 2:
    print("but...why?")
    
print("================")

# Rule 5: Input/Output constrols storage

#   1           2 PUSH_NULL
#               4 LOAD_NAME                0 (input)
#               6 LOAD_CONST               0 ('Yes ?')
#               8 CALL                     1
#              16 RETURN_VALUE

dis("input('Yes ?')")
