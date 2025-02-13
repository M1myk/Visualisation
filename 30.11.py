#def appender():
#    lista = []
#    for i in range(2,10001):
#        lista.append(i)
#    return lista
#
#
#def wielokrotnosci(lista):
#    j = 0
#    for elements in range(2, 101):
#        while j < len(lista):
#            if lista[j] % elements == 0 and lista[j] != elements:
#                lista.pop(j)
#                continue
#            j += 1
#        j = 0
#    print(lista)
#
#
#
#
#def main():
#    new_lista = appender()
#
#    print(wielokrotnosci(new_lista))
#if __name__ == '__main__':
#    main()
def zad1_a():
    set1 = {'a','b','c'}
    set2 = {'a',1,2}
    set3 = set1 ^ set2
    print(set3)

def zad1_b():
    set1 = {'a', 'b', 'c'}
    set2 = {'a', 1, 2}
    set3 = {3,4,5}
    print('roznica ',set1-set2-set3)

def zad1_c():
    set1 = {'a', 'b', 'c'}
    set2 = {'a', 1, 2}
    set3 = {3, 4, 5}
    for element in set3:
        if element != set1 and element != set2:
            print(set1 & set2)
            break

def zad1_d():
    set1 = {'a', 'b', 'c',8,9,20}
    set2 = {'a', 1, 2}
    set3 = {3, 4, 5}
    setm = set()
    for i in range(1,26):
        setm.add(i)
        if i in set1:
            setm.remove(i)
    print(set1)
    print(setm)


def zad1_e():
    set1 = {'a', 'b', 'c', 8, 9, 20}
    set2 = {'a', 1, 2}
    set3 = {3, 4, 5}
    mset = set()
    for i in range(1, 26):
        mset.add(i)


def remove(napis,usuwany):
    if usuwany in napis:
            napis = napis.replace(usuwany,'',1)
    print(napis)

def remove_all(napis,usuwany):
    if usuwany in napis:
        napis = napis.replace(usuwany,'')
    print(napis)

def reverse(napis):
    reversed_napis = ''
    for element in reversed(napis):
        reversed_napis += element
    print(reversed_napis)


def palindrom(napis):
    wynik = True
    reversed_napis = ''
    for element in reversed(napis):
        reversed_napis += element
    if napis == reversed_napis:
        print(wynik)
    else:
        wynik = False
        print(wynik)

def mirror(napis):
    reversed_napis = ''
    for element in reversed(napis):
        reversed_napis += element
    wynik = napis + reversed_napis
    print(wynik)

def main():
    napis = input('Wpisz; ')
    usuwany = input('wpisz: ')
    remove(napis,usuwany)
    remove_all(napis,usuwany)
    reverse(napis)
    palindrom(napis)
    mirror(napis)
    #zad1_a()
    #zad1_b()
    #zad1_c()

    zad1_d()
    zad1_e()


if __name__ == '__main__':
    main()
