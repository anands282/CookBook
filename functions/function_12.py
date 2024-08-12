#If you want an anonymous function to capture a value at the point of definition and
#keep it, include the value as a default value, like this:
x = 10
a = lambda y, x=x: x+y
print(a(10))