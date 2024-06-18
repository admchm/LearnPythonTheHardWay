# Step 1: Passing a dict to a Function
becky = {
    "name": "Becky",
    "age": 34,
    "eyes": "green"
}

def talk(who, words):
    print(f"I am {who["name"]} and {words}")
    
# talk(becky, becky["age"])

# Step 2: talk inside the dict
def talk(who, words):
    print(f"I am {who["name"]} and {words}")
    
becky = {
    "name": "Becky",
    "age": 34,
    "eyes": "green",
    "talk": talk
}

becky["talk"](becky, "bla bla bla")

becky_talk = becky["talk"]
print(becky_talk)

becky_talk(becky, "bla bla bla")
print(becky_talk)

# Step 3: Closures
# A closure is any function that's created inside another function, but accesses data in its parent.

print("\nClosures section:")

# this function makes functions
def constructor(color, size):
    print(">>> constructor color:", color, "size:", size)

    # watch the indent!
    def repeater():
        # notice this function is using color, size
        print("### repeater color:", color, "size:", size)

    print("<<< exit constructor")
    return repeater

# what's returned are repeater functions
blue_xl = constructor("blue", "xl")
green_sm = constructor("green", "sm")

# see how these repeaters "know" the parameters?
for i in range(0,4):
    blue_xl()
    green_sm()

# Step 4: A Person Constructor
print("\nPerson constructor section:")

def Person_new(name, age, eyes):
    person = {
        "name": name,
        "age": age,
        "eyes": eyes
    }
    
    def talk(words):
        print(f"I am {person['name']} and {words}")
        
    person["talk"] = talk
    
    return person

becky = Person_new("Becky", 39, "green")
becky["talk"]("I am talking here!")