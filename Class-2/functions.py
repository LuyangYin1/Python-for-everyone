# Creating the function 
def hello():
    print("Hello World")

hello()

# Function with parameters 
def adding_two_numbers(number1,number2):
    print("Adding two numbers")
    return number1 + number2 

total = adding_two_numbers(2,3)
print(total)

#Default function
def say(text="hello"):
    if text == "hello":
        print("Please call the function with a text parameter")
    else :
        print("This is the correct way to call the function")
        print(text)

say()
say("Hi")



# Base Case and Recursive Cases 
# # Factorial 5! = 5*4*3*2*1

# def factorial(n):
#     if n <= 0:
#         return 1 # base case 
#     return n * factorial(n-1) # recursive

# print(factorial(5))

# # def func1(x, y):
# #    return x+y

# def func2(a,b,c):
#     return adding_two_numbers(a*b,c)

# print(func2(1,2,3)) # prints 1 * 2 + 3  = 5  