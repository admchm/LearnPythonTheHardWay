## Study Drill #3: 
## It should return this dict so people can assign the results to 
## anything they want and use later.

# Answer: 

def car_factory(color, speed, size):
    ordered_car = {
        "color": color,
        "speed": speed,
        "size": size
    }
    
    return ordered_car
    
car = car_factory("blue", "240", "medium")

# changing values before printing
car["speed"] = 100
car["size"] = "small"

print(f"Your requested car will have {car['color']} color. It will be moving with the limit of {car['speed']} km/h and it will be {car['size']} sized car.")