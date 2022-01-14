import pandas as pd

#Read data from our data file
data = pd.read_csv('IMDB-Movie-Data.csv')

#reading data with specific explicit index
indexed_Data = pd.read_csv('IMDB-Movie-Data.csv', index_col="Title")

#Viewing data from the source
#head gives you the first five rows and tail gives the last five rows
print(data.head())
print(data.tail())

#understanding information about the data
print(data.info())
#Getting a statistical summary of the data frame
# print(data.shape)
# #Getting a data series from the data frame
# print(data.describe())
print(data["Rank"])
# #Getting a data frame from within the data serie
# print(data[["Revenue (Millions)"]])
# #Getting multiple data frames from data series
# print(data[["Year", "Rating", "Revenue (Millions)"]])


# HOW TO ACCESS SPECIFIC ROW WE NEED FROM OUR DATA
# we use loc and iloc methods
suicideRow = indexed_Data.loc[["Suicide Squad"]][["Genre", "Rating", "Year", "Revenue (Millions)"]]
print(suicideRow)

# #i(indexing location) in iloc means indexing
# suicide_I = data.iloc[10:15][["Title", "Director", "Year", "Revenue (Millions)"]]
# print(suicide_I)


# Looking at Data Selection
# How we can filter our data
# yearBetween = data[((data['Year'] >= 2010)&(data['Year']<=2011)&(data['Rating']< 6.0))]
# print(yearBetween)


# === GROUP BY OPERATION ON THE DATA ===
#first five rows but not in order
directorData = data.groupby('Director')[['Rating']].mean().head()
print(directorData)

# min average(rating of each director ) last five rows
averageData = data.groupby('Director')[['Rating']].min().tail()
print(averageData)

# ===sorting OPERATIONS on our Data ===

sortedData = data.groupby('Director')[['Rating']].mean().sort_values(['Rating'], ascending=False).head()
print(sortedData)

# === Dealing with missing values in our dataset ===
missingValues = data.isnull().sum()
print(missingValues)

# ===Droping Row with null values ==
# This can be achieved using two methods...first:drop method.
# this ignores the column, inplace= Ture deleted the column tempoarily
# axis means we re dealing with column that is going to be dropped in this case 'Metascore' 
print(data.drop('Metascore', axis = 1).head())

# second method
# dropna will delete all columns of all missing values and null values
# print(data.dropna('Metascore', axis =1))

# filling missing values 
# meanRevenue = indexed_Data['Revenue (Millions)'].mean()
# print("The mean revenue is:", meanRevenue)

# handle missing values in the revenue
# indexed_Data['Revenue (Millions)'].fillna(meanRevenue, inplace=True)
# print(indexed_Data.isnull().sum())



