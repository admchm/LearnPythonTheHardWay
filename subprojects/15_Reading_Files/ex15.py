# from sys import argv

# python ex13.py test_file.txt

# script, filename = argv

# txt = open(filename)

# print(f"Here's is your file {filename}:")
# print(txt.read())

# print("Type the filename again:")
# file_again = input("> ")

# txt_again = open(file_again)

# print(txt_again.read())

## Study Drills
## This is a big jump, so be sure you do this Study Drill as best you can before moving on.

## 1. Above each line, write out in English what that line does.
# Answer: 

#from sys import argv                           - importing module argv from sys
#python ex13.py test_file.txt                   - sample way of compiling a file
#script, filename = argv                        - assigning passed arguments to script and filename variables
#txt = open(filename)                           - opening a filename
#print(f"Here's is your file {filename}:")      - printing filename
#print(txt.read())                              - reading txt file contents and printing it out to the console
#print("Type the filename again:")              - asking for providing a filename again
#file_again = input("> ")                       - getting a filename from the user
#txt_again = open(file_again)                   - opening a file again, but this time from other variable
#print(txt_again.read())                        - reading file contents and printing it out to the console


## 2. If you are not sure, ask someone for help or search online. Many times searching for "python3 THING" will find answers to what that THING does in Python. Try searching for "python3 open."
# Answer: "python open site:python.org"

## 3. I used the word "commands" here, but commands are also called "functions" and "methods." You will learn about functions and methods later in the book.

## 4. Get rid of the lines 10-15 where you use input and run the script again.
# Answer:

# from sys import argv

# # python ex13.py test_file.txt

# script, filename = argv

# txt = open(filename)

# print(f"Here's is your file {filename}:")
# print(txt.read())

## 5. Use only input and try the script that way. Why is one way of getting the filename better than another?
# Answer:
# In my opinion, getting a filename from a user is a little bit better, because you don't need to ensure that
# you are providing all of the required arguments just to compile the program. This way, you don't also need to
# import any modules and the code is simpler

# filename = input("Enter your filename: > ")
# txt = open(filename)

# print(f"Here's is your file {filename}:")
# print(txt.read())

## 6. Start python3 to start the python3 shell, and use open from the prompt just like in this program. Notice how you can open files and run read on them from within python3?
# Answer:

#python3
#open("test_file.txt")

## 7. Have your script also call close() on the txt and txt_again variables. It's important to close files when you are done with them.
# Answer:

# python3 ex15.py test_file.txt 
from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's is your file {filename}:")
print(txt.read())

txt.close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()