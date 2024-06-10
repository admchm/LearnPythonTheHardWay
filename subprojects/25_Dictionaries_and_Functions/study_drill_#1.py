## Study Drill #1: 
## You now have a nice piece of code that's controlling a car. In this 
## study drill you're going to create a new function that creates any car. 
## Your creator function should meet these requirements:

# It should take parameters to set things like the color, speed, or anything else your cars can do

# Answer: 

def car_factory(color, speed, size):
    print(f"Your requested car will have {color} color. It will be moving with the limit of {speed} km/h and it will be {size} sized car.")

car_factory("blue", "240", "medium")
