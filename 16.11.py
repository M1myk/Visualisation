import math


def main():
    print(zad1_a())
    print(zad1_b())
    print(zad1_c())
    print(zad1_d())
    print(zad5_c())
    print(zad2_a())
    print(zad2_b())
    print(zad2_c())
    print(zad2_d())
    print(zad2_e())
    print(zad4_a())
    print(zad4_b())
    print(zad5_a())
    print(zad5_b())
    print(zad8())

def zad1_a():
    n = int(input("a) Wpisz liczbę naturalną: "))
    i = 2
    while n > 1:
        i = i ** n
        return i


def zad1_b():
    n = int(input("b) Wpisz liczbę naturalną: "))
    silnia = 1
    while n > 1:
        silnia *= n
        n -= 1
    return silnia


def zad1_c():
    n = int(input("c) Wpisz liczbę naturalną: "))
    mianownik = 0
    i = 1
    wynik = 1
    while n > 0:
        mianownik += 1
        if i == 1:
            wynik = 2
        else:
            wynik *= 1 + 1 / (mianownik ** 2)
        n -= 1
        i += 1
    return wynik


def zad1_d():
    n = int(input("d) Wpisz liczbę naturalną: "))
    i = 1
    mianownik = math.sin(i)
    wynik = 1 / (1 + mianownik)
    while n > 1:
        i += 1
        mianownik += math.sin(i)
        wynik += 1 / mianownik
        n -= 1
    return wynik


def zad2_a():
    n = int(input("a) Wpisz liczbę naturalną: "))
    a = float(input("Wpisz liczbę rzeczywistą: "))
    while n > 1:
        a = a ** n
        return a


def zad2_b():
    n = int(input("b) Wpisz liczbę naturalną: "))
    a = float(input("Wpisz liczbę rzeczywistą: "))
    wynik = 1
    while n >= 1:
        wynik *= (a + (n - 1))
        n -= 1
    return wynik


def zad2_c():
    n = int(input("c) Wpisz liczbę naturalną: "))
    a = float(input("Wpisz liczbę rzeczywistą: "))
    wynik = 1 / (a * (a + n))
    while n >= 1:
        n -= 1
        wynik += 1 / (a * (a + n)) + 1 / a
    return wynik


def zad2_d():
    a = float(input("d) Wpisz Liczbę rzeczywistą: "))
    n = int(input("Wpisz liczbę naturalną: "))
    wynik = 0
    while n >= 1:
        wynik += 1 / a ** (2 * n)
        n -= 2
        return wynik


def zad2_e():
    a = float(input("e) Wpisz Liczbę rzeczywistą: "))
    n = int(input("Wpisz liczbę naturalną: "))
    wynik = 1
    while n >= 1:
        wynik *= a - n * n
        n -= 1
    return wynik


def zad4_a():
    a = float(input("4a) Wpisz liczbę rzeczywistą: "))
    sum = 0
    while True:
        for i in range(1, 10000000):
            sum += 1 / i
            print(sum)
            if a < sum:
                return sum


def zad4_b():
    a = float(input("4b) Wpisz liczbę rzeczywistą: "))
    n = int(input('Wpisz liczbę naturalną: '))
    sum = 0
    while True:
        for i in range(1, n):
            sum += 1 / i
            print(sum)
            if a < sum:
                return sum


def zad5_a():
    n = int(input("5a) Wpisz liczbę naturalną: "))
    ile = 0
    while n > 0:
        ile += 1
        n //= 10
    return ile


def zad5_b():
    n = int(input("5b) Wpisz liczbę naturalną: "))
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma


def zad5_c():
    n = int(input("5c) Wpisz liczbę naturalną: "))
    liczba = 0
    while n > 0:
        liczba = n % 10
        n //= 10
    return liczba


def zad6():
    m = int(input("6) Wpisz liczbę naturalną m: "))
    n = int(input("Wpisz liczbę naturalną n: "))


def zad8():
    m = int(input("9) Wpisz liczbę naturalną m: "))
    n = int(input("Wpisz liczbę naturalną n: "))
    ile = 0
    while n > 0:
        for i in range(m,n):
            ile +=1
        return ile

def zad_2_1():
    n = int(input("Wpisz liczbę naturalną n: "))
    suma = 0
    while n >= 1:
        suma += n
        n -= 1
    return suma
print(zad_2_1())

def zad_2_5():
    n = int(input("Wpisz liczbę naturalną n: "))
    result = 0
    while n >= 1:
        result += (-1) ** (n - 1) * n
        n -= 1
    return result

print(zad_2_5())
if __name__ == '__main__':
    main()
