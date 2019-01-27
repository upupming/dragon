import numpy as np
import csv

# species = [2524, 7655, 2098]
# species = [252, 765, 209]

species_by_state = np.array([
    # WA
    [2.1, 14.2],
    # NT
    [2.2, 0],
    # Qld
    [11.1, 2.1],
    # NSW
    [5.3, 26.9],
    # Vic
    [3.6, 15.2],
    # Tas
    [0.7, 2.1],
    # SA
    [1.1, 11.5],
]) * 10

species_by_state = np.array(species_by_state, dtype=int)

# latitudes = [-35.633, -20.683]
# longitudes  = [120.15, 140.633]

longitudes_by_state = np.array([
    # WA
    [110.98415, 125.241595],
    # NT
    [126.7195, 138.629683],
    # Qld
    [138.629683, 154.625841],
    # NSW
    [141.324688, 156.886167],
    # Vic
    [141.019693, 154.799712],
    # Tas
    [142.628722, 150.626801],
    # SA
    [126.893372, 142.367915]
])
latitudes_by_state = np.array([
    # WA
    [-37.392651, -12.355187],
    # NT
    [-25.65634, -10.094861],
    # Qld
    [-28.699087, -9.834054],
    # NSW
    [-36.349424, -27.65586],
    # Vic
    [-39.739914, -34.43684],
    # Tas
    [-44.260567, -39.2183],
    # SA
    [-39.044428, -26.525696]
])

NUM_OF_STATES = len(latitudes_by_state)



with open('./data/init-dis.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['species', 'dd long', 'dd lat'])


    for i in range(NUM_OF_STATES):
        cow = np.random.rand(2, species_by_state[i][0])
        cow[0] = cow[0] * (longitudes_by_state[i][1]-longitudes_by_state[i][0]) + longitudes_by_state[i][0]
        cow[1] = cow[1] * (latitudes_by_state[i][1]-latitudes_by_state[i][0]) + latitudes_by_state[i][0]

        for j in range(species_by_state[i][0]):
            csv_writer.writerow(['cow', cow[0][j], cow[1][j]])

        sheep = np.random.rand(2, species_by_state[i][1])
        sheep[0] = sheep[0] * (longitudes_by_state[i][1]-longitudes_by_state[i][0]) + longitudes_by_state[i][0]
        sheep[1] = sheep[1] * (latitudes_by_state[i][1]-latitudes_by_state[i][0]) + latitudes_by_state[i][0]

        for j in range(species_by_state[i][1]):
            csv_writer.writerow(['sheep', sheep[0][j], sheep[1][j]])

