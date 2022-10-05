import numpy as np
from matplotlib import pyplot as plt

path = 0
xs = []
path_length = 10000
for i in range(path_length):
    step = np.random.choice([1,-1], p=[0.5,0.5])
    path += step
    xs.append(path)

plt.plot(xs)
plt.xlabel("steps")
plt.ylabel("path")
plt.show()