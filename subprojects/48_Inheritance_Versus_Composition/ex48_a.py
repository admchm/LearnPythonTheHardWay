# Most of the uses of inheritance can be simplified or replaced with 
# composition, and multiple inheritance should be avoided at all costs.

# Inheritance is used to indicate that one class will get most or all
# of its features from a parent class.

# Implicit Inheritance
# Very handy for repetitive code you need in many classes.

class Parent(object):
    
    def implicit(self):
        print("PARENT implicit()")
        
class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()