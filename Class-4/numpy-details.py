import numpy as np

# world without numpy 
a = [1,2,3,4]  # list a 
b = [ 11,12,13,14] # list b 

print (a+b)

output = []

for item1, item2 in zip(a,b):
    output.append(item1+item2)

print ("world with out numpy using forloop" , output)

# Numpy 

a = np.array([1,2,3,4], dtype=np.int64)
b = np.array([11,12,13,14], dtype=np.int64)

print ("world of numpy" , a+b)

