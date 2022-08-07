a = input('Ваедите число от 3 до 9: ')
while a.isdigit() == False:
    print("Введено не число!")
    break
if int(str(a)) < 3 or int(str(a)) > 9:
    print("Число не соответствует условию!")
else:
   for i in range(2, int(a)+2):
    for b in range(1, i):
           print(b, end="")
    for c in range(i-2, 0, -1):
           print(c, end="")
    print()

