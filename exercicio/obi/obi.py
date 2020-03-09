

'''
n = numero de figurinhas do album
c = numero de figurinhas carimbadas,
m = numeros de figurinhas ja compradas
'''

def obi_fig(l, lc, lm):

    n=l[0]
    c=l[1]
    m=l[2]
    if 1>n or n>100:
        return
    if 1>c or c>n/2:
        return
    if 1>m or m>300:
        return

    for x in lm:
        if x<1 or x>n:
            return
    for y in lc:
        if y<1 or y>n:
            return

    cont=0
    for x in lm:
        for y in lc:
            if x==y:
                cont+=1
            print('x', x, 'y', y, 'cont', cont)
    return len(lc)-cont

result = obi_fig([10, 2, 5], [4, 7], [7, 1, 2, 8, 3])

print(result)

print(obi_fig([10, 2, 6],[4, 7], [7, 1, 8, 4, 9, 3]))

print(obi_fig([8, 4, 10], [2, 4, 6, 8], [3, 1, 1, 5, 3, 1, 7, 7, 1, 1]))