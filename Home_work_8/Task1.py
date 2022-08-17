n = int(input('Введите размер таблицы: '))
matrix =[[i if i %2 == 0 else j for j in range(-n, -0)]for i in range(1, n +1)]
for x in matrix:
    print(*list(map('{{:>{length}}}'.format(length=n).format, x)))

