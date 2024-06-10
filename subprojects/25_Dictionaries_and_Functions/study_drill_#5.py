## Study Drill #5: 
## Your code should test #4 by changing settings in a few different 
## cars and then confirming they didn't change in other cars.

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
cars[0]["color"] = "black"
cars[1]["color"] = "green"
cars[2]["color"] = "gray"

print(cars[0])
print(cars[1])
print(cars[2])
