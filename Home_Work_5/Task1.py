num = int(input("Введите число: "))
while num > 10:
    alfa = num // 10
    gamma = num % 10
    num //= 10
    while alfa != 0:
        if gamma == alfa % 10:
            print('ДА')
            exit()
        alfa = alfa // 10
print('НЕТ')