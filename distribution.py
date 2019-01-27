import csv
import numpy as np

############## Get Species Dictionary #################

filename = './data/alltrain.csv'

species = {}
LONG_KEY = 'long'
LAT_KEY = 'lat'

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
        # elif line_count == 100:
        #     print(species)
        #     exit()
        else:
            if species.get(row[0]):
                # 二次以上遇到，增加物种
                species[row[0]][LONG_KEY] = np.append(species[row[0]][LONG_KEY], row[1])
                species[row[0]][LAT_KEY] = np.append(species[row[0]][LAT_KEY], row[2])
            else:
                # 第一次遇到，创建新物种
                species[row[0]] = {
                    LONG_KEY: np.array([row[1]]),
                    LAT_KEY: np.array([row[2]])
                }
            # print(f'\tSepcies {row[0]} lives at ({row[1]}, {row[2]}).')
            line_count += 1
    print(f'Processed {line_count} lines.')

# print(species)
############## Get Species Dictionary #################



############## Show species in a map ##################
import matplotlib.pyplot as plt

for animal in species.keys():
    print(species[animal][LONG_KEY])
    plt.scatter(species[animal][LONG_KEY], species[animal][LAT_KEY])
plt.show()
############## Show species in a map ##################