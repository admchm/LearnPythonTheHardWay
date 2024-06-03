## Study Drill #3:
## There's too much repetition in this file. Use strings, formats, and escapes to print out 
## line1, line2, and line3 with just one target.write() command instead of six.

# Answer:

filename = "test.txt"
print(f"We are going to erase {filename}.")
print(f"If you don't want that, hit CTRL-C (^C).")
print(f"If you do want that, hit RETURN.")

input("? ")
print(f"Opening the file...")

target = open(filename, 'w')
print(f"Truncating the file. Goodbye!")
# target.truncate() - this line is not required

print(f"Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print(f"I'm going to write these to the file.")
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("And finally, we close it.")
target.close()