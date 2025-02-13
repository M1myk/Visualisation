import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('dane.csv', header=0, sep=";")
print(df)

seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
wedges, texts, autotext = plt.pie(x=seria, labels=seria.index,
                                  autopct=lambda pct: "{:.1f}%".format(pct),
                                  textprops=dict(color="black"),
                                  colors=['green','red'])
plt.title("suma zamowien")
plt.legend(loc='lower right')
plt.ylabel('procentowy wynik')
plt.show()