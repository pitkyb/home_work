a = input("Введите два слова через пробел: ")
b = a.count(' ') + 1
while b != 2:
   print("Неправильно ввели!")
   a = input("Введите два слова через пробел: ")
   b = a.count(' ') + 1
с = a[::-1]
first_word = с[:с.find(' ')]
second_word = с[с.find(' ') + 1:]
d = (second_word + ' ' + first_word)
if b == 2:
   print(d.title())