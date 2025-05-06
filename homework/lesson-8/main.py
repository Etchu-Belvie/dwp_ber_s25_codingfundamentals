# Lesson 8 Homework

european_cities = [("Istanbul", [15460000, "Kebab", "Hagia Sophia"]),
                   ("Moscow", [12678079, "Borscht", "Red Square"]),
                   ("London", [8982000, "Fish and Chips", "Big Ben"]),
                   ("St. Petersburg", [5383890, "Blini", "Hermitage Museum"]),
                   ("Berlin", [3669491, "Currywurst", "Brandenburg Gate"]),
                   ("Madrid", [3348536, "Paella", "Royal Palace of Madrid"]),
                   ("Kiev", [2884000, "Borscht", "Saint Sophia's Cathedral"]),
                   ("Paris", [2140526, "Croissant", "Eiffel Tower"])]

# Exercise 1:Create an empty dictionary: european_cities_info
print("\n# Exercise 1:Create an empty dictionary: european_cities_info")

european_cities_info = {}
# european_cities_info = dict()

# Exercise 2: Loop over the european_cities and unpack each tuple
print("\n# Exercise 2:Loop over the european_cities and unpack each tuple")

for key,value in european_cities:
    european_cities_info[key] = value

# Exercise 3:Print dictionary with the format City --> [Population, Dish, Landmark]
print("\n# Exercise 3:Print dictionary with the format City --> [Population, Dish, Landmark")

for key, value in european_cities_info.items():
    print(key, "-->", value)

# Exercise 4:Sort the european_cities_info dictionary alphabetically by city (use sorted)
print("\n# Exercise 4:Sort the european_cities_info dictionary alphabetically by city (use sorted)")

for key in sorted(european_cities_info):
    print(key,"-->", european_cities_info[key])

# Exercise 5:Safely print the 'Berlin' info from the european_cities_info dictionary
print("\n# Exercise 5:Safely print the 'Berlin' info from the european_cities_info dictionary")

print("Berlin Infos:",european_cities_info["Berlin"])
#print(european_cities_info.get("Berlin"))

# Exercise 6:Safely print the type of 'London' from the european_cities_info dictionary
print("\n# Exercise 6:Safely print the type of 'London' from the european_cities_info dictionary")

print("Londons' Info Type:",type(european_cities_info["London"]))
#print(type(european_cities_info.get("London")))

# Exercise 7:Safely print 'Barcelona' from the european_cities_info dictionary or 'Not Found'
print("\n# Exercise 7:Safely print 'Barcelona' from the european_cities_info dictionary or 'Not Found'")

if "Barcelona" in european_cities_info:
    print(european_cities_info["Barcelona"])
else:
    print("Barcelona: Not Found")

# Exercise 8:Add new city ("Rome", [2870500, "Pasta", "Colosseum"])
print("\n# Exercise 8: Add new city")

european_cities_info["Rome"] = [2870500, "Pasta", "Colosseum"]
for key,value in sorted(european_cities_info.items()):
    print(key, "-->", value)

# Exercise 9:Remove "Madrid" from european_cities_info
print("\n# Exercise 9:Remove 'Madrid' from european_cities_info")

(european_cities_info.pop("Madrid"))
for key,value in sorted(european_cities_info.items()):
  print(key, "-->", value)


# Exercise 10:Check to see if Amsterdam is in european_cities_info and print whether it is there or not
print("\n# Exercise 10:Check to see if Amsterdam is in european_cities_info and print whether it is there or not")

if "Amsterdam" in european_cities_info:
    print(european_cities_info.get("Amsterdam"))
else:
    print("Amsterdam:Not Found")

#print(european_cities_info)   


# Bonus Exercise
print("\n# Bonus Exercise")
'''Bonus: Create a dictionary from two lists:
Use the functions dict() and zip()'''

dishes = ["Pizza", "Sauerkraut", "Paella", "Hamburger"]

countries = ["Italy", "Germany", "Spain", "USA"]

dishes_countries_dict = dict(zip(dishes,countries))
print(dishes_countries_dict)


