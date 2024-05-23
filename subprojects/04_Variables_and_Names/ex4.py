cars = 100
space_in_cars = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_cars
average_passenger_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passenger_per_car, "in each car.")

## Study drills:
## When I wrote this program the first time I had a mistake, and Python told me about it like this:
## Explain this error in your own words. Make sure you use line numbers and explain why.

## Traceback (most recent call last):
##   Cell In[1], line 8, in <module>
##     average_passengers_per_car = car_pool_capacity / passenger
## NameError: name 'car_pool_capacity' is not defined

# Answer: the variable car_pool_capacity wasn't recognized, because it was defined as carpool_capacity

## Here are more study drills:

## I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
# Answer: it will make a difference. 4.0 is a floating point number, 4 is just an integer

## Remember that 4.0 is a floating point number. It's just a number with a decimal point, and you need 4.0 instead of just 4 so that it is floating point.
# Answer: 

## Write comments above each of the variable assignments.
# Answer:
# some comment
cars = 100
# some comment
space_in_cars = 4.0
# some comment
drivers = 30
# some comment
passengers = 90
# some comment
cars_not_driven = cars - drivers
# some comment
cars_driven = drivers
# some comment
carpool_capacity = cars_driven * space_in_cars
# some comment
average_passenger_per_car = passengers / cars_driven

## Make sure you know what = is called (equals) and that its purpose is to give data (numbers, strings, etc.) names (cars_driven, passengers).
# Answer: = is just an assignment, and by using it we're assigning some value to variable

## Remember that _ is an underscore character.
# Answer: ---

## Try running python3 from the Terminal as a calculator like you did before, and use variable names to do your calculations. Popular variable names are also i, x, and j.