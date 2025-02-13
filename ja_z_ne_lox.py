def pisia():
    n = int(input("Wpisz liczbe: "))
    bin = ''
    try:
        if n < 0:
            raise ValueError

        if n == 0:
            bin = '0000'
        else:
            while n > 0:
                liczba = n % 2
                bin = str(liczba) + bin
                n //= 2
        bin = bin.zfill(4)
        return bin


    except ValueError:
        print("Wpisz liczbe wieksza od zera!")

print(pisia())