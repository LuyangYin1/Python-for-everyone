import numpy as np

a = np.array([10,23,21,2,35,4])
b = np.array([11,12,13,14])

print("*******sin of a******")
print(np.sin(a))

print("********exp of a *********")
print(np.exp(a))

#### Student need to implement log and cos funtions 
print("********log of a *********")
print(np.log(a))    # log of a

print("********acosh of a *********")
print(np.shape(a))    # sqrt of a
#########################

print("********type of a *********")
print (type(a))
print (np.shape(a))
print (a.ndim)  # number of dimensions
print (a.size)  # number of elements
print (a.dtype) # data type of the elements
print (a.itemsize) # size of each element in bytes
print (a.data) # buffer containing the actual elements
print (a.strides) # tuple of bytes to step in each dimension when traversing an array
print (a.flags) # dictionary containing information related to the memory layout of the array
print (a.real) # real part of the array