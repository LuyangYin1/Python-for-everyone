"""
Python String Operations and Methods

This module demonstrates comprehensive string manipulation in Python.
It covers fundamental string operations that are essential for text processing.

The module covers:
- String creation and basic operations
- String formatting (old-style %, .format(), f-strings)
- String methods (case conversion, searching, replacing)
- String slicing and indexing
- Common string manipulation patterns

Key concepts demonstrated:
- String immutability
- Different formatting methods
- Built-in string methods
- String searching and replacement
- Text processing techniques

Author: Avnit
Date: 2024
"""

def demonstrate_string_basics():
    """
    Demonstrate basic string operations and slicing.
    
    This function shows fundamental string concepts:
    - String creation and assignment
    - Indexing and slicing
    - String concatenation
    - String immutability
    """
    print("=== STRING BASICS ===")
    
    # Basic string creation
    text = "where is San Antonio TX?"
    print(f"Original text: '{text}'")
    
    # String slicing examples
    print("\n1. String Slicing:")
    print(f"   First 5 characters: '{text[:5]}'")  # 'where'
    print(f"   Characters 6 to 11: '{text[6:11]}'")  # 'is Sa'
    print(f"   Last 3 characters: '{text[-3:]}'")  # 'TX?'
    print(f"   Every 2nd character: '{text[::2]}'")  # 'wreei aotn TX'
    
    # String iteration
    print("\n2. String Iteration:")
    print("   Iterating through each character:")
    for char in text:
        print(f"     '{char}'", end=" ")
    print()  # New line after iteration


def demonstrate_string_formatting():
    """
    Demonstrate different string formatting methods in Python.
    
    This function shows three main formatting approaches:
    1. Old-style % formatting (similar to C printf)
    2. .format() method (more flexible)
    3. f-strings (Python 3.6+, most readable)
    
    Each method has its advantages and use cases.
    """
    print("\n=== STRING FORMATTING ===")
    
    # Variables for formatting
    name, age = "john", 25
    
    print("1. Old-style % formatting:")
    print(f"   '%s is my name' % name: {name} is my name")
    print(f"   '%d is my age' % age: {age} is my age")
    print(f"   '%s is %d years old' % (name, age): {name} is {age} years old")
    
    print("\n2. .format() method:")
    print(f"   '{{}} is my name'.format(name): {name} is my name")
    print(f"   '{{}} is {{}} years old'.format(name, age): {name} is {age} years old")
    print(f"   '{{0}} is {{1}} years old'.format(name, age): {name} is {age} years old")
    print(f"   '{{n}} is {{a}} years old'.format(n=name, a=age): {name} is {age} years old")
    
    print("\n3. f-strings (recommended):")
    print(f"   f'{{name}} is {{age}} years old': {name} is {age} years old")
    print(f"   f'{{name.lower()}} is {{age}} years old': {name.lower()} is {age} years old")
    print(f"   f'{{name.upper()}} is {{age}} years old': {name.upper()} is {age} years old")
    
    # Formatting with different data types
    print("\n4. Formatting different data types:")
    pi = 3.14159
    print(f"   Float formatting: {pi:.2f}")  # 3.14
    print(f"   Integer formatting: {age:03d}")  # 025
    print(f"   String alignment: '{name:>10}'")  # Right-aligned
    print(f"   String alignment: '{name:<10}'")  # Left-aligned


def demonstrate_case_methods():
    """
    Demonstrate string case conversion methods.
    
    These methods are useful for:
    - Text normalization
    - Case-insensitive comparisons
    - Display formatting
    - Data cleaning
    """
    print("\n=== CASE CONVERSION METHODS ===")
    
    text = "where is San Antonio TX?"
    
    print(f"Original text: '{text}'")
    print(f"upper(): '{text.upper()}'")  # Convert to uppercase
    print(f"lower(): '{text.lower()}'")  # Convert to lowercase
    print(f"title(): '{text.title()}'")  # Title case (first letter of each word)
    print(f"capitalize(): '{text.capitalize()}'")  # First letter capitalized
    print(f"swapcase(): '{text.swapcase()}'")  # Swap case of each character
    print(f"casefold(): '{text.casefold()}'")  # Aggressive lowercase (for comparisons)
    
    # Practical examples
    print("\nPractical Examples:")
    user_input = "  HELLO WORLD  "
    print(f"User input: '{user_input}'")
    print(f"Normalized: '{user_input.strip().title()}'")


def demonstrate_search_methods():
    """
    Demonstrate string searching and counting methods.
    
    These methods help with:
    - Finding substrings
    - Counting occurrences
    - Text analysis
    - Data validation
    """
    print("\n=== SEARCH AND COUNT METHODS ===")
    
    text = "hello world and welcome to python world"
    
    print(f"Text: '{text}'")
    
    # count() method
    print(f"\n1. count() method:")
    print(f"   count('world'): {text.count('world')}")  # 2 occurrences
    print(f"   count('python'): {text.count('python')}")  # 1 occurrence
    print(f"   count('x'): {text.count('x')}")  # 0 occurrences
    
    # find() method
    print(f"\n2. find() method:")
    print(f"   find('world'): {text.find('world')}")  # First occurrence at index 6
    print(f"   find('python'): {text.find('python')}")  # First occurrence at index 27
    print(f"   find('x'): {text.find('x')}")  # -1 (not found)
    
    # index() method
    print(f"\n3. index() method:")
    print(f"   index('world'): {text.index('world')}")  # First occurrence at index 6
    print(f"   index('python'): {text.index('python')}")  # First occurrence at index 27
    # Note: index() raises ValueError if not found, unlike find()
    
    # Practical example: Safe searching
    print(f"\n4. Safe searching example:")
    search_term = "x"
    position = text.find(search_term)
    if position != -1:
        print(f"   '{search_term}' found at position {position}")
    else:
        print(f"   '{search_term}' not found in text")


def demonstrate_string_manipulation():
    """
    Demonstrate string manipulation methods.
    
    These methods are essential for:
    - Text processing
    - Data cleaning
    - String transformation
    - Formatting
    """
    print("\n=== STRING MANIPULATION ===")
    
    # join() method
    print("1. join() method:")
    names = ["avnit", "loves", "hockey"]
    separator = ","
    joined = separator.join(names)
    print(f"   List: {names}")
    print(f"   Separator: '{separator}'")
    print(f"   Joined: '{joined}'")
    
    # replace() method
    print("\n2. replace() method:")
    txt = "Hello, welcome to my world."
    print(f"   Original: '{txt}'")
    replaced = txt.replace("world", "life")
    print(f"   After replace('world', 'life'): '{replaced}'")
    
    # strip(), lstrip(), rstrip() methods
    print("\n3. Strip methods:")
    messy_text = "   hello world   "
    print(f"   Original: '{messy_text}'")
    print(f"   strip(): '{messy_text.strip()}'")  # Remove both sides
    print(f"   lstrip(): '{messy_text.lstrip()}'")  # Remove left side
    print(f"   rstrip(): '{messy_text.rstrip()}'")  # Remove right side
    
    # split() method
    print("\n4. split() method:")
    sentence = "Python is a great programming language"
    words = sentence.split()
    print(f"   Original: '{sentence}'")
    print(f"   split(): {words}")
    
    # Split with custom delimiter
    csv_data = "apple,banana,cherry,date"
    fruits = csv_data.split(",")
    print(f"   CSV data: '{csv_data}'")
    print(f"   split(','): {fruits}")


def demonstrate_string_validation():
    """
    Demonstrate string validation methods.
    
    These methods help check string properties:
    - Content validation
    - Character type checking
    - Format validation
    """
    print("\n=== STRING VALIDATION ===")
    
    # isalpha(), isdigit(), isalnum()
    print("1. Character type validation:")
    test_strings = ["Hello", "123", "Hello123", "Hello World", "123.45", ""]
    
    for s in test_strings:
        print(f"   '{s}':")
        print(f"     isalpha(): {s.isalpha()}")  # Only letters
        print(f"     isdigit(): {s.isdigit()}")  # Only digits
        print(f"     isalnum(): {s.isalnum()}")  # Letters and digits
        print(f"     isspace(): {s.isspace()}")  # Only whitespace
        print()
    
    # startswith(), endswith()
    print("2. Prefix and suffix checking:")
    filename = "document.txt"
    print(f"   Filename: '{filename}'")
    print(f"   startswith('doc'): {filename.startswith('doc')}")
    print(f"   endswith('.txt'): {filename.endswith('.txt')}")
    print(f"   endswith('.pdf'): {filename.endswith('.pdf')}")


def demonstrate_practical_examples():
    """
    Show practical examples of string operations.
    
    These examples demonstrate real-world applications
    of string manipulation techniques.
    """
    print("\n=== PRACTICAL EXAMPLES ===")
    
    # Example 1: Email validation
    print("1. Email validation:")
    email = "user@example.com"
    print(f"   Email: '{email}'")
    print(f"   Contains @: {'@' in email}")
    print(f"   Ends with .com: {email.endswith('.com')}")
    print(f"   Has valid format: {'@' in email and '.' in email}")
    
    # Example 2: Text cleaning
    print("\n2. Text cleaning:")
    dirty_text = "  Hello, World!  "
    print(f"   Original: '{dirty_text}'")
    cleaned = dirty_text.strip().lower().replace(",", "")
    print(f"   Cleaned: '{cleaned}'")
    
    # Example 3: Password strength checker
    print("\n3. Password strength checker:")
    password = "MyPass123!"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)
    
    print(f"   Password: '{password}'")
    print(f"   Has uppercase: {has_upper}")
    print(f"   Has lowercase: {has_lower}")
    print(f"   Has digit: {has_digit}")
    print(f"   Has special char: {has_special}")
    
    strength = sum([has_upper, has_lower, has_digit, has_special])
    print(f"   Strength score: {strength}/4")
    
    # Example 4: Text analysis
    print("\n4. Text analysis:")
    text = "Python is a great programming language. Python is versatile."
    print(f"   Text: '{text}'")
    print(f"   Length: {len(text)} characters")
    print(f"   Word count: {len(text.split())} words")
    print(f"   'Python' occurrences: {text.count('Python')}")
    print(f"   Most common word: 'Python' (appears {text.count('Python')} times)")


def main():
    """
    Main function to demonstrate all string concepts.
    
    This function runs all the demonstration functions
    in a logical order to show the progression of concepts.
    """
    print("=" * 60)
    print("PYTHON STRING OPERATIONS AND METHODS DEMONSTRATION")
    print("=" * 60)
    
    # Run demonstrations in logical order
    demonstrate_string_basics()
    demonstrate_string_formatting()
    demonstrate_case_methods()
    demonstrate_search_methods()
    demonstrate_string_manipulation()
    demonstrate_string_validation()
    demonstrate_practical_examples()
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)


# Example usage and testing
if __name__ == "__main__":
    # Run the main demonstration
    main()
    
    # Additional practice examples
    print("\n=== Practice Examples ===")
    
    # Practice 1: String formatting
    print("1. String formatting practice:")
    name = "Alice"
    age = 30
    city = "New York"
    print(f"   {name} is {age} years old and lives in {city}.")
    
    # Practice 2: String methods
    print("\n2. String methods practice:")
    text = "  Python Programming  "
    print(f"   Original: '{text}'")
    print(f"   Stripped: '{text.strip()}'")
    print(f"   Uppercase: '{text.strip().upper()}'")
    print(f"   Title case: '{text.strip().title()}'")
    
    # Practice 3: String searching
    print("\n3. String searching practice:")
    sentence = "The quick brown fox jumps over the lazy dog"
    print(f"   Sentence: '{sentence}'")
    print(f"   Contains 'fox': {'fox' in sentence}")
    print(f"   'the' appears {sentence.lower().count('the')} times")
    print(f"   Position of 'fox': {sentence.find('fox')}")
    
    print("\n=== Module Complete ===")
    print("This module demonstrates Python string operations and methods.")
    print("Key concepts covered: formatting, methods, searching, and manipulation.")
    print("String manipulation is essential for text processing and data analysis!")
