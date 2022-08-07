# num = numbers_list = []
# while True:
#    numbers = int(input("Введите числа: "))
#    if numbers == 0:
#       break
#    else:
#       numbers_list.append(numbers)
#
# cnt = 0
# for i in range(numbers):
#     cnt += i
# print(cnt)

n = int(input('Введите числа: '))

suma = 0
while n > 0:
    digit = n % 10
    suma = suma + digit
    n = n // 10
print("Сумма:", suma)