#date_of_programming=010120
#weightage=20

import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(100)
y = []
mean = 0
for i in range(1, 101):
    mean = (mean + x[i-1])/i
    y.append(mean)

plt.scatter(x, y)
plt.show()

k = []
f1_array = []
f2_array = []
for i in range(1, 101):
    f1 = (1/i)**0.5
    f2 = -(1/i)**0.5
    f1_array.append(f1)
    f2_array.append(f2)
    k.append(i)
plt.scatter(k, f1_array)
plt.show()

plt.scatter(k, f2_array)
plt.show()

