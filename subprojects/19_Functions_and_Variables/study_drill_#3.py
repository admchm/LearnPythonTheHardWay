## Study Drill #3: 
## Delete one of the + symbols in the math to see what error you get.

# Answer:

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man, that's not enough for a party")
    print(f"Get a blanket.\n")
    
print("We can even do a math inside too:")
# cheese_and_crackers(10 20, 5 + 6) - problematic function call

# Error description:
# File "/Users/(...)/LearnPythonTheHardWay/subprojects/19_Functions_and_Variables/study_drill_#3.py", line 13
#     cheese_and_crackers(10 20, 5 + 6)
#                         ^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?