types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

# playing with the code on my own
print("\n")
some_text = "Today I drank {} cups of tea."
print(some_text)

cups_of_tea = 3
print(some_text.format(cups_of_tea))

## Study Drills
## 1. Go through this program and write a comment above each line explaining it.
# Answer: ---
## 2. Find all the places where a string is put inside a string.
# Answer: lines #2, #6, #11, #12
## 3. Are you sure there are only four places? How do you know? Maybe I like lying.
# Answer: I think that we could also mark the line #22. It gives a new string based on the two provided earlier
## 4. Explain why adding the two strings w and e with + makes a longer string.
# Answer: It is called string concatenation. Variables w and e are linked together, which gives us a new variable with longer text

## Break it
#print(non_existent_value)

## Common Student Questions
## 1. Why do you put ' (single-quotes) around some strings and not others? Mostly it's because of style, but I'll use a single-quote 
## inside a string that has double-quotes. Look at lines 6 and 15 to see how I'm doing that.

## 2. If you thought the joke was funny could you write hilarious = True? Yes, and you'll learn more about these boolean values later.