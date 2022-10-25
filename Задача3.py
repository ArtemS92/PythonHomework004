# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import *

n = int(input('Введите размер списка:'))
some_list = []
for i in range(n):
    some_list.append(randint(1, 9))
print(some_list)
print(set(some_list))
new_list = []
for i in some_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)
