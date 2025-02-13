import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def zad1():
    x = ['A', 'B','C','D','E']
    y = [27.2, 8.8,28.1,21.1, 14.9]
    explode = (0,0.15,0,0,0)
    plt.subplot(2,1,1)
    plt.pie(y, autopct='%.1f%%', labels=x, radius= 1.1, shadow=True, explode=explode, colors=['purple', 'grey','yellow', 'red','orange'])
    plt.title('Tytul 1')


    plt.subplot(2,1,2)
    x1 = ['A', 'B','C','D','E']
    y1 = [25.7,21.2,13.4,12.8,26.8]
    plt.pie(y1, autopct='%.1f%%', labels=x1, radius=1.1, shadow=True, explode=explode,
            colors=['purple', 'grey', 'yellow', 'red', 'orange'])
    plt.title('Tytul 2')
    plt.subplots_adjust(hspace=0.15, bottom=0.03, top=0.9)
    plt.show()

#zad1()


def zad2():
    df = pd.read_excel('ceny02.xlsx')
    df = pd.DataFrame(df)
    print(df.head())


    plt.figure(figsize=(8,7))
    jabkła = df[df['Rodzaje towarów i usług'] == 'jabłka - za 1kg']
    cytryny = df[df['Rodzaje towarów i usług'] == 'cytryny - za 1 kg']

    plt.plot(jabkła['Miesiące'], jabkła['Wartosc'], color='g', marker='o', linestyle='--', linewidth=2, label='Jabłka')

    plt.plot(cytryny['Miesiące'], cytryny['Wartosc'], color='red', marker='>', linestyle=':', linewidth=2, label='Cytryny')

    plt.ylabel("Wartosci")
    plt.xlabel('Miesiące')
    plt.xticks(rotation=45)

    plt.annotate(text='Najwyzsza',
                 xy=(7, 14),  # Współrzędne punktu do zaznaczenia
                 xytext=(8.5, 14),  # Współrzędne początku tekstu
                 arrowprops=dict(facecolor='red'),  # Właściwości strzałki (kolor)
                 fontsize=12,  # Rozmiar czcionki
                 color='blue',  # Kolor tekstu
                 fontweight='bold')
    plt.show()


#zad2()


def zad3():
    df = pd.read_excel('samochody02.xlsx', header=None).T
    df = pd.DataFrame(df)


    df.columns=["Rodzaj", "Rok", "Wartość"]

    print(df.head())

    #df = df.groupby(['Rodzaj'])

    df["Rok"] = df["Rok"].astype(int)
    df["Wartość"] = df["Wartość"].astype(int)


    r2017 = df[df['Rok'] == 2017]
    r2018 = df[df['Rok'] == 2018]

    x = np.arange(len(r2017["Rodzaj"]))

    print(df.head())

    plt.barh(r2017['Rodzaj'], r2017['Wartość'])
    plt.barh(x + 0.33, r2018['Wartość'])
    plt.yticks(x + 0.33 / 2, r2017["Rodzaj"])
    plt.tight_layout()
    plt.xticks([0,10000000,20000000], [0, '10 mln', '20 mln'])
    plt.show()

    print(x)

zad3()