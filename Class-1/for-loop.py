"""
Python Loops and Control Flow

This module demonstrates various types of loops and control flow statements in Python.
It covers fundamental concepts that are essential for any Python programmer.

The module covers:
- For loops with range()
- While loops
- Nested loops
- Break and continue statements
- Loop control flow
- Common loop patterns and examples

Key concepts demonstrated:
- Iteration over sequences
- Loop termination conditions
- Control flow manipulation
- Infinite loop prevention
- Loop optimization techniques

Author: Avnit
Date: 2024
"""

def demonstrate_multiplication_table():
    """
    Demonstrate nested for loops by creating a multiplication table.
    
    This example shows how nested loops work:
    - Outer loop iterates through multiplicands (1-10)
    - Inner loop iterates through multipliers (1-10)
    - Each iteration calculates and displays the product
    
    The nested structure allows us to create a 10x10 multiplication table.
    
    Example Output:
        1 * 1 = 1
        1 * 2 = 2
        ...
        10 * 10 = 100
    """
    print("=== Multiplication Table (Nested For Loops) ===")
    
    # Nested for loops to create multiplication table
    for x in range(1, 11, 1):  # Outer loop: x goes from 1 to 10
        for y in range(1, 11, 1):  # Inner loop: y goes from 1 to 10
            z = x * y  # Calculate product
            print(f"{x} * {y} = {z}")
    
    print("Note: This creates a 10x10 multiplication table")
    print("Each outer loop iteration runs the inner loop 10 times")


def demonstrate_while_loop():
    """
    Demonstrate basic while loop with counter.
    
    This example shows:
    - While loop syntax and structure
    - Counter variable management
    - Loop termination condition
    - Increment operation
    
    The while loop continues as long as the condition is True.
    """
    print("\n=== While Loop with Counter ===")
    
    number = 0  # Initialize counter
    while number <= 10:  # Continue while number is less than or equal to 10
        print(f"Current number: {number}")
        number += 1  # Increment counter (same as number = number + 1)
    
    print(f"Loop completed. Final number: {number}")


def demonstrate_infinite_loop_prevention():
    """
    Demonstrate how to prevent infinite loops.
    
    This example shows a potentially dangerous loop pattern
    and explains why it could cause problems.
    
    WARNING: The commented code below would create an infinite loop
    because the condition never becomes False.
    """
    print("\n=== Infinite Loop Prevention ===")
    
    # DANGEROUS PATTERN (commented out to prevent infinite loop):
    # numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # for number in numbers:
    #     while number < 50:  # This condition never changes!
    #         print(number)
    #         number += 10    # This modifies the loop variable incorrectly
    
    print("The commented code above would create an infinite loop because:")
    print("1. The while condition 'number < 50' never becomes False")
    print("2. Modifying the loop variable inside a for loop is bad practice")
    print("3. The loop would run forever, consuming system resources")
    
    # CORRECT PATTERN:
    print("\nCorrect pattern - separate loop variables:")
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for number in numbers:
        current = number  # Use separate variable for inner loop
        while current < 50:
            print(f"Processing: {current}")
            current += 10
            if current > 50:  # Safety check
                break


def demonstrate_range_function():
    """
    Demonstrate the range() function with different parameters.
    
    The range() function creates a sequence of numbers:
    - range(stop): 0 to stop-1
    - range(start, stop): start to stop-1
    - range(start, stop, step): start to stop-1 with step increment
    
    Args:
        start (int): Starting number (inclusive)
        stop (int): Ending number (exclusive)
        step (int): Increment value (can be negative)
    """
    print("\n=== Range Function Examples ===")
    
    # Example 1: range with step parameter
    print("Range with step (10 to 20, step 2):")
    for x in range(10, 20, 2):  # Start at 10, go up to 19, increment by 2
        print(f"  x = {x}")
    
    # Example 2: range with different step values
    print("\nRange with different steps:")
    print("Step 1 (default):", list(range(1, 6, 1)))
    print("Step 2:", list(range(1, 6, 2)))
    print("Step -1 (reverse):", list(range(5, 0, -1)))


def demonstrate_break_statement():
    """
    Demonstrate the break statement to exit loops early.
    
    The break statement immediately terminates the loop and
    continues with the next statement after the loop.
    
    This is useful for:
    - Exiting loops when a condition is met
    - Avoiding unnecessary iterations
    - Implementing search algorithms
    """
    print("\n=== Break Statement ===")
    
    number = 0
    while number < 10:
        print(f"Processing number: {number}")
        if number == 5:
            print("  Found number 5! Breaking out of loop.")
            break  # Exit the loop immediately
        number += 1
    
    print(f"Loop ended. Final number: {number}")
    print("Note: The loop stopped at 5, didn't continue to 9")


def demonstrate_continue_statement():
    """
    Demonstrate the continue statement to skip loop iterations.
    
    The continue statement skips the rest of the current iteration
    and continues with the next iteration of the loop.
    
    This is useful for:
    - Skipping specific values
    - Implementing filtering logic
    - Avoiding certain conditions
    """
    print("\n=== Continue Statement ===")
    
    number = 0
    while number < 5:
        number += 1  # Increment first to avoid infinite loop
        if number == 3:
            print(f"  Skipping number {number} with continue")
            continue  # Skip the rest of this iteration
        print(f"  Processing number: {number}")
    
    print("Note: Number 3 was skipped, but the loop continued")


def demonstrate_loop_patterns():
    """
    Demonstrate common loop patterns and best practices.
    
    This function shows various useful loop patterns that
    students will encounter in real-world programming.
    """
    print("\n=== Common Loop Patterns ===")
    
    # Pattern 1: Iterating over a list
    print("1. Iterating over a list:")
    fruits = ["apple", "banana", "cherry", "date"]
    for fruit in fruits:
        print(f"  I like {fruit}")
    
    # Pattern 2: Using enumerate() to get index and value
    print("\n2. Using enumerate() for index and value:")
    for index, fruit in enumerate(fruits):
        print(f"  {index}: {fruit}")
    
    # Pattern 3: Loop with else clause
    print("\n3. Loop with else clause:")
    for i in range(3):
        print(f"  Iteration {i}")
    else:
        print("  Loop completed normally (no break)")
    
    # Pattern 4: Loop with break and else
    print("\n4. Loop with break (else won't execute):")
    for i in range(5):
        if i == 3:
            print(f"  Breaking at {i}")
            break
        print(f"  Iteration {i}")
    else:
        print("  This won't print because of break")


def demonstrate_loop_optimization():
    """
    Demonstrate loop optimization techniques.
    
    This function shows how to write efficient loops
    and avoid common performance pitfalls.
    """
    print("\n=== Loop Optimization ===")
    
    # Example 1: Avoid unnecessary computations in loops
    print("1. Efficient loop (compute once outside):")
    numbers = [1, 2, 3, 4, 5]
    length = len(numbers)  # Compute once, not in every iteration
    
    for i in range(length):
        print(f"  Element {i}: {numbers[i]}")
    
    # Example 2: Use list comprehension for simple operations
    print("\n2. List comprehension (more efficient):")
    squares = [x**2 for x in range(5)]
    print(f"  Squares: {squares}")
    
    # Example 3: Early exit for better performance
    print("\n3. Early exit pattern:")
    target = 3
    found = False
    
    for num in range(10):
        if num == target:
            found = True
            print(f"  Found {target} at position {num}")
            break  # Exit early, don't check remaining numbers
    
    if not found:
        print(f"  {target} not found")


def main():
    """
    Main function to demonstrate all loop concepts.
    
    This function runs all the demonstration functions
    in a logical order to show the progression of concepts.
    """
    print("=" * 60)
    print("PYTHON LOOPS AND CONTROL FLOW DEMONSTRATION")
    print("=" * 60)
    
    # Run demonstrations in logical order
    demonstrate_multiplication_table()
    demonstrate_while_loop()
    demonstrate_infinite_loop_prevention()
    demonstrate_range_function()
    demonstrate_break_statement()
    demonstrate_continue_statement()
    demonstrate_loop_patterns()
    demonstrate_loop_optimization()
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)


# Example usage and testing
if __name__ == "__main__":
    # Run the main demonstration
    main()
    
    # Additional practice examples
    print("\n=== Practice Examples ===")
    
    # Practice 1: Count even numbers
    print("1. Count even numbers from 1 to 10:")
    even_count = 0
    for i in range(1, 11):
        if i % 2 == 0:
            even_count += 1
            print(f"  Found even number: {i}")
    print(f"  Total even numbers: {even_count}")
    
    # Practice 2: Sum of first 5 numbers
    print("\n2. Sum of first 5 numbers:")
    total = 0
    for i in range(1, 6):
        total += i
        print(f"  Adding {i}, total so far: {total}")
    print(f"  Final sum: {total}")
    
    # Practice 3: Pattern printing
    print("\n3. Pattern printing:")
    for i in range(5):
        print("  " + "*" * (i + 1))
    
    print("\n=== Module Complete ===")
    print("This module demonstrates Python loops and control flow concepts.")
    print("Key concepts covered: for loops, while loops, break, continue, and optimization.")
    print("Practice these concepts to become proficient in Python programming!")
