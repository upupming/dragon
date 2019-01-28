import numpy as np

size = 9
percentage_max = 0.08
xis = np.linspace(0.1 * (1-percentage_max), 0.1 * (1+percentage_max), size)

E_n = [
 85219342462.9973,
 85219254693.4412,
 85219173007.4296,
 85219096895.7433,
 85219025899.6604,
 85218959605.1170,
 85218897637.6421,
 85218839657.9502,
 85218785358.0968
]

percentage = np.empty(size)

for i in range(len(xis)):
    percentage[i] = (E_n[i] - E_n[size//2])/E_n[size//2]*100

print(percentage)

# [ 3.71470260e-04  2.68477348e-04  1.72623153e-04  8.33101319e-05
#   0.00000000e+00 -7.77931251e-05 -1.50508665e-04 -2.18544754e-04
#  -2.82262747e-04]