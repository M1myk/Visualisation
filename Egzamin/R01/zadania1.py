import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def zad1():
    x = ['Olstyn', 'Gdansk', 'Torun', 'Warszawa', 'Kraków']
    A = [48, 60, 65, 65, 50]
    B = [52, 55, 50, 40, 56]

    plt.figure()
    plt.bar(x,A, color=['pink', 'tab:brown', 'green', 'brown', 'bisque'], label='A')
    plt.bar(x,B, bottom=A, color=['purple','purple', 'blue', 'grey', 'darkorchid'], label='B')
    plt.xticks(x)
    plt.ylabel("Wartości")
    plt.title("Wylres słupkowy pogrupowany", fontsize=15)
    plt.ylim(0,150)
    plt.yticks(np.arange(0,160,10))
    plt.xticks(rotation=45, fontsize=12)
    plt.subplots_adjust(bottom=0.2, top=0.93)

    plt.legend(loc='upper right')
    plt.show()


#zad1()



def zad2():
    df = pd.read_excel('parki01.xlsx')
    df = pd.DataFrame(df)

    # Extract data for the specific regions
    lodzkie = df[(df['Nazwa'] == 'ŁÓDZKIE')]
    slaskie = df[(df['Nazwa'] == 'ŚLĄSKIE')]
    podkarpackie = df[(df['Nazwa'] == 'PODKARPACKIE')]

    # Plot the data with different styles
    plt.figure(figsize=(12, 8))

    plt.plot(lodzkie['Rok'], lodzkie['Wartosc'], label='Łódzkie', linestyle='-', color='blue', linewidth=2)
    plt.plot(slaskie['Rok'], slaskie['Wartosc'], label='Śląskie', linestyle='--', color='green', linewidth=2)
    plt.plot(podkarpackie['Rok'], podkarpackie['Wartosc'], label='Podkarpackie', linestyle='-.', color='red',
             linewidth=2)

    # Add grid, legend, and title
    plt.grid(True)
    plt.legend()
    plt.title('Powierzchnia parków spacerowo-wypoczynkowych w województwach')
    plt.xlabel('Rok')
    plt.ylabel('Powierzchnia (ha)')

    # Add text with the current date
    plt.text(2020, 4000, 'Data: 2024-05-30', fontsize=12, ha='right', va='top')


    plt.savefig('zad2', format='svg')


    plt.show()


#zad2()


def zad3():
    df = pd.read_csv('medale01.csv', sep=';')
    df = pd.DataFrame(df)
    print(df.head())


    letnie = df[df['Rodzaj'] == 'Letnie']
    zimowe = df[df['Rodzaj'] == 'Zimowe']

    #letnie = letnie.groupby(['Brązowe'])
    letnie = letnie['Brązowe'].astype(int)

    zimowe = zimowe['Brązowe']



    plt.figure(figsize=(8,6))
    plt.subplot(1,2,1)
    letnie.plot.pie(subplots=True, autopct='%.0f%%')
    plt.xlabel("Letnie")
    plt.ylabel("Ilosc")


    plt.subplot(1,2,2)
    zimowe.plot.pie(subplots=True, autopct='%.0f%%', fontsize=10)
    plt.xlabel("Zimowe")
    plt.ylabel("Ilosc")

    plt.suptitle("Wykres kolowe")
    plt.show()
zad3()