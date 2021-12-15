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