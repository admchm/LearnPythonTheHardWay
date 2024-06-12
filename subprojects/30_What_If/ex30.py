people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")
    
if people > cats:
    print("Not many cats! The world is saved!")
    
if people < dogs:
    print("The world is drooled on!")
    
if people > dogs:
    print("The world is dry!")
    
dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")
    
if people <= dogs:
    print("People are less than or equal to dogs.")
    
if people == dogs:
    print("People are dogs.")
    
from dis import dis

dis('''
if people < cats:
    print("Too many cats! The world is doomed!")
''')

#   0           0 RESUME                   0

#   2           2 LOAD_NAME                0 (people)
#               4 LOAD_NAME                1 (cats)
#               6 COMPARE_OP               2 (<)
#              10 POP_JUMP_IF_FALSE        9 (to 30)

#   3          12 PUSH_NULL
#              14 LOAD_NAME                2 (print)
#              16 LOAD_CONST               0 ('Too many cats! The world is doomed!')
#              18 CALL                     1
#              26 POP_TOP
#              28 RETURN_CONST             1 (None)

#   2     >>   30 RETURN_CONST             1 (None)