def sum_pair(num, k):
    for i in range(len(num)):
        for j in range(len(num)):
            if num[i] + num[j] == k:
                return True
    return False


num = [10, 15, 3, 7,25,2,6,10]
print(sum_pair(num, 25))
print(sum_pair(num, 29))