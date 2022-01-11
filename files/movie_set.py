import pandas as pd

#Read data from our data file
data = pd.read_csv('IMDB-Movie-Data.csv')

#reading data with specific explicit index
indexed_Data = pd.read_csv('IMDB-Movie-Data.csv', index_col="Title")

#Viewing data from the source
#head gives you the first five rows and tail gives the last five rows
# print(data.head())
# print(data.tail())

#understanding information about the data
# print(data.info())
#Getting a statistical summary of the data frame
# print(data.shape)
#Getting a data series from the data frame
# print(data.describe())
# print(data["Rank"])
#Getting a data frame from within the data serie
print(data[["Revenue (Millions)"]])
#Getting multiple data frames from data series
print(data[["Year", "Rating", "Revenue (Millions)"]])