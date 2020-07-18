#date_of_programming=311219
#weightage=15

import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt
##question 2_a plot
x_array = np.random.uniform(-1, 1, size=100)               
y_array = np.random.uniform(-1, 1, size=100)        
dataset = []                               
for i in range(100):
    dataset.append((x_array[i], y_array[i]))
plt.scatter(x_array, y_array, color='red')
plt.show()
##question 2_b plot
x_array = np.random.uniform(-1, 1, size=100)              
y_array = np.random.uniform(-1, 1, size=100)        
dataset = []                               
for i in range(100):
    dataset.append((x_array[i], y_array[i]))
distances_array = []
def distance_finder(x, y):
    temp = 1
    for point in dataset:
        distance = ((point[0]-x)**2+(point[1]-y)**2)**0.5
        distances_array.append((temp, distance))
        temp = temp + 1
x = int(input())
y = int(input())
distance_finder(x, y)
# print("dataset=", dataset)
# print("distances_array=", distances_array)
distances_array = sorted(distances_array, key=itemgetter(1))
x_coord = []
y_coord = []
def num_of_points(z):
    for i in range(z):
        tup = distances_array[i]
        index = tup[0]
        ele = dataset[index-1]
        x_coord.append(ele[0])
        y_coord.append(ele[1])
num_of_points(15)

plt.scatter(x_coord, y_coord, color='blue')
plt.show()
