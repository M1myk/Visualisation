import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def zad1():
    x = np.linspace(-3, 3, 400)
    y = np.cos(x)
    y1 = np.sin(x)
    plt.plot(x, y1, linestyle='--', color='purple', label='sin(x)')
    plt.plot(x, y, linestyle='--', color='turquoise', label='cos(x)')
    plt.xticks(np.arange(-3, 4, 1))
    plt.ylim(-1, 1)
    plt.yticks(np.arange(-1, 1.25, 0.25))
    plt.xlabel('oś dolna', color='blue', fontsize=11)
    plt.ylabel('oś lewa', color='red', fontsize=11)
    plt.title('Wykres funkcji trugonometrycznych', fontsize=13)
    plt.legend(loc='lower center')
    plt.xlim(-3, 3)
    plt.tight_layout()
    plt.show()


zad1()


def zad2():
    data = pd.read_excel('ceny11.xlsx')
    data = pd.DataFrame(data)
    print(data.head())

    plt.plot(data['Rok'], data['Wartość'])
    plt.yticks(np.arange(3.7, 4.6, 0.1))
    plt.text(2020, 4.48, 'Data: 2024-05-30', fontsize=10, ha='right', va='top')
    plt.grid()
    plt.show()


zad2()


def zad3():
    data = pd.read_csv('sport11.csv', sep=';')
    data = pd.DataFrame(data)
    data['Rok'] = data['Rok'].astype(int)
    data['Wartość'] = data['Wartość'].astype(float)
    print(data.head())

    mazury = data[data['Nazwa'] == 'WARMIŃSKO-MAZURSKIE']
    pomorskie = data[data['Nazwa'] == 'POMORSKIE']

    x = np.arange(len(mazury['Gry zespołowe']))
    plt.barh(mazury['Gry zespołowe'], mazury['Wartość'], height=0.7, label='WARMIŃSKO-MAZURSKIE')

    plt.barh(x + 0.3, pomorskie['Wartość'], height=0.45, label='POMORSKIE')
    plt.legend()
    plt.xticks(np.arange(0, 3100, 200), rotation=45)
    plt.tight_layout()
    plt.grid()
    plt.show()


zad3()
