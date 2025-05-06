# Data Structure:Dictionaries
print("\n# Dta Structure:Dictionaries")
# Exercise 1
print("\n# Exercise 1")

print("#1:")
personal_info = {"name":"Bella", "age":25, "occupation":"Financial Analyst"}

print("#2:")
personal_info["hobby"] = ["Trying New Things", "Painting", "Self Time"]
print(personal_info)

print("#3:")
print(personal_info.get("occupation"))
print(personal_info["occupation"])

print("#4:")
personal_info["Nationality"] = "Cameroonian"
print(personal_info.get("Nationality"))
print(personal_info["Nationality"])

print("#5:")
if "Nationality" in personal_info:
    print(personal_info.get("Nationality"))
else:
    print("unknown")

print("#6:")
print(personal_info.keys())

print("#7:")
print(personal_info.values())

print("#8:")
personal_info["occupation"] = "Sofware Engineer"
print(personal_info)

print("#9:")
personal_info.pop("age")
print(personal_info.keys())

print("#10:")
print("Favorite colour" in personal_info)

print("#11:appending a hobby")

personal_info["hobby"].append("cleaning")
print(personal_info.values())


# Exercise 2: Looping over Dictionaries
print("\n# Exercise 2: Looping over Dictionaries")

print("Exercise 2.1: Sum in looping")
incomes = {"Mother": 3600.00, "Father": 2500.00, "Daughter": 500.00}

count = 0
for income in incomes.values():
    count = count + income
print(count)

print("Exercise 2.2:converting dict to a list of tuples with for loop")

'''Using the dictionary my_dict , convert the dictionary into a list of tuples using a for loop. (
hint: use the method append())'''
my_dictionary = {"name":"Bella", "age":25, "occupation":"Financial Analyst"}
print(my_dictionary)
my_list =[]

for key, val in my_dictionary.items():
    my_list.append((key,val))
print(my_list)

# Exercise 2.3:

print("\n# Exercise 2.3: ")

'''Create dictionaries similar to the Rapunzel one for you and 2 of your friends. Create a list of
dictionaries with both information ( myList = [ my_dict, my_friend_dict_1 ,
my_friend_dict_2] . Calculate the average of all your ages.'''

my_friend_dict_1 = {"name":"friend1", "age":35, "occupation":"Lawyer"}
my_friend_dict_2 = {"name":"friend2", "age": 27, "occupation":"Software Engineer"}

my_dictionaries = [my_dictionary,my_friend_dict_1,my_friend_dict_2]

total_count = 0
for item in my_dictionaries:
    #total_count = total_count + item.get("age")
    total_count += item.get("age")

average = total_count / len(my_dictionaries)
print(average)



