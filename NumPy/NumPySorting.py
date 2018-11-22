import numpy as np

dt = np.dtype([('name','S10'),('age',int)])
a = np.array([("raju",21),("Shubham",22)],dtype = dt)

print(np.sort(a,order='name'))
