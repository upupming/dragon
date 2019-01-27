import numpy as np
import matplotlib.pyplot as plt

# def generate_species_randomly(name, number, center_x, center_y, mean, cov):
#     """
#     Generate a group of animals
#     Using 2d Guassian distribution.
#     """
#     return np.random.multivariate_normal(mean, cov, 5000).T

exp  = 'distribution'
# kg
MASS = [
    [753, 87.5, 3.94625],
    [0, 0, 0],
    [0, 0, 0]
]
# 只/km^2
DENSITY = [
    [3.4130, 9.4514, 2.426],
    [0, 0, 0],
    [0, 0, 0]
]
# calorie/kg
ENERGY_PER_MASS = [
    [1250000, 1180000, 1020000],
    [0, 0, 0],
    [0, 0, 0]
]

# 卡路里 / 千克 / 度
SPECIFIC_HEAT = [
    [351.33843212, 358.50860421, 389.5793499],
    [0, 0, 0],
    [0, 0, 0]
]

# 边长, km
SIDE_LENGTH = 30.0
AREA = SIDE_LENGTH ** 2

if __name__ == "__main__":

    # print(generate_species_randomly(

    # ))
    # common_cov = [[1000000, 0], [0, 1000000]]
    number_of_animals_PER_ANIMAL = np.array(AREA * np.array(DENSITY), dtype=int)
    # print(number_of_animals_PER_ANIMAL)
    number_of_animals = np.sum(number_of_animals_PER_ANIMAL)
    # 3 行 3 列，每个元素都是一个二维向量，两行表示 x, y 坐标，每行表示坐标位置
    species = [[[np.empty((2, number_of_animals_PER_ANIMAL[x][y]))] for y in range(3)] for x in range(3)]
    spe_name = [
        ['Cow', 'Sheep', 'Hare'],
        ['D', 'E', 'F'],
        ['G', 'H', 'J'],
    ]
    COW = spe_name[0][0]
    SHEEP = spe_name[0][1]
    HARE = spe_name[0][2]
    total = np.array(
        [
            # This is the dragon's position
            [0.0],
            [0.0]
        ]
    )
    # # Number of all species
    # TOTAL = number_of_animals
    # klass_x = np.empty(TOTAL)
    # klass_y = np.empty(TOTAL)

    # print(species)
    a = b = c = 0
    for mu_x in range(3):
        for mu_y in range(3):
            # species[mu_x][mu_y] = np.random.multivariate_normal([(mu_x-1)*1000, (mu_y-1)*1000], common_cov, number_of_animals).T
            species[mu_x][mu_y] = np.random.rand(2, number_of_animals_PER_ANIMAL[mu_x][mu_y]) * SIDE_LENGTH

            # print(species[mu_x][mu_y].shape)
            total = np.concatenate((total, species[mu_x][mu_y]), axis=1)

    # Delete it self
    total = np.delete(total, 0, axis=1)
    np.savetxt(f'./data/total-{exp}', total)
    np.savetxt(f'./data/species-cow-{exp}', species[0][0])
    np.savetxt(f'./data/species-sheep-{exp}', species[0][1])
    np.savetxt(f'./data/species-hare-{exp}', species[0][2])