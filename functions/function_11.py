# In the below code the value of x used in the anonymous function will not be set to an initial value it
# can change based on reassignment
x = 10
a = lambda y: x +y
print(a(10))
x = 20
print(a(20))