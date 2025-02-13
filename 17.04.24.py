import pandas as pd
import numpy as np

s = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
print(s)

data = {'Kraj': ['Belgia', 'India', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 1303171035, 207847528]}

df = pd.DataFrame(data)
print(df)

print("")
print("to 3 indeks s tabe;i s: ", s['c'])
print("to 3 indeks s tabe;i s: ", s.c)
print("")

print(df[0:1])
print("")

print(df['Populacja'])
print("")
print(df.iloc[0, 0])
print(df.loc[0, 'Kraj'])
print(df.at[0, 'Kraj'])
print("")
print(df.loc[0])

print("")
print('Kraj: ' + df.Kraj)
print("")
print(df.sample())

print("")
print(df.sample(2))
print(df.sample(frac=0.5))
print(df.sample(n=10, replace=True))
print(df.head())
print(df.head(2))
print(df.tail(1))
print(df.describe())
print(df.T)
print("")

print("")
print(s[s > 9])
print(s.where(s > 10, 'za duze'))
seria = s.copy()
seria.where(seria > 10, 'za duze', inplace=True)
print("#########")
print(seria)

print("#########")
print(s[~(s > 10)])

print("#########")
print(s[(s < 13) & (s > 8)])

print("")
print("")
print(df[df['Populacja'] > 120000000])
print(df[(df.Populacja > 1000000) & (df.index.isin([0,2]))])

print("#########")
szukaj = ['Belgia', 'Brasilia']
print(df.isin(szukaj))
print("")


print("")
s['e'] = 15
print("dodalem nowa wartosz: ",s.e)
print("")

df.loc[3]='dodane'
print(df)
print("")

df.loc[4] = ['Polska', 'Warszawa', 38675467]
print(df)
print("")

print("#####################################")
print("")

new_df = df.drop([3])
print(new_df)
print("")

df.drop([3], inplace=True)
print(df)
print("")

#df.drop('Kraj', axis=1, inplace=True)

df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Poludniowa', 'Europa']
print(df)
print("")
print("")

print(df.sort_values('Kraj'))

grouped = df.groupby(['Kontynent'])
print(grouped.get_group('Europa'))

print(df.groupby(['Kontynent']).agg({'Populacja': ['sum']}))


print("skfmsifmsfsfm")
print(s.where(s > 10, 'za duze'))