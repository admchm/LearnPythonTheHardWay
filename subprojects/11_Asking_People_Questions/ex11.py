# print("How old are you?")
# By adding end = ' ', we are telling the print() that we don't want to finish the line with \n

print("How old are you?", end = ' ')
age = input()
print("How tall are you?", end = ' ')
height = input()
print("How much do you weigh?", end = ' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

## Study Drills
## 1. Go online and find out what Python's input does.

# Answer:
# input() / input(prompt)
# If the prompt argument is present, it is written to standard output without a trailing newline. 
# The function then reads a line from input, converts it to a string (stripping a trailing newline), 
# and returns that.
# If the readline module was loaded, then input() will use it to provide elaborate line editing and history features.

## 2. Can you find other ways to use it? Try some of the samples you find.

# Answer: input() could be used for providing data for tests and it can be used to direct the flow of the
# program depending on the user's response (for example: yes/no, option selection).

## 3. Write another "form" like this to ask some other questions.
print("Where are you from?", end = ' ')
origin = input()
print("How many records do you have in your collection?", end = ' ')
vinyl_count = input()
print("How many CDs do you have in your collection?", end = ' ')
cd_count = input()

print(f"Okay, you're from {origin}, and you have {vinyl_count} vinyls and {cd_count} CDs in your collection. Nice!")