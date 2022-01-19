# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 14:44:51 2022

@author: nicks
"""

import pandas as pd

import matplotlib.pyplot as  plt
ax=plt.gca()
movie_data=pd.read_csv('IMDB-Movie-Data.csv')

indexed_data =pd.read_csv('IMDB-Movie-Data.csv',index_col="Title")


print(movie_data[['Revenue (Millions)']])

visualOne=movie_data[['Revenue (Millions)','Title','Rating']]

print(visualOne)

visualOne.plot(kind='scatter',x='Title',y='Revenue (Millions)',ax=ax)
visualOne.plot(kind='line', color= 'Red',y='Rating',ax=ax)

plt.show()

print(movie_data.info())

print(movie_data[['Director']])

slicedSsr=movie_data.iloc[[0]][['Title','Revenue (Millions)']]
print(slicedSsr)

