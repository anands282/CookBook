#you want to create a function that will accept only certain keyword arguments
def recv(maxsize, *, block):
    #'Receives a message'
    pass


#recv(1024, True) # TypeError
recv(1024, block=True) # Ok
