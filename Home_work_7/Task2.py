a = list(input("Введите числа: "))
k = int(input("Введите число k: "))
C = input("Введите значение с: ")
a.append(1)
for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = C
print(a)