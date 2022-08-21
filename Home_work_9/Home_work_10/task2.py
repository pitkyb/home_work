stamps = set(range(1,36))
icons = set(range(36,59))
stam_icon = set(range(43,59))
allstud = set(range(1,53))
a = (stamps | icons)
b = (a - stam_icon)
c = (allstud - b)
print(""
      "Не увлекаются коллекционированием: "+ str(len(c)) + " школьников")


def get_non_collection(a,b,c,d):
    print("Не увлекаются коллекционированием: " + str(d-(a+b-c)) + " школьников")


get_non_collection(35,23,16,52)
