# name = input("Enter your name: ")
# print(f"Hello, {name}! Welcome.")

#try:
#    length = float(input("Enter the length of the rectangle: "))
#    width = float(input("Enter the width of the rectangle: "))
#    area = length * width
#    print(f"The area of the rectangle is: {area}")
# except ValueError:
#     print("Invalid input. Please enter numeric values for length and width.")


try:
    number = int(input("Enter an integer: "))
    if number % 2 == 0:
      print(f"{number} is even.")
    else:
      print(f"{number} is odd.")
except ValueError:
    print("Invalid input. Please enter an integer.")
