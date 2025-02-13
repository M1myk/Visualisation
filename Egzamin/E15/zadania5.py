import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def zad3():
    data = pd.read_excel('rod15.xlsx', header=None).T
    data = pd.DataFrame(data)

    data.columns = data.iloc[0]
    data = data[1:]
    print(data.head())
    data['Rok'] = data['Rok'].astype(int)
    data['Wartosc'] = data['Wartosc'].astype(float)



    odrody = data[(data['Rodzaje terenu'] == 'ogrody') & (data['Ogrody'] == 'powierzchnia')]
    dzialki = data[(data['Rodzaje terenu'] == 'działki') & (data['Ogrody'] == 'powierzchnia')]

    fig, ax1 = plt.subplots()

    ax1.plot(odrody['Rok'], odrody['Wartosc'], color='green', marker='>', linestyle='--', linewidth=2, label='Ogrody')


    plt.plot(dzialki['Rok'], dzialki['Wartosc'], color='red', marker='o', linestyle=':', linewidth=2, label='Dzialka')


    plt.xticks(np.arange(2014,2018))
    plt.grid(True, color='grey', linestyle='--', which='both')
    plt.ylim(30000,45000)
    plt.legend()


    #plt.show()

#zad3()




