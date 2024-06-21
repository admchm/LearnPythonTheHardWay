## Study Drill #6 
## Do you think there's such thing as an "is-many" relationship? Read 
## about "multiple inheritance," then avoid it if you can.

# Answer:

# Multiple inheritance is a feature in some object-oriented programming
# languages where a class can inherit features (methods and properties)
# from more than one parent class. This capability allows a child class 
# to acquire and combine behaviors and attributes from multiple parent 
# classes, which can lead to more flexible and reusable code.

# However, multiple inheritance can also introduce certain complexities 
# and problems, such as the "diamond problem." This occurs when two parent 
# classes inherit from the same grandparent class, and the child class inherits
# from both of these parent classes. This creates an ambiguity about which 
# parent class the methods or attributes should be inherited from if both 
# parents have overridden methods or attributes from the grandparent.