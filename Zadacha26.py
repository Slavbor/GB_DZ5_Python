def to_power(a, b):
    if b == 1:
        return a
    return a * to_power(a, b - 1)


n1 = int(input("Введите число: "))
n2 = int(input("Введите степень в которую возводим число: "))

print(to_power(n1, n2))
