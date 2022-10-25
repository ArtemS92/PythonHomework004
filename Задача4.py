# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.

from sympy import *

x = Symbol('x')
k = int(input('Введите коэфициент многочлена:'))


def poly(k):
    a = randint(-10, 10)
    if k == 0:
        return a
    else:
        return a * x ** k + poly(k - 1)


# print((f'{poly(k)} = 0'))

with open('polynom.txt', 'w', encoding='utf-8') as file:
    file.write(f'{poly(k)} = 0')