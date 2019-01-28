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


fig, axes = plt.subplots(
    nrows=1, ncols=1,
    figsize=(12, 8)
)
axes.set_xlabel('Age/year')
axes.set_ylabel('Number of preys')
axes.set_title('Preys eaten changes with time')
axes.plot(np.arange(0, years), eaten[:,0], label='Cow')
axes.plot(np.arange(0, years), eaten[:,1], label='Sheep')
axes.legend()
import save_fig as sf
sf.save_to_file(f'Number of prey intake-age={years}')