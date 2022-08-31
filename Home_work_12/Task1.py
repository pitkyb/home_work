import random

def sort_matrix():
    #сортировка по возрастанию сумм
    list_sum = [sum([matrix[x][i] for x in range(M)]) for i in range(M)]
    flag = True
    while flag:
        flag = False
        for i in range(M - 1):
            j = i + 1
            if list_sum[i] > list_sum[j]:
                list_sum[i], list_sum[j] = list_sum[j], list_sum[i]
                flag = True
                for colum in range(M):
                    matrix[colum][i], matrix[colum][j] \
                        = matrix[colum][j], matrix[colum][i]
    # сортировка нечетных столбцов
    for colum1 in range(M):
        if colum1 % 2 != 0:
            flag = True
            while flag:
                flag = False
                for i in range(M - 1):
                    j = i + 1
                    if matrix[i][colum1] > matrix[j][colum1]:
                        matrix[i][colum1], matrix[j][colum1] \
                            = matrix[j][colum1], matrix[i][colum1]
                        flag = True
        # сортировка четных столбцов
        else:
            flag = True
            while flag:
                flag = False
                for i in range(M - 1):
                    j = i + 1
                    if matrix[i][colum1] < matrix[j][colum1]:
                        matrix[i][colum1], matrix[j][colum1] \
                            = matrix[j][colum1], matrix[i][colum1]
                        flag = True


M = int(input("Введите любое число не меньше 5 : "))
if M > 5:
    print("До сортировки: ")
    matrix = [[random.randint(0, 51) for i in range(M)] for j in range(M)]
    for x in matrix:
        print(*list(map('{{:>{length}}}'.format(length=M).format, x)))
    list_sum = [sum([matrix[x][i] for x in range(M)]) for i in range(M)]
    print(*list(map('{{:>{length}}}'.format(length = M).format, list_sum)))
    print()
    sort_matrix()
    print("После сортировки: ")
    for x in matrix:
        print(*list(map('{{:>{length}}}'.format(length=M).format, x)))
    list_sum = [sum([matrix[x][i] for x in range(M)]) for i in range(M)]
    print(*list(map('{{:>{length}}}'.format(length = M).format, list_sum)))
else:
    print("Введите значение больше 5 ")
