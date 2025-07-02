"""
Python Sequences and Data Structures

This module demonstrates the fundamental data structures in Python:
- Lists: Mutable, ordered collections
- Tuples: Immutable, ordered collections  
- Dictionaries: Key-value pairs for mapping data

The module covers:
- Creating and accessing sequences
- Basic operations (indexing, slicing)
- Modifying sequences (where applicable)
- Built-in functions and methods
- Common use cases and patterns

Key concepts demonstrated:
- Indexing and slicing
- Mutability vs immutability
- Sequence operations and methods
- Data structure selection
- Performance considerations

Author: Avnit
Date: 2024
"""

def demonstrate_lists():
    """
    Demonstrate list creation, access, and manipulation.
    
    Lists are the most versatile data structure in Python:
    - Mutable (can be changed after creation)
    - Ordered (elements maintain their position)
    - Heterogeneous (can contain different data types)
    - Indexed (access elements by position)
    """
    print("=== LIST DEMONSTRATION ===")
    
    # Creating lists with different data types
    numbers = [10, 20, 30, 40]  # List of integers
    names = ["john", "Alex", "Bob"]  # List of strings
    mixed = ["John", 10, "Bob", 1.2]  # Mixed data types
    
    print("1. List Creation:")
    print(f"   Numbers: {numbers}")
    print(f"   Names: {names}")
    print(f"   Mixed: {mixed}")
    
    # Accessing elements by index
    print("\n2. Indexing (accessing elements):")
    print(f"   First name: {names[0]}")  # Index 0 is first element
    print(f"   Second name: {names[1]}")  # Index 1 is second element
    print(f"   Third number: {numbers[2]}")  # Index 2 is third element
    
    # Slicing (getting a portion of the list)
    print("\n3. Slicing (getting portions):")
    print(f"   Names from index 1 onwards: {names[1:]}")  # From index 1 to end
    print(f"   Mixed first 2 elements: {mixed[:2]}")  # From start to index 1
    print(f"   Mixed elements 0 to 2: {mixed[0:2]}")  # Explicit range
    
    # Modifying lists (demonstrating mutability)
    print("\n4. Modifying Lists (mutability):")
    print(f"   Original numbers: {numbers}")
    numbers[2] = 13  # Change element at index 2
    print(f"   After modification: {numbers}")
    
    # List operations
    print("\n5. List Operations:")
    
    # Addition (concatenation)
    numbers2 = [1, 2, 3]
    combined = numbers + numbers2
    print(f"   Addition: {numbers} + {numbers2} = {combined}")
    
    # Multiplication (repetition)
    repeated = numbers * 2
    print(f"   Multiplication: {numbers} * 2 = {repeated}")
    print(f"   Length of repeated list: {len(repeated)}")
    
    # List methods
    print("\n6. List Methods:")
    
    # append() - add element to end
    repeated.append(1)
    print(f"   After append(1): {repeated}")
    
    # count() - count occurrences
    count_10 = repeated.count(10)
    print(f"   Count of 10: {count_10}")
    
    # sort() - sort in ascending order
    repeated.sort()
    print(f"   After sort(): {repeated}")
    
    # reverse() - reverse the order
    repeated.reverse()
    print(f"   After reverse(): {repeated}")
    
    # Built-in functions
    print("\n7. Built-in Functions:")
    print(f"   Maximum value: {max(repeated)}")
    print(f"   Minimum value: {min(repeated)}")
    print(f"   Length: {len(repeated)}")


def demonstrate_tuples():
    """
    Demonstrate tuple creation, access, and immutability.
    
    Tuples are similar to lists but with key differences:
    - Immutable (cannot be changed after creation)
    - Faster than lists for iteration
    - Used for data that shouldn't change
    - Syntax: parentheses () instead of brackets []
    """
    print("\n=== TUPLE DEMONSTRATION ===")
    
    # Creating tuples
    tpl = (10, 20, 30, 40)  # Tuple of integers
    mixed_tuple = ("John", 25, 3.14, True)  # Mixed data types
    
    print("1. Tuple Creation:")
    print(f"   Integer tuple: {tpl}")
    print(f"   Mixed tuple: {mixed_tuple}")
    
    # Accessing elements (same as lists)
    print("\n2. Accessing Elements:")
    print(f"   First element: {tpl[0]}")
    print(f"   Last element: {tpl[-1]}")  # Negative indexing
    print(f"   Slice: {tpl[1:3]}")  # Elements 1 and 2
    
    # Demonstrating immutability
    print("\n3. Immutability (cannot change):")
    print(f"   Original tuple: {tpl}")
    print("   Trying to modify tuple[0] = 99 would cause an error!")
    print("   Tuples are immutable - they cannot be changed after creation")
    
    # Tuple operations (similar to lists)
    print("\n4. Tuple Operations:")
    tpl2 = (50, 60)
    combined = tpl + tpl2
    print(f"   Addition: {tpl} + {tpl2} = {combined}")
    
    repeated = tpl * 2
    print(f"   Multiplication: {tpl} * 2 = {repeated}")
    
    # Built-in functions work with tuples
    print("\n5. Built-in Functions:")
    print(f"   Maximum: {max(tpl)}")
    print(f"   Minimum: {min(tpl)}")
    print(f"   Length: {len(tpl)}")
    print(f"   Sum: {sum(tpl)}")
    
    # Tuple unpacking
    print("\n6. Tuple Unpacking:")
    x, y, z, w = tpl
    print(f"   Unpacked values: x={x}, y={y}, z={z}, w={w}")
    
    # Common use cases for tuples
    print("\n7. Common Use Cases:")
    coordinates = (3, 4)  # x, y coordinates
    rgb_color = (255, 128, 0)  # Red, Green, Blue values
    print(f"   Coordinates: {coordinates}")
    print(f"   RGB Color: {rgb_color}")


def demonstrate_dictionaries():
    """
    Demonstrate dictionary creation, access, and manipulation.
    
    Dictionaries are key-value pairs:
    - Mutable (can be changed after creation)
    - Unordered (in Python < 3.7, ordered since 3.7)
    - Fast lookup by key
    - Keys must be immutable (strings, numbers, tuples)
    - Values can be any data type
    """
    print("\n=== DICTIONARY DEMONSTRATION ===")
    
    # Creating dictionaries
    person1 = {"Name": "John", "Age": "21", "Gender": "Male"}
    person2 = {"Name": "John2", "Age": "31", "Gender": "Male"}
    
    print("1. Dictionary Creation:")
    print(f"   Person 1: {person1}")
    print(f"   Person 2: {person2}")
    
    # Accessing values by key
    print("\n2. Accessing Values:")
    print(f"   Person 1 name: {person1['Name']}")
    print(f"   Person 2 name: {person2['Name']}")
    print(f"   Person 1 age: {person1['Age']}")
    
    # Adding and modifying entries
    print("\n3. Modifying Dictionaries:")
    person1["City"] = "New York"  # Add new key-value pair
    print(f"   After adding city: {person1}")
    
    person1["Age"] = "22"  # Modify existing value
    print(f"   After updating age: {person1}")
    
    # Dictionary methods
    print("\n4. Dictionary Methods:")
    
    # keys() - get all keys
    keys = person1.keys()
    print(f"   Keys: {list(keys)}")
    
    # values() - get all values
    values = person1.values()
    print(f"   Values: {list(values)}")
    
    # items() - get key-value pairs
    items = person1.items()
    print(f"   Items: {list(items)}")
    
    # get() - safe access with default value
    print(f"   Age: {person1.get('Age', 'Unknown')}")
    print(f"   Phone: {person1.get('Phone', 'Not provided')}")
    
    # Built-in functions
    print("\n5. Built-in Functions:")
    print(f"   Length: {len(person1)}")
    print(f"   Keys: {list(person1.keys())}")
    print(f"   Values: {list(person1.values())}")
    
    # Nested dictionaries
    print("\n6. Nested Dictionaries:")
    student = {
        "name": "Alice",
        "grades": {"Math": 95, "Science": 88, "English": 92},
        "contact": {"email": "alice@email.com", "phone": "555-1234"}
    }
    print(f"   Student: {student}")
    print(f"   Math grade: {student['grades']['Math']}")
    print(f"   Email: {student['contact']['email']}")


def demonstrate_sequence_comparisons():
    """
    Compare different sequence types and their characteristics.
    
    This function helps students understand when to use each
    data structure based on their requirements.
    """
    print("\n=== SEQUENCE COMPARISONS ===")
    
    # Creating similar data in different structures
    list_data = [1, 2, 3, 4, 5]
    tuple_data = (1, 2, 3, 4, 5)
    dict_data = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    
    print("1. Memory and Performance:")
    print(f"   List: {list_data} (mutable, slower iteration)")
    print(f"   Tuple: {tuple_data} (immutable, faster iteration)")
    print(f"   Dict: {dict_data} (key-value, fast lookup)")
    
    print("\n2. Use Cases:")
    print("   Lists: When you need to modify the collection")
    print("   Tuples: When data should not change (coordinates, RGB values)")
    print("   Dictionaries: When you need to associate keys with values")
    
    print("\n3. Common Operations Comparison:")
    
    # Accessing elements
    print("   Accessing:")
    print(f"     List[0]: {list_data[0]}")
    print(f"     Tuple[0]: {tuple_data[0]}")
    print(f"     Dict['a']: {dict_data['a']}")
    
    # Length
    print("   Length:")
    print(f"     List: {len(list_data)}")
    print(f"     Tuple: {len(tuple_data)}")
    print(f"     Dict: {len(dict_data)}")


def demonstrate_practical_examples():
    """
    Show practical examples of when to use each data structure.
    
    These examples help students understand real-world applications
    of different data structures.
    """
    print("\n=== PRACTICAL EXAMPLES ===")
    
    # Example 1: Shopping cart (list)
    print("1. Shopping Cart (List):")
    cart = ["apple", "banana", "milk", "bread"]
    print(f"   Cart: {cart}")
    cart.append("eggs")  # Add item
    print(f"   After adding eggs: {cart}")
    cart.remove("banana")  # Remove item
    print(f"   After removing banana: {cart}")
    
    # Example 2: Student grades (dictionary)
    print("\n2. Student Grades (Dictionary):")
    grades = {"Math": 95, "Science": 88, "English": 92, "History": 85}
    print(f"   Grades: {grades}")
    print(f"   Math grade: {grades['Math']}")
    grades["Art"] = 90  # Add new subject
    print(f"   After adding Art: {grades}")
    
    # Example 3: Coordinates (tuple)
    print("\n3. Coordinates (Tuple):")
    point1 = (3, 4)
    point2 = (7, 2)
    print(f"   Point 1: {point1}")
    print(f"   Point 2: {point2}")
    print("   Tuples are perfect for coordinates (immutable)")
    
    # Example 4: Mixed data structure
    print("\n4. Complex Data Structure:")
    class_data = {
        "name": "Python Programming",
        "students": ["Alice", "Bob", "Charlie", "Diana"],
        "grades": {"Alice": 95, "Bob": 88, "Charlie": 92, "Diana": 87},
        "schedule": ("Monday", "Wednesday", "Friday"),
        "room": "Lab 101"
    }
    print(f"   Class data: {class_data}")
    print(f"   Number of students: {len(class_data['students'])}")
    print(f"   Alice's grade: {class_data['grades']['Alice']}")


def main():
    """
    Main function to demonstrate all sequence concepts.
    
    This function runs all the demonstration functions
    in a logical order to show the progression of concepts.
    """
    print("=" * 60)
    print("PYTHON SEQUENCES AND DATA STRUCTURES DEMONSTRATION")
    print("=" * 60)
    
    # Run demonstrations in logical order
    demonstrate_lists()
    demonstrate_tuples()
    demonstrate_dictionaries()
    demonstrate_sequence_comparisons()
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
    
    # Practice 1: List operations
    print("1. List Operations:")
    numbers = [1, 2, 3, 4, 5]
    print(f"   Original: {numbers}")
    numbers.append(6)
    print(f"   After append: {numbers}")
    numbers.insert(0, 0)
    print(f"   After insert: {numbers}")
    
    # Practice 2: Dictionary operations
    print("\n2. Dictionary Operations:")
    info = {"name": "John", "age": 25}
    print(f"   Original: {info}")
    info["city"] = "New York"
    print(f"   After adding city: {info}")
    
    # Practice 3: Tuple unpacking
    print("\n3. Tuple Unpacking:")
    coords = (10, 20)
    x, y = coords
    print(f"   Coordinates: {coords}")
    print(f"   x = {x}, y = {y}")
    
    print("\n=== Module Complete ===")
    print("This module demonstrates Python sequences and data structures.")
    print("Key concepts covered: lists, tuples, dictionaries, and their operations.")
    print("Understanding these data structures is fundamental to Python programming!")
