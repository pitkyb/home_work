dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
#1
dictionary_3 = {**dictionary_1, **dictionary_2}
print(dictionary_3)
#2
dictionary_4 = dictionary_1 | dictionary_2
print(dictionary_4)
#3
dictionary_5 = {}
for key,value in dictionary_1.items():
    dictionary_5[key]= value
for key,value in dictionary_2.items():
    dictionary_5[key] = value
print(dictionary_5)
#4
dictionary_6 = dict(list(dictionary_1.items()) + list(dictionary_2.items()))
print(dictionary_6)
#5
dictionary_7 = dictionary_1.copy()
dictionary_7.update(dictionary_2)
print(dictionary_7)

