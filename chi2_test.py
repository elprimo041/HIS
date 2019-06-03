#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, csv
import pandas as pd
import numpy as np
import scipy.stats as st

def get_normal(inp):
    result = (inp - inp.min()) / (inp.max() - inp.min())
    return result


def get_chi2_test(l1, l2, alpha):
    k = 10
    l1_normal = get_normal(l1)
    l2_normal = get_normal(l2)
    hist1 ,_ = np.histogram(l1_normal, bins = k)
    hist2 ,_ = np.histogram(l2_normal, bins = k)
    chi2 = 0
    for i in range(k):
        exp = (hist1[i] + hist2[i]) * len(l1) / (len(l1) + len(l2))
        chi2 += (hist1[i] - exp)**2 / exp
        exp = (hist1[i] + hist2[i]) * len(l2) / (len(l1) + len(l2))
        chi2 += (hist2[i] - exp)**2 / exp
    p = st.distributions.chi2.isf(alpha, k-1)
    if p > chi2:
        return True
    else:
        return False

alpha = 0.1 
ID = 'naoki'

os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/result/data_clean')

file_name = ID + '_test1_clean.csv'
df = pd.read_csv(file_name,header = None)
test1 = df.values.flatten()
file_name = ID + '_test2_clean.csv'
df = pd.read_csv(file_name,header = None)
test2 = df.values.flatten()
file_name = ID + '_test3_clean.csv'
df = pd.read_csv(file_name,header = None)
test3 = df.values.flatten()
file_name = ID + '_test4_clean.csv'
df = pd.read_csv(file_name,header = None)
test4 = df.values.flatten()

result = []
tmp = ['', 'test1', 'test2', 'test3', 'test4']
result.append(tmp)
get_chi2_test(eval('test'+str(1)), test2, alpha)
for i in range(4):
    tmp = []
    tmp.append('test' + str(i+1))
    for j in range(4):
        if i == j:
            tmp.append('-')
        else:
            if get_chi2_test(eval('test'+str(i+1)), eval('test'+str(j+1)), alpha) == True:
                tmp.append('独立')
            else:
                tmp.append('独立でない')
    result.append(tmp)
    
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/result/')    
with open('chi2-test.csv', 'w', encoding="utf_8_sig") as f:
    writer = csv.writer(f)
    writer.writerows(result)