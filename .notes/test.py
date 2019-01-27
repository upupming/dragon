import numpy as np

a = [
    [1, 2, 3],
    [4, 5, 6]
]

b = [
    [7, 8, 9],
    [10, 11, 12]
]

c = [
    [90, 90, 98],
    [43, 45, 43]
]

cow = np.array(a)

sheep = np.array(b)

hare = np.array(c)

total = np.append(
    np.append(cow, sheep, axis=1),
    hare,
    axis=1
)
print(total)