def merge(left, right):
    # Если левая последовательность пуста или = 0, то ничего не нужно для объединения,
    # и можно вернуть правую последовательность в качестве результата
    if len(left) == 0:
        return right
    # Если правая последовательность пуста или =0, то ничего не нужно для объединения,
    # и можно  вернуть левую последовательность как результат
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
    # Перебираем обе последовательности, пока все элементы результата меньше
    # длинны левого списка + длинна правого списка
    while len(result) < len(left) + len(right):
        #Если элементы левого списка меньше либо равны элементам правого списка,
        # добавить элемент левого списка в список с результатом
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
            # если что то другое то добавить элемент правого списка в список с результатом
        else:
            result.append(right[index_right])
            index_right += 1
        # Если функция дошла до конца списка, вы можете добавить,
            # оставшиеся элементы из другого списка в список с результатом,
            #и завершить цикл.
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result

__all__=['rezult','left','right']