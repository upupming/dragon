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

# sepcies = [
#     [27645, 76556, 19650],
#     [27433, 83164, 22393],
#     [27238, 90312, 25523],
#     [27048, 98158, 29110],
#     [ 26868, 106748,  33218],
#     [ 26714, 115992,  37852],
#     [ 26560, 126215,  43205],
#     [ 26413, 137469,  49301],
#     [ 26301, 149593,  56368],
#     [ 26191, 163013,  64420],
#     [ 26104, 177659,  73650],
#     [ 25992, 194153,  84543],
#     [ 25874, 212489,  97403]
# ]

# sepcies_normal = [
#     [ 27645,  76556,  19650],
#     [ 28023,  84945,  22880],
#     [ 28406,  94254,  26641],
#     [ 28795, 104583,  31020],
#     [ 29189, 116044,  36119],
#     [ 29588, 128761,  42056],
#     [ 29993, 142871,  48969],
#     [ 30403, 158528,  57018],
#     [ 30819, 175900,  66390],
#     [ 31241, 195176,  77303],
#     [ 31668, 216565,  90010],
#     [ 32101, 240298, 104806],
#     [ 32540, 266632, 122034]
# ]

DAYS = 10
sepcies = np.array(sepcies)
sepcies_normal = np.array(sepcies_normal)

for i in range(len(sepcies)):
    fig, axes = plt.subplots(
        nrows=1, ncols=1,
        figsize=(8, 6)
    )
    axes.set_title(f'Preys percentage after {DAYS * i} days')
    # axes.set_xlabel('Percentage')
    axes.set_ylabel('Percentage/%')
    
    percentage = sepcies[i] / np.sum(sepcies[i]) * 100
    percentage_normal = sepcies_normal[i] / np.sum(sepcies_normal[i]) * 100
    ind = np.arange(len(percentage))
    width = 0.35
    bar = axes.bar(ind+width/2, percentage, width, color='SkyBlue', label='With dragon')
    bar_normal = axes.bar(ind-width/2, percentage_normal, width, color='IndianRed', label='Without dragon')
    axes.set_xticks(ind)
    axes.set_xticklabels(('Cattle', 'Sheep', 'Hare'))
    axes.set_ylim(0, 80)
    axes.legend()


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
    fig.savefig(f'./figures/percentage-{len(sepcies)}-day={DAYS * i}.svg')

# plt.show()