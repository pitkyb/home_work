def simpl_num(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


for number in range(1, 101):
    if simpl_num(number):
        print(number, end=' ')
