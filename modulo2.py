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
freq = df_sheldon_penny.groupby('Location').count()
x = freq.index
y = freq['Text']
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
plt.show()