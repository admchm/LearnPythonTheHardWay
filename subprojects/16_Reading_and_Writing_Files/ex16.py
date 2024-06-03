## List of commands to remember:

## close -- Closes the file. Like File->Save.. in a text editor or word processor.
## read -- Reads the contents of the file. You can assign the result to a variable.
## readline -- Reads just one line of a text file.
## truncate -- Empties the file. Watch out if you care about the file.
## write('stuff') -- Writes "stuff" to the file.
## seek(0) -- Move the read/write location to the beginning of the file.

filename = "test.txt"
print(f"We are going to erase {filename}.")
print(f"If you don't want that, hit CTRL-C (^C).")
print(f"If you do want that, hit RETURN.")

input("? ")
print(f"Opening the file...")

# from search: python open site:"python.org"
# 'r' - open for reading (default)
# 'w' - open for writing, truncating the file first
# 'x' - open for exclusive creation, failing if the file already exists
# 'a' - open for writing, appending to the end of file if it exists
# 'b' - binary mode
# 't' - text mode (default)
# '+' - open for updating (reading and writing)

target = open(filename, 'w')
print(f"Truncating the file. Goodbye!")
# target.truncate() - this line is not required, because we are passing 'w' argument

print(f"Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print(f"I'm going to write these to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()