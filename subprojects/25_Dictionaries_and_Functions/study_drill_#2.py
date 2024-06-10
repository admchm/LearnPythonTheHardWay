## Study Drill #2: 
## It should create a dict that has the correct settings, and already 
## contains all the functions you've created.

# Answer: 

def car_factory(color, speed, size):
    car = {
        "color": color,
        "speed": speed,
        "size": size
    }
    
    print(f"Your requested car will have {car['color']} color. It will be moving with the limit of {car['speed']} km/h and it will be {car['size']} sized car.")

car_factory("blue", "240", "medium")
