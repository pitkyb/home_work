start = True
while start == True:
   num1 = input("Введите число: ")
   num2 = set(num1)
   if len(num1) != len(num2):
      print('Да')
   elif len(num1) == len(num2):
      print('НЕТ')
      start = False
