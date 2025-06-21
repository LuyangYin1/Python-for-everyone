# testing script for class 2
import sys

print("The platform you are using = " + sys.platform)
print("The process implementation name is " + sys.implementation.name)
print("Version of python is " + str(sys.version_info))
print("The version of Python is " + sys.version)
print(
    "The version of Python is " + sys.version.split()[0]
)  # Get only the major.minor version
if sys.version_info.major == 3:
    print("You are using Python 3. Use 'python3' to run scripts.")
elif sys.version_info.major == 2:
    print("You are using Python 2. Use 'python' to run scripts.")
else:
    print("You are not using python that needs an update for this class")


print(sys.executable)
print(sys.prefix)
print(sys.path)
print(sys.modules)

##################################
# Use spaces instead of tabs for indentation.
my_instrictions = """
1. Use four spaces for each level of syntactically significant indenting.
2. Lines should be 79 characters in length or less.
3. Continuations of long expressions onto additional lines should be indented by four extra spaces from their normal indentation level.
4. In a file, functions and classes should be separated by two blank lines.
5. In a class, methods should be separated by one blank line.
6. In a dictionary, put no whitespace between each key and colon; put a single space before the corresponding value if it fits on the same line.
7.one—and only one—space before and after the = operator in a variable assignment.
8. For type annotations, ensure that there is no separation between the variable name and the colon, and use a space before the type information.
"""

print(my_instrictions)
# Should print the instructions without any formatting issues.
# Check if the instructions are printed correctly
