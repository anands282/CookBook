# attaching informational metadata to functions
def add(x:int,y:int)->int:
    return x+y

print(add.__annotations__)
#/Users/anandsatheesh/CookBook/.venv/bin/python /Users/anandsatheesh/CookBook/functions/function_7.py
#{'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}