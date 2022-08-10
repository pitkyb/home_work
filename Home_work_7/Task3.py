a = list(input("СПИСОК 1 введите цифры через пробел: ").split())
b = list(input("СПИСОК 2 введите цифры через пробел: ").split())
e = (len(set(a) - set(b)))
print("В каждом списке по " + str(e) + " уникальных элемента")
c = []
for x in a:
    if x not in b:
        c.append(x)
print("В первом списке " + str(c))
d = []
for y in b:
    if y not in a:
        d.append(y)
print("Во втором списке " + str(d))



