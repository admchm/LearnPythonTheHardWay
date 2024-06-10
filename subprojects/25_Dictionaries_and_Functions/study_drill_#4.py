## Study Drill #4: 
## It should be written so that someone can create any number of different 
## cars and each one they make is independent.

# Answer: 

def car_factory(order_count, color, speed, size):
    ordered_cars = []
    iterator = 0
    
    
    while iterator < order_count:
        car = {
            "color": color,
            "speed": speed,
            "size": size
        }
        ordered_cars.append(car) 
        iterator += 1   
    
    return ordered_cars
    
cars = car_factory(3, "blue", "240", "medium")

# important - len vs count. Len will give you number of the items in list, where count will return
#                               the count of the occurences of a specific element in thelist.
print(f"Requested cars count {len(cars)}") 

# changing values before printing
#car["speed"] = 100
#car["size"] = "small"

#print(f"Your requested car will have {car['color']} color. It will be moving with the limit of {car['speed']} km/h and it will be {car['size']} sized car.")