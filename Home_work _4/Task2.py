class1 = input("Введите количество учеников в 1 классе:")
class2 = input("Введите количество учеников в 2 классе:")
class3 = input("Введите количество учеников в 3 классе:")
desk_stud = 2

desk1 = int(class1) // (desk_stud)+ int(class1) % (desk_stud)
desk2 = int(class2) // (desk_stud)+ int(class2) % (desk_stud)
desk3 = int(class3) // (desk_stud)+ int(class3) % (desk_stud)

print ("Всего в 3 классах нужно закупить: " + str(int(desk1) + int(desk2) + int(desk3)) + " парт")

