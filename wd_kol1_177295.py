import math
import random



e = math.e
wynik = 0
wynik11 = 0
for x in range(30,61):

    wynik += (e**(math.sin(x))+math.log(32,3))**(1/4)

print(round(wynik,2))




def zad2():
    lista = []
    roznica = []
    try:
        min = int(input("Wpisz min znaczenie: "))
        max = int(input("Wpisz max znaczenie: "))
        ile = int(input("Wpisz ilosc generowan: "))

        for i in range(1,ile+1):
            a = random.randint(min,max)
            lista.append(a)
        print(lista)


        for elem in lista:
            for elem1 in lista:
                roz = elem - elem1
                roznica.append(roz)
        print(roznica)
    except:
        ValueError
        print("Znaczenie musi byc liczba!")

zad2()


def zad3():
    a = open("../Visualisation/liczby.txt")
    m = [a.read()]
    print(m)
    lista = [x for x in a.read()]
    lista1 = []
    suma = 0
    wynik = []
    for elem in lista:
        if elem.isnumeric():
            lista1.append(int(elem))
    print(lista1)

    for index, element in enumerate(lista1):
        suma += element
        if (index + 1) % 5 == 0:
            wynik.append(suma)
            suma = 0
    print(suma)
    print(wynik)







zad3()


def zad4():

    try:
        a = int(input("Wpisz bok: "))
        h = int(input("Wpisz wysokosc: "))
        podstawa = a*a
        bok = a*h
        wynik = podstawa*2 + bok
        return  wynik
    except:
        ValueError
        print("Podana musi byc liczba!")
print(zad4())