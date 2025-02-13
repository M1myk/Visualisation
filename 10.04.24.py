import numpy as np

a = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])
print(a)
print(a.sum())  # suma macierzy

print(a.sum(axis=0))  # suma kazdej z kolumn

print(a.sum(axis=1))  # suma kazdego wierza

print(a.cumsum(axis=1))

b = np.arange(6).reshape(2, 3)

for b in a.flat:
    print(b, end=" ")
print("")
print("---------------------")

c = np.arange(1,10)
print(c.flat)

d = c.ravel() # robi z macierzy wektor
print(d)
print(d.shape)
print("")

e = np.arange(9).reshape((3,3)).T # transpozycja macierzy
print(e)
print(e.shape)


log = np.log(100) / np.log(np.exp(1))
print(log)
print(np.exp(1))
