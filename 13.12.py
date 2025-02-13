def zad1():
    dict = {}
    a = input('Wpisz: ')
    for elem in a:
        if elem not in dict:
            dict[elem] = elem
            dict[elem] = 0
        if elem in dict:
            dict[elem] += 1
    print(dict)

#zad1()

def zad1b():
    dict = {}
    a = input('Wpisz: ')
    b = a.lower()
    for elem in b:
        if elem not in dict:
            dict[elem] = elem
            dict[elem] = 0
        if elem in dict:
            dict[elem] += 1
    most_used_sign = max(dict, key=dict.get)
    print(dict)
    print(most_used_sign, dict[most_used_sign])

#zad1b()


def zad2():
    wynik = True
    dict = {}
    while wynik:

        a = input('Wpisz liczbe: ')
        if a == '':
            wynik = False
        elif a.replace('.', '', 1).isdigit():
            a = float(a)
            if a.is_integer():
                a = int(a)
                if a not in dict:
                    dict[a] = 1
                else:
                    if a in dict:
                        dict[a] += 1

        else:
            print('Wpisz liczbe')


    print(dict)
#zad2()

def function():
    slownik = {}
    try:
        n = int(input(' WPROWADZ ILE CHCESZ WPROWADZIC LICZB:  '))
        for i in range(n):
            j = float(input('CO CHCESZ DODAC DO SLOWNIKA :'))
            if j not in slownik:
                slownik[j] = 1
            else:
                slownik[j] += 1
    except Exception as e:
        print(f'OOPS MAMY TAKI BLAD {e}')
        print('SPROBUJEMY JESZCZE RAZ')
        function()
    finally:
        print(slownik)
function()
