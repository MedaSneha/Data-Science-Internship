# Variables
print("\n----- Variables -----")
name = "Sneha"
age = 22
height = 5.3

print("Name:", name)
print("Age:", age)
print("Height:", height)

# Data Types
print("\n----- Data Types -----")
print(type(name))
print(type(age))
print(type(height))


# Operators
print("\n----- Operators -----")
a = 20
b = 5

print("\n----- Operators -----")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# Conditional Statement
# if statement
print("\n----- if statement -----")
age = 20
if age >= 18:
    print("You are eligible to vote.")

# if...else statement
print("\n----- if...else statement -----")
number = 7

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# if...elif...else Statement
print("\n-----if...elif...else Statement-----")
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# For Loop
print("\n----- For Loop -----")
for i in range(1, 6):
    print(i)

# While Loop
print("\n----- While Loop -----")
count = 1

while count <= 5:
    print(count)
    count += 1

# Function
print("\n----- Function -----")

def greet(name):
    return f"Hello, {name}! Welcome to Python."

print(greet("Sneha"))