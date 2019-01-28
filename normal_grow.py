import numpy as np

# origin = [3071, 8506, 2183]
origin = [27645, 76556, 19650]

# import eat3spe as grow

res = np.array([origin])
now = origin
DAYS = 10

def get_reproduction_res(index, now, period):
    """
    Index: 0-cow,1-sheep,2-hare
    period: in days
    """
    per_day_animal = np.array([0.5, 4, 6]) / 365

    return int(now + now * per_day_animal[index] * period)

for i in range(12):
    temp0 = get_reproduction_res(0, now[0], 10)
    temp1 = get_reproduction_res(1, now[1], 10)
    temp2 = get_reproduction_res(2, now[2], 10)
    now = np.array([temp0, temp1, temp2])

    res = np.vstack([res, now])

print(res)