import math


def zad1():

    print(f"ZADANIE 1\n")
    a = 0
    for i in range(2, 101):
        if i % 2 == 0:
            a += i
    print(f'Zadanie (a): {a}')

    wynik = 1
    for i in range(1, 101):
        wynik = wynik + (i ** 2)
    print(f'Zadanie (b): {wynik}')

    a = 0
    for i in range(1, 64):
        wynik = a + (2 ** i)
    print((f'Zadanie (c): {wynik}'))
    print(f'\n(d)\n')
    a = int(input('Podaj liczbe "a": '))
    b = int(input('Podaj liczbe "b": '))

    suma = 0

    if a > b:
        suma = 0
    else:
        for i in range(a + 1, b):
            if i % 2 != 0:
                suma += i
    print(f'Suma wszystkich liczb nieparzystych pimiedzy {a} i {b} = {suma}')


zad1()


def zad2():
    print(f'\nZADANIE 2\n')

    n = int(input('(a) Podaj ilosc liczb: '))  # A
    suma = 0
    for i in range(1, n + 1):
        a = int(input(f'Podaj liczbe {i}: '))
        suma += a
    print(f'Suma = {suma}')

    n = int(input('(b) Podaj ilosc liczb: '))  # B
    wynik = 1
    for i in range(1, n + 1):
        a = int(input(f'Podaj liczbe {i}: '))
        wynik = wynik * a
    print(f'Iloczyn = {wynik}')

    n = int(input('(c) Podaj ilosc liczb: '))  # C
    suma = 0
    for i in range(1, n + 1):
        a = abs(int(input(f'Podaj liczbe {i}: ')))
        suma = suma + a
    print((f'Suma mod = {suma}'))

    n = int(input('(d) Podaj ilosc liczb: '))  # D
    suma = 0

    for i in range(1, n + 1):
        a = abs(int(input(f'Podaj liczbe {i}: ')))
        sqrt = math.sqrt(a)
        suma = suma + sqrt
    print((f'Suma sqrt + mod = {suma}'))

    n = int(input('(b) Podaj ilosc liczb: '))  # E
    wynik = 1
    for i in range(1, n + 1):
        a = int(input(f'Podaj liczbe {i}: '))
        wynik = abs(wynik * a)
    print(f'Iloczyn = {wynik}')

    n = int(input("(f) Podaj ilosc liczb: ")) # F
    dob = 0
    for i in range(0, n):
        a = float(input(f'Podaj liczbe {i}: '))
        b = a ** 2
        dob = dob + b
    print(f'Iloczyn = {dob}')

    n = int(input("(h) Podaj ilosc : "))  # H
    suma = 0
    for i in range(1,n+1):
        a = int(input(f'Podaj liczbe {i}: '))
        suma +=(-1)**(i+1)*a
    print(suma)

    n = int(input("(i) Podaj ilosc : "))  # I
    suma = 0
    for i in range(1,n+1):
        a = int(input(f'Podaj liczbe {i}: '))
        factorial=math.factorial(n)
        suma +=((-1) ** n) * (a / factorial)
    print(f'Wynik = {suma}')
zad2()

def zad3():
    print(f'\nZADANIE 3\n')
    n = int(input("Podaj ilość liczb: "))
    list = []

    for i in range(n):
        a = int(input("Podaj kolejną liczbę: "))
        list.append(a)

    # Przesuń elementy ciągu w odpowiedniej kolejności
    zm_liczby = list[1:] + [list[0]]

    # Wypisz liczby w nowej kolejności
    for number in zm_liczby:
        print(number)

zad3()

def zad4():
    print(f'\nZADANIE 4\n')
    zdanie='Mężny bądz, chroń pułk twój i sześć flag.'
    ilosc = 64
    for i in range(ilosc):
        print(zdanie)

zad4()
