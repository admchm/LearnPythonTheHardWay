i = 0 
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    
    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")
    
print("The numbers: ")

for num in numbers:
    print(num)
    
from dis import dis

dis('''
i = 0
while i < 6:
    i = i + 1
''')

# output
#               2 LOAD_CONST               0 (0)
#               4 STORE_NAME               0 (i)

#               6 LOAD_NAME                0 (i)
#               8 LOAD_CONST               1 (6)
#              10 COMPARE_OP               2 (<)
#              14 POP_JUMP_IF_FALSE       12 (to 40)

#         >>   16 LOAD_NAME                0 (i)
#              18 LOAD_CONST               2 (1)
#              20 BINARY_OP                0 (+)
#              24 STORE_NAME               0 (i)

#              26 LOAD_NAME                0 (i)
#              28 LOAD_CONST               1 (6)
#              30 COMPARE_OP               2 (<)
#              34 POP_JUMP_IF_FALSE        1 (to 38)
#              36 JUMP_BACKWARD           11 (to 16)
#         >>   38 RETURN_CONST             3 (None)
#         >>   40 RETURN_CONST             3 (None)