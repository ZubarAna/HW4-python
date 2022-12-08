'''
Вычислить число pi c заданной точностью d
        *Пример:*

        - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''
'''
Формула Бэйли-Борвайна-Плаффа
Sum (1 / 16 ** x * ( 4 / (8 * x + 1) - (2 / (8 * x + 4) - 1 / (8 * x + 5) - 1 / (8 * x + 6))
'''
# import math
# from math import pi

# print(pi)

n = 1000
my_pi = sum(1/16 ** x * (4 / (8 * x + 1) - 2 / (8 * x + 4) - 1 / (8 * x + 5) - 1 / (8 * x + 6)) for x in range(n))
print(my_pi)
d = input("Введите точность d:  ")
def get_count(d):
    s = str(d)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0
print(f'Число Пи с заданной точностью {d} => {round(my_pi, get_count(d))}')
