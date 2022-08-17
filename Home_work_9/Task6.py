text = "Любіть Україну, як сонце любіть,як вітер, і трави, і води...В годину щасливу і в радості мить,любіть у годину негоди.Любіть Україну у сні й наяву,вишневу свою Україну,красу її, вічно живу і нову,і мову її солов'їну.Без неї — ніщми, як порох і дим,розвіяний в полі вітрами...Любіть Україну всім серцем своїмі всіми своїми ділами."

text3 = text.replace(","," ").replace("...", " ").replace(".", " ").replace("—", " ")
text4 = text3.split()
text5 = dict.fromkeys(text4,0)
for i in text5:
    text5[i] = text4.count(i)
print(text5)
max_value = max(text5.values())
max_element = max(text5, key=text5.get)
print("Наиболее  встречающееся слово: " + str(max_element),"встречается: " + str(max_value) + " раз")

# min_val_key = min(text5.values())
# min_element = min(text5, key=text5.get)
# print(min_val_key, min_element)

min_value = min(text5.values())
min_element = {i for i in text5 if text5[i] == min_value}
print("Слова" + str(min_element) + "втсречаются всего " +  str(min_value) + " раз")

