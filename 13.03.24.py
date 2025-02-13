import math
import random


def zad1():
    e = math.e
    wynik1 = (math.e ** 4 - math.log2(34)) ** (1 / 3)
    print(round(wynik1, 2))

    wynik2 = (math.log(20, e) + math.cos(45) + e) ** (1 / 3)
    print(round(wynik2, 2))

    wynik3 = (math.log(20, 3) + math.sin(45) * (5 / 8)) ** (1 / 4)
    print(round(wynik3, 2))

    wynik4 = (math.log(23, 3) + (math.sin(34) + 5) ** (1 / 3))
    print(round(wynik4, 2))

    wynik5 = (math.log(32, 2) + math.pi + math.sin(56)) ** (1 / 4)
    print(round(wynik5, 2))


zad1()


def zad2():
    a = "A"
    n = int(input("wpisz wysokosc wiezy: "))
    for i in range(1, n + 1):
        print(a)
        a += "A"
    print(a)


zad2()


def zad3():
    n = int(input("wpisz wysokosc wiezy: "))
    for i in range(n):
        miejsce = " " * (n - i - 1)
        literki = "A" * (2 * i + 1)
        print(miejsce + literki + miejsce)
    print(f"\t")


zad3()


def zad4():
    lista = []
    wyniki = []
    suma = 0
    a = int(input("Wpisz n wiersz: "))
    b = int(input("Wpisz m kolumn: "))
    for i in range(1, a * b + 1):
        if i % a == 0:
            k = random.randint(-100, 100)
            print(k)
            lista.append(k)

        else:
            l = random.randint(-100, 100)
            print(l, end=' ')
            lista.append(l)

    for i, liczba in enumerate(lista, start=1):
        suma += liczba
        if i % a == 0:
            wyniki.append(suma)
            suma = 0

    if suma != 0:
        wyniki.append(suma)
    return wyniki


print(zad4())
