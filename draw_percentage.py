import numpy as np
import matplotlib.pyplot as plt

sepcies = [
    [3071, 8506, 2183],
    [2530,7595,2050],
    [1984, 6552, 1819],
    [1452, 5179, 1539],
    [ 891, 3871, 1224],
    [ 319, 2452,  933]
]

sepcies_normal = [
    [ 3071,  8506,  2183],
    [ 3113,  9438,  2541],
    [ 3155, 10472,  2958],
    [ 3198, 11619,  3444],
    [ 3241, 12892,  4010],
    [ 3285, 14304,  4669]
]

DAYS = 10
sepcies = np.array(sepcies)
sepcies_normal = np.array(sepcies_normal)

for i in range(len(sepcies)):
    fig, axes = plt.subplots(
        nrows=1, ncols=1,
        figsize=(8, 6)
    )
    axes.set_title(f'Species percentage after {DAYS * i} days')
    # axes.set_xlabel('Percentage')
    axes.set_ylabel('Percentage/%')
    
    percentage = sepcies[i] / np.sum(sepcies[i]) * 100
    percentage_normal = sepcies_normal[i] / np.sum(sepcies_normal[i]) * 100
    ind = np.arange(len(percentage))
    width = 0.35
    bar = axes.bar(ind+width/2, percentage, width, color='SkyBlue')
    bar_normal = axes.bar(ind-width/2, percentage_normal, width, color='IndianRed')
    axes.set_xticks(ind)
    axes.set_xticklabels(('Cow', 'Sheep', 'Hare'))
    axes.set_ylim(0, 80)


    def autolabel(rects, xpos='center'):
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
    autolabel(bar_normal, "center")
    fig.savefig(f'./figures/percentage-day={DAYS * i}.svg')

# plt.show()