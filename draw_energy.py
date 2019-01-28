import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, HPacker, VPacker

years = 501
eaten = np.loadtxt(f'./data/eaten-{years}.txt')

cattle = eaten[:,0]
sheep = eaten[:,1]
print(cattle.shape)
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
# axes.set_ylabel('Energy/million calories', color='g')
axes.set_title('Energy expenditures of a dragon and number of preys eaten in two days changes with age')
axes.plot(np.arange(0, years), eaten[:,0] * ENERGY_PER_MASS[0][0] * MASS[0][0] + eaten[:,1] * ENERGY_PER_MASS[0][1] * MASS[0][1], 'r')



ybox1 = TextArea("Energy/million calories", textprops=dict(color="r", size=15,rotation=90,ha='left',va='bottom'))

ybox = VPacker(children=[ybox1],align="bottom", pad=0, sep=5)

anchored_ybox = AnchoredOffsetbox(loc=8, child=ybox, pad=0., frameon=False, bbox_to_anchor=(-0.08, 0.4), 
                                  bbox_transform=axes.transAxes, borderpad=0.)

axes.add_artist(anchored_ybox)


# Draw preys
ax_number = axes.twinx()
# ax_number.set_ylabel(r'Number of cattles \n \{textcolor}{}', color='g')
ax_number.plot(np.arange(0, years), eaten[:,1], label='Sheep', color='b')
ax_number.plot(np.arange(0, years), eaten[:,0], label='Cattle', color='g')
ax_number.legend(loc='upper left')

ybox2 = TextArea("Number of cattles", textprops=dict(color="g", size=15,rotation=90,ha='left',va='bottom'))
ybox = VPacker(children=[ybox2],align="bottom", pad=0, sep=5)

anchored_ybox = AnchoredOffsetbox(loc=8, child=ybox, pad=0., frameon=False, bbox_to_anchor=(1.10, 0.4), 
                                  bbox_transform=axes.transAxes, borderpad=0.)
ax_number.add_artist(anchored_ybox)
ax_number.set_ylim(0, 600)

ybox2 = TextArea("Number of sheep", textprops=dict(color="b", size=15,rotation=90,ha='left',va='bottom'))
ybox = VPacker(children=[ybox2],align="bottom", pad=0, sep=5)

anchored_ybox_sheep = AnchoredOffsetbox(loc=8, child=ybox, pad=0., frameon=False, bbox_to_anchor=(1.08, 0.4), 
                                  bbox_transform=axes.transAxes, borderpad=0.)
ax_number.add_artist(anchored_ybox_sheep)

# plt.show()
import save_fig as sf
sf.save_to_file(f'Prey intake-age={years}')