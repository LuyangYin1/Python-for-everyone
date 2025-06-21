# Python Homework
# Do one from each part and submit it by email.
# Deadline: 26th March 2025

# Part 1: Python Basics

# Write a Python program that takes a user's name as input and prints a personalized greeting message.
# Create a program to calculate the area of a rectangle. Take the length and width as input from the user.
# Write a Python program to check if a given number is even or odd.


# 1. Personalized Greeting
def greet_user():
    """Takes a user's name and prints a personalized greeting."""
    name = input("Enter your name: ")
    print(f"Hello, {name}! Welcome.")


# 2. Area of a Rectangle
def calculate_rectangle_area():
    """Calculates the area of a rectangle."""
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print(f"The area of the rectangle is: {area}")
    except ValueError:
        print("Invalid input. Please enter numeric values for length and width.")


# 3. Even or Odd Check
def check_even_odd():
    """Checks if a number is even or odd."""
    try:
        number = int(input("Enter an integer: "))
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
    except ValueError:
        print("Invalid input. Please enter an integer.")


# Run the programs
greet_user()
calculate_rectangle_area()
check_even_odd()

# Part 2: Functions and Modules

# Write a function called calculate_average that takes a list of numbers as input and returns the average.
# Create a module named my_math containing functions to calculate the square and cube of a number.
# Explain the difference between local and global variables in Python, providing examples.


# 1. Calculate Average Function
def calculate_average(numbers):
    """Calculates the average of a list of numbers."""
    if not numbers:  # Handle empty list case
        return 0
    total = sum(numbers)
    return total / len(numbers)


# 2. my_math Module (create a separate file named my_math.py)
# my_math.py
def square(x):
    """Calculates the square of a number."""
    return x * x


def cube(x):
    """Calculates the cube of a number."""
    return x * x * x


# 3. Local vs. Global Variables


# Example for Local Variables
def my_function():
    local_variable = 10  # This variable is local to my_function
    print(f"Inside the function: {local_variable}")


my_function()

# Example for Global Variables
global_variable = 20  # This variable is global


def another_function():
    print(f"Inside another function: {global_variable}")


another_function()
print(f"Outside the function: {global_variable}")


def modify_global():
    global global_variable  # explicitly declare intent to modify global variable.
    global_variable = 30
    print(f"Inside modify_global: {global_variable}")


modify_global()
print(f"Outside modify_global: {global_variable}")

# Example using the my_math module
import cube as my_math

number = 5
print(f"Square of {number}: {my_math.square(number)}")
print(f"Cube of {number}: {my_math.cube(number)}")
# Part 3: Classes and Objects

# Create a class called BankAccount with attributes for account holder name, account number, and balance. Include methods to deposit and withdraw money.
# Explain the concept of inheritance in object-oriented programming, providing a Python example.
# What is operator overloading? Demonstrate how to overload the / operator for a custom class in Python.


# 1. BankAccount Class
class BankAccount:
    def __init__(self, holder_name, account_number, balance=0):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def __str__(self):
        return f"Account Holder: {self.holder_name}, Account Number: {self.account_number}, Balance: ${self.balance}"


# 2. Inheritance
# Inheritance allows a new class (subclass/child class) to inherit attributes and methods from an existing class (superclass/parent class).
# This promotes code reusability and creates a hierarchical relationship between classes.


class SavingsAccount(BankAccount):  # Inherits from BankAccount
    def __init__(self, holder_name, account_number, balance=0, interest_rate=0.01):
        super().__init__(
            holder_name, account_number, balance
        )  # Call parent's constructor
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Added interest of ${interest}. New balance: ${self.balance}"


# 3. Operator Overloading
# Operator overloading allows you to redefine the behavior of built-in operators (like +, -, *, /) for custom classes.
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __truediv__(self, other):  # Overloading the / operator
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


# Example Usage
account1 = BankAccount("Alice Smith", "1234567890", 1000)
print(account1.deposit(500))
print(account1.withdraw(200))
print(account1)

savings_account1 = SavingsAccount("Bob Johnson", "9876543210", 2000, 0.02)
print(savings_account1.add_interest())
print(savings_account1)

fraction1 = Fraction(1, 2)
fraction2 = Fraction(2, 3)
result = fraction1 / fraction2
print(result)  # prints 3/4


# Part 4: File Handling
# open a file in read mode and write mode and read the content of the file and write some content to the file.
def read_and_write_file(filename):
    """
    Reads the content of a file and writes new content to it.

    Args:
      filename: The name of the file to open.

    Raises:
      FileNotFoundError: If the file cannot be found.
    """
    try:
        # Open the file in read mode ('r')
        with open(filename, "r") as file:
            content = file.read()
            print(f"Original content:\n{content}")

        # Open the file in write mode ('w') (overwrites existing content)
        with open(filename, "w") as file:
            new_content = "This is the new content."
            file.write(new_content)
            print(f"Wrote new content:\n{new_content}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


# Example usage
filename = "my_file.txt"  # Replace with the actual filename
read_and_write_file(filename)
# Explain the difference between read, readline, and readlines methods of a file object in Python. (refer to the official documentation)
# read  - single string
# readline -  Reads a single line from the file, including the newline character (\n) at the end of the line.
# readlines - Reads all lines from the file and returns them as a list of strings. Each string in the list represents a line, including the newline character (\n).

# Bonus:

# Research and implement a simple data analysis task using Pandas. You can choose a dataset of your interest.
# Submission:

# Submit your Python code files (.py) and a brief report explaining your solutions.
# Make sure your code is well-commented and easy to understand.
# Include any references used in your research.
# Submit your homework via email "abambah@gmail.com". Copy the code and add it as an attachment to the email.
