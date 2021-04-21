# Создайте итерируемый объект, возвращающий генератор тридцати пяти чисел трибоначчи и выведите эти числа.
def tribonacci_generator(n):
    a, b, c = 1, 2, 3
    for i in range(n):
        a, b, c = b, c, a + b + c
        yield a


for i in tribonacci_generator(35):
    print(i)
