## Study Drill #1: 
## Do this same kind of mapping with cities and states/regions in your
## country or some other country.

# Answer:

voivodeship = {
    "Podlaskie": "POD",
    "Silesian": "SLA",
    "Świętokrzyskie": "SWK"
}

cities = {
    "POD": "Bialystok",
    "SLA": "Katowice",
    "SWK": "Kielce"
}

print("\nVoivodeship abbreviations:")
print(voivodeship["Podlaskie"])
print(voivodeship["Silesian"])
print(voivodeship["Świętokrzyskie"])

print("\nFull city names:")
print(cities["POD"])
print(cities["SLA"])
print(cities["SWK"])

print("\nFull voivodeship names with abbreviations:")

for voivodeship, abbrev in list(voivodeship.items()):
    print(voivodeship, abbrev)