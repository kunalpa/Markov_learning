import numpy as np
from matplotlib import pyplot as plt

p_values = [[.1,.9],[.2,.8],[.3,.7],[.4,.6],[.5,.5],[.9,.1],[.8,.2],[.7,.3],[.6,.4]]
for ps in p_values:
    path = 0
    xs = []
    path_length = 1000
    for i in range(path_length):
        step = np.random.choice([1,-1], p=ps)
        path += step
        xs.append(path)

    plt.plot(xs)
plt.show()