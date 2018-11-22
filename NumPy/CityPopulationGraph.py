from matplotlib import pyplot as plt
import numpy as np
x = np.load('citylist.npy')
y = np.load('poplist.npy')


plt.bar(x,y, align='center')
plt.title("City-Population Graph")
plt.xlabel("City Name")
plt.ylabel("Population in Lakh")
plt.show()