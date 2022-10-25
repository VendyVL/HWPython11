# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

import math
# import sympy
# from matplotlib import pyplot as plt

def f(x):
    a = math.cos(x)
    b = math.sin(a)
    y = -12*x**4*b - 18*x**3+5*x**2 + 10*x - 30
    return y

# l = [-3, -2, -1, 0, 1, 2, 3, 4]
# for x in l: print(f(x))

for i in range(2, 3):
    if f(i) < f(i + 0.1):
        i+=0.1
    else: print(i)

# plt.plot(f(x for x in range(-3, 3)))