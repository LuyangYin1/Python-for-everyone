"""
Python Variables and Data Types Demonstration

This module demonstrates fundamental Python concepts including:
- Variable assignment and dynamic typing
- Numeric data types (int, float, complex)
- String operations and concatenation
- Type checking and conversion
- Complex number operations

Author: Avnit
Date: 2024
"""

def demonstrate_integer_operations():
    """
    Demonstrate integer variable assignment and type checking.
    
    Shows how Python handles integer values and type information.
    """
    # Integer variable assignment
    a = 10
    print(f"Value of a: {a}")
    print(f"Type of a: {type(a)}")
    print(f"Value of a is {a} with type {type(a)}")

def demonstrate_float_operations():
    """
    Demonstrate float variable assignment and operations.
    
    Shows floating-point arithmetic and type information.
    """
    # Float variable assignment
    b = 1.1
    print(f"Value of b: {b}")
    print(f"Type of b: {type(b)}")

def demonstrate_complex_numbers():
    """
    Demonstrate complex number creation and operations.
    
    Shows how to create complex numbers and perform operations with them.
    """
    a = 10
    b = 1.1
    
    # Creating complex number from real and imaginary parts
    c = complex(a, b)
    print(f"Complex number c: {c}")
    print(f"Type of c: {type(c)}")
    
    # Complex number arithmetic
    result = a / c
    print(f"Result of a / c: {result}")
    
    # Accessing real and imaginary parts
    print(f"Real part of c: {c.real}")
    print(f"Imaginary part of c: {c.imag}")
    
    # Alternative complex number syntax
    d = 1 + 2j
    print(f"Complex number d: {d}")
    print(f"Type of d: {type(d)}")
    print(f"Real part of d: {d.real}")
    print(f"Imaginary part of d: {d.imag}")

def demonstrate_string_operations():
    """
    Demonstrate string variable assignment and concatenation.
    
    Shows string creation, concatenation, and formatting.
    """
    # String variable assignment
    a = "avnit"
    print(f"String a: {a}")
    
    # String concatenation
    b = "my name is " + a
    print(f"Concatenated string b: {b}")
    
    # String formatting with f-strings (modern approach)
    c = f"Hello, {a}!"
    print(f"Formatted string c: {c}")
    
    # String formatting with .format() method
    d = "Welcome, {}!".format(a)
    print(f"Formatted string d: {d}")

def demonstrate_print_formatting():
    """
    Demonstrate advanced print statement formatting.
    
    Shows various print statement options including separators and end parameters.
    """
    c = complex(10, 1.1)
    
    # Print with custom separator and end
    print("The real part of complex number is:", c.real, sep="/", end="Avnit")
    print()  # New line
    
    # Print with multiple values
    print("Complex number:", c, "Real part:", c.real, "Imaginary part:", c.imag)

def main():
    """
    Main function to run all demonstrations.
    
    Executes all the demonstration functions in a logical order.
    """
    print("=" * 50)
    print("PYTHON VARIABLES AND DATA TYPES DEMONSTRATION")
    print("=" * 50)
    
    print("\n1. Integer Operations:")
    print("-" * 20)
    demonstrate_integer_operations()
    
    print("\n2. Float Operations:")
    print("-" * 20)
    demonstrate_float_operations()
    
    print("\n3. Complex Number Operations:")
    print("-" * 20)
    demonstrate_complex_numbers()
    
    print("\n4. String Operations:")
    print("-" * 20)
    demonstrate_string_operations()
    
    print("\n5. Print Formatting:")
    print("-" * 20)
    demonstrate_print_formatting()
    
    print("\n" + "=" * 50)
    print("DEMONSTRATION COMPLETE")
    print("=" * 50)

if __name__ == "__main__":
    main()
