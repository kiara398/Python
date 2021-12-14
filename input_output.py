# A program to input the Name, year of birth of the user and then outputs the age of the user


def user_age():
    name = input('Please input your name: ')
    year_of_birth = input('Please enter your Year of birth: ')
    age = 2021 - int(year_of_birth)
    print('Your name is: ' , name)
    print('Your year of birth is: ' , year_of_birth)
    print('Your age is: ' , age)

user_age()
