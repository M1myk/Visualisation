

import numpy as np
import math



a = np.array([0, 1, 'a', 'b'])
print(a)
print(a.dtype)

a = np.arange(2)
print(a)
print(type(a))

print(a.dtype)

a = np.arange(2, dtype='int32')
print(a.dtype)

b = a.astype('float')
print(b)
print(b.dtype)
print(b.shape)
print(f"\n\n\n\n  ")
print(13131, a.ndim)

m = np.array((np.arange(2), np.arange(2)))
print(m)
print(m.shape)

m1 = np.array([[5, 4, 5],
               [4, 8, 3]])
print(m1)
print(m1.shape)
print(44, m1.ndim)

zera = np.zeros((5, 5), dtype=int)
jedynki = np.ones((4, 4))
print(zera)
print(jedynki)
print(zera.dtype)
print(jedynki.dtype)

pusta = np.empty((2, 2))
print(pusta)
poz_1 = pusta[1, 1]
poz_2 = pusta[0, 1]
print(poz_1)
print(poz_2)

liczby = np.arange(1, 2, 0.1)
print(liczby)

liczby_lin = np.linspace(1, 2, 5)
print(liczby_lin)
z = np.indices((5, 3))
print(z)

print(z[0, 3, 2])
print(" ")
x, y = np.mgrid[0:5, 0:5]
print(x)
print(" ")
print(y)
print(" ")
mat_diag_k = np.diag([a for a in range(5)], k=-1)
print(mat_diag_k)

z = np.fromiter(range(5), dtype='int32')
print(z)

znaki = b'abcdef'
zn1 = np.frombuffer(znaki, dtype='S1')
print(zn1)
zn2 = np.frombuffer(znaki, dtype='S2')
print(zn2)

znaki = 'abcdef'
zn3 = np.array(list(znaki))
zn4 = np.array(list(znaki), dtype='S1')
zn5 = np.array(list(b'abcdef'))
zn6 = np.fromiter(znaki, dtype='S1')
zn7 = np.fromiter(znaki, dtype='U1')
print(zn3)
print(zn4)
print(zn5)
print(zn6)
print(zn7)

mat = np.ones((2, 2))
mat_1 = np.array([[4, 6],
                  [7, 5]])
mat = mat + mat_1
print(mat)
print(mat - mat_1)
print(mat * mat_1)
print(mat / mat_1)

a = np.dot(mat, mat_1)
b = mat.dot(mat_1)
print(a)
print(b)

a = np.arange(10)
print(a)
s = slice(2, 7, 2)
print(a[s])
s = range(2, 7, 2)
print(a[s])
print(a[2:7:2])
print(a[1:])
print(a[2:5])

mat = np.arange(25)
mat = mat.reshape((5, 5))
print(mat[1:])
print(mat[:, 1])
print(mat[:, -1])
print(mat[2:6, 1:3])
print(mat[:, range(2, 6, 2)])
print('')

x = np.array([[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8],
              [9, 10, 11]])
print(x)
print("")
rows = np.array(([0, 0], [3, 3]))
cols = np.array(([0, 2], [0, 2]))
y = x[rows, cols]
print(y)

# x = np.arange(x*3 for x in range(15))
# print(x)
