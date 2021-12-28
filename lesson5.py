#A list is identified by square braces []
#A tuple is identified with parenthesis ()
#A dictionary is identified by braces {}
#A set is identified by parenthesis ()
#A  list is useed to store elements or items of different data types

numbers = []
num = [24,10,13,6,9,8,17,5,4, 'Lucky Dube']
print(num[0])
print(num[-1])

#num2 is having all the values of 
num2 = num[:]
print(num2)

#range of elements of nums
num3 = num2[1:4]
print(num3)

#a list is a mutable object, in that allows us to move anything within once its created
numbers.append([1, 2,3,4,5,6,7,8])
numbers.append([10])
print(numbers)

print(numbers[-1])
numbers[-1].append(20)
print(numbers)

#printing element 8 in the first list of numbers
print(numbers[0][7])

#a list of names
guests = ['Dube', 'John', 'Fred', 'Emma', 'Mark', 'Abalo', 'Zac', 'Fred', 'Yassin']
#reversing the sor Z-A
guests.sort(reverse=True)
print(guests)

#set removes repeated values in a list
#print(set(guests))

#Removing the last element in a guests list- pop() function
#guests.pop()
guests.remove('Dube')
print(guests)


