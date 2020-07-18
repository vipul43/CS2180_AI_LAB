#date_of_programming=311219
#weightage=20

import numpy as np

#np.random.uniform is a function to return random numbers which are uniformly distributed in given interval
#three parameters lower bound(inclusive), upper bound(exclusive), size of output array
x_array = np.random.uniform(-1, 1, size=100)        #function returns array of size given                
y_array = np.random.uniform(-1, 1, size=100)        
dataset = []                               
for i in range(100):
    dataset.append((x_array[i], y_array[i]))
    print("(x", i+1, ", y", i+1, ")=(", x_array[i], ", ", y_array[i], ")")


