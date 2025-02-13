import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def zad3():
    data = pd.read_csv('muzea16.csv' , sep='#')
    data = pd.DataFrame(data)
    print(data)
    print('---------------')

    data['2017'] = data['2017'].astype(float)
    data['2018'] = data['2018'].astype(float)
    data['2016'] = data['2016'].astype(float)
    data['2019'] = data['2019'].astype(float)

    wielopolskie = data[data['Województwo'] == 'WIELKOPOLSKIE']
    warminskie = data[data['Województwo'] == 'WARMIŃSKO-MAZURSKIE']

    print(warminskie['2016'])
    bar_width= 0.3
    plt.bar(2016, wielopolskie['2016'], width=bar_width, edgecolor='grey', label='WIELKOPOLSKIE', color='aqua')
    plt.bar(2017, wielopolskie['2017'], width=bar_width, edgecolor='grey', color='aqua')
    plt.bar(2018, wielopolskie['2018'], width=bar_width, edgecolor='grey', color='aqua')
    plt.bar(2019, wielopolskie['2019'], width=bar_width, edgecolor='grey', color='aqua')

    plt.bar(2016+bar_width, warminskie['2016'], width=bar_width, edgecolor='grey', label='WARMIŃSKO-MAZURSKIE', color='navy')
    plt.bar(2017+bar_width, warminskie['2017'], width=bar_width, edgecolor='grey', color='navy')
    plt.bar(2018+bar_width, warminskie['2018'], width=bar_width, edgecolor='grey', color='navy')
    plt.bar(2019+bar_width, warminskie['2019'], width=bar_width, edgecolor='grey', color='navy')


    plt.xlabel('Rok')
    plt.ylabel('Wartosc')
    plt.title('Wykres slupkowy')
    plt.grid(True, which='both', color='gray', linewidth=0.5, linestyle='--')
    plt.xticks(np.arange(2016,2020))
    plt.ylim(0,120)
    plt.yticks(np.arange(0,130,10))
    plt.legend()
    plt.tight_layout()



    plt.show()
#zad3()



def zad4():
    dane = {
        'Rok': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018],
        'Team A': [15, 18, 20, 25, 30, 20, 33, 40, 35],
        'Team B': [23, 21, 21, 22, 24, 25, 30, 20, 29],
        'Team C': [23, 21, 21, 22, 24, 25, 23, 20, 29],
        'Team D': [23, 21, 21, 22, 24, 25, 23, 20, 29]
    }

    # Tworzenie DataFrame
    df = pd.DataFrame(dane)

    x = df['Rok']
    y1 = df['Team A']
    y2 = df['Team B']
    y3 = df['Team C']
    y4 = df['Team D']

    plt.stackplot(x,y1,y2,y3,y4, labels=['Team A','Team B','Team C','Team D'])
    plt.legend()
    plt.show()

zad4()