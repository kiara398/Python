import pandas as pd
# creating a serie
# myList = [10,20,30,40,50,60, 70, 80, 90]
# firstSerie = pd.Series(myList)
# print("The series values are: ", firstSerie.values ) 
# print("The index values of the serie are: ", firstSerie.index.values)
# secondSerie =pd.Series(myList, index = ["Uganda", "Rwanda", "Congo", "Ghana", "Moroco", "Angola", "Tunisia", "Kenya", "Tanzania"])
# print("Rugby Scores for Countries", secondSerie)

# serieCopy = myList[1:4]
# print(serieCopy)
# print(secondSerie["Moroco"])

# working with a dictionary
# fruits = {"apples":40, "bananas": 50, "grapes": 80, "mangoes": 20, "oranges": 30}
# fruitSerie = pd.Series(fruits)
# print("Fruits and quantities on market: ", fruitSerie)
# print(fruitSerie["grapes"])



# Converting a data frame from a data serie
my_Marks = pd.Series([45,56,76,53,34], index = ["Math", "Science", "SST",  "English", "GP"])
print("Marks obtained by the student are: ", my_Marks)

df_marks = pd.DataFrame(my_Marks, columns = ["student1"])
print("The dataframe created from the data series is:\n ", df_marks)

# #Example
heights = pd.Series([5.3, 5.8, 5.0,4.7], index = ["winnie", "mark", "collines", "Fred"])
weights = pd.Series([60, 70, 90, 40], index = ["winnie", "mark", "collines", "Fred"])

df_person = pd.DataFrame({"Heights":heights, "Weights": weights})
print("The personal details are: \n", df_person)

