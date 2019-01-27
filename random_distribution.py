import numpy as np
import matplotlib.pyplot as plt

# def generate_species_randomly(name, number, center_x, center_y, mean, cov):
#     """
#     Generate a group of animals
#     Using 2d Guassian distribution.
#     """
#     return np.random.multivariate_normal(mean, cov, 5000).T


if __name__ == "__main__":
    # print(generate_species_randomly(

    # ))
    common_cov = [[1000000, 0], [0, 1000000]]
    number_of_animals = 5000
    species = [[[(0, 0) for x in range(number_of_animals)] for y in range(3)] for z in range(3)]
    energy = [[ 0 for y in range(3)] for z in range(3)]
    energy = [
        [100, 200, 300],
        [400, 500, 600],
        [700, 800, 900]
    ]
    spe_name = [
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'J'],
    ]
    total = np.array(
        [
            # This is the dragon's position
            [0.0],
            [0.0]
        ]
    )
    dragon_pos = np.array([
        [0],
        [0]
    ])
    # # Number of all species
    TOTAL = number_of_animals * 9
    # klass_x = np.empty(TOTAL)
    # klass_y = np.empty(TOTAL)

    # print(species)

    for mu_x in range(3):
        for mu_y in range(3):
            # species[mu_x][mu_y] = np.random.multivariate_normal([(mu_x-1)*1000, (mu_y-1)*1000], common_cov, number_of_animals).T
            species[mu_x][mu_y] = np.random.rand(2, number_of_animals) * 2000 - 1000

            # print(species[mu_x][mu_y].shape)
            plt.scatter(species[mu_x][mu_y][0], species[mu_x][mu_y][1], linewidth='1')
            total = np.concatenate((total, species[mu_x][mu_y]), axis=1)
            
    # plt.plot(total[0], total[1])
    plt.show()
    # Delete it self
    total = np.delete(total, 0, axis=1)
    print(total.shape)

    ########## Find and eat ############
    # No reachable area
    NOT_REACHABLE = np.inf
    
    iter_times = 0
    import find
    while iter_times < TOTAL:
        iter_times += 1

        idx = find.find_nearest(total, dragon_pos)

        # Calculate klass
        index1 = idx // number_of_animals
        x = index1 // 3
        y = index1 % 3

        print(f'Nearest point {spe_name[x][y]} found', total[0][idx], total[1][idx])
        total[0][idx] = total[1][idx] = NOT_REACHABLE


    ########## Find and eat ############
