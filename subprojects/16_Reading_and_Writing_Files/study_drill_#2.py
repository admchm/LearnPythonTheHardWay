## Study Drill #2:
## Write a .py script similar to the last Exercises 14 that uses read (Exercise 15) and argv 
## (Exercise 13) to read the file you just created. Be sure you run this in Terminal/PowerShell instead of Jupyter.

# Command for running the program:
# python3 study_drill_#2.py "This is a first line" "This is a second line" "This is a third line"

from sys import argv

script, line1, line2, line3 = argv

filename = "test.txt"
print(f"We are going to erase {filename}.")
print(f"If you don't want that, hit CTRL-C (^C).")
print(f"If you do want that, hit RETURN.")

input("? ")
print(f"Opening the file...")

target = open(filename, 'w')
print(f"Truncating the file. Goodbye!")
target.truncate()

print(f"I'm going to passed lines as arguments to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()