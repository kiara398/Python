#sets - unordered, unchangable, unindexed collection.
#it allows no duplicate values.
#sets are used to store multiple items in a single variable
#sets identified by curl braces
my_set={2,4,4,5,"grace", 55, 55}
print(my_set)
print(len(my_set))

print(type(my_set))

this_set = set((2,3,65,23,89)) #set constructor uses set method to create a set 
print(this_set)

#accessing items using loops
for x in my_set:
    print(x)

print("grace" in my_set) 


#adding an items
my_set.add("Fred")
print(my_set)

#adding items from another set
other_set = {8,6,10,"Kwesiga"}
my_set.update(other_set)
print(my_set)

other_list = [2,55,78, "dref"]
my_set.update(other_list)
print(my_set)

my_set.update(("bob", "winnie"))
print(my_set)

my_set.update(("rob", "romeo"))
print(my_set)


#removing items(remove or discard methods)
my_set.discard("dref")
print(my_set)

x = my_set.pop()#pop method removes random item
print(x)
print(my_set)

"""
my_set.clear()
print(my_set)


a_set={1,3,5,6,6}
del a_set
print(a_set)
"""

members={"grace", "ushinde", "winnie", "dora"}
for item in members:
    print(item)

#joining sets
#using update method
set_one = {34,56,77,66,6}
set_two = {"boy", "girl", "unisex"}
set_three = set_one.union(set_two)
print(set_three)

set_un = {34,56,77,66,6}
set_deux = {"boy", "girl", "unisex"}
set_un.update(set_deux)
print(set_un)

#keeping duplicate values
numbers = {1,2,3,3,5,5,66,"five"}
letters = {"a", "b",5,3,"c"}

numbers.intersection_update(letters)
print(numbers)
#using intersection method
random_one={1,2,3,5,"five"}
random_two = {"a","b", 5, 3, "c", "five"}
random_three = random_one.intersection(random_two)
print(random_three, "another string")


#getting uncommon items
#
nums = {1,2,3,5,"five"}
lets={"a","b", 5, 3, "c", "five"}
nums.symmetric_difference_update(lets)
print(nums)

num1 = {1,2,3,5,"five"}
num2 = {"a","b", 5, 3, "c", "five"}
num3 = num1.symmetric_difference(num2)
print(num3)


