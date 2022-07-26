x = 987
y = 123
print(x,y)

z = x
x = y
y = z
print(x,y)

x = 987
y = 123
x,y = y,x
print(x,y)

x = 987
y = 123
x = x+y
y = x-y
x = x-y
print(x,y)