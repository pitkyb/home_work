import random
n = int(input("Введите любое число: "))
matrix = [ [random.randint(0, 101) for i in range(n)] for j in range(n)]
for x in matrix:
    print(x)
summ = sum(matrix[i][i] for i in range(n))
print("Сумма по диагонали " + str(summ))
i = n-1
summ1 = sum(matrix[j][i] for j in range(n))
print("Сумма последнего столбца " + str(summ1))




