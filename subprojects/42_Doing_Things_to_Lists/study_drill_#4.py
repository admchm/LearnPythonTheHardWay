## Study Drill #4
## Read up on what a "class" is in Python. Do not read about how other
## languages use the word "class." That will only mess you up.

# Answer: 

# In Python, a class is a blueprint for creating objects, and it 
# encapsulates data for the object along with methods to manipulate 
# that data. Here are the base concepts of classes in Python:

# 1. Class Definition:
#    - A class is defined using the `class` keyword followed by the 
# class name and a colon. Inside, methods and attributes are defined 
# to describe the behavior and data of the class.

#python
#    class MyClass:
#        def __init__(self, value):
#            self.attribute = value
# 

# 2. Initialization (`__init__` method):
#    - The `__init__` method is called automatically every time a class
# is being used to create a new object. It can take arguments to 
# initialize the object’s attributes.

# 3. Instance Attributes:
#    - These are attributes that belong to the object. Each object of
# a class has its own set of attributes.

# 4. Class Attributes:
#    - Attributes that are shared by all instances of a class. They are
# defined outside of all methods, usually just under the class header.

# 5. Methods:
#    - Methods are functions defined within a class that describe the 
# behaviors of the objects. They can modify object state or perform actions
# on the object’s data.

# 6. Self:
#    - The `self` keyword is used in method definitions and in the `__init__`
# method to refer to the instance of the class. It binds the attributes with
# the given arguments.

# 7. Inheritance:
#    - Classes can inherit from other classes, gaining access to their methods
# and properties. This promotes code reuse.

#    class DerivedClass(BaseClass):
#        pass

# 8. Encapsulation:
#    - This principle is used to restrict access to methods and variables from 
# outside interference and misuse. Public, private, and protected access modifiers
# are used to ensure encapsulation.

# 9. Polymorphism:
#    - Polymorphism allows methods to do different things based on the object it
# is acting upon.

# 10. Special Methods:
#     - These are methods that have double underscores at the beginning and the 
# end of their names (`__str__`, `__repr__`, `__add__`, etc.). They allow classes
# to implement operator overloading and customization of default behaviors.

# These concepts are fundamental to understanding and working with classes and objects in Python.