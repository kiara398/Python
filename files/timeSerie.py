#Time Series is a set where values are measured at different points in time.
from datetime import date
import pandas as pd

import matplotlib.pyplot as plt


my_data = pd.read_csv('avocado.csv')
print(my_data.head(4))
print(my_data.dtypes)

my_data['Date'] = pd.to_datetime(my_data['Date'])
print(my_data.dtypes)

my_data = my_data.set_index('Date')
print(my_data)

my_dataframe = my_data[['AveragePrice', 'type', 'region']]
print(my_dataframe)

print(my_dataframe.loc['2015-12-06 '])
my_dataframe['AveragePrice'].plot()
plt.show()


# my_data['Year'] = pd.to_datetime(my_data['Year'])
# print(my_data)
# print(my_data.dtypes)
# print(my_data[['Year']])

# print(my_data[['Runtime (Minutes)']])

# my_dataframe = my_data[['Year', 'Director', 'Genre', 'Rating']]


# my_dataframe = my_dataframe.set_index('Year')
# print(my_dataframe)



# print(my_dataframe.index)
# print(my_dataframe.dtypes)


# print(my_dataframe.sample(5, random_state=0))


