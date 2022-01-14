import pandas as pd

#Read data from our data file
data = pd.read_csv('avocado.csv')

#reading data with specific explicit index
indexed_data = pd.read_csv('avocado.csv', index_col="Total Bags")

#understanding information about the data
print(data.info())

# #Returning the first five rows.
# print(data.head())
# #Returning the last five rows
# print(data.tail())

#Returning or printing a tuple of the DataFrame
#Thereare 18249 Rows and 14 columns
# print(data.shape)

# #Getting a data series from the data frame
print(data.describe())
#Returning the type of bags that were made.eg conventional and organic
# print(data["type"])

# #Getting multiple data frames from data series
print(data[["year", "type", "Total Volume", "region"]])

# # we use loc and iloc methods
# totalbagsRow = data.loc[["year"]][["type", "Total Volume", "Average Price"]]
# print(totalbagsRow )

# Looking at Data Selection and filtering our data
yearBetween = data[((data['year'] >= 2015)&(data['year']<=2016)&(data['AveragePrice']< 6.0))]
print(yearBetween)

#first five rows but not in order
bags = data.groupby('Date')[['Total Volume']].mean().head()
print(bags)

# min average(Total Volume ) last five rows
bagData = data.groupby('Date')[['Total Volume']].min().tail()
print(bagData)

#Dealing with missing values in our dataset
missingValues = data.isnull().sum()
print(missingValues)

print(data.drop(['4225', '4225', '4770', ], axis = 1).head())