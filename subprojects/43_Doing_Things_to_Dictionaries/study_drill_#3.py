## Study Drill #3: 
## Find out what you can't do with dictionaries. A big one is that they 
## do not have order, so try playing with that.

# Answer:

# Python dictionaries are versatile data structures, but there are 
# some things you can't do with them directly or inherently. Here 
# are a few limitations:

# 1. **Non-hashable Keys**:
#    - You cannot use any object as a key in a dictionary if it is not
# hashable. For instance, lists or other dictionaries cannot be used as 
# keys because they are mutable (changeable) and therefore not hashable. 
# Only immutable data types like strings, numbers, and tuples can serve 
# as dictionary keys.

# 2. **Ordered Operations by Default**:
#    - Before Python 3.7, dictionaries did not maintain the order of 
# insertion. Starting from Python 3.7, dictionaries preserve the order 
# in which items are added, but operations that depend on sorting (like 
# obtaining the smallest key) aren't inherently supported. You would need 
# to use functions like `sorted()` to handle these operations.

# 3. **Direct Subtraction or Addition of Dictionaries**:
#    - Python does not support direct arithmetic operations on 
# dictionaries. You cannot directly add or subtract one dictionary 
# from another to merge or differentiate their key-value pairs. You must 
# use methods like `.update()` or dictionary comprehensions or the `|` 
# (merge) and `|=` (update) operators introduced in Python 3.9 for merging
# dictionaries.

# 4. **Indexing Like Lists**:
#    - Dictionaries cannot be accessed by an integer index like lists. 
# Dictionary elements must be accessed by their keys or via methods that 
# retrieve keys, values, or items.

# 5. **Immutability**:
#    - Dictionaries themselves are mutable, which means you cannot use a 
# dictionary as an element of a set or as a key in another dictionary because
# these require immutable objects.

# 6. **Built-in Functionality for Deep Copy**:
#    - Modifying objects nested within a dictionary (like lists or other 
# dictionaries) affects the original objects because Python handles them by 
# reference. To manipulate copies without affecting the originals, you must 
# use the `copy` module for deep copying.

# 7. **Multi-dimensional Access**:
#    - Python dictionaries do not support built-in multi-dimensional access. 
# For example, attempting to access an element with `dict[a][b]` will fail 
# unless `dict[a]` itself is another dictionary. Setting up and handling such
# structures requires careful initialization and management.

# 8. **Limitations on Methods**:
#    - Certain convenient methods available in other data structures (like 
# lists) aren't available for dictionaries. For instance, there's no direct 
# method to reverse a dictionary's order or shuffle its items without external
# libraries or additional code.

# Each of these limitations can often be worked around with additional coding,
# use of external libraries, or by choosing appropriate data structures for 
# your specific needs.