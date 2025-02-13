import numpy as np
import matplotlib.pyplot as plt
import  pandas as pd


# Tworzenie wskazanej macierzy
macierz = np.array([
    [5, 14, 5, 8],
    [4, 10, 9, 7],
    [3, 1, 15, 2],
    [6, 9, 3, 12]
])

# Wycięcie elementów 5, 7, 1, 3
elementy = [5, 7, 1, 3]
indices = []

for i in range(len(elementy)):
    for wiersz in range(macierz.shape[0]):
        for kolumna in range(macierz.shape[1]):
            if macierz[wiersz,kolumna] == elementy[i]:
                if macierz[wiersz,kolumna] not in indices:
                    indices.append(macierz[wiersz,kolumna])
                    print(macierz[wiersz,kolumna])
                else:
                    continue

nowa_macierz = np.array(indices).reshape(2,2)


# Znalezienie indeksów tych elementów
#indices = []
#for element in elementy:
#    result = np.where(macierz == element)
#    indices.append((result[0][0], result[1][0]))
#
## Utworzenie nowej macierzy 2x2 z wyciętych elementów
#nowa_macierz = np.array([macierz[i, j] for i, j in indices]).reshape(2, 2)
#
#print(indices)
#print("Oryginalna macierz:")
print(macierz)

print(nowa_macierz)



#x = np.arange(-1,1, 0.1)
#y = np.cos(x)*np.sin(x)
#y1 = np.cos(x) - np.tan(x)
#
#plt.subplot(3,1,1)
#plt.plot(x,y,label='cos(x)')
#plt.plot(x,y1, label='tan(x)')
#plt.legend(loc='upper right')
#plt.title("Wykres funkcji")
#
#
#x = np.arange(1,5)
#y = x**(2/np.power(2,1/2))
#plt.subplot(3,1,2)
#plt.scatter(x,y, color='yellow',marker='>', label='cos(x)')
#plt.legend(loc='upper left')
#
#
#
#
#plt.yticks([2.5,5,7.5])
#plt.title("Wykres funkcji")
#
#
#plt.subplot(3,1,3)
#
#
#plt.subplots_adjust(hspace=0.8)

#plt.show()

def szmata():
    df = pd.read_table('glass.data', sep=',')
    df = pd.DataFrame(df)


    df = df[df['Refractive index'] < 1.51766]
    print(df.head())

    grupa = df.groupby(['Type of glass']).size()
    print(grupa)

    grupa.plot.bar(label='ksfsf')
    plt.title("wykres slupkowy")
    plt.xlabel('Type of glass')
    plt.ylabel('ilosc')
    plt.legend()
    plt.xticks(rotation=0)

    plt.savefig('dupa')
    plt.show()

szmata()


M = np.array([
    [2,2,3],
    [5,5,9],
    [8,8,9]
        ]).reshape(3,3)
print(M)
lista = [2,5,8,9]
nowa_macierz = []

for i in range(len(lista)):
    for wiersz in range(M.shape[0]):
        for kolumna in range(M.shape[1]):
            if(lista[i] == M[wiersz][kolumna]):
                if M[wiersz][kolumna] in nowa_macierz:
                    continue
                else:
                    nowa_macierz.append(M[wiersz][kolumna])
nowa_macierz = np.array(nowa_macierz).reshape(2,2)
print(nowa_macierz)

