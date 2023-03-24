def summa(a, b):
    if b == 0:
        return a
    return a + summa(1, b - 1)


n1 = int(input("Введите число для сложения: "))
n2 = int(input("Введите число для сложения: "))

print(summa(n1, n2))
