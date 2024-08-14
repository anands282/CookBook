#If you need to reduce the number of arguments to a function, you should use func
#tools.partial(). The partial() function allows you to assign fixed values to one or
#more of the arguments, thus reducing the number of arguments that need to be supplied
#to subsequent calls.
from functools import partial

def spam(a, b, c, d):
    print(a, b, c, d)

s1 = partial(spam,1)
s1(2,3,4)