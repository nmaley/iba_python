# Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99). Размер списка n ввести с клавиатуры.
# Задание 3_вариант_4. Найти значение минимального элемента списка.
import random

n = int(input('Введите размер списка: \n'))
A = []
for i in range(n):
    A.append(random.randint(0, 99))
print("Элементы списка:")
for i in range(n):
    print(A[i])
minimum = A[0]
for i in range(1, len(A)):
    if A[i] < minimum:
        minimum = A[i]
print("Минимальный элемент списка:" + str(minimum))
