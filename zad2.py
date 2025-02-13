import math


def zad1():
    """
    Opis działania programu
    """
    print(f'\nZadanie 1\n')
    x = float(input('Podaj liczbe: '))
    if x >= 0:
        print(f'wartosc bezwgledna z podanej liczby to {x}')
    else:
        x *= -1
        print(f'wartosc bezwgledna z podanej liczby to {x}')


def zad2():
    """
    Opis działania programu
    """
    print(f'\nZadanie 2\n')
    number = float(input("Wczytaj liczbę zmiennoprzecinkową: "))

    def sgn(x):
        if x < 0:
            return -1
        elif x == 0:
            return 0
        else:
            return 1

    print(sgn(number))


def zad3():
    print(f'\nZadanie 3\n')
    number1 = float(input("Wczytaj liczbę zmiennoprzecinkową: "))
    number2 = float(input("Wczytaj liczbę zmiennoprzecinkową: "))

    if number2 != 0:
        x = number1 / number2
        print(f'Wynik dzielenia jest: {x}')
    else:
        print('Dzielenie niemożliwe!')


def zad4():
    print(f'\nZadanie 4\n')
    a = float(input("Wczytaj liczbę a: "))
    x = float(input("Wczytaj liczbę x: "))
    b = float(input("Wczytaj liczbę b: "))
    num = a * x + b
    if a == 0:
        print(math.sqrt(b))
    else:
        print(math.sqrt(num))


def zad5():
    print(f'\nZadanie 5\n')
    a = float(input("Wczytaj 1 liczbę: "))
    b = float(input("Wczytaj 2 liczbę: "))
    c = float(input("Wczytaj 3 liczbę: "))
    if a < b < c:
        print(f'Najmniejsza jest  {a}\nNajwieksza jest  {c}')

    if c < a < b:
        print(f'Najmniejsza jest  {c}\nNajwieksza jest  {b}')

    if b < c < a:
        print(f'Najmniejsza jest  {b}\nNajwieksza jest  {a}')


def zad6():
    print(f'\nZadanie 6\n')
    a = float(input("Podaj pierwszy bok: "))
    b = float(input("Podaj drugi bok: "))
    c = float(input("Podaj trzeci bok: "))
    if a <= 0:
        print('To nie są boki trójkąta! Kończę program.')
    else:
        y = a + b + c
        x = math.sqrt((y / 2) * (y / 2 - a) * (y / 2 - b) * (y / 2 - c))
        print(f'Pole trójkąta {y}\nObwód trójkąta {x}')


def max3(x, y, z):
    if x >= y and x >= z:
        maximum = x
    elif y >= x and y >= z:
        maximum = y
    else:
        maximum = z

    if x <= y and x <= z:
        minimum = x
    elif y <= x and y <= z:
        minimum = y
    else:
        minimum = z

    return minimum, maximum


def zad7():
    print(f'\nZadanie 7\n')
    x = float(input("Wprowadź pierwszą liczbę: "))
    y = float(input("Wprowadź drugą liczbę: "))
    z = float(input("Wprowadź trzecią liczbę: "))
    minimum, maximum = max3(x, y, z)
    print(f"Najmniejsza liczba: {minimum}")
    print(f"Największa liczba: {maximum}")


def poprawne_boki(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return a, b, c


def pole_trojkata(a, b, c):
    if a > 0 and b > 0 and c > 0:
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


def obwod_trojkata(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return a + b + c


def zad8():
    print(f'\nZadanie 8\n')
    a = float(input("Wprowadź pierwszą liczbę: "))
    b = float(input("Wprowadź drugą liczbę: "))
    c = float(input("Wprowadź trzecią liczbę: "))

    a, b, c = poprawne_boki(a, b, c)
    x = pole_trojkata(a, b, c)
    y = obwod_trojkata(a, b, c)

    print(f'{x}\n{y}')


def main():
    zad1()
    zad2()
    zad3()
    zad4()
    zad5()
    zad6()
    zad7()
    zad8()


main()
