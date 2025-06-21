import fractions as f

fraction1 = f.Fraction(1, 2)
fraction2 = f.Fraction(2, 3)
result = fraction1 / fraction2
print(result)


# # 1. Create a cube class with the following methods:
# #     - cube: calculates the volume of the cube
# #     - square: calculates the area of the square
# #     - area: calculates the surface area of the cube
# import cube as c

# # 3. Create an instance of the cube class and call the cube, square, and area methods with an argument of 3.0.
# c3 = c.cube()
# c3.length = 3
# output = c3.cube() # Output: 27
# print(f"The cube of 3 is {output}")
# output_sq = c3.square() # Output: 9
# print(f"The square of 3 is {output_sq}")
# output_area = c3.area() # Output: 54
# print(f"The area of 3 is {output_area}")
"""
import bankaccount as b
xyz = b.BankAccount("Sumit", 123456, 1000)
print(xyz.deposit(100))
print(xyz.withdraw(200))
print(xyz.get_balance())
print(xyz.get_account_number())
print(xyz.get_holder_name())
print(xyz.withdraw(1200))
print(xyz.get_balance())

# # 2. Inheritance Example
bsc = b.SavingsAccount("Sumit-savings", 123456, 900, 0.01)
print(bsc.add_interest())
print(bsc.withdraw(1000))
print(bsc.get_balance())
# # 1. Calculate Average Function
# def calculate_average(numbers):
#   Calculates the average of a list of numbers.
#   if not numbers:  # Handle empty list case
#     return 0
#   total = sum(numbers)
#   return total / len(numbers)
  

# # 2. my_math Module (create a separate file named my_math.py)
# # my_math.py
# def square(x):
#   Calculates the square of a number.
#   return x * x

# def cube(x):
#   Calculates the cube of a number.
#   return x * x * x

# w = calculate_average([1, 2, 3, 4, 5])  # Output: 3.0
# print(f"The average of the list is {w}")
# print(calculate_average([0]) ) # Output: 0
 """
