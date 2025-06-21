x = 100
y = 2
print("we will be learning OR and AND operator.")
print("The power point has all the details about truth table.")
if x > 10 or y < 10:
    print("OR operator example : True")
else:
    print("False")
if (x<=100 and y>1):
    print("The and operator needs both the condition to be met")
else:
    print("condition not met.")
### Class 2 HW #### 
### Adding new code here #### 
snacks = [("bacon", 350), ("donut", 240), ("muffin", 190)]
for rank, (name, calories) in enumerate(snacks, 1):
    print(f"#{rank}: {name} has {calories} calories")
