# TODO: Create a 2-dimensional matrix with filled with ones of size 1000 x 1000.
# Afterward, flatten the matrix to a vector and loop over the vector.
# In each loop iteration, add a random number between 1 and 10000.
# TODO: Now, do the same with a list of the same size and fill it with random numbers. 
# Then, sort the list as you have done with the Numpy vector before.
# You can use the `time` module to compare the runtime of both approaches.
import time
import numpy as np
import random as rd

x = np.ones((1000,1000))
x = x.flatten()

start = time.time()

for i in range(len(x)):
    x[i] += np.random.randint(1, 10000)
x.sort()

end = time.time()
print("Numpy slow:", end - start) # time in seconds

z = np.ones((1000,1000))
z = z.flatten()

start = time.time()

z += np.random.randint(1, 10000)
z.sort()

end = time.time()
print("Numpy fast:", end - start) # time in seconds


start = time.time()
y = []
for i in range(1000000):        
    y.append(rd.randint(1, 10000))
y.sort()

end = time.time()
print("List:", end - start) # time in seconds

