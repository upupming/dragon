import numpy as np
import matplotlib.pyplot as plt

# Age 500
energy = [
    # Base: 
    62802262167.9236,
    # Grorth: 
    15169.2502730480,
    # Fly: 
    16938322.4758825,
    # Fire: 
    17015835982.26229,
    # Hurt: 
    6280226216.79237
]


# Age 50
energy = [
    # Base: 
    18147472775.3776,
    # Grorth: 
    55592228.6929860,
    # Fly: 
    1545989.43032548,
    # Fire: 
    4920744443.09981,
    # Hurt: 
    1814747277.53776
]

# Age 10

energy = [
    # Base: 
    577455216.649645,
    # Grorth: 
    13020949.4440174,
    # Fly: 
    5139.02535476123,
    # Fire: 
    197266491.39531675,
    # Hurt: 
    57745521.6649645
]

energy = [
    # Base: 
    8921857.68315007,
    # Grorth: 
    968472.753254238,
    # Fly: 
    7.19626182274897,
    # Fire: 
    8626613.288803123,
    # Hurt: 
    892185.768315007
]

AGE = 1

fig, axes = plt.subplots(
    nrows=1, ncols=1,
    figsize=(8, 6)
)
axes.set_title(f'Energy percentage when the dragon is {AGE} year old')
# axes.set_xlabel('Percentage')
axes.set_ylabel('Energy/calories')

# percentage = energy / np.sum(energy) * 100
ind = np.arange(len(energy))
width = 0.35
bar = axes.bar(ind, energy, width, color='SkyBlue')
axes.set_xticks(ind)
axes.set_xticklabels(('Basic metabolish', 'Growth', 'Flying', 'Breathing fire', 'Rcovery from trauma'))
# axes.set_ylim(0, 80)


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


# plt.show()

fig.savefig(f'./figures/percentage-energy-age={AGE}.svg')
