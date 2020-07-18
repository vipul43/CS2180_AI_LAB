#date_of_programming=010120
#weightage=10

import numpy as np

x_array = np.random.uniform(-1, 1, size=100)            
y_array = np.random.uniform(-1, 1, size=100)        
dataset = []                               
for i in range(100):
    dataset.append((x_array[i], y_array[i]))
pos_angle_vec = []
def angle_finder(x, y):
    given = (x, y)
    for point in dataset:
        dot = np.dot(given, point)
        if(dot>0):
            pos_angle_vec.append(point)

x = int(input())
y = int(input())
angle_finder(x, y)
def num_of_points(z):
    print("#", z, "POINTS:")
    for i in range(z):
        print(pos_angle_vec[i])
num_of_points(5)
num_of_points(10)
num_of_points(15)
