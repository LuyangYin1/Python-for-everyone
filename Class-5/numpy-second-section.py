import numpy as np
import pandas as pd

#print (np.random.random((2,2))) # float 
# print (np.random.randint(1,100,(10,10))) # int 
print (np.eye(4)) # identity matrix
print(np.empty(3)) # empty matrix


x = np.random.randint(1,100,(10,10))
print(x)
print(x[-1,1])
# # Array slicing 
# # x[start:stop:step,start:stop:step]
print(x[0:5:1,0:5:2])
print(x[0:5:1,0:5:2].shape)

# # Copy an array 
y = x[0:5,0:6].copy()
print(y)

# # Reshape an array
print(y.reshape(6,5)) # works 
print(y.reshape(3,10)) # work
#print(y.reshape(6,6)) # does not work

# # Flatten an array
print(y.flatten())

# # Transpose an array
print(y.T)

z = np.random.randint(1,100,(5,6))
# # Concatenate arrays
print(np.concatenate([y,z],axis=1))

# # Split an array
a,b = np.split(x,[5],axis=1)
print(a)
print(b)

# # vertical split
a,b = np.vsplit(x,[2])
print(a)
print(b)

# # horizontal split
a,b = np.hsplit(x,[2])
print(a)
print(b)

# # sorting arrays
rng = np.random.default_rng(seed=42)
X = rng.integers(0, 10, (4, 6))
print(X)

print(np.sort(X,axis=0)) # column wise 
print(np.sort(X,axis=1)) # row wise