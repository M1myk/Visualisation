import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def zad1():
    x = np.arange(2,5,0.1)
    x1 = np.arange(2, 5, 0.1)
    y = np.exp(2*x)
    y1 = np.sin(2*x)

    fig,ax1 = plt.subplots()
    ax1.plot(x, y1, color='brown', linestyle=':', label='sin(2x)')
    plt.legend(loc='upper left')


    ax2 = ax1.twinx()
    ax2.plot(x, y, color='turquoise', linestyle=':', label='$e^{2x}$')
    fig.tight_layout()
    ax1.set_ylim(-12,12)
    plt.xticks(np.arange(2,5.5,0.5))
    plt.xlim(1.92,5.1)
    plt.legend(loc='lower center')
    plt.yticks(np.arange(0,20000,2500))
    plt.ylim(-500,19000)
    plt.show()

#zad1()


def zad2():
    data = pd.read_excel('ceny12.xlsx')
    data = pd.DataFrame(data)
    print(data.head())

    jabka = data[data['Rodzaje towarów i usług'] == 'jabłka - za 1kg']
    cytryny = data[data['Rodzaje towarów i usług'] == 'cytryny - za 1 kg']

    plt.scatter(jabka['Miesiące'], jabka['Wartosc'])
    plt.scatter(cytryny['Miesiące'], cytryny['Wartosc'])
    plt.ylim(0,10)
    plt.yticks(np.arange(0,16,1))
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

#zad2()


def zad3():
    data = pd.read_excel('turystyka12.xlsx', )
    data = pd.DataFrame(data)
    print(data.head())

    slaskie = data['ŚLĄSKIE'].astype(int)
    podlaqskie = data['PODLASKIE'].astype(int)
    print(slaskie)



    plt.subplot(1,2,1)
    slaskie.plot.pie(labels=data['Nazwa'], autopct='%.1f%%',  fontsize=10, pctdistance=0.735)
    circle = plt.Circle((0, 0), 0.5, color='white')
    p = plt.gcf()
    p.gca().add_artist(circle)
    plt.ylabel("")
    plt.title('ŚLĄSKIE')


    plt.subplot(1, 2, 2)
    podlaqskie.plot.pie(labels=data['Nazwa'], autopct='%.1f%%', fontsize=10)
    plt.ylabel("")
    plt.title('PODLASKIE')

    plt.tight_layout()
    plt.show()

zad3()