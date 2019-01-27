import numpy as np

ENERGY = [
    [125, 118, 102],
    [0, 0, 0],
    [0, 0, 0]
]

a = np.array(ENERGY)

# Per 100g
a = a / 100

# large calorie = kilocalorie = 1,000 small calories
a = a * 1000

# 1g * 10^-3 kg/g
a = a / (10 ** -3)

print(a)