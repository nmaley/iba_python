# 1. Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами a и b
# на квадраты с наибольшей возможной на каждом этапе стороной.
# Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.

import math

a = int(input('Enter the first side:\n'))
b = int(input('Enter the second side:\n'))


def func(m, c):
    if c == 0:
        return 0
    else:
        if m < c:
            r = m
            m = c
            c = r
        print("Длины ребер:" + str(m) + ' ' + str(c))
        print("Количество квадратов:" + str(math.floor(m / c)))
        return func(c, m % c)


func(a, b)
