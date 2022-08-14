import random
r = [random.randint(0,101) for _ in range(15)]
print(r)
c = []
d = []
x = [c.append(i)for i in r if i %2 ==0]
t =[d.append(i) for i in r if i %2 ==1]
if sum(d) > sum(c):
    print("YES")
else:
    print("NO")