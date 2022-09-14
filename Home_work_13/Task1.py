import random
M = int(input('Введите кол-во строк:'))
N = int(input('Введите кол-во строк:'))
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random.randint(0, 101)))
        print("%3d" % b[j], end='  ')
    a.append(b)
    print('   ', sum(b))

for i in range(M):
    print("   ", end='')
print()
for i in range(M):
    s = 0
    for j in range(N):
        s += a[j][i]
    print("%4d" % s, end=' ')
print()