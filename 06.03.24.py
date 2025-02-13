import random
def zad1():
   wynik = 1
   a = input("Wpisz zdanie: ")
   for i in a:
       if i == ' ':
           wynik += 1
       else:
           continue
   print(wynik)
zad1()


def zad2():
   a = int(input("Wpisz liczbe: "))
   b = int(input("Wpisz liczbe: "))
   c = int(input("Wpisz liczbe: "))

   wynik = a**b+c
   print(wynik)

zad2()

def zad3_2():
    import sys


    a = int(sys.stdin.readline().strip())
    b = int(sys.stdin.readline().strip())
    c = int(sys.stdin.readline().strip())


    wynik = a * b + c


    sys.stdout.write(str(wynik) + '\n')

zad3_2()


def zad3():
   a = input("Wpisz slowo: ")
   wynik = a[::-1]
   if a == wynik:
       return print(True)
   else:
       return print(False)

zad3()


def zad4():
   a = int(input("Wpisz liczbe: "))

   for i in range(2, int(a**0.5)+1):
       if a % i == 0:
           return False
       else:
           return True

print(zad4())


def ile(n):
   suma = 0
   for i in range(1, n):
       if n % i == 0:
           suma += i
   return suma == n


def zad5():
   number = 1000
   wyniki = []

   for i in range(2, number):
       if ile(i):
           wyniki.append(i)

   print("Liczby doskonałe mniejsze od 1000:", wyniki)


zad5()


def zad6():
   lista = []
   k = int(input("Podaj zakres listy: "))
   for i in range(1, k + 1):
       rand = random.randint(0, 1)
       if rand == 0:
           c = random.randint(-100, 100)
           lista.append(c)
       else:
           r = round(random.uniform(-100.0, 100.0), 2)
           lista.append(r)
   print(lista)
   for i in range(len(lista)):
       lista[i] = round((lista[i] ** 2), 2)
   print(lista)

zad6()

def zad7():
   lista = []
   n = 0
   while n < 10:
       a = int(input("Podaj liczbę: "))
       if a % 2 == 0:
           lista.append(a)
       n += 1
   return lista

parzyste = zad7()
print("Liczby parzyste:", parzyste)

def zad8():
    lista = []
    slownik = {}
    beg = True
    while beg:
        a = input("Wpisz tegas albo ' ': ")
        if a == ' ':
            beg = False
        else:
            lista.append(a)
    print(lista)

    for elem in lista:
        if elem not in slownik:
            slownik[elem] = 1
        else:
            slownik[elem] += 1
    print(slownik)
    slownik_bez_liczb = {}
    for key, value in slownik.items():  #
        if not str(key).isdigit():
            slownik_bez_liczb[key] = value
    print(slownik_bez_liczb)


zad8()
