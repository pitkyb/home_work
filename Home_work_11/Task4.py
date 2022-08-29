x = {}


def multiple(func):

   def wrapper(*args, **kwargs):
      y = func(*args,**kwargs)
      x = list(y)
      x.sort()
      print(" ", "_"*len(str(x[-1])), " ", "_"*13, " ", "_"*10)
      for i in range(len(x)):
         print("|", str(x[i]).ljust(len(str(x[-1])), " "), "|", "кратное 3 ".ljust(13, " ") if x[i] % 3 == 0
               else "не кратное 3".ljust(13, " "),
               "|", "парное ".ljust(10, " ") if x[i] % 2 == 0
               else "непарное".ljust(10, " "), "|")
      print(" ", "_"*len(str(x[-1])), " ", "_"*13, " ", "_"*10)
   return wrapper


@multiple
def numbers(z):
   import random
   test = set(random.randint(1,101) for i in range(z))
   return test
numbers(12)









