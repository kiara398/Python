
numbers = [23,2,3,45,6,7,98,7,4,4,1,1,2]
sum=0

for fred in numbers:
    if fred%2 !=0:
        print(fred)

    sum = sum + fred

print(sum)


index = 0
total = 0

#while loop
#len is a funtion in python that considers length 
while index < len(numbers):
    num = numbers[index]
    if num > 0:
        print(num)
        total += numbers[index]
    index +=1

print('This is the total', total)
