## Study Drill #5: 
## Finally, have your code run a little fight club using loops to make different people battle.

# Answer:

import time

def set_job(selected_job):
    new_job = {
        "job": "I have no job",
        "hit_points": 50,
        "damage": 5,
        "dialogue": "I have nothing to say."
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

        print(f"{hitted_by["name"]} hit {target["name"]} for {hitted_by["damage"]} HP.\n")
        time.sleep(2)
        print(f"{hitted_by["name"]} HP: {hitted_by["hit_points"]}.")
        time.sleep(1)
        print(f"{target["name"]} HP: {target["hit_points"]}.\n")
        time.sleep(1)
        
        if target["hit_points"] <= 0:
            target["is_alive"] = False
            print(f"{target["name"]} is dead!")
            time.sleep(1)
        
    person["hit"] = hit
    
    return person

first_name = input("First fighter's name: > ")
first_age = int(input("First fighter's age: > "))
first_eye_color = input("First fighter's eye color: > ")
first_job = input("First fighter's job: > ")

first_fighter = Person_new(first_name, first_age, first_eye_color, set_job(first_job))
first_fighter["talk"]()

second_name = input("Second fighter's name: > ")
second_age = int(input("Second fighter's age: > "))
second_eye_color = input("Second fighter's eye color: > ")
second_job = input("Second fighter's job: > ")

second_fighter = Person_new(second_name, second_age, second_eye_color, set_job(second_job))
second_fighter["talk"]()

while first_fighter["is_alive"] and second_fighter["is_alive"]:
    
    first_fighter["hit"](first_fighter, second_fighter)
    
    if second_fighter["is_alive"]:
        second_fighter["hit"](second_fighter, first_fighter)
        
#Output:
# First fighter's name: > Adam
# First fighter's age: > 33
# First fighter's eye color: > green
# First fighter's job: > Fighter
# I am Adam - fighter. Where I walk, thunder follows.
# Second fighter's name: > Mark
# Second fighter's age: > 54
# Second fighter's eye color: > blue
# Second fighter's job: > Fighter
# I am Mark - fighter. Where I walk, thunder follows.
# Adam hit Mark for 35 HP.

# Adam HP: 250.
# Mark HP: 215.

# Mark hit Adam for 35 HP.

# Mark HP: 215.
# Adam HP: 215.

# Adam hit Mark for 35 HP.

# Adam HP: 215.
# Mark HP: 180.

# Mark hit Adam for 35 HP.

# Mark HP: 180.
# Adam HP: 180.

# Adam hit Mark for 35 HP.

# Adam HP: 180.
# Mark HP: 145.

# Mark hit Adam for 35 HP.

# Mark HP: 145.
# Adam HP: 145.

# Adam hit Mark for 35 HP.

# Adam HP: 145.
# Mark HP: 110.

# Mark hit Adam for 35 HP.

# Mark HP: 110.
# Adam HP: 110.

# Adam hit Mark for 35 HP.

# Adam HP: 110.
# Mark HP: 75.

# Mark hit Adam for 35 HP.

# Mark HP: 75.
# Adam HP: 75.

# Adam hit Mark for 35 HP.

# Adam HP: 75.
# Mark HP: 40.

# Mark hit Adam for 35 HP.

# Mark HP: 40.
# Adam HP: 40.

# Adam hit Mark for 35 HP.

# Adam HP: 40.
# Mark HP: 5.

# Mark hit Adam for 35 HP.

# Mark HP: 5.
# Adam HP: 5.

# Adam hit Mark for 35 HP.

# Adam HP: 5.
# Mark HP: -30.

# Mark is dead!