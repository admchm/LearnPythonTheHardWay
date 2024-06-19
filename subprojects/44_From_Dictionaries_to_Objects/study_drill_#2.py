## Study Drill #2: 
## Add a new function hit which makes one person hit another person.

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
        
    def hit(hitted_by, target):
        hitted_by = hitted_by["name"]
        target = target["name"]
        
        print(f"{hitted_by} hit {target}")
        
    person["hit"] = hit
    
    return person

mark = Person_new("Mark", 47, "brown")
mark["talk"]("I'm shouting right now!")

adam = Person_new("Adam", 33, "green")
adam["talk"]("I wanted to say hi!")

# adam[""]
adam["hit"](adam, mark)