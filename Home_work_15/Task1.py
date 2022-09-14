def testInput(x):
    try:
        x = int(x)
        return True
    except:
        return False
a = input('Введите первое значение: ')
b = input('Введите второе значение: ')

if testInput(a) and testInput(b):
    print(int(a) + int(b))
else:
    print(a + b)
