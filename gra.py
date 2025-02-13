"""
1) питання про вік
2) який приз ти хочеш получити
3)
"""

for i in range (1,6):
    for j in range(1,6):
        print(i*j,end = ' ')
        if j == 5:
            print(f'')

def chuj(n):
    w = '*'
    k = '          '
    while n > 0:
        print(k+w+w)
        n -= 1
        k = k[:-1]
        w = '*' + w
chuj(10)

def lista():
    lista = [6,9,2,835,83,27,1,7,26,572,721,7,94]
    min = max = lista[0]
    for elem in lista:
        if elem < min:
            min = elem
        elif elem > max:
            max = elem
    return min, max
def main():
    print(lista())
main()
