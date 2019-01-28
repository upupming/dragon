import numpy as np

size = 9
percentage_max = 0.08
xis = np.linspace(0.1 * (1-percentage_max), 0.1 * (1+percentage_max), size)

E_n = [
    85234237006.6091,
    85173675833.8670,
    85136123962.1822,
    85166734768.2697,
    85175171419.9296,
    85211229595.9737,
    85198772420.2746,
    85197085263.4944,
    85300372025.9663
]

percentage = np.empty(size)

for i in range(len(xis)):
    percentage[i] = (E_n[i] - E_n[size//2])/E_n[size//2]*100

print(percentage)

# [ 0.06934601 -0.00175589 -0.04584371 -0.00990506  0.          0.04233414
#   0.02770878  0.02572797  0.1469919 ]
