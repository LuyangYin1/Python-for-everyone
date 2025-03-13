import numpy as np 
a = np.array([ -5, -4 ,-3,-2,-1,0,1,2,3,4,5]) 

print (a[1:3])
print (a[1:-2])
print(a[-4:3])
print(a[-5:-2])

# # omitting indices 
print(a[:3])

a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a[0,1:4])
print(a[0:2,2])
print(a[0:2,1:4])   

a = np.arange(125).reshape(25,5)
print (a)

print(a[1,-1]) # we can count backwards