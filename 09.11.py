def zad1():
    def zad1_a():
        n = abs(int(input('Wpisz ilosc liczb: ')))
        counter = 0
        for i in range(1, n + 1):
            a = abs(int(input('Wpisz kolejną liczbe naturalną: ')))
            if a % 2 != 0:
                counter += 1
        return counter

    print('Liczbami nieparzystami jest ', zad1_a(), ' liczb')

    def zad1_b():
        n = abs(int(input('Wpisz ilosc liczb: ')))
        counter = 0
        for i in range(1, n + 1):
            a = abs(int(input('Wpisz kolejną liczbe naturalną: ')))
            if a % 3 == 0 and a % 5 != 0:
                counter += 1
        return counter

    print('Wynik jest: ', zad1_b())

    def zad1_c():
        n = abs(int(input('Wpisz ilosc liczb: ')))
        counter = 0
        for i in range(1, n + 1):
            a = abs(int(input('Wpisz kolejną liczbe naturalną: ')))
            if a % 2 == 0 and (a ** 0.5).is_integer():
                counter += 1
        return counter

    print(f'Są kwadratami liczby parzystej: {zad1_c()}')

    def zad1_d():
        a = abs(float(input('Wpisz 1 liczbę: ')))
        b = abs(float(input('Wpisz 2 liczbę: ')))
        c = abs(float(input('Wpisz 3 liczbę: ')))
        counter = 0
        if b < (a + c) / 2 and c >= 2:
            counter += 1
        return counter

    print(f'Spełniają warunek (d): {zad1_d()}')

    def zad1_f():
        n = abs(int(input('Wpisz ilosc liczb: ')))
        counter = 0
        for i in range(1, n + 1):
            a = abs(int(input('Wpisz kolejną liczbe naturalną: ')))
            if a % 2 == 0 and a % 2 != 0:
                counter += 1
        return counter

    print(f'Mają nieparzysty numer i są liczbami parzysymi: {zad1_f()}')

    def zad1_g():
        n = abs(int(input('Wpisz ilosc liczb: ')))
        counter = 0
        for i in range(0, n):
            a = abs(int(input('Wpisz kolejną liczbe naturalną: ')))
            if a % 2 != 0 and a > 0:
                counter += 1
        return counter

    print(f'Są nieparzyste i nieujemne: {zad1_g()}')

    def zad1_h():
        n = abs(int(input('Wpisz ilosc liczb: ')))
        counter = 0
        for i in range(0, n):
            a = abs(int(input('Wpisz kolejną liczbe naturalną: ')))
            if a < n ** 2:
                counter += 1
        return counter

    print(f'Spełniają warunek (h): {zad1_h()}')


def zad2():
    n = abs(int(input('Wpisz liczbe naturalna: ')))
    a = abs(int(input('Wpisz ilosz liczb rzeczywistych: ')))
    counter = 0
    for i in range(0, a):
        b = float(input('Wpisz liczbe rzeczywistą: '))
        if b > 0:
            counter += b * 2 + (n * 2)
    print(counter)


def zad3():
    n = abs(int(input('Wpisz liczbe naturalna: ')))
    a = abs(int(input('Wpisz ilosz liczb rzeczywistych: ')))
    counter = 0
    counter1 = 0
    counter2 = 0
    for i in range(0, a):
        b = float(input('Wpisz liczbe rzeczywistą: '))
        if b > 0:
            counter += 2
        elif b < 0:
            counter1 += 1
        else:
            counter2 += 1
    print(f'Dodatnich: {counter}\nUjemnych: {counter1}\nZer: {counter2}')


def zad4():
    n = abs(int(input('Wpisz liczbe naturalna: ')))
    a = abs(int(input('Wpisz ilosz liczb rzeczywistych: ')))

    min_value = float('inf')  # Встановлюємо min_value на нескінченність
    max_value = float('-inf')  # Встановлюємо max_value на від'ємну нескінченність

    for i in range(a):
        b = float(input('Wpisz liczbe rzeczywistą: '))

        min_value = min(min_value, b)
        max_value = max(max_value, b)
    print("Min:", min_value)
    print("Max:", max_value)


def zad5():
    n = abs(int(input("Wpisz ilosc liczb: ")))

    counter = 0
    prev_number = float(input("Wpisz liczbę rzeczywistą: "))

    for i in range(n - 1):
        current_number = float(input("Wpisz liczbę rzeczywistą: "))

        if prev_number > 0 and current_number > 0:
            counter += 1
        prev_number = current_number

    print(f"Ilość sąsiadujących par (a, b) takich, że a > 0 i b > 0: {counter}")


def main():
    #zad1()
    zad2()
    zad3()
    zad4()
    zad5()


main()
