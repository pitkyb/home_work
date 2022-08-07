numbers_list = []
while True:
   numbers = int(input("Введите числа: "))
   if numbers == 0:
      break
   else:
      numbers_list.append(numbers)
for i in numbers_list:
    x = 0
s = numbers
summ = 0
for i in range(s):
    x = int(input("введи: "))
    sum += x
print(int(summ))
# num1 = [i for i in numbers_list if i % 2 == 0]
# print("Четные числа :" + str((num1)))
# print("Сумма четных чисел: " + str(sum(num1)))
# num2 = [i for i in numbers_list if i % 2 == 1]
# print("Нечетные числа :" + str((num2)))
# print("Сумма нечетных чисел: " + str(sum(num2)))
# for i in range(numbers):
#      if (numbers > max):
#          max = numbers
# for x in range(numbers):
#     if numbers < min:
#         min = numbers
# print("Максимальное значение введеных чисел: " + str(i))
# print("Минимальное значение введеных чисел: " + str(x))
# num3 = [i for i in numbers_list if i +i]
# print(i)

