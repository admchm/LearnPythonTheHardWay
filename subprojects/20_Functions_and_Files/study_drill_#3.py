## Study Drill #3: 
## Find each place a function is used, and check its def to make sure that you are giving it the right arguments.

# Answer:

from sys import argv

input_file = "ex20_test.txt"

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file) # we are passing here current_file, so it is correct

print("Now let's rewind, kind of like a tape.")

rewind(current_file) # we are passing here current_file, so it is correct

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file) # it's correct, because current_line becomes line_count, but it doesn't really matter

current_line = current_line + 1
print_a_line(current_line, current_file) # it's correct, because current_line becomes line_count, but it doesn't really matter

current_line = current_line + 1
print_a_line(current_line, current_file) # it's correct, because current_line becomes line_count, but it doesn't really matter