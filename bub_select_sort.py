import random
import datetime
import prettytable  # пакет для таблицы
import matplotlib.pyplot as plt  # библиотека для графика


def BubbleSort(A):  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a

def SelectSort(B):  # сортировка выбором
    for i in range(len(B) - 1):  # i - счетчик прохода по списку
        m = i  # m - номер для мин. из неотсортированных
        for j in range(i + 1, len(B)):
            if A[j] < A[m]:  # сравнение текущего элемента с текущим минимальным
                m = j
        A[i] = A[m]
        A[m] = A[i]

table_2 = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время выбором"])
x = []
y1 = []
y2 = []

for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random() * (max - min) + min)))

    # print(A)

    B = A.copy()
    # print(B)

    # BubbleSort(A)
    print("---")
    print(A)

    # QuickSort(B, 0, len(B)-1)
    print("---")
    print(B)

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2 - t1).total_seconds())
    print("Пузырьковая сортировка   " + str(N) + "   заняла   " + str((t2 - t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    SelectSort(B)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Выбором   " + str(N) + "   заняла   " + str((t4 - t3).total_seconds()) + "c")

    table_2.add_row([str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds())])
print(table_2)

plt.plot(x, y1, "C20")
plt.plot(x, y2, "C14")
plt.show()
