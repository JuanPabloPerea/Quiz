#primero los convierte en string 
#luego los une
def punto1():
    return(''.join(y[-1:] for y in [ str(x) for x in [11,12,13,14,15,126]]))
print(punto1())



