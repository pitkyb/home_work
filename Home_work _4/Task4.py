year = input("Введите год для проверки:")
if int(year) >= 1900 and int(year) <= 1_000_000:
       print()
else:
    print('Год не отвечает условиям')

if int(year) % 4 == 0:
    print(str(year) + " год является высокосным!")
else:
    print(str(year) + " год является не высокостным!")

