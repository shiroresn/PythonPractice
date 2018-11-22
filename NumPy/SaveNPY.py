import numpy as np
a = np.array(['Mumbai','Pune','Nashik','Nagpur','Aurangabad'])
np.save('citylist',a)

b = np.array([121,60,30,35,20])
np.save('poplist',b)
