import random


def update_dictionary(dct, key, default_value):
    try:
        dct[key]

    except KeyError as k:
        print("Ключ", k,  "не в ходит в существующий словарь: ", dct)
        dct_1 = {key: default_value for key in [key]}
        dct_1.update(dct)
        print("Новый словарь с ключем", k,  "и значением ",default_value,": ", dct_1)
    try:
        dct_1[key]
        key == int
        assert key == list, "Ошибка!! ключ словаря не может быть изменяемым!!"
    except AssertionError as s:
        print(s)
    else:
        print("Ключ", key, "входит в существующий словарь: ", dct)
        return key
    finally:
        print("Завершение программы")
        return key


n = [random.randint(1,100) for i in range(0,11)]
r = [random.randint(10,100) for c in range(0,11)]
dct = {k: v for k, v in zip(n,r)}
key = int(input("Введите число key: "))
default_value = int(input("Введите число default_value: "))
update_dictionary(dct, key, default_value)
