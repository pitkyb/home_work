numbers_list = 0
sum = 0
ser = 0
del1 = 0
del2 = 0
q = 0
qmax = 0
qmin = 0
while True:
   numbers_list = int(input("введите числа: "))
   if numbers_list == 0:
      break
   else:
      sum += numbers_list
      ser += 1
      if (numbers_list %2 == 0):
         del1 += 1
      else:
         del2 += 1
         if numbers_list > qmax:
            qmax = numbers_list
            q = q + numbers_list
         elif numbers_list < qmin:
            qmin = numbers_list
            q = q + numbers_list
print ("Сумма введенных чисел " + str(sum))
print("Среднее арифметическое чисел " + str(sum / ser))
print("Количество четных чисел : " + str(del1))
print("Количество нечетных чисел : " + str(del2))
print("Максимально число : " + str(qmax))
print("Минимально число : " + str(qmin))