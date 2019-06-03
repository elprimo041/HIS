# coding: utf-8

import numpy as np
import scipy.stats as stats
import pandas as pd
import os

def smirnov_grubbs(data, alpha):
    x, o = list(data), []
    while True:
        n = len(x)
        t = stats.t.isf(q=(alpha / n) / 2, df=n - 2)
        tau = (n - 1) * t / np.sqrt(n * (n - 2) + n * t * t)
        i_min, i_max = np.argmin(x), np.argmax(x)
        myu, std = np.mean(x), np.std(x, ddof=1)
        i_far = i_max if np.abs(x[i_max] - myu) > np.abs(x[i_min] - myu) else i_min
        tau_far = np.abs((x[i_far] - myu) / std)
        if tau_far < tau: break
        o.append(x.pop(i_far))
    return (np.array(x), np.array(o))

alpha = 0.05
ID = 'naoki'
for i in range(4):
    file_name = ID + '_test' + str(i+1) + '.csv'
    os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/result/row_data')
    df = pd.read_csv(file_name,header = None)
    os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/result/data_clean')
    inp = df.values
    data_clean , out = smirnov_grubbs(inp, alpha)
    file_name = ID + '_test' + str(i+1) + '_clean.csv'
    with open(file_name, 'w') as f:
        for j in range(len(data_clean)):
            print(float(data_clean[j]), file=f)