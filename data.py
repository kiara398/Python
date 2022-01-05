import pandas as pd
# creating a serie
myList = [10,20,30,40,50,60, 70, 80, "wululu"]
firstSerie = pd.Series(myList)
print("The series values are: ", firstSerie.values ) 
print("The index values of the serie are: ", firstSerie.index.values)
secondSerie =pd.Series(myList, index = ["Uganda", "Rwanda", "Congo", "Ghana", "Moroco", "Angola", "Tunisia", "Kenya", "Tanzania"])
print("Rugby Scores for Countries", secondSerie)

serieCopy = myList[1:4]
print(serieCopy)
print(secondSerie["Moroco"])

# working with a dictionary
fruits = {"apples":40, "bananas": 50, "grapes": 80, "mangoes": 20, "oranges": 30}
fruitSerie = pd.Series(fruits)
print("Fruits and quantities on market: ", fruitSerie)
print(fruitSerie["grapes"])
