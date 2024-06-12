## Study Drill #4: 
## Above each line write an English description of what the line does.

# Answer: 

people = 30 # assigning 30 to people
cars = 40   # assigning 40 to cars
trucks = 15 # assigning 15 to trucks

if cars > people:   # checking if cars value are bigger than people
    print("We should take the cars.")   # print if true
elif cars < people: # else, if cars value is lower than people value
    print("We should not take the cars.")   # print if true
else:                                   # if previous conditions are false, then
    print("We can't decide.")           # print this line
    
if trucks > cars: # checking if trucks value is bigger than cars value
    print("That's too many trucks.")        # print if true
elif trucks < cars:                         # if previous condition was false, check if trucks value is lower than cars
    print("Maybe we could take the trucks.") # print if true
else:                                        # if previous conditions are false, then
    print("We still can't decide.")          # print this line

if people > trucks: # checking if people variable contains bigger value than trucks var
    print("Alright, let's just take the trucks.")   # print if true     
else:                                               # if it was false
    print("Fine, let's stay home then.")            # print this line