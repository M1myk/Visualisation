def suma(n):
    a = 0
    b = 0
    dl_listy = len(n)
    for i in range(dl_listy):
        print(n)
        i = n.pop()


def zad1():
    lista = []
    a = 1
    while a < 11:
        lista.append(a)
        a += 1
    return lista


def minmax(n):
    min_c = n[0]
    max_c = n[0]
    for i in n:
        if min_c > i:
            min_c = i
        if max_c < i:
            max_c = i
    return min_c, max_c


def ile_ujemnych(lista):
    a = 0
    for elemenets in lista:
        if elemenets < 0:
            a += 1
    return a


def iloczyn(lista):
    a = 1
    for elemenets in lista:
        a *= elemenets
    return a


def appender(n):
    result = 0
    sign = 1
    for element in n:
        result += sign * element
        sign *= -1
    return result


def zad7(n):
    a = int(input('Dodaj liczbe: '))
    n.append(a)
    for i in range(9):
        x = int(input('Dodaj kolejna liczbe: '))
        n.append(x)
    return n


def zad8(n, limit):
    for num in range(2, limit):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            n.append(num)
    return n


def zad9():
    def a():
        lista = [1, 2, 3, 4, 5, 6, 7]
        a = lista.pop()
        lista.insert(0, a)
        b = lista.pop(1)
        lista.append(b)
        print(lista)

    a()

    def b():
        lista = [1, 2, 3, 4, 5, 6, 7]
        a = lista.pop()
        lista.insert(0, a)
        print(lista)

    b()

    def c():
        lista = [3, 1, 2, 3, 4, 5, 6, 7, 8]
        for element in lista:
            if element % 2 == 0:
                lista.pop(element)
                lista.insert(element, 0)
        print(lista)

    c()

    def e():
        lista = [1, 2, 3, 10, 5, 6, 7, 1]
        if len(lista) % 2 == 0:
            middle_index = len(lista) // 2
            middle_number = lista[middle_index]
            middle_number1 = lista[middle_index - 1]
            print(middle_number1, middle_number)
        else:
            middle_index = len(lista) // 2
            middle_number = lista[middle_index]
            print(middle_number)

    e()


def main():
    lista1 = []
    lista2 = []
    lista = [4, -20, 5, 12, -4, -5]
    # print(f'Suma jest: {ile_ujemnych(lista)}')
    # print(f'Iloczyn jest: {iloczyn(lista)}')
    # print(f'1) {zad1()}')
    # print(minmax(lista))
    # print(type(minmax(lista)))
    # suma(lista)
    # print(f'+- {appender(lista)}')
    # print(f'zad 7 {zad7(lista1)}')
    # print(f'{zad8(lista2, 10001)}')
    print(zad9())


if __name__ == '__main__':
    main()
