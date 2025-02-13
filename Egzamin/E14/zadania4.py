import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize


def zad1():
    x = [0.37, 0.45, 0.47, 0.67, 0.68, 0.85, 0.86]
    y = [-0.4, -0.095, -0.73, -0.32, -0.7, -0.14, -0.73]
    z = [10, 10, 20, 7.5, 17.5, 20, 19]

    norm = Normalize(vmin=0, vmax=20)
    plt.scatter(x, y, c=z, cmap='spring', norm=norm)
    plt.colorbar()
    plt.ylim((-0.76, -0.05))
    plt.xlim(0.35, 0.9)
    plt.xticks(np.arange(0.4, 0.9, 0.1))
    plt.title('Wyniki doświadczenia (7 próbek)', fontsize=14)
    plt.xlabel('Rozkład', fontsize=12)
    plt.ylabel('Wartość', fontsize=12)
    plt.show()


zad1()


def zad2():
    data = pd.read_excel('ceny14.xlsx')
    data = pd.DataFrame(data)
    print(data.head())

    data1 = data[data['Rodzaje produktów'] == 'pstrąg świeży niepatroszony - za 1 kg']
    data2 = data[data['Rodzaje produktów'] == 'śledź solony, niepatroszony - za 1kg']
    plt.plot(data1['Rok'], data1['Wartosc'], color='green', marker='>', linewidth=2, linestyle='--',
             label='pstrąg świeży niepatroszony - za 1 kg')
    plt.plot(data2['Rok'], data2['Wartosc'], color='red', marker='o', linewidth=2, linestyle=':',
             label='śledź solony, niepatroszony - za 1kg')
    plt.grid(True)

    plt.xlabel('Lata')
    plt.ylabel('Wartosc')
    plt.title('Wykres liniowy')
    plt.legend()
    plt.tight_layout()
    plt.show()


zad2()


def zad3():
    data = pd.read_csv('sprzedaz14.csv', sep='@', header=None).T
    data = pd.DataFrame(data)

    data.columns = ['Rodzaj', 'Rok', 'Ilosc']
    print(data.head(20))

    data['Rok'] = data['Rok'].astype(int)
    data['Ilosc'] = data['Ilosc'].astype(int)

    jablka = data[data['Rodzaj'] == 'Jabłka']
    gruszki = data[data['Rodzaj'] == 'Gruszki']
    sliwki = data[data['Rodzaj'] == 'Śliwki']

    x = np.arange(len(jablka))
    plt.bar(jablka['Rok'], jablka['Ilosc'], width=0.2, label='Jablka', color='green', edgecolor='black')
    plt.bar(gruszki['Rok'] + 0.2, gruszki['Ilosc'], width=0.2, label='Gruszki', color='gold', edgecolor='black')
    plt.bar(sliwki['Rok'] + 0.4, sliwki['Ilosc'], width=0.2, label='Sliwki', color='purple', edgecolor='black')

    plt.legend()

    plt.title('Ilosc owoc kupionych przez targi', fontsize=14)
    plt.xlabel('Rok', fontsize=12)
    plt.ylabel('Ilosc', fontsize=12)
    plt.ylim(5000, 25000)
    plt.xticks(np.arange(2011, 2015), fontsize=10)
    plt.yticks(fontsize=9)

    plt.grid(True, which='both', color='gray', linewidth=0.5, linestyle='--')
    plt.tight_layout()

    plt.savefig('zad_3.pdf', format='pdf')
    plt.show()


zad3()



