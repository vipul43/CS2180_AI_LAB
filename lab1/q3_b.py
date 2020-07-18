#date_of_programming=010120
#weightage=15

import numpy as np
import matplotlib.pyplot as plt
random_integers = np.random.randint(1, 6, 100)
plt.hist(random_integers)
plt.show()