import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def zad4():
    data = pd.read_excel('rod15.xlsx', header=None).T
    data = pd.DataFrame(data)

    data.columns = data.iloc[0]
    data = data[1:]
    print(data)
zad4()