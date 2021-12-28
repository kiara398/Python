



class Car:
    pass 
#the word pass is a phrase word to ignore in python


print(Car())

# instances of the class car 
nissan = Car()
toyota = Car()
mitsubishi = Car()
ford = Car()
 
print(nissan == toyota)


# defining a class with properties, attributes or characters
# in python , defining properties or structures of a an object we use __int__() method
# RULE, self is the first attribute of an object
# self - keyword used to identify properties of a class 
# name , color, model nd prices are parameters to be assigned to the propertiesof the class
# init - intialising
class Phone:
    def __int__(self, name1, model1, color1, price1):
        self.name = name1
        self.model = model1
        self.color = color1
        self.price = price1


tecno = Phone('tecno', 'camon15', 'blue', 700)
samsung = Phone('sumsang', 'galaxyprime', 'white', 800)
iphone = Phone('iphone', '12', 'grey', 1800)

tecno.name = 2222
print(tecno.name)
# print(Phone())
