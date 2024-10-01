# This program creates a simple calculator

# Function to add two numbers
def add(x, y):
   return x + y

# Function to subtract two numbers
def subtract(x, y):
   return x - y

# Function to multiply two numbers
def multiply(x, y):
   return x * y

# Function to divide two numbers
def divide(x, y):
   return x / y

# Get input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Show the available operations to the user
print("Available operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get the user's choice of operation
choice = int(input("Enter operation choice (1/2/3/4): "))

# Perform the selected operation and display the result
if choice == 1:
   print(num1, "+", num2, "=", add(num1, num2))

elif choice == 2:
   print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == 3:
   print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == 4:
   print(num1, "/", num2, "=", divide(num1, num2))

else:
   print("Invalid input. Please choose a valid operation.")