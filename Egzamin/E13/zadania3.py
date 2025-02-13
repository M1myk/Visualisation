import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def zad1():
    x = ['a', 'b', 'c', 'd', 'e', 'f']
    y = [16.81, 20.35, 10.18, 17.70, 16.81, 18.14]

    x1 = ['a', 'b', 'c', 'd', 'e', 'f']
    y1 = [21.7, 12.2, 21.7, 8.1, 20.4, 15.8]

    explode = (0, 0, 0.05, 0, 0, 0.1)
    explode1 = (0, 0, 0.05, 0, 0, 0.1)
    plt.subplot(1, 2, 1)
    plt.pie(y, labels=x, autopct='%.2f%%', radius=1.3,
            colors=['tab:orange', 'royalblue', 'tab:red', 'papayawhip', 'darkkhaki', 'blue'], explode=explode)

    plt.subplot(1, 2, 2)
    plt.pie(y1, labels=x1, autopct='%.2f%%', radius=1.3,
            colors=['tab:orange', 'royalblue', 'tab:red', 'papayawhip', 'darkkhaki', 'blue'], explode=explode1)
    plt.show()


# zad1()


def zad2():
    data = pd.read_excel('kolej13.xlsx')
    data = pd.DataFrame(data)
    print(data.head())
    plt.plot(data['Rok'], data['Wartosc'], color='green', marker='.', linestyle='--', label='cos tam')
    plt.text(2019, 19400, 'Data: 18-12-2035', va='top', ha='right')
    plt.grid()
    plt.title('Wykres')
    plt.xlabel('Lata')
    plt.ylabel('Wartosc')
    plt.tight_layout()
    plt.legend()
    plt.show()


# zad2()


def zad3():
    data = pd.read_csv('pekin13.csv', sep='#')
    data = pd.DataFrame(data)
    print(data.head())

    data['Złote'] = data['Złote'].astype(float)
    data['Srebrne'] = data['Srebrne'].astype(float)
    data['Brązowe'] = data['Brązowe'].astype(float)
    data['Razem'] = data['Razem'].astype(float)

    grupa = data[data['Państwo'].isin(['Niemcy', 'Austria', 'Szwajcaria'])]
    niemcy = data[data['Państwo'] == 'Niemcy']
    austria = data[data['Państwo'] == 'Austria']
    szwajcaria = data[data['Państwo'] == 'Szwajcaria']

    x = np.arange(len(grupa))

    plt.figure(figsize=(9,7))
    plt.bar(x, grupa['Złote'], width=0.2, edgecolor='grey', label='Złote')
    plt.bar(x+0.2, grupa['Srebrne'], width=0.2, edgecolor='grey', label='Srebrne')
    plt.bar(x+0.4, grupa['Brązowe'], width=0.2, edgecolor='grey', label='Brązowe')
    plt.bar(x+0.6, grupa['Razem'], width=0.2, edgecolor='grey', label='Razem')
    plt.xticks(np.arange(0,3,1), ['Niemcy', 'Austria', 'Szwajcaria'])
    plt.title("Wykres", fontsize=15)
    plt.ylabel('Wartosc', fontsize=13)
    plt.xlabel('Panstwo', fontsize=13, color='blue')

    plt.yticks(np.arange(0,31,2))
    plt.legend()
    plt.tight_layout()

    plt.show()


zad3()
