import numpy as np

a = np.array([[2,3],4,[1,7]])
print(a)

#Exmaple second

a = np.array([[1,2,3],[4,5,6]])
print (a.shape)
a.shape=(3,2)
print (a.shape)

#Example 3

b = np.arange(24)
print (b)
c = b.reshape(2,4,3)
print (c)

#Arange Example

d = np.arange(10,20,2)
print(d)

#Slice Ecample

print("Slicing Example")
h = np.arange(10)
s = slice(2,7,2)
print (a[s])

#summery Example

p = np.array([[1,2,3],[3,4,5],[4,5,6]])

print(p[...,1])
print(p[1,...])
print(p[...,1:])


#indexing

x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0,1,2], [0,1,0]]
print (y)