
def piso(l, c):

    lado = (l*c) +((l-1)*(c-1))
    comp = (2*(l-1))+(2*(c-1))
    return lado, comp

print(piso(3,5))
print(piso(1,1))