"""
Conditional Statements in Python

This module demonstrates the use of conditional statements (if-elif-else)
to implement decision-making logic in Python programs.

The module covers:
- Basic if statements
- if-elif-else chains
- Input validation and type conversion
- Grade calculation logic
- User input handling

Key concepts demonstrated:
- Boolean expressions and comparisons
- Logical flow control
- Input validation
- Error handling for user input

Author: Avnit
Date: 2024
"""

def get_grade(marks: int) -> str:
    """
    Determine grade based on marks obtained.
    
    This function implements a grading system where:
    - A+: 91-100 marks
    - A:  71-90 marks
    - B+: 66-70 marks
    - B:  61-65 marks
    - C:  51-60 marks
    - D:  41-50 marks
    - F:  0-40 marks
    
    Args:
        marks (int): Marks obtained (0-100)
        
    Returns:
        str: Grade letter (A+, A, B+, B, C, D, or F)
        
    Raises:
        ValueError: If marks are outside valid range (0-100)
        
    Example:
        >>> get_grade(85)
        'A'
        >>> get_grade(95)
        'A+'
        >>> get_grade(35)
        'F'
    """
    # Input validation
    if not isinstance(marks, int):
        raise TypeError("Marks must be an integer")
    
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")
    
    # Grade determination using if-elif-else chain
    if marks > 90:
        return "A+"
    elif marks > 70:
        return "A"
    elif marks > 65:
        return "B+"
    elif marks > 60:
        return "B"
    elif marks > 50:
        return "C"
    elif marks > 40:
        return "D"
    else:
        return "F"


def get_grade_with_feedback(marks: int) -> tuple[str, str]:
    """
    Determine grade and provide feedback based on marks.
    
    This function extends the basic grading by providing
    additional feedback comments for each grade level.
    
    Args:
        marks (int): Marks obtained (0-100)
        
    Returns:
        tuple[str, str]: (grade, feedback_message)
        
    Example:
        >>> get_grade_with_feedback(85)
        ('A', 'Excellent work! Keep it up.')
        >>> get_grade_with_feedback(35)
        ('F', 'You need to work harder. Consider seeking help.')
    """
    grade = get_grade(marks)
    
    # Provide feedback based on grade
    if grade == "A+":
        feedback = "Outstanding performance! You're a star student!"
    elif grade == "A":
        feedback = "Excellent work! Keep it up."
    elif grade == "B+":
        feedback = "Good work! You're doing well."
    elif grade == "B":
        feedback = "Satisfactory performance. Room for improvement."
    elif grade == "C":
        feedback = "Average performance. Consider studying more."
    elif grade == "D":
        feedback = "Below average. You need to work harder."
    else:  # Grade F
        feedback = "You need to work harder. Consider seeking help."
    
    return grade, feedback


def validate_input(user_input: str) -> int:
    """
    Validate and convert user input to integer.
    
    This function handles user input validation and conversion,
    providing helpful error messages for invalid input.
    
    Args:
        user_input (str): Raw user input string
        
    Returns:
        int: Validated integer value
        
    Raises:
        ValueError: If input cannot be converted to integer
        ValueError: If input is outside valid range (0-100)
        
    Example:
        >>> validate_input("85")
        85
        >>> validate_input("abc")
        ValueError: Please enter a valid integer
    """
    try:
        marks = int(user_input)
        
        # Check if marks are in valid range
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")
        
        return marks
        
    except ValueError as e:
        if "invalid literal" in str(e):
            raise ValueError("Please enter a valid integer") from e
        else:
            raise


def demonstrate_conditional_logic():
    """
    Demonstrate various conditional logic patterns.
    
    This function shows different ways to use conditional statements
    and logical operators in Python.
    """
    print("=== Conditional Logic Examples ===")
    
    # Example 1: Simple if statement
    print("\n1. Simple if statement:")
    x = 85
    if x > 80:
        print(f"  {x} is greater than 80")
    
    # Example 2: if-else statement
    print("\n2. if-else statement:")
    y = 65
    if y >= 70:
        print(f"  {y} is passing grade")
    else:
        print(f"  {y} is below passing grade")
    
    # Example 3: Multiple conditions with logical operators
    print("\n3. Multiple conditions:")
    z = 75
    if z >= 90 and z <= 100:
        print(f"  {z} is in the A+ range")
    elif z >= 70 and z < 90:
        print(f"  {z} is in the A range")
    elif z >= 0 and z < 70:
        print(f"  {z} is below A range")
    else:
        print(f"  {z} is invalid")
    
    # Example 4: Nested if statements
    print("\n4. Nested if statements:")
    score = 88
    if score >= 70:
        if score >= 90:
            print(f"  {score} is excellent")
        elif score >= 80:
            print(f"  {score} is very good")
        else:
            print(f"  {score} is good")
    else:
        print(f"  {score} needs improvement")


def main():
    """
    Main function to run the grade calculation program.
    
    This function demonstrates the complete workflow:
    1. Get user input
    2. Validate input
    3. Calculate grade
    4. Display results
    """
    print("=== Grade Calculator ===")
    print("This program calculates grades based on marks obtained.")
    print("Marks should be between 0 and 100.\n")
    
    try:
        # Get user input
        user_input = input("Enter the marks obtained as an integer only: ")
        
        # Validate and convert input
        marks = validate_input(user_input)
        
        # Calculate grade
        grade = get_grade(marks)
        grade_with_feedback = get_grade_with_feedback(marks)
        
        # Display results
        print(f"\nResults:")
        print(f"  Marks: {marks}")
        print(f"  Grade: {grade}")
        print(f"  Feedback: {grade_with_feedback[1]}")
        
    except ValueError as e:
        print(f"Error: {e}")
        print("Please run the program again with valid input.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Example usage and demonstration
if __name__ == "__main__":
    # Run the main program
    main()
    
    # Demonstrate additional conditional logic
    print("\n" + "="*50)
    demonstrate_conditional_logic()
    
    # Test the grading function with various inputs
    print("\n" + "="*50)
    print("Testing grading function with sample inputs:")
    test_marks = [95, 85, 68, 62, 55, 45, 35]
    
    for marks in test_marks:
        grade = get_grade(marks)
        print(f"  Marks: {marks:2d} -> Grade: {grade}")
    
    print("\n=== Module Complete ===")
    print("This module demonstrates conditional statements and decision-making in Python.")
    print("Key concepts covered: if-elif-else chains, input validation, and logical flow control.")
