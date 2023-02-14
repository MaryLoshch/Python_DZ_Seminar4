# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random

n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))

array_n = [random.randint(0, 9) for i in range(n)]
array_m = [random.randint(0, 9) for i in range(m)]

print(array_n, array_m)


def repeated_elements(array_01, array_02):
    return sorted(set([number for number in array_01 if number in array_02]))


print(repeated_elements(array_n, array_m))