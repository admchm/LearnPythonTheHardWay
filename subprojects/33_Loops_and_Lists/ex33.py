the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")
    
# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")
    
# also we can go through mixed lists too
for i in change:
    print(f"I got {i}")
    
# we can also build lists, first start with the empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    
    # append is a function that lists understand
    elements.append(i)
    
# now we can print them out
for i in elements:
    print(f"Element was: {i}")
    
from dis import dis

dis('''
for number in the_count:
    print(number)
''')

# output: 
# 0 LOAD_NAME     0 (the_count) # get the count list
#  2 GET_ITER                    # start iteration
#  4 FOR_ITER      6 (to 18)     # for-loop jump to 18
#  6 STORE_NAME    1 (number)    # create number variable

#  8 LOAD_NAME     2 (print)     # load print()
# 10 LOAD_NAME     1 (number)    # load number
# 12 CALL_FUNCTION 1             # call print()
# 14 POP_TOP                     # clean stack
# 16 JUMP_ABSOLUTE 2 (to 4)      # jump back to FOR_ITER at 4

# 18 LOAD_CONST    0 (None)      # jump here when FOR_ITER done
# 20 RETURN_VALUE