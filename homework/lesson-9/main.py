# Exercise 1: Student Grouping
print("\n # Exercise 1: Student Grouping")
# Imagine you are a teacher who needs to group their students into pairs or small groups. Given the following list of dictionaries, create random pairs or groups of students – each pair has to have the same project choice.

import random
#import inquire
import pprint



# Student list
students = [
    {"name": "Jane", "choice": "Project B"},
    {"name": "Janet", "choice": "Project A"},
    {"name": "Jack", "choice": "Project A"},
    {"name": "Jimmy", "choice": "Project B"},
    {"name": "Jean", "choice": "Project A"},
    {"name": "Juan", "choice": "Project B"},
    {"name": "Juanita", "choice": "Project B"},
    {"name": "Janine", "choice": "Project A"},
    {"name": "Jill", "choice": "Project B"},
    {"name": "John", "choice": "Project B"},
]


def pick_random_name(list_names):
    return random.choice(list_names)

def make_student_groups(student_list):
    project_groups = {}
    result = []

    
    for student in student_list:
        project = student["choice"]
        name = student["name"]
        if project not in project_groups:
            project_groups[project] = []
        project_groups[project].append(name)


    for project, names in project_groups.items():
        while len(names) >= 2:
            name1 = pick_random_name(names)
            names.remove(name1)
            name2 = pick_random_name(names)
            names.remove(name2)
            result.append((project, [name1, name2]))

    return result


groups = make_student_groups(students)
for i, (project, pair) in enumerate(groups, 1):
    print("Group: ",(i), (project,pair))


# Exercise 2: Meal cost calculator
'''print("\n# Exercise 2: Meal cost calculator")

def inquire(name):
  breakfast_base = random.randint(2, 6)
  lunch_base = random.randint(10, 21)
  dinner_base = random.randint(30, 51)
  questions = [
      inquirer.List(
          "breakfast",
          message=f"How much did {name} pay for breakfast? 🥐 ☕",
          choices=[f"${breakfast_base}", f"${breakfast_base + 2}"],
      ),
      inquirer.List(
          "lunch",
          message=f"How much did {name} pay for lunch? 🍔",
          choices=[f"${lunch_base}", f"${lunch_base + 7}"],
      ),
        inquirer.List(
          "dinner",
          message=f"How much did {name} pay for dinner? 🍽️",
          choices=[f"${dinner_base}", f"${dinner_base + 15}"],
      ),
  ]
  
  transactions = inquirer.prompt(questions)
  return {name: transactions}

def convert_dollars(value):
    number_value = int(value.replace("$", ""))
    return number_value

    
people = ["John", "Jane", "Bella"]
result = [inquire(person) for person in people]
print("Result: ")
pprint(result)'''

# Exercise 3: Meal cost Game
'''print("\n# Exercise 3: Meal cost Gamen")

def play_game():
    name = "ReDi"
    lower_limit = 42 
    higher_limit = 55 
    meals = inquire(name)[name] 
    total = 0

    for meal_value in meals.values(): 
        total += convert_dollars(meal_value) 
    if (lower_limit > total or higher_limit < total): 
        print("You lost.. try again!") 
    else: 
        print("Congrats! You won 👏")

# Uncomment the lines below to test your answer 👇👇👇
# play_game()'''

# Exercise 4: Credit Card Masking
print("\n# Exercise 4: Credit Card Masking")

sample_credit_card_number = '1234567890987654'
expected_credit_card_result = 'XXXXXXXXXXXX7654'

def mask_credit_card_number(credit_card_number):
    masked_credit_card_number = 'X' * 12 + credit_card_number[-4:]
    return masked_credit_card_number

# Uncomment the lines below to test your answer 👇👇👇
print('Expected result: ', expected_credit_card_result)
result = mask_credit_card_number(sample_credit_card_number)
print('Your result:', result)