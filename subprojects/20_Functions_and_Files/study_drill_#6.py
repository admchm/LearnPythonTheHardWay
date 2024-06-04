## Study Drill #6: 
## Can you convert this to a Terminal (command line) script that uses argv like in Exercise 14?

# Answer:

# compiling it by: python3 study_drill_#6.py "ex20_test.txt" 1

from sys import argv

script, input_file, current_line = argv
current_line = int(current_line) # we need to cast the current_line value, because all of the argv arguments
                                 # are always treated as string
def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

print(f"Current line: {current_line}")

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)