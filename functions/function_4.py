#create a python function that accepts any number of positional as well as keyword arguments
def func(*args,**kwargs):
    print(args) #prints a tuple
    print(kwargs) # prints a dictionary