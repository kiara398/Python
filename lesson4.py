numbers = [23,2,3,45,6,7,98,7,4,4,1,1,2]
sum=0

for fred in numbers:
    if fred%2 !=0:
        print(fred)

    sum = sum + fred

print(sum)