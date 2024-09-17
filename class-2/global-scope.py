
def function():
    global number 
    number = 10
    print(number)
    number += 10
    print(number)   

function()
print(number)

# Scope is global 
z = 100 
def make_a_number():
    return z 

print(make_a_number())