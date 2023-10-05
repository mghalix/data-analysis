# to iterate over each element in 2d array you need to use np.nditer(array)
import numpy as np

data = np.array([
    [172, 160, 180, 150, 190],
    [80, 70, 84, 60, 90]
])

for x in np.nditer(data):
    print(x)