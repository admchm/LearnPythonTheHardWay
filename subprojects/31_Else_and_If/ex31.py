people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
    
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
    
from dis import dis

dis('''
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
''')

#  0           0 RESUME                   0

#   2           2 LOAD_NAME                0 (cars)
#               4 LOAD_NAME                1 (people)
#               6 COMPARE_OP              68 (>)
#              10 POP_JUMP_IF_FALSE        9 (to 30)

#   3          12 PUSH_NULL
#              14 LOAD_NAME                2 (print)
#              16 LOAD_CONST               0 ('We should take the cars.')
#              18 CALL                     1
#              26 POP_TOP
#              28 RETURN_CONST             3 (None)

#   4     >>   30 LOAD_NAME                0 (cars)
#              32 LOAD_NAME                1 (people)
#              34 COMPARE_OP               2 (<)
#              38 POP_JUMP_IF_FALSE        9 (to 58)

#   5          40 PUSH_NULL
#              42 LOAD_NAME                2 (print)
#              44 LOAD_CONST               1 ('We should not take the cars.')
#              46 CALL                     1
#              54 POP_TOP
#              56 RETURN_CONST             3 (None)

#   7     >>   58 PUSH_NULL
#              60 LOAD_NAME                2 (print)
#              62 LOAD_CONST               2 ("We can't decide.")
#              64 CALL                     1
#              72 POP_TOP
#              74 RETURN_CONST             3 (None)