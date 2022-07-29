login = input("Введите логин: ")
if login == "hillel":
    print("Логин верный! ")
elif login != "hillel":
    print("Логин неверный! \n Попробуйте вснова")

parol = input("Введите пароль: ")
if parol == str(int(1234)):
    print("Добро пожаловать 'Hillel!'")
elif parol != 1234:
    print("Доступ запрещен! \n Забыли пароль?")