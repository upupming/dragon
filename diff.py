import numpy as np

def get_mu_and_weight_at(age):
    mu_m = 2523.8311119211758
    lam = 19.76261573148329
    v = - 1/3
    A = 281.6 * 1000

    from sympy import symbols, exp, solve
    from sympy import Symbol

    t = symbols('t')

    temp1 = (mu_m / A) * ((1+v) ** (1 + 1/v)) * (lam - t)
    temp2 = exp(temp1)
    temp3 = v * exp(1 + v) * temp2
    temp4 = A * (1 + temp3)**(-1/v)

    y = temp4
    # y_derivative = y.diff(t)
    # 直接用算过的答案，节省时间
    y_derivative = 16475.9049382786*(1 - 0.967130801320884*exp(-0.0201655539837452*t))**2.0*exp(-0.0201655539837452*t)
    print(y_derivative)
    # 16475.9049382786*(1 - 0.967130801320884*exp(-0.0201655539837452*t))**2.0*exp(-0.0201655539837452*t)

    return (y_derivative.subs(t, age), y.subs(t, age))


if __name__ == "__main__":
    # Inflection
    print(get_mu_and_weight_at(52))