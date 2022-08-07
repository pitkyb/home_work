string = input("Введите строку: ")
char = input("Введите символ для поиска: ")
start = -1
count = 0

while True:
    start = string.find(char, start+1)
    if start == -1:
        break
    count += 1

print("В строке", string ,",", count , "символа" , char )
