#Writing Functions That Accept Any Number of positional parameters
def avg(first, *rest):
    return (first + sum(rest))/(1+len(rest))

print(avg(1,2,3,4,5,6))