## Study Drill #1: 
## Use Person_new to create a few more people.

# Answer:

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

mark = Person_new("mark", 47, "brown")
mark["talk"]("I'm shouting right now!")