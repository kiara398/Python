
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

=======
# list is identified by square brackets []
# tuple is identified by parentheses ()
# dictionary is identified by curly braces {}
# a set is identified by parentheses ()


#A list is used to store elements of different datatypes
numbers = []
numbers2 = [2,4,6,8,6,5,4,3,2,1,'Kiara']
print(numbers2[3])
print(numbers2[0])
print(numbers2[-1])

num2 = numbers2[:]
print(num2)

#range of elements
num3 = num2[1:4]
print(num3)
#a list is a mutable object. it allows us to add or remove anything within it after it has been created.

numbers.append([1,2,3,4,5,6,7,8])  #adding an element to an existing empty list
numbers.append([10])
print(numbers)
print(numbers[-1])

numbers[1].append(20)
print(numbers)

print(numbers[0][7])

#list of names
guests = ['Ozzy', 'Jacksen', 'David', 'Skylar', 'Skylar', 'Whitney', 'Fred', 'Alicia']
guests.sort(reverse=True)  #reversing the order of the values.
print(guests)

#using set to emit repeated values
print(set(guests))

#using pop to remove the last element
# guests.pop()
# print(guests)

guests.remove('Ozzy')
print(guests)

#deleting in ranges
del guests[2:4]
print(guests)

