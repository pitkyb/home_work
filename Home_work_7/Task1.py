num = input("Введите числа через пробел = ").split()
print(num)
k = int(input("Введие индекс элемента, который будет удален = "))
for i in range(k, len(num) - 1):
    num[i] = num[i + 1]
num.pop()
print(num)