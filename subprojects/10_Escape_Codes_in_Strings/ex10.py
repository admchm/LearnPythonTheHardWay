problematic_string = "I \"understand\" Joe"
print(problematic_string)

second_problematic_string = "I am 6'2\" tall."
third_problematic_string = 'I am 6\'2" tall.'
print(second_problematic_string)
print(third_problematic_string)

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

## Escape Sequences

## Escape	What it does.
## \\	Backslash (\)
## \'	Single-quote (')
## \"	Double-quote (")
## \a	ASCII bell (BEL)
## \b	ASCII backspace (BS)
## \f	ASCII formfeed (FF)
## \n	ASCII linefeed (LF)
## \N{name}	Character named name in the Unicode database (Unicode only)
## \r	Carriage Return (CR)
## \t	Horizontal Tab (TAB)
## \uxxxx	Character with 16-bit hex value xxxx
## \Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx
## \v	ASCII vertical tab (VT)
## \000	Character with octal value 000
## \xhh	Character with hex value hh

# Testing those characters on my own:
# Example of escape sequences in strings
print("Backslash (\\): '\\\\'")
print("Single-quote ('): '\\'This is quoted\\''")
print("Double-quote (\"): \"\\\"This is double quoted\\\"\"")
print("ASCII bell (BEL): '\\a' (You might hear a beep!)")
print("ASCII backspace (BS): 'Back\\bspace'")
print("ASCII formfeed (FF): 'Formfeed\\fNew Page'")
print("ASCII linefeed (LF): 'First Line\\nSecond Line'")
print("Character named in Unicode: '\\N{COPYRIGHT SIGN}'")
print("Carriage Return (CR): 'First Line\\rOverwrite'")
print("Horizontal Tab (TAB): 'Column 1\\tColumn 2'")
print("16-bit Unicode: '\\u00A9' (Copyright sign)")
print("32-bit Unicode: '\\U0001F600' (Emoji smiley face)")
print("ASCII vertical tab (VT): 'Top\\vBottom'")
print("Character with octal value: '\\041' (Exclamation mark)")
print("Character with hex value: '\\x21' (Exclamation mark)")


### Study Drills
### 1. Memorize all the escape sequences by putting them on flash cards.
# Answer: ----
### 2. Use ''' (triple-single-quote) instead. Can you see why you might use that instead of """?
# Answer:
# they are the same, and giving us the same results
triple_single_quote = '''
let's see what we will get.
I want to be surprised! 
'''

print(triple_single_quote)

### 3. Combine escape sequences and format strings to create a more complex format.
# Answer: (not sure if this is acceptable, but at least I tried)
combined_escape_sequences = "\t\t??%\\bs"
print(f"I'm going to use here - {combined_escape_sequences} - combined escape sequences")