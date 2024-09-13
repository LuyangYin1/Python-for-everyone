""" # number = 0

for x in range(1,10,1): # x =1 
    for y in range (1,10,1): # y =2 
        z = x * y  # z = 2 
        print (str(x),"*",str(y),"=",str(z))



while number < 10:
    print(number)
    number += 1 

# End less loop 
numbers = [10,20,30,40,50,60,70,80,90,100]
for number in numbers:
    while number < 50:
        print(number)
        number += 10
# Range 
for x in range(10,20,2):
    print(x)

# Break 
number = 0 
while number < 10:
    print(number)
    if number == 5:
        break
    number += 1 """

# Continue 
number = 0 
while number < 10:
    number += 1
    if number == 5:
        continue

    print(number)