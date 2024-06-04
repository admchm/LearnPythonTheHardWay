## Study Drill #1: 
## Write English comments for each line to understand what that line does.

# Answer:

from sys import argv # importing feature from module

input_file = "ex20_test.txt" # storing filename as input_file variable

def print_all(f):   # function that takes f param
    print(f.read()) # printing contents of the file object
    
def rewind(f):      # function that takes f param
    f.seek(0)       # going back to the first line of the file

def print_a_line(line_count, f):    # function that takes line_count and f params
    print(line_count, f.readline()) # printing the value of a current line, also printing contents from this specific line

current_file = open(input_file)     # storing contents of a file as file object

print("First let's print the whole file: \n")           # print message
print_all(current_file)                                 # passing file object to print its contents

print("\nNow let's rewind, kind of the like a tape.")   # print message
rewind(current_file)                                    # passing file object to go back to the first line

print("Let's print three lines: \n")                    # print message

current_line = 1                                        # setting the current_line line as 1
print_a_line(current_line, current_file)                # printing current line count and its data

current_line = current_line + 1                         # setting current_line as 2
print_a_line(current_line, current_file)                # printing current line count and its data

current_line = current_line + 1                         # setting current line as 3
print_a_line(current_line, current_file)                # printing current line count and its data

    

