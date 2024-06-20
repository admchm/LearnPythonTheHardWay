## Study Drill #4
## Remember how you could get the talk function from becky.__class__.__dict__ 
## but it was different from becky.talk()? Try calling it and see what
## error you get. Can you fix the error?

# Answer:

class Person(object):
    
    # this is double underscores around init
    def __init__(self, name, age, eyes):
        self.name = name
        self.age = age
        self.eyes = eyes
    
    def talk(self, words):
        print(f"I am {self.name} and {words}")

becky = Person("Becky", 39, "green")

print(becky.talk("bla bla bla"))

#print(becky.__class__.__dict__["talk"]) - this one will give:
# <function Person.talk at 0x105458c20>

# print(becky.__class__.__dict__["talk"]()) - this function call will give us an error:

# Traceback (most recent call last):
#   File "/Users/adamc/LearnPythonTheHardWay/subprojects/45_Basic_Object_Oriented_Programming/study_drill_#5.py", line 23, in <module>
#     print(becky.__class__.__dict__["talk"]())
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: Person.talk() missing 2 required positional arguments: 'self' and 'words'

print(becky.__class__.__dict__["talk"](becky, "bl bl bl"))

# or:
talk_function = becky.__class__.__dict__["talk"]
talk_function(becky, "bla bla bla!")

