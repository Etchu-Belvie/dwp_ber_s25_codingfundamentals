score = int(input())
if score > 90:
    print("Grade A")
elif score > 80 and score <= 90:
    print("Grade B")
elif score >= 60 and score <= 80:
    print("Grade C")
elif score >= 40 and score  <= 60:
    print("Grade D")
else:
    print("Grade F")

number = 1
while number <= 100:
    print(number)
    number = number + 1

count = 1
for count in range(1, 4):
    print(count)

count1 = 1
for count1 in range(1, 100):
    if count1 % 2 != 0:
        print(count1)

# Input():Exercise
# 1.
name = input("what is your name? ")
print( "Hello", name)

#2.
number1 = int(input())
number2 = int(input())
print(number1 + number2)


