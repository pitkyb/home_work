import random
n = 21
test = [random.randint(1,100) for j in range(n) for i in range(n)]
c = dict(zip(range(n),test))
print(c)

result = 1
for key in c:
    result = result * c[key]
print("Результат умножения всех чисел: " + str(result))
