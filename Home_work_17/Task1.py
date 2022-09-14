try:
    with open("input_text.txt","w") as file:
        while True:
            s = input("Введите данные для записи в файл: ")
            if s == '':
                break
            file.write(s+'\n')
except:
    print("Ошибка при работе с файлом")