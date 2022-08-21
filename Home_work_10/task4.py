klass = 40
book_a = set(range(1,26))
book_b = set(range(26,48))
book_c = set(range(26,48))
book_a_b =set(range(1,34))
book_a_c =set(range(1,33))
book_b_c =set(range(3,35))
a_b_c = 10
a_b = (book_a | book_b) - book_a_b
a_b1 = len(a_b)
a_c = (book_a | book_c) - book_a_c
a_c1 = len(a_c)
b_c = (book_b | book_c) - book_b_c
b_c1 = len(b_c)
a1 = len(book_a) - a_b1 - a_c1 + a_b_c
b1 = len(book_b) - a_b1 - b_c1 + a_b_c
c1 = len(book_c) - a_c1 - b_c1 + a_b_c
a1_b1_c1 = a1+b1+c1
print("По одной книге прочли " + str(a1_b1_c1) + " учеников")
a_b_c1 = (a_b1 - a_b_c) + (a_c1- a_b_c) + (b_c1 - a_b_c)
print("Ровно по две книги прочли " + str(a_b_c1)+ " учеников")
print("Не прочли ни одной книги " + str(klass - a_b_c - a1_b1_c1 - a_b_c1)+ " ученика")