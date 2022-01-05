#OOP Programming
#An object is an instance of a class
#Am object of a class is identified by the key word 'is a'
#A class of an object is identified by the key word class followed by the name of the class

class Car:
    pass
#the word pass is a phase word to 'ignore' in python 
print(Car())

pajero = Car()
nissan = Car()
toyota = Car()
subaru = Car()
ford = Car()
mitsubishi = Car()
print (nissan == toyota)


#Creating a class with attributes.
class Phone:
    def __init__(self,phonename,phonemodel,phonebrand,phonecolor,phoneprice):
        self.name =  phonename
        self.model = phonemodel
        self.brand = phonebrand
        self.color = phonecolor
        self.price = phoneprice
iphone = Phone('iphone13', 'iphone','apple','white','$2000')   
samsung = Phone('note10plus', 'note','samsung','aura black','$1500')
tecno = Phone('Camon11', 'Camon','tecno','black','$500')   
print(iphone.price)  
print(samsung.name) 
iphone.price = '$900'
print(iphone.price)   
       
# __init__()for definining properites of the object.        
#As a rule in python the first attribute is always self
#name,model,brand,color,price are parameters. self is a keyword used to indentify properties of an object

"""
class Animal:
    def __init__(self,name,type,) :
        
"""               
    