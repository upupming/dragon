import numpy as np
import matplotlib.pyplot as plt

# def generate_species_randomly(name, number, center_x, center_y, mean, cov):
#     """
#     Generate a group of animals
#     Using 2d Guassian distribution.
#     """
#     return np.random.multivariate_normal(mean, cov, 5000).T


# kg
MASS = [
    [753, 87.5, 3.94625],
    [0, 0, 0],
    [0, 0, 0]
]
# 只/km^2
DENSITY = [
    [3.4130, 9.4514, 0],
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
SIDE_LENGTH = 10.0
AREA = SIDE_LENGTH ** 2

if __name__ == "__main__":
    ###### Sub figures #####
    fig, axes = plt.subplots(
        nrows=1, ncols=1,
        figsize=(12, 8)
    )
    axes.set_xlabel('x/km')
    axes.set_ylabel('y/km')


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
    # HARE = spe_name[0][2]
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
            # if spe_name[mu_x][mu_y] != COW and spe_name[mu_x][mu_y] != SHEEP and spe_name[mu_x][mu_y] != HARE:
            #     continue
            if spe_name[mu_x][mu_y] != COW and spe_name[mu_x][mu_y] != SHEEP:
                continue
            if spe_name[mu_x][mu_y] == COW:
                a = axes.scatter(species[mu_x][mu_y][0], species[mu_x][mu_y][1], linewidth='1')
            elif spe_name[mu_x][mu_y] == SHEEP: 
                b = axes.scatter(species[mu_x][mu_y][0], species[mu_x][mu_y][1], linewidth='1')
            # elif spe_name[mu_x][mu_y] == HARE:
            #     c = axes.scatter(species[mu_x][mu_y][0], species[mu_x][mu_y][1], linewidth='1')
            


    # plt.plot(total[0], total[1])
    import save_fig as sf
    axes.set_title('Intial distribution of three species')
    axes.legend((a, b, c),
        #    (f'Cow \n {number_of_animals_PER_ANIMAL[0][0]}', f'Sheep \n {number_of_animals_PER_ANIMAL[0][1]}', f'Hare \n {number_of_animals_PER_ANIMAL[0][2]}'),
           (f'Cow \n {number_of_animals_PER_ANIMAL[0][0]}', f'Sheep \n {number_of_animals_PER_ANIMAL[0][1]}'),
           scatterpoints=1,
           loc='lower left',
           ncol=3,
           fontsize=8)

    sf.save_to_file('init-distribution')
    # Delete it self
    total = np.delete(total, 0, axis=1)
    print(total.shape)
    total_backup = np.array(total)

    
    # np.savetxt('./data/species.txt', species)
    np.savetxt('./data/total.txt', total)

    # exit()
    ########## Find and eat ############
    import find
    import diff
    accr = np.cumsum(number_of_animals_PER_ANIMAL)
    def get_pos(idx):
        # Calculate klass
        index1 = 0
        for i in range(len(accr)):
            if idx < accr[i]:
                index1 = i
                break
        x = index1 // 3
        y = index1 % 3
        return (x, y)
    def get_base_consumption(weight):
        """
        Weight is in kg,
        return energy in calories
        """
        m_d = weight
        V_E = 2.25
        period = 2 * 24
        V_O2 = m_d * V_E * period
        density_o2 = 1.429
        m_O2 = V_O2 * density_o2
        M_O2 = 32
        n_O2 = m_O2 / M_O2
        n_glucuse = n_O2 / 6
        energy = 277485.66 * n_glucuse
        return energy
    def get_growth_consumption(mu):
        period = 2 * 24
        dmd = mu / 365 / 24 * period
        rho_m = 1.12 * 1e3
        rho_b = 1.23 * 1e3
        r_b = 4
        r_m = 5
        coefficient_1 = rho_m + rho_b * (r_b ** 2) / (r_m ** 2)
        coefficient_2 = (r_b ** 2) / (r_b ** 2 + r_m ** 2)
        dS = dmd / coefficient_1 / coefficient_2

        E_p = 17130 * 1000 / 4.184
        E_b = 0.1 * E_p
        coefficient_3 = rho_m * (r_m ** 2) / (r_b ** 2 + r_m ** 2) * E_p
        coefficient_4 = rho_b * coefficient_2 * E_b
        E_g = (coefficient_3 + coefficient_4) * dS
        return E_g
    def get_fly_energy(weight, distance):
        """
        Weight in kg
        distance in km
        """
        m_d = weight
        # v_d is in m/s
        v_d = 5.70 * (m_d ** 0.16)
        # 转为 m
        L_d = distance * 1000
        # 得到小时时间
        temp_time = L_d / v_d / 60 / 60
        E_v = 300 / 4.184
        E_f = m_d * E_v * temp_time
        return E_f
    def get_fire_energy(weight, x, y):
        c_p = SPECIFIC_HEAT[x][y]
        m_p = MASS[x][y]
        constant = 5
        delta_T = 80 - 25
        return c_p * m_p * constant * delta_T

    def eat_when_age(age, xi):
        print(f'Age: {age}')
        dragon_pos = np.array([
            [0],
            [0]
        ])
        # Get weight and mu
        (mu, weight) = diff.get_mu_and_weight_at(age)
        print(mu, weight)
        # Recovery the eaten animals
        total = np.array(total_backup)
        ENERGY_GOT = 0
        base_cons = get_base_consumption(weight)
        print('Base consumption:', base_cons)
        growth_cons = get_growth_consumption(mu)
        print('Growth consumption:', growth_cons)
        hurt_cons = xi * base_cons
        print('Hurt consumption:', hurt_cons)
        fly_cons = 0
        fire_cos = 0
        ENERGY_CONSUMPTION = base_cons + growth_cons + hurt_cons
        
        
        # No reachable area
        NOT_REACHABLE = np.inf
        
        iter_times = 0
        eaten = 0
        eaten_each = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        while eaten < number_of_animals:
            iter_times += 1
            print('=======================')
            print(f'Iteration: {iter_times}')

            idx = find.find_nearest(total, dragon_pos)

            (x, y) = get_pos(idx)

            # if spe_name[x][y] != COW and spe_name[x][y] != SHEEP and spe_name[x][y] != HARE:
            if spe_name[x][y] != COW and spe_name[x][y] != SHEEP:
                # 不可能出现
                assert False
                # print(spe_name[x][y])
                total[0][idx] = total[1][idx] = NOT_REACHABLE
                continue

            ######### Begin eaten ##########
            eaten += 1
            eaten_each[x][y] += 1

            ENERGY_GOT += ENERGY_PER_MASS[x][y] * MASS[x][y]

            temp1 = get_fire_energy(weight, x, y)
            fire_cos += temp1
            ENERGY_CONSUMPTION += temp1
            temp2 = get_fly_energy(weight, np.linalg.norm(dragon_pos-np.array([total[:,idx]]).T))
            fly_cons += temp2
            ENERGY_CONSUMPTION += temp2

            print(f'Energy Delta this round: {ENERGY_PER_MASS[x][y] * MASS[x][y] - temp1 - temp2}')

            print(f'Nearest point {spe_name[x][y]} eaten', total[0][idx], total[1][idx])
            dragon_pos = np.array([total[:,idx]]).T
            print(dragon_pos)
            # axes.plot(total[0][idx],total[1][idx],'wo', mec='w')
            total[0][idx] = total[1][idx] = NOT_REACHABLE
            ######### End eaten ##########
            
            # if eaten % 75 == 0:
            #     # num_of_fig = int(4-eaten//75)
            #     # axes[num_of_fig].set_title(f'Eaten: {eaten}')
            #     # for i in range(len(total[0])):
            #     #     (x, y) = get_pos(i)
            #     #     if x == 0 and y == 0:
            #     #         axes[num_of_fig].sactter(total[])
            #     axes.set_title(f'Eaten total: {eaten} \n Eaten cow: {eaten_each[0][0]} \n Eaten sheep: {eaten_each[0][1]} \n Eaten hare: {eaten_each[0][2]} \n')
            #     sf.save_to_file(f'age={age}-eaten-{eaten}')
            
            if ENERGY_GOT * 0.57 * 0.7 >= ENERGY_CONSUMPTION:
                print('Success got all energy')
                print('Summary:')
                print('=== ENERGY_CONSUMPTION ===')
                print('E_n = ', ENERGY_CONSUMPTION)
                print('[')
                print('\t#Base:')
                print(f'\t{base_cons},')
                print('\t#Grorth:')
                print(f'\t{growth_cons},')
                print('\t#Fly:')
                print(f'\t{fly_cons},')
                print('\t#Fire:')
                print(f'\t{fire_cos},')
                print('\t#Hurt:')
                print(f'\t{hurt_cons}')
                print(']')
                break
            else:
                print('ENERGY_GOT * 0.57 * 0.7', ENERGY_GOT * 0.57 * 0.7)
                print('ENERGY_CONSUMPTION:', ENERGY_CONSUMPTION)
                print('Still need these:', ENERGY_CONSUMPTION - ENERGY_GOT * 0.57 * 0.7)
                print('Energy got:', ENERGY_GOT)
                print('Fire energy need:', temp1)
                print('Fly energy need:', temp2)

        print(eaten_each)
        print('################################################################')
        return eaten_each

    ########## Find and eat ############
    percentage_max = 0.08
    xis = np.linspace(0.1 * (1-percentage_max), 0.1 * (1+percentage_max), 9)
    # print(xis)
    # print(xis[1:])
    # exit()
    AGE = 280
    eaten = np.array([eat_when_age(AGE, xis[0])[0]], dtype=int)
    
    for xi in xis[1:]:
        eaten = np.vstack([eaten, eat_when_age(AGE, xi)[0]])
        print(eaten)
    # plt.close()

    # fig, axes = plt.subplots(
    #     nrows=1, ncols=1,
    #     figsize=(12, 8)
    # )
    # axes.set_xlabel('Age/year')
    # axes.set_ylabel('Energy consumption in two days/million calories')
    # np.savetxt(f'./data/eaten-{years}.txt', eaten)
    # axes.set_title('Energy consumption in two days changes with age')
    # a = axes.plot(np.arange(0, years), eaten[:,0], label=COW)
    # b = axes.plot(np.arange(0, years), eaten[:,1], label=SHEEP)
    # c = axes.plot(np.arange(0, years), eaten[:,2], label=HARE)
    # axes.legend()
    # print(eaten[:,0].shape)
    # print(eaten[:,1].shape)
    # ENERGY_PER_MASS = np.array(ENERGY_PER_MASS)/1e6
    # axes.plot(np.arange(0, years), eaten[:,0] * ENERGY_PER_MASS[0][0] * MASS[0][0] + eaten[:,1] * ENERGY_PER_MASS[0][1] * MASS[0][1])
    # sf.save_to_file(f'Prey intake-age={years}')

    # eat_when_age(10)
    # eat_when_age(20)
    # eat_when_age(30)
    # eat_when_age(40)
    # eat_when_age(50)
    # eat_when_age(60)