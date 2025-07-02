"""
Python Functions Demonstration

This module demonstrates fundamental Python function concepts including:
- Function definition and calling
- Parameters and arguments
- Return values
- Default parameters
- Recursion
- Function composition
- Scope and namespaces

Author: Avnit
Date: 2024
"""

def hello():
    """
    Simple function that prints a greeting message.
    
    This function demonstrates the basic structure of a Python function
    with no parameters and no return value.
    
    Returns:
        None: This function only prints to console
    """
    print("Hello World")


# Example 1: Basic function call
print("=== Example 1: Basic Function Call ===")
hello()


def adding_two_numbers(number1: float, number2: float) -> float:
    """
    Add two numbers and return the result.
    
    This function demonstrates:
    - Function parameters
    - Return statements
    - Type hints (optional but recommended)
    
    Args:
        number1 (float): First number to add
        number2 (float): Second number to add
        
    Returns:
        float: The sum of the two numbers
        
    Example:
        >>> result = adding_two_numbers(5, 3)
        >>> print(result)
        8
    """
    print("Adding two numbers")
    return number1 + number2


# Example 2: Function with parameters and return value
print("\n=== Example 2: Function with Parameters and Return Value ===")
total = adding_two_numbers(2, 3)
print(f"Total: {total}")


def say(text: str = "hello") -> None:
    """
    Print a message with conditional logic based on the input.
    
    This function demonstrates:
    - Default parameters
    - Conditional statements within functions
    - Function behavior based on parameter values
    
    Args:
        text (str, optional): The text to process. Defaults to "hello".
        
    Returns:
        None: This function only prints to console
        
    Example:
        >>> say()  # Uses default parameter
        Please call the function with a text parameter
        >>> say("Hi there!")
        This is the correct way to call the function
        Hi there!
    """
    if text == "hello":
        print("Please call the function with a text parameter")
    else:
        print("This is the correct way to call the function")
        print(text)


# Example 3: Function with default parameters
print("\n=== Example 3: Function with Default Parameters ===")
say()  # Uses default parameter
say("Hi")  # Uses provided parameter


def factorial(n: int) -> int:
    """
    Calculate the factorial of a number using recursion.
    
    Factorial is defined as: n! = n * (n-1) * (n-2) * ... * 1
    For example: 5! = 5 * 4 * 3 * 2 * 1 = 120
    
    This function demonstrates:
    - Recursion (function calling itself)
    - Base case (stopping condition)
    - Recursive case (continuing condition)
    
    Args:
        n (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of n
        
    Raises:
        RecursionError: If n is too large (Python recursion limit)
        
    Example:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if n <= 0:
        return 1  # Base case: factorial of 0 or negative is 1
    return n * factorial(n-1)  # Recursive case: n * (n-1)!


# Example 4: Recursive function
print("\n=== Example 4: Recursive Function (Factorial) ===")
result = factorial(5)
print(f"Factorial of 5: {result}")

# Demonstrate factorial calculation step by step
print("\nFactorial calculation breakdown:")
print("5! = 5 * 4!")
print("4! = 4 * 3!")
print("3! = 3 * 2!")
print("2! = 2 * 1!")
print("1! = 1 * 0!")
print("0! = 1")
print("Therefore: 5! = 5 * 4 * 3 * 2 * 1 * 1 = 120")


def func2(a: float, b: float, c: float) -> float:
    """
    Demonstrate function composition by calling another function.
    
    This function shows how functions can call other functions,
    creating a composition of operations.
    
    Args:
        a (float): First number
        b (float): Second number  
        c (float): Third number
        
    Returns:
        float: Result of (a * b) + c
        
    Example:
        >>> func2(1, 2, 3)
        5  # Because (1 * 2) + 3 = 5
    """
    return adding_two_numbers(a * b, c)


# Example 5: Function composition
print("\n=== Example 5: Function Composition ===")
result = func2(1, 2, 3)  # prints 1 * 2 + 3 = 5
print(f"Result of func2(1, 2, 3): {result}")


def demonstrate_function_scope():
    """
    Demonstrate variable scope within functions.
    
    This function shows how variables behave differently
    inside and outside of functions.
    """
    local_var = "I'm local to this function"
    print(f"Inside function: {local_var}")
    
    # This would cause an error if uncommented:
    # print(global_var)  # NameError: name 'global_var' is not defined


# Example 6: Function scope demonstration
print("\n=== Example 6: Function Scope ===")
global_var = "I'm global"
print(f"Outside function: {global_var}")
demonstrate_function_scope()


def calculate_area(length: float, width: float | None = None) -> float:
    """
    Calculate area of rectangle or square.
    
    This function demonstrates:
    - Multiple parameters
    - Default parameters with None
    - Conditional logic based on parameters
    
    Args:
        length (float): Length of the rectangle
        width (float, optional): Width of the rectangle. If None, assumes square.
        
    Returns:
        float: Area of the rectangle or square
        
    Example:
        >>> calculate_area(5, 3)  # Rectangle
        15.0
        >>> calculate_area(4)     # Square
        16.0
    """
    if width is None:
        # If no width provided, assume it's a square
        return length * length
    else:
        return length * width


# Example 7: Function with conditional default parameters
print("\n=== Example 7: Conditional Default Parameters ===")
rectangle_area = calculate_area(5, 3)
square_area = calculate_area(4)
print(f"Rectangle area (5x3): {rectangle_area}")
print(f"Square area (4x4): {square_area}")


def demonstrate_multiple_returns(x: float) -> str:
    """
    Demonstrate multiple return paths in a function.
    
    This function shows how functions can have different
    return values based on conditions.
    
    Args:
        x (float): Input number
        
    Returns:
        str: Description of the number's characteristics
    """
    if x > 0:
        return "Positive number"
    elif x < 0:
        return "Negative number"
    else:
        return "Zero"


# Example 8: Multiple return paths
print("\n=== Example 8: Multiple Return Paths ===")
print(f"5 is: {demonstrate_multiple_returns(5)}")
print(f"-3 is: {demonstrate_multiple_returns(-3)}")
print(f"0 is: {demonstrate_multiple_returns(0)}")


print("\n=== Module Complete ===")
print("This module demonstrates Python function concepts and best practices.")
print("Key concepts covered: function definition, parameters, recursion, and composition.")
