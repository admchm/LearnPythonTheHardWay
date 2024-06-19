## Study Drill #3: 
## Give people hit points in their dict and have hit randomly reduce 
## each person's hit points. You'll need random for this.

# Answer:

import random

def Person_new(name, age, eyes):
    person = {
        "name": name,
        "age": age,
        "eyes": eyes,
        "hit_points": random.randint(0, 100)
    }
    
    def talk(words):
        print(f"I am {person['name']} and {words}")
    
    person["talk"] = talk
        
    def hit(hitted_by, target):    
        hit_value = random.randint(1, 50)
        target["hit_points"] -= hit_value

        print(f"{hitted_by["name"]} hit {target["name"]} for {hit_value} HP. Currently he has {target["hit_points"]} HPs left.") # 
        
    person["hit"] = hit
    
    return person

mark = Person_new("Mark", 47, "brown")
mark["talk"]("I'm shouting right now!")

adam = Person_new("Adam", 33, "green")
adam["talk"]("I wanted to say hi!")

print(f"{mark["name"]}\'s HP = {mark["hit_points"]} ")

adam["hit"](adam, mark)