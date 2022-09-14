from random import randint
#подключаем модуль random
def quicksort(array):
    # Если длинна последовательности меньше двух элементов,
    # нужно вернуть её как результат функции
    if len(array) < 2:
        return array
# 'low''same''high' задаем как пустые списки
    low, same, high = [], [], []

    # Выберите середину последовательности `pivot` случайным образом
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
         # Элементы, которые меньше, чем `pivot`, переходят в последовательность `low`.
        if item < pivot:
            low.append(item)
            #Элементы, которые равны `pivot` переходят к последовательности ` same`.
        elif item == pivot:
            same.append(item)
            #Элементы которые превышают`pivot` переходят в последовательность` high`.
        elif item > pivot:
            high.append(item)

    # Окончательный результат объединяет отсортированные `low`'same''high' последовательности
    return quicksort(low) + same + quicksort(high)
__all__=[' low', 'same', 'high','pivot']