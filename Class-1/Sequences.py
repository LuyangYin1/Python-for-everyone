# List
numbers = [10, 20, 30, 40]  # integers
names = ["john", "Alex", "Bob"]
Mixed = ["John", 10, "Bob", 1.2]
print(names)  # ['john', 'Alex', 'Bob']
print(numbers)  # [10, 20, 30, 40]
print(names[1])  # Alex
print(numbers[2])  # 30

# print(numbers[2])
print(names[1:])  # ['Alex', 'Bob']
print(Mixed[:2])  # ['John', 10]
print(Mixed[0:2])  # ['John', 10]

# # # Modifying elements
numbers[2] = 13
print(numbers)

# # # Addition
numbers2 = [1, 2, 3]
number3 = numbers + numbers2
print(number3)

# # # multiplication
number4 = numbers * 2
print(number4)
print(len(number4))  # 8
# Max min list(element)
number4.append(1)
print(number4.count(10))
number4.sort()
print(number4)
number4.reverse()
print(number4)
print(max(number4))
print(min(number4))

# # Tuples
tpl = (10, 20, 30, 40)
print(tpl)
# # tuples are immutable and cannot be changed where as list can be chagned/
# # if we are asked to change tuple then we cannot do it.
# # difference in syntax is [] vs ()

# # Truple functions max len min

# Dictionaries
# key-value pair
dct = {"Name": "John", "Age": "21", "Gender": "Male "}

dct2 = {"Name": "John2", "Age": "31", "Gender": "Male "}

print(dct["Name"])
print(dct2["Name"])

# # Functions
# print(len(dct))
