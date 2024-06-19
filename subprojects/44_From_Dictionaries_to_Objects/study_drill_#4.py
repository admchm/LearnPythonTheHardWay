## Study Drill #4: 
## Add a job attribute to person and give different jobs different hit 
## points, damage, and dialogue. For example, a "boxer" would have more 
## HP and damage than a person with the job "baby." Python has way better 
## tools for this same problem, but for this code it is a fun challenge.

# Answer:

import random

def set_job(selected_job):
    new_job = {
        "job": "none",
        "hit_points": 0,
        "damage": 0,
        "dialogue": "none"
    }
    
    if selected_job == "Ranger":
        new_job["job"] = "ranger"
        new_job["hit_points"] = 120
        new_job["damage"] = 15
        new_job["dialogue"] = "Nature's whisper guides my arrow."
    
    if selected_job == "Ninja":
        new_job["job"] = "ninja"
        new_job["hit_points"] = 140
        new_job["damage"] = 20
        new_job["dialogue"] = "Silence is not just golden; it's deadly."
    
    if selected_job == "Fighter":
        new_job["job"] = "fighter"
        new_job["hit_points"] = 250
        new_job["damage"] = 35
        new_job["dialogue"] = "Where I walk, thunder follows."
    
    if selected_job == "Thief":
        new_job["job"] = "thief"
        new_job["hit_points"] = 95
        new_job["damage"] = 10
        new_job["dialogue"] = "What's yours is mine, and what's mine is... also mine."
    
    if selected_job == "Bard":
        new_job["job"] = "bard"
        new_job["hit_points"] = 60
        new_job["damage"] = 12
        new_job["dialogue"] = "A tune for your heart, and a tale for your soul."
    
    if selected_job == "none":
        new_job["job"] = "nomad"
        new_job["hit_points"] = 75
        new_job["damage"] = 15
        new_job["dialogue"] = "Home is where my journey takes me."

    return new_job

def Person_new(name, age, eyes, job):
    person = {
        "name": name,
        "age": age,
        "eyes": eyes,
        "hit_points": job["hit_points"], # should use values from the job object directly
        "damage": job["damage"],         # should use values from the job object directly
        "job": job,
        "is_alive": True
    }
    
    def talk():
        job = person["job"]
        
        print(f"I am {person['name']} - {job["job"]}. {job["dialogue"]}")
    
    person["talk"] = talk
        
    def hit(hitted_by, target):
        target["hit_points"] -= hitted_by["damage"]

        print(f"{hitted_by["name"]} hit {target["name"]} for {hitted_by["damage"]} HP. Currently he has {target["hit_points"]} HPs left.") # 
        
    person["hit"] = hit
    
    return person

mark = Person_new("Mark", 47, "brown", set_job("Bard"))
mark["talk"]()

adam = Person_new("Adam", 33, "green", set_job("Ranger"))
adam["talk"]()

adam["hit"](adam, mark)