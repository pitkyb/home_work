numbers_list = []
while True:
   numbers = int(input("Введите числа: "))
   if numbers == 0:
      break
   else:
      numbers_list.append(numbers)
print("Максимальное значение введеных чисел: " + str(max(numbers_list)))
print("Минимальное значение введеных чисел: " + str(min(numbers_list)))
print("Сумма всех введеных чисел: " + str((sum(numbers_list))))
print("Среднее арифметическое введеных чисел: " + str(int(sum(numbers_list) / len(numbers_list))))
num = [i for i in numbers_list if i % 2 == 0]
print("Четные числа :" + str((num)))
print("Сумма четных чисел: " + str(sum(num)))
num2 = [i for i in numbers_list if i % 2 == 1]
print("Нечетные числа :" + str((num2)))
print("Сумма нечетных чисел: " + str(sum(num2)))