# # y(1) = 30
# mu_res =  1895.4219068468078
# lam_res =  26.314724049505035

# # y(1) = 35
# mu_res =  2224.2521876543
# lam_res =  22.424392662354208

# y(1) = 40
mu_res =  2523.8311119211758
lam_res =  19.76261573148329

v = - 1/3
A = 281.6 * 1000

from sympy import symbols, exp, solve
from sympy import Symbol, init_printing, pprint

t = symbols('t')

temp1 = (mu_res / A) * ((1+v) ** (1 + 1/v)) * (lam_res - t)
temp2 = exp(temp1)
temp3 = v * exp(1 + v) * temp2
temp4 = A * (1 + temp3)**(-1/v)
init_printing(use_unicode=True)
y = temp4
y_derivative = y.diff(t)
# 直接用算过的答案，节省时间
# y_derivative = 16475.9049382786*(1 - 0.967130801320884*exp(-0.0201655539837452*t))**2.0*exp(-0.0201655539837452*t)
pprint(y)
pprint(y_derivative)