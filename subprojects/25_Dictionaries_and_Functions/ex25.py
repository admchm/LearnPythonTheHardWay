# step 1: function names are variables
def print_number(x):
    print("NUMBER IS", x)
    
rename_print = print_number
rename_print(100)
print_number(100)

def function_to_copy():
    return 5

copied_function = function_to_copy
print(copied_function)

assigned_function_call = function_to_copy()
print(assigned_function_call)

print("\n")

def fingers_count(is_finger_missing):
    if is_finger_missing:
        return 19
    else:
        return 20

print(fingers_count(False))

counting_fingers = fingers_count
print(counting_fingers(False))
    
# step 2: dictionaries with variables
color = "Red"

corvette = {
    "color": color
}

print("LITTLE", corvette["color"], "CORVETTE")

# step 3: dictionaries with functions
def run():
    print("VROOOOM")
    
corvette = {
    "color": "Red",
    "run": run
}

print("My", corvette["color"], "can go")
corvette["run"]()

# step 4: deciphering the last line
def singing_a_song():
    return "lalalala"

person = {
    "name": "Adam",
    "age": 33,
    "favorite_song": singing_a_song()   # decided to call it a little bit different
}

print("\n")
print(person["name"])
print(person["age"])
print(person["favorite_song"])