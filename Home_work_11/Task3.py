def simpl_num():
    num = 1
    while num < 100:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                yield num
        num += 1


def simpl_num_1(x):
    for num in x:
        if (num % 2) != 0:
            yield num


simpl_dimple = simpl_num_1(simpl_num())

for i in simpl_dimple:
    print(i, end=' ')








