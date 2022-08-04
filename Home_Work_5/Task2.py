N = int(input("Введите число: "))

for i in range(1, N+1):
    d = 1
    while i >= d:
        d = d * 10
        if((i * i % d) == i):
            print("Число" , i , i*i)