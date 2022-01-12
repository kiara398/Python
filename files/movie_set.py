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
# print(data[["Revenue (Millions)"]])
#Getting multiple data frames from data series
# print(data[["Year", "Rating", "Revenue (Millions)"]])


# HOW TO ACCESS SPECIFIC ROW WE NEED FROM OUR DATA
# we use loc and iloc methods
# suicideRow = indexed_Data.loc[["Suicide Squad"]][["Genre", "Rating", "Year", "Revenue (Millions)"]]
# print(suicideRow)

# #i(indexing location) in iloc means indexing
# suicide_I = data.iloc[10:15][["Title", "Director", "Year", "Revenue (Millions)"]]
# print(suicide_I)


# Looking at Data Selection
# How we can filter our data
yearBetween = data[((data['Year'] >= 2010)&(data['Year']<=2011))]
print(yearBetween)

