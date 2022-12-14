# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 19:52:39 2022

@author: anton
"""

import pandas as pd
import matplotlib.pyplot as plt

archivo = r'C:\Users\anton\Downloads\big_bang_theory_dataset.csv'
df = pd.read_csv(archivo, encoding='UTF-8')
df.fillna('', inplace=True)
df['Text'] = df['Text'].apply(lambda x: x.strip())
df_sheldon_penny = df[(df.Speaker == 'Sheldon') & (df.Text == 'Penny.')]
x = df_sheldon_penny['Location']

plt.hist(x, bins=len(x), orientation='horizontal')
plt.show()
