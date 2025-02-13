import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
start_time = time.time()
my_arr = np.arange(1000000)
my_list = list(range(1000000))
start_time = time.time()
my_arr2 = my_arr * 2
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
my_list2 = [x * 2 for x in my_list]
print("--- %s seconds ---" % (time.time() - start_time))


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("a")
print(a)
print("r1")
r1 = np.delete(a, 1, axis=1)
print(r1)
print("r2")
r2 = np.delete(a, 2, axis=0)
print(r2)


tab = np.array(np.arange(0,110,10))

for i in range(len(tab)):
    tab[i] = tab[i]**2
print(tab)


x = ['a', 'b','c','d']

A = [10,20,30,40]
B = [20,30,40,50]

x1 = np.arange(1,10,0.1)
y = x1**2

plt.bar(x, A, color=['purple','yellow','brown','orange'], label='A')
plt.bar(x, B, bottom=A, color=['blue','green','pink','grey'],label='B')
plt.plot(x1,y, marker='>', color='black', linestyle=':')


plt.yticks(np.arange(0,105,5))
plt.xlabel("liczby")
plt.ylabel('wartosci')
plt.title('Wykres slupkowy')
plt.grid(True, which='both', color='gray', linewidth=0.5, linestyle='--')
plt.legend()
plt.show()

fig, ax1 = plt.subplots()
t = np.arange(0.01, 10.0, 0.01)
s1 = np.exp(t)
ax1.plot(t, s1, 'b-')
ax1.set_xlabel('time (s)')

ax1.set_ylabel('exp', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
s2 = np.sin(2 * np.pi * t)
ax2.plot(t, s2, 'r.')
ax2.set_ylabel('sin', color='r')
ax2.tick_params('y', colors='r')

fig.tight_layout()
plt.show()