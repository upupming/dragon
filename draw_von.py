import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import save_fig as sf

v = - 1/3
A = 281.6 * 1000
    

def rechards_equations(A, v, mu_m, lam, t):
    temp1 = (mu_m / A) * ((1+v) ** (1 + 1/v)) * (lam - t)
    temp2 = np.exp(temp1)
    # print(temp2)
    temp3 = v * np.exp(1 + v) * temp2
    temp4 = A * (1 + temp3)**(-1/v)

    return temp4

def plt_point(x, y, color='pink'):
    plt.annotate(r'(%3.2f, %3.2f)' % (x, y[x]), xy=(x * 1.03, y[x] * 0.97), textcoords='data')
    plt.scatter(x, y[x], linewidth=1, color=color)

def plt_point_move(x, y):
    str = r'(%3.2f, %3.2f)' % (x, y[x])
    plt.annotate(str, xy=(x * 30, y[x] * 200), textcoords='data')
    plt.scatter(x, y[x], linewidth=1, color='pink')

def draw_40():
    y_1 = 40
    (mu_m, lam) = (2523.8311119211758, 19.76261573148329)

    rcParams['figure.figsize'] = 12, 8

    t = np.linspace(0, 300, 300)
    
    tangent_y = mu_m * (t - lam)
    plt.plot(t[20:len(t)//2], tangent_y[20:len(t)//2], color='cyan')

    y = np.empty(t.shape)
    for i in range(len(t)):
        y[i] = rechards_equations(A, v, mu_m, lam, t[i])

    # Draw flection - 中心速率最大点
    idx = np.argwhere(np.diff(np.sign(y-tangent_y))).flatten()
    # plt.plot(t[idx], y[idx], 'ro')
    plt_point(idx[0], y, color='r')
    # Draw upper bound - 与 y = A 交点
    lam_upper = int((A / mu_m + lam))
    plt_point(lam_upper, y, color='r')
    # plt.annotate(r'(%3.2f, %3.2f)' % (lam_upper, y[lam_upper]), xy=(lam_upper * 1.03, y[lam_upper] * 0.97), textcoords='data')
    # plt.scatter(lam_upper, y[lam_upper], linewidth=1, color='r')
    plt.axvline(x=lam_upper, linewidth=2, color='r', linestyle='--')
    # plt.annotate(f'$x$ = {"{:.2f}".format(lam_upper)}', xy=(lam_upper * 1.05, y[lam_upper//1] * 0.99), textcoords='data')
    # Draw lower bound
    lam_lower = int(0 / mu_m + lam)
    plt.annotate(r'(%3.2f, %3.2f)' % (lam_lower, y[lam_lower]), xy=(lam_lower * 1.3, y[lam_lower] * 0.8), textcoords='data')
    plt.scatter(lam_lower, y[lam_lower], linewidth=1, color='r')
    plt.axvline(x=lam_lower, linewidth=2, color='r', linestyle='--')
    # plt.annotate(f'x = {"{:.2f}".format(lam_lower)}', xy=(lam_lower * 2, 0), textcoords='data')

    plt.plot(t, y, linewidth=4)
    plt.title(f'Growth Curve of Dragon \n $A$ = {"{:.2f}".format(A)}, $y(1)$ = {"{:.2f}".format(y_1)} \n $\mu_m$ = {"{:.2f}".format(mu_m)}, $\lambda$ = {"{:.2f}".format(lam)}')
    # plt.annotate('(%3.2f, %3.2f)' % (150, y[150]), xy=(150, y[150]), textcoords='data')
    # plt.scatter(150, y[150], linewidth=1, color='y')
    plt.annotate(r'(%3.2f, %3.2f)' % (0, y[0]), xy=(-15, -12000), textcoords='data')
    plt.scatter(0, y[0], linewidth=1, color='pink')
    plt.annotate(r'(%3.2f, %3.2f)' % (1, y[1]), xy=(-15, 8000), textcoords='data')
    plt.scatter(1, y[1], linewidth=1, color='pink')
    # plt_point(0, y)
    # plt_point_move(1, y)
    # plt_point(30, y)
    # plt_point(60, y)
    # plt_point(90, y)
    # plt_point(100, y)
    # plt_point(125, y)
    # plt_point(150, y)
    # plt_point(280, y)

    # Draw stages
    plt.annotate('Initial growth stage', xy=(35, 20000), textcoords='data', color='b')
    plt.annotate('Exponential growth stage', xy=(64, 100000), textcoords='data', color='b')
    plt.annotate('Steady growth stage', xy=(150, 230000), textcoords='data', color='b')

    plt.annotate(f'y = {A}', xy=(50, A * 0.95), textcoords='data')
    plt.axhline(y=A, linewidth=2, color='r', linestyle='--')
    # plt.axvline(x=280, linewidth=2, color='r', linestyle='--')
    # plt.annotate(f'x = {280}', xy=(280 * 1.02, 10), textcoords='data')
    
    plt.xlabel('Time $t$/year')
    plt.ylabel('Weight of the dragon $y$/kg')
    # plt.show()
    sf.save_to_file(f'Growth-curve-y_1={y_1}')
    plt.close()

def draw_30():
    y_1 = 30
    (mu_m, lam) = (1895.4219068468078, 26.314724049505035)

    rcParams['figure.figsize'] = 12, 8

    t = np.linspace(0, 380, 380)
    # draw_tangent(lam, mu_m, t)

    y = np.empty(t.shape)
    for i in range(len(t)):
        y[i] = rechards_equations(A, v, mu_m, lam, t[i])

    plt.plot(t, y)
    plt.title(f'Growth curve of Dragon \n $A$ = {"{:.2f}".format(A)}, $y(1)$ = {"{:.2f}".format(y_1)} \n $\mu_m$ = {"{:.2f}".format(mu_m)}, $\lambda$ = {"{:.2f}".format(lam)}')
    # plt.annotate('(%3.2f, %3.2f)' % (150, y[150]), xy=(150, y[150]), textcoords='data')
    # plt.scatter(150, y[150], linewidth=1, color='y')
    plt_point(0, y)
    plt_point_move(1, y)
    # plt_point(30, y)
    # plt_point(60, y)
    # plt_point(90, y)
    # plt_point(100, y)
    # plt_point(125, y)
    # plt_point(150, y)
    # plt_point(280, y)
    # plt_point(350, y)

    plt.annotate(f'y = {A}', xy=(10, A * 0.95), textcoords='data')
    plt.axhline(y=A, linewidth=2, color='r', linestyle='--')
    plt.axvline(x=350, linewidth=2, color='r', linestyle='--')
    plt.annotate(f'x = {350}', xy=(350 * 1.02, 10), textcoords='data')
    
    plt.xlabel('Time $t$/year')
    plt.ylabel('Weight of the dragon $y$/kg')
    # plt.show()
    sf.save_to_file(f'Growth-curve-y_1={y_1}')
    plt.close()

def draw_35():
    y_1 = 35
    (mu_m, lam) = (2224.2521876543, 22.424392662354208)

    rcParams['figure.figsize'] = 12, 8

    t = np.linspace(0, 380, 380)
    
    tangent_y = mu_m * (t - lam)
    plt.plot(t[20:len(t)//2], tangent_y[20:len(t)//2], color='cyan')

    y = np.empty(t.shape)
    for i in range(len(t)):
        y[i] = rechards_equations(A, v, mu_m, lam, t[i])

    plt.plot(t, y)

    # Draw flection - 中心速率最大点
    idx = np.argwhere(np.diff(np.sign(y-tangent_y))).flatten()
    plt.plot(t[idx], y[idx], 'ro')
    plt_point(idx[0], y)
    # Draw upper bound - 与 y = A 交点
    lam_upper = A / mu_m + lam
    plt.plot(lam_upper, A, 'ro')
    plt.axvline(x=lam_upper, linewidth=2, color='r', linestyle='--')
    plt.annotate(f'$x$ = {"{:.2f}".format(lam_upper)}', xy=(lam_upper * 1.02, 10), textcoords='data')
    # Draw lower bound
    lam_lower = 0 / mu_m + lam
    plt.plot(lam_lower, 0, 'ro')
    plt.axvline(x=lam_lower, linewidth=2, color='r', linestyle='--')
    plt.annotate(f'x = {"{:.2f}".format(lam_lower)}', xy=(lam_lower * 1.2, 100000), textcoords='data')

    plt.title(f'Growth curve of Dragon \n $A$ = {"{:.2f}".format(A)}, $y(1)$ = {"{:.2f}".format(y_1)} \n $\mu_m$ = {"{:.2f}".format(mu_m)}, $\lambda$ = {"{:.2f}".format(lam)}')
    # plt.annotate('(%3.2f, %3.2f)' % (150, y[150]), xy=(150, y[150]), textcoords='data')
    # plt.scatter(150, y[150], linewidth=1, color='y')
    plt_point(0, y)
    plt_point_move(1, y)
    # plt_point(30, y)
    # plt_point(60, y)
    # plt_point(90, y)
    # plt_point(100, y)
    # plt_point(125, y)
    # plt_point(150, y)
    # plt_point(280, y)
    # plt_point(350, y)

    plt.annotate(f'y = {A}', xy=(60, A * 0.95), textcoords='data')
    plt.axhline(y=A, linewidth=2, color='r', linestyle='--')
    plt.axvline(x=350, linewidth=2, color='r', linestyle='--')
    plt.annotate(f'x = {350}', xy=(350 * 1.02, 10), textcoords='data')
    
    plt.xlabel('Time $t$/year')
    plt.ylabel('Weight of the dragon $y$/kg')
    plt.show()
    # sf.save_to_file(f'Growth-curve-y_1={y_1}')
    plt.close()


if __name__ == "__main__":
    draw_40()
    # draw_30()
    # draw_35()