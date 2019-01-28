import numpy as np
import matplotlib.pyplot as plt

years = 501
eaten = np.loadtxt(f'./data/eaten-{years}.txt')

cow = eaten[:,0]
sheep = eaten[:,1]
print(cow.shape)
print(sheep.shape)

# kg/只
MASS = [
    [753, 87.5, 3.94625],
    [0, 0, 0],
    [0, 0, 0]
]
# calorie/kg
# 所有能量都按照 million 计算
ENERGY_PER_MASS = np.array([
    [1250000, 1180000, 1020000],
    [0, 0, 0],
    [0, 0, 0]
]) / 1e6

# 只/km^2
DENSITY = [
    [3.4130, 9.4514, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def cal_v():
    constant = 365
    v_cow = 1 * ENERGY_PER_MASS[0][0] * MASS[0][0] * DENSITY[0][0] / constant
    v_sheep = 8 * ENERGY_PER_MASS[0][1] * MASS[0][1] * DENSITY[0][1] / constant
    return (v_cow, v_sheep)


energy_per_two_day = cow * ENERGY_PER_MASS[0][0] * MASS[0][0] + sheep * ENERGY_PER_MASS[0][1] * MASS[0][1]

(v_cow, v_sheep) = cal_v()
s_area = energy_per_two_day / (v_cow + v_sheep) * 3

fig, axes = plt.subplots(
    nrows=1, ncols=1,
    figsize=(12, 8)
)
axes.set_xlabel('Age/year')
axes.set_ylabel(r'Area/$km^2$')
axes.set_title('Minimum area required to support the three dragons')
axes.plot(np.arange(years), s_area, c='pink')
import save_fig as sf
sf.save_to_file(f'area-{years}')