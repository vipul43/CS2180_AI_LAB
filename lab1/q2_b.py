#date_of_programming=311219
#weightage=10

import numpy as np
from operator import itemgetter

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
print("dataset=", dataset)
print("distances_array=", distances_array)
distances_array = sorted(distances_array, key=itemgetter(1))
def num_of_points(z):
    print("#", z, "POINTS:")
    for i in range(z):
        tup = distances_array[i]
        index = tup[0]
        print("(x", index, ", y", index, ")=(", dataset[index-1])
num_of_points(5)
num_of_points(10)
num_of_points(15)



