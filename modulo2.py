# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 19:52:39 2022

@author: anton
"""

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine('sqlite:///big_ban_theory.db')

archivo = r'C:\Users\anton\Downloads\big_bang_theory_dataset.csv'
df = pd.read_csv(archivo, encoding='UTF-8')
df.fillna('', inplace=True)

df.to_sql('big_ban_theory', engine, if_exists='replace')

df['Text'] = df['Text'].apply(lambda x: x.strip())
df_sheldon_penny = df[(df.Speaker == 'Sheldon') & (df.Text == 'Penny.')]
x = df_sheldon_penny['Location']

diff_locations = len(pd.unique(x))

plt.hist(x, bins=diff_locations, orientation='horizontal')
plt.show()

df_sheldon_contains_penny = df[(df.Speaker == 'Sheldon') & (df.Text.str.contains('Penny'))]

x = df_sheldon_contains_penny['Location']

diff_locations = len(pd.unique(x))

plt.hist(x, bins=diff_locations, orientation='horizontal')
plt.show()

df_scene_speaker = df[['Scene', 'Speaker']]

plt.scatter(df_scene_speaker['Speaker'], df_scene_speaker['Scene'], alpha=0.5)

plt.show()


