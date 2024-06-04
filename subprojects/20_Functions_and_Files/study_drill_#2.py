## Study Drill #2: 
## Each time print_a_line is run, you are passing in a variable current_line. Write out what current_line is equal to on each function call, and trace how it becomes line_count in print_a_line.

# Answer:

from sys import argv

input_file = "ex20_test.txt"

def print_all(f):
    print(f.read())
    
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    # line_count is the same as current_line
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file: \n")
print_all(current_file)

print("\nNow let's rewind, kind of the like a tape.") 
rewind(current_file)

print("Let's print three lines: \n")

current_line = 1
print_a_line(current_line, current_file)    # current_line = 1

current_line = current_line + 1             # current_line = 2
print_a_line(current_line, current_file)

current_line = current_line + 1             # current_line = 3
print_a_line(current_line, current_file)

    

