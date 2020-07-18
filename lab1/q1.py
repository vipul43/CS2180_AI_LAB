#date_of_programming=311219
#weightage=25

import numpy as np

#np.random.randint is a function to return random integers which lie in given interval
#three parameters lower bound(inclusive), upper bound(exclusive), size of output array
random_integer = np.random.randint(2, 67, size=1)  #function returns array of size given
print(random_integer)
random_integer = np.random.randint(2, 67, size=10) #function returns array of size given
print(random_integer)
random_integer = np.random.randint(2, 67)          #function returns an integer
print(random_integer)

#np.random.rand is a function to return random numbers which are uniformly distributed in interval [0, 1)
#only parameter is size of output array
random_number = np.random.rand(10)                   #function returns array of size given
print(random_number)

