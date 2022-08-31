def simpl_num_gen(a,b):
    simpl_num = []
    for number in range(a, b + 1):
        for i in simpl_num:
            if number % i == 0:
                break
        else:
            simpl_num.append(number)
            yield str(number)


for x in simpl_num_gen(2,100):
    print(x,end=' ')



