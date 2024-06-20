## Study Drill #1: 
## Python 3 allows you to write classes as class Person or using class 
## Person(object). Research why they have this second form and whether you really need to use it in Python 3.

# Answer:

# In Python, there are two ways to define a class that SD #1 mentioned: 
# `class Person` and `class Person(object)`. The choice between these 
# two forms stems from the changes that occurred between Python 2 and 
# Python 3 regarding the type of classes they support.

# ### Background: Old-style and New-style Classes

# In Python 2, there were two types of classes:

# 1. Old-style classes: 
# Created by `class Person:` without explicitly inheriting from `object`.

# 2. New-style classes:
# Introduced in Python 2.2, where classes 
# explicitly inherit from `object` as in `class Person(object):`. This form
# brings a model that provides better integration of classes and types, and
# introduces features like descriptors, properties, and `__slots__`.

# ### Python 3: Unified Class Model

# In Python 3, all classes implicitly inherit from `object`, whether you 
# specify it or not. This means:

# - `class Person:` is equivalent to `class Person(object):` in Python 3.
# - The unified model incorporates all the benefits and functionalities of 
# new-style classes by default.

# ### Do You Need to Use `class Person(object)` in Python 3?
# No, you do not need to use `class Person(object)` in Python 3 for functionality
# because `class Person:` automatically makes `Person` a new-style class 
# inheriting from `object`. However, there might be some cases where you might
# still see `class Person(object):`:

# 1. Compatibility with Python 2: 
# If you are writing code that needs to run on both Python 2 and Python 3, using
# `class Person(object):` ensures that your class is treated as a new-style class in Python 2.

# 2. Explicit is better than implicit:
# Some developers prefer to explicitly inherit from `object` to make the inheritance 
# clear, as recommended by Python's Zen (`import this` in the Python interpreter).

# ### Conclusion

# In Python 3, using `class Person:` is perfectly fine and is the more modern and 
# concise way to define a class. The explicit form (`class Person(object):`) is 
# redundant but can be used if preferred for clarity or compatibility reasons with
# older Python versions.