import numpy as np

size = 9
percentage_max = 0.08
xis = np.linspace(0.1 * (1-percentage_max), 0.1 * (1+percentage_max), size)

E_n = [
 84657253663.8712,
 84816187156.9210,
 85030589679.3547,
 85154927105.2999,
 85279264531.2452,
 85493671300.5446,
 85618008726.4898,
 85742346152.4350,
 85948119105.5213
]

percentage = np.empty(size)

for i in range(len(xis)):
    percentage[i] = (E_n[i] - E_n[size//2])/E_n[size//2]*100

print(percentage)

# [-0.72938113 -0.54301286 -0.29160061 -0.1458003   0.          0.25141724
#   0.39721754  0.54301784  0.78431091]