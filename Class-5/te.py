def calculate_average(numbers):
    """
    Calculates and prints the average of a list of numbers.

    Args:
        numbers: A list of numbers (int or float).
    """
    if not numbers:
        print("The list is empty, cannot calculate the average.")
        return

    if not all(isinstance(num, (int, float)) for num in numbers):
        print("The list must contain only numbers")
        return

    total = sum(numbers)
    average = total / len(numbers)
    print(f"The average is: {average}")


# Example usage:
my_numbers = [10, 20, 30, 40, 50]
calculate_average(my_numbers)  # Output: The average is: 30.0

empty_list = []
calculate_average(
    empty_list
)  # Output: The list is empty, cannot calculate the average.

mixed_list = [10, 20, "a"]
calculate_average(mixed_list)  # Output: The list must contain only numbers

mixed_list = [10, 20, 30, 40, 50]
