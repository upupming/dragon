import numpy as np
SPECIFIC_HEAT = [
    [1.47, 1.5, 1.63],
    [0, 0, 0],
    [0, 0, 0]
]
a = np.array([[1,2, 3]])
b = np.array([4, 5, 6])

a = np.vstack([a, b])

print(a)