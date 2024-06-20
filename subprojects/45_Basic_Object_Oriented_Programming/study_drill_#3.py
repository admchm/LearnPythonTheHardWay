## Study Drill #3: 
## Repeat the same Study Drills from Exercise 44 where you made people 
## who can fight each other. That means adding hit points, a way to have 
## one person attack another, and a job that gives people different combat 
## abilities.

# Answer:

import time

class Person:
    def __init__(self, name, age, eyes, job, hit_points=0, damage=0, dialogue="", is_alive=True):
        self.name = name
        self.age = age
        self.eyes = eyes
        self.hit_points = job.hit_points
        self.damage = job.damage
        self.selected_job = job.selected_job
        self.dialogue = job.dialogue
        self.is_alive = True
        
        self.talk()
    
    def talk(self):
        print(f"I am {self.name} - {self.selected_job}. {self.dialogue}")
    
class Job:
    def __init__(self, selected_job, hit_points=50, damage=5, dialogue="Some message"):
        self.selected_job = selected_job
        self.hit_points = hit_points
        self.damage = damage
        self.dialogue = dialogue
        
        self.set_job()
        
    def set_job(self):
        
        # setting defaults for optional parameters
        self.hit_points = 50
        self.damage = 5
        self.dialogue = "I have nothing to say."
        
        if self.selected_job == "Ranger":
            self.selected_job = "ranger"
            self.hit_points = 120
            self.damage = 15
            self.dialogue = "Nature's whisper guides my arrow."
        
        if self.selected_job == "Ninja":
            self.selected_job = "ninja"
            self.hit_points = 140
            self.damage = 20
            self.dialogue = "Silence is not just golden; it's deadly."
        
        if self.selected_job == "Fighter":
            self.selected_job = "fighter"
            self.hit_points = 250
            self.damage = 35
            self.dialogue = "Where I walk, thunder follows."
            
        if self.selected_job == "Thief":
            self.selected_job = "thief"
            self.hit_points = 95
            self.damage = 10
            self.dialogue = "What's yours is mine, and what's mine is... also mine."
        
        if self.selected_job == "Bard":
            self.selected_job = "bard"
            self.hit_points = 60
            self.damage = 12
            self.dialogue = "A tune for your heart, and a tale for your soul."
        
        if self.selected_job == "none":
            self.selected_job = "nomad"
            self.hit_points = 75
            self.damage = 15
            self.dialogue = "Home is where my journey takes me."

def prepare_fighters(Person, Job):
    first_name = input("First fighter's name: > ")
    first_age = int(input("First fighter's age: > "))
    first_eye_color = input("First fighter's eye color: > ")
    first_job_selected = input("First fighter's job: > ")

    first_job = Job(first_job_selected)
    first_fighter = Person(first_name, first_age, first_eye_color, first_job)

    second_name = input("Second fighter's name: > ")
    second_age = int(input("Second fighter's age: > "))
    second_eye_color = input("Second fighter's eye color: > ")
    second_job_selected = input("Second fighter's job: > ")

    second_job = Job(second_job_selected)
    second_fighter = Person(second_name, second_age, second_eye_color, second_job)
    return first_fighter,second_fighter

def fight(hit, first_fighter, second_fighter):
    while first_fighter.is_alive and second_fighter.is_alive:
        hit(first_fighter, second_fighter)

        if second_fighter.is_alive:
            hit(second_fighter, first_fighter)
            
def calculate_HP(hitted_by, target):
        target.hit_points -= hitted_by.damage

        print(f"{hitted_by.name} hit {target.name} for {hitted_by.damage} HP.\n")
        time.sleep(2)
        print(f"{hitted_by.name} HP: {hitted_by.hit_points}.")
        time.sleep(1)
        print(f"{target.name} HP: {target.hit_points}.\n")
        time.sleep(1)
        
        if target.hit_points <= 0:
            target.is_alive = False
            print(f"{target.name} is dead!")
            time.sleep(1)
    
first_fighter, second_fighter = prepare_fighters(Person, Job)

fight(calculate_HP, first_fighter, second_fighter)
        
# First fighter's name: > Adam
# First fighter's age: > 33
# First fighter's eye color: > green
# First fighter's job: > Fighter
# I am Adam - fighter. Where I walk, thunder follows.
# Second fighter's name: > Mark
# Second fighter's age: > 54
# Second fighter's eye color: > blue
# Second fighter's job: > Thief
# I am Mark - thief. What's yours is mine, and what's mine is... also mine.
# Adam hit Mark for Adam HP.

# Adam HP: 250.
# Mark HP: 60.

# Mark hit Adam for Mark HP.

# Mark HP: 60.
# Adam HP: 240.

# Adam hit Mark for Adam HP.

# Adam HP: 240.
# Mark HP: 25.

# Mark hit Adam for Mark HP.

# Mark HP: 25.
# Adam HP: 230.

# Adam hit Mark for Adam HP.

# Adam HP: 230.
# Mark HP: -10.

# Mark is dead!