## Study Drill #2: 
## Change the name of cheese_and_crackers to have a spelling mistake and view the error message. Now fix it.

# Answer:

def chese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man, that's not enough for a party")
    print(f"Get a blanket.\n")
    
# cheese_and_crackers(20, 30) - problematic function call

# Traceback (most recent call last):
#   File "/(...)/LearnPythonTheHardWay/subprojects/19_Functions_and_Variables/study_drill_#2.py", line 12, in <module>
#     cheese_and_crackers(20, 30)
#     ^^^^^^^^^^^^^^^^^^^
# NameError: name 'cheese_and_crackers' is not defined. Did you mean: 'chese_and_crackers'?

# After fixing it:
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man, that's not enough for a party")
    print(f"Get a blanket.\n")
    
cheese_and_crackers(20, 30)