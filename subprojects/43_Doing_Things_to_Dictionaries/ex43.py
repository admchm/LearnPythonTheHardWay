print("Lists:")
things = ['a', 'b', 'c', 'd']
print(things[1])

things[1] = 'z'
print(things[1])

print(things)

print("\nDictionaries:")
stuff = {"name": "Zed", "age": 39, "height": 6 * 12 + 2}

print(stuff["name"])
print(stuff["age"])
print(stuff["height"])

stuff["city"] = "SF"
print(stuff["city"])

print(stuff)

stuff[1] = "Wow"
stuff[2] = "Neato"

print(stuff)

stuff.pop("city")
stuff.pop(1)
stuff.pop(2)

print(stuff)

print("\nA Dictionary Example:")

# create a mapping of state to abbreviation
states = {
    "Oregon": "OR", 
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}

# create a basic set of states and some cities in them
cities = {
    "CA": "San Francisco",
    "MI": "Detroit",
    "FL": "Jacksonville"
}

# add some more cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

# print out some cities
print("-" * 10)
print("NY state has: ", cities["NY"])
print("OR state has: ", cities["OR"])

# print some states
print("-" * 10)
print("Michigan's abbreviation is: ", states["Michigan"])
print("Florida's abbreviation is: ", states["Florida"])

# do it by using the state then cities dict
print("-" * 10)

# print("Michigan has: ", cities["MI"])
print("Michigan has: ", cities[states["Michigan"]])
print("Florida has: ", cities[states["Florida"]])

# print every state abbreviation
print("-" * 10)
# print(states.items()) - ('Oregon', 'OR'), etc.
for state, abbrev in list(states.items()):
    print(f"{state}, {abbrev}")

# print every city in state
print("-" * 10)
for state in states:
    print(state)

# now do both at the same time
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state}, {abbrev}")
    print(f"and has city {cities[abbrev]}")

print("-" * 10)
# safely get abbreviation by state that might not be there
state = states.get("Texas")

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get("TX", "Does Not Exist")
print(f"The city for the state 'TX' is {city}")