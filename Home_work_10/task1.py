newspaper = set(range(1,76))
magazine = set(range(76,103))
all_1 = (newspaper | magazine)
news_mag = set(range(1,14))
N = (all_1 - news_mag)
print('В доме живет: ' + str(len(N)) + " семей")


def get_sum(a,b,c):
    print('В доме живет: ' + str(a+b-c) + " семей")


get_sum(75,27,13)