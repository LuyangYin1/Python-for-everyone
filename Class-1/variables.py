"""
Python Variables and Data Types Demonstration

This module demonstrates fundamental Python concepts including:
- Variable assignment and dynamic typing
- Different data types (int, float, complex, str)
- Type conversion and checking
- String operations and formatting
- Complex number operations

Author: Avnit
Date: 2024
"""

# Example 1: Basic variable assignment and type checking
print("=== Example 1: Variable Assignment and Type Checking ===")
a = 10  # Integer variable
print(f"Value of a is: {a}, Type: {type(a)}")

# Example 2: Float data type
print("\n=== Example 2: Float Data Type ===")
b = 1.1  # Float variable
print(f"Value of b is: {b}, Type: {type(b)}")

# Example 3: Complex numbers
print("\n=== Example 3: Complex Numbers ===")
c = complex(a, b)  # Creating complex number from int and float
print(f"Complex number c: {c}, Type: {type(c)}")

# Example 4: Mathematical operations with complex numbers
print("\n=== Example 4: Complex Number Operations ===")
result = a / c  # Division of int by complex number
print(f"Result of {a} / {c} = {result}")

# Example 5: Accessing complex number components
print("\n=== Example 5: Complex Number Components ===")
print(f"The real part of complex number is: {c.real}", sep="/", end="Avnit\n")
print(f"The imaginary part of complex number is: {c.imag}")

# Example 6: String variables and concatenation
print("\n=== Example 6: String Operations ===")
a = "avnit"  # String variable (reassigning 'a')
b = "my name is " + a  # String concatenation
c = a + b  # Another string concatenation
print(f"String a: {a}")
print(f"String b: {b}")
print(f"String c: {c}")

# Example 7: Alternative complex number creation
print("\n=== Example 7: Alternative Complex Number Syntax ===")
d = 1 + 2j  # Direct complex number creation
print(f"Complex number d: {d}, Type: {type(d)}")
print(f"Real part: {d.real}")
print(f"Imaginary part: {d.imag}")

# Example 8: Type conversion examples
print("\n=== Example 8: Type Conversion ===")
# Converting string to integer
str_num = "123"
int_num = int(str_num)
print(f"String '{str_num}' converted to integer: {int_num}, Type: {type(int_num)}")

# Converting float to string
float_num = 3.14
str_float = str(float_num)
print(f"Float {float_num} converted to string: '{str_float}', Type: {type(str_float)}")

# Example 9: Variable naming conventions
print("\n=== Example 9: Variable Naming Conventions ===")
# Good variable names
user_name = "John"
age = 25
is_student = True
PI = 3.14159  # Constants in uppercase

print(f"User: {user_name}, Age: {age}, Student: {is_student}, PI: {PI}")

# Example 10: Multiple assignment
print("\n=== Example 10: Multiple Assignment ===")
x, y, z = 1, 2, 3
print(f"x = {x}, y = {y}, z = {z}")

# Tuple unpacking
coordinates = (10, 20, 30)
x_coord, y_coord, z_coord = coordinates
print(f"Coordinates: x={x_coord}, y={y_coord}, z={z_coord}")

print("\n=== Module Complete ===")
print("This module demonstrates Python's dynamic typing and various data types.")
print("Key concepts covered: variables, data types, type conversion, and operations.")
