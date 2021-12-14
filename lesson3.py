#Conditionals
#loops and conditions are what we call control statements

num1 = 1
num2 = 0
if num1 != num2:
    print(num1)


#Else
num3 = 3
num4 = -5
if num3 >= num4:
    print('Num3 is a positive number')

else :
    print ('Num3 is negative')

#elif
num5 = 3.4
if num5 > 0:
    print ('Num5 is positive')

elif num5 == 0 :
    print('Num5 is zero')
else :
    print('Negative')


#LOOPS
#for loop (commonly used loop)
for i in range(10) :
    print(i)

#example 2, 
mylist = [6,5,3,8,2,5,4,11]
sum = 0
for item in mylist :
    sum = sum + item
    #ans = sum + item
print('total is', sum)
#print('ans is', ans)




