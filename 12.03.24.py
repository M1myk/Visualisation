import random
import math

a = [x**2 for x in range(-10,10)]
print(a)

def zad1():
    A = [1-x for x in range(1,11)]
    B = [4**x for x in range(8)]
    C = [x/2 for x in B]
    print(A)
    print(B)
    print(C)
zad1()

def zad2():
    lista1 = [random.randint(-100,100) for x in range(10)]
    print(lista1)
    nowa_lista = [x for x in lista1 if x % 2 == 0]
    print(nowa_lista)

zad2()

def zad3():
    produkty = { "jaja": "2 szt",
                 "jabka": "5 kg",
                 "chleb": "1 szt",
                 "paczki": "10 szt"
                }
    print(produkty.items())
    lista = [produkt for produkt, ilosc in produkty.items() if "szt" in ilosc]
    print(lista)
zad3()

def zad4():
    a = int(input("podaj wymiar A trajkata: "))
    b = int(input("podaj wymiar B trajkata: "))
    c = int(input("podaj wymiar C trajkata: "))

    if a**2+b**2 == c**2:
        return True

print(zad4())

def zad5():
    a = int(input("podaj wymiar A trapezu: "))
    b = int(input("podaj wymiar B trapezu: "))
    h = int(input("podaj wymiar wysokosc trapezu: "))

    wynik = (a+b)*h/2
    return wynik

print(zad5())

def zad6():
    ciag = []
    ilocyn = 1

    for i in range(1,11):
        a = float(input("Wpisz liczbe: "))
        ciag.append(a)
    for elem in ciag:
        ilocyn *= elem * 4
    print(ilocyn)

zad6()


def zad7():
    try:
        n = float(input("Podaj liczbę: "))
        if n < 0:
            raise ValueError("Podana liczba musi być nieujemna.")
        pierwiastek = math.sqrt(n)
        print("Pierwiastek: ", pierwiastek)
    except ValueError as e:
        print("Błąd:", e)

zad7()
