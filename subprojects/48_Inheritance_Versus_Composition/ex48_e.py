# composition
# another way to do the exact same thing is just to use other classes 
# and modules, rather than rely on implicit inheritance

class Other(object):
    
    def override(self):
        print("OTHER override()")
        
    def implicit(self):
        print("OTHER implicit()")
        
    def altered(self):
        print("OTHER altered()")
        
class Child(object):
    
    def __init__(self):
        self.other = Other()
        
    def implicit(self):
        self.other.implicit()
        
    def override(self):
        print("CHILD override()")
    
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")
        
son = Child()

son.implicit()
son.override()
son.altered()

# The question of "inheritance versus composition" comes down to an 
# attempt to solve the problem of reusable code. You don't want to 
# have duplicated code all over your software, since that's not clean 
# and efficient. Inheritance solves this problem by creating a mechanism 
# for you to have implied features in base classes. Composition solves 
# this by giving you modules and the capability to call functions in 
# other classes.

# If both solutions solve the problem of reuse, then which one is 
# appropriate in which situations? The answer is incredibly subjective, 
# but I'll give you my three guidelines for when to do which:

# 1. Avoid multiple inheritance at all costs, as it's too complex to be 
# reliable. If you're stuck with it, then be prepared to know the class 
# hierarchy and spend time finding where everything is coming from.

# 2. Use composition to package code into modules that are used in many 
# different unrelated places and situations.

# 3. Use inheritance only when there are clearly related reusable pieces 
# of code that fit under a single common concept or if you have to 
# because of something you're using.