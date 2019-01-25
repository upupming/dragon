import numpy as np
from scipy.optimize import fsolve
# from sympy import symbols, exp, solve
# from sympy import Symbol

# mu_m, lam, t = symbols('mu_m, lam, t')
v = - 1/3
A = 281.6 * 1000

INITIAL_WEIGHT = 10
ONE_YEAR_WEIGHT = 35


def rechards_equations(A, v, mu_m, lam, t):
    temp1 = (mu_m / A) * ((1+v) ** (1 + 1/v)) * (lam - t)
    temp2 = np.exp(temp1)
    temp3 = v * np.exp(1 + v) * temp2
    temp4 = A * (1 + temp3)**(-1/v)

    return temp4

def equations(p):
    mu_m, lam = p
    return (rechards_equations(A, v, mu_m, lam, 0) - INITIAL_WEIGHT, rechards_equations(A, v, mu_m, lam, 1)-ONE_YEAR_WEIGHT)



# print(equations((mu_m, lam)))



# (15.954190216465834, -11.657871577866423)

error = 10000
best_mu_0 = 0
best_lam_0 = 0
mu_res = 0
lam_res = 0
for mu_m_0 in range(1, 1000, 10):
    for lam_0 in range(1, 1000, 10):
        print('=======')
        print('mu_m_0 = ', mu_m_0)
        print('lam_0 = ', lam_0)
        mu_m, lam = fsolve(equations, (mu_m_0, lam_0))
        temp1 = rechards_equations(A, v, mu_m, lam, 0) - INITIAL_WEIGHT
        temp2 = rechards_equations(A, v, mu_m, lam, 1) - ONE_YEAR_WEIGHT
        print(temp1)
        print(temp2)
        if np.abs(temp1) + np.abs(temp2) < error:
            error = np.abs(temp1) + np.abs(temp2)
            best_lam_0 = lam_0
            best_mu_0 = mu_m_0
            mu_res = mu_m
            lam_res = lam
        print()
    
print('best_mu_0 = ', best_mu_0)
print('best_lam_0 = ', best_lam_0)
print('error = ', error)

print('mu_res = ', mu_res)
print('lam_res = ', lam_res)