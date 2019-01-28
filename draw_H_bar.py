import numpy as np
import matplotlib.pyplot as plt

energy_H_low = np.loadtxt('./data/energy-for-humidity=low.txt') / 1e6
energy_H_high = np.loadtxt('./data/energy-for-humidity=high.txt') / 1e6

energy = [energy_H_low, energy_H_high]

H_low_eaten = np.loadtxt('./data/eaten-for-humidity=low.txt', dtype=int)
H_high_eaten = np.loadtxt('./data/eaten-for-humidity=high.txt', dtype=int)

cow = [H_low_eaten[0], H_high_eaten[0]]
sheep = [H_low_eaten[1], H_high_eaten[1]]

# print(energy_H_low, energy_H_high)
# print(cow, sheep)
# exit()

fig_energy, ax_energy = plt.subplots()
fig_eaten, ax_eaten = plt.subplots()

ax_energy.set_title(f'Energy expenditures of a dragon in two days')
ax_eaten.set_title(f'Preys eaten of a dragon in two days')
# axes.set_xlabel('Percentage')
ax_energy.set_ylabel('Energy/million calories')
ax_eaten.set_ylabel('Number')

# percentage = energy / np.sum(energy) * 100
ind = np.arange(len(energy))
width = 0.45
bar = ax_energy.bar(ind, energy, width, color='r')
ax_energy.set_xticks(ind)
ax_energy.set_xticklabels(('Low humidity', 'High humidity'))
ax_eaten.set_xticks(ind)
ax_eaten.set_xticklabels(('Low humidity', 'High humidity'))
# axes.set_ylim(0, 80)


def autolabel(rects, xpos='center', axes=ax_energy):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.54, 'left': 0.46}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        # print(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height)
        axes.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{:.2f}'.format(height), ha=ha[xpos], va='bottom')
autolabel(bar, "center")


bar_sheep = ax_eaten.bar(ind-width/2, sheep[0:2], width, color='b', label='Sheep')
bar_cow = ax_eaten.bar(ind+width/2, cow[0:2], width, color='g', label='Cattle')
ax_eaten.legend()
autolabel(bar_cow, "center", ax_eaten)
autolabel(bar_sheep, "center", ax_eaten)
# plt.show()

fig_energy.savefig(f'./figures/energy-H.svg')
fig_eaten.savefig(f'./figures/eaten-H.svg')