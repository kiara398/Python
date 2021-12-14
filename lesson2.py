#We comment in python using # for singleline comment

"""
   #We comment in python using tripple quotations for
   multiline comment
"""

#These are statements
num,num2 = 10, 20
num =10
num2 = 20

# A function is a group of statement ...

#Exampl: belowis afunction to add two numbers
"""
def sum():
    num, num2 = 10, 20
    ans = num + num2
    print(ans)

   sum() #Invoking or calling a function
"""
# Example 2: afunction to ...
"""
def operators():
    print("Addition: 20 + 30")
    print(20 + 30)

    print("Subtraction: 50-10")
    print(50-10)

    print("Multiplication: 5 times 10")
    print(5 * 10)

    print("Division: 50 / 10")
    print(50 / 10)
    
operators()  
"""
# a function to demostrate the order of precedence
def precedence():
    """
        1: Parenthesis / Brackets ()
        2: Exponential (**)
        3: Unary Operators
            +=
            -=
        3.---
              3.1 Multiplication (*)
              3.2 Division (/)
              3.3 Floor diving (//) returns integer
        4. ---
             4.1 Addition (+)
             4.2 Subtration (-)
            
        5. Bitwise shift operators
           5.1 Bitwise shift greater than >>
           5.2 Bitwise shift greater than <<
        6. ---
           6.1 AND (ANDing) &
           6.2 XOR (XORing) ^
           6.3 OR (ORing) |
        7. ---
           Equal (==)
           Not equal (!=)  
           Greater than (>)
           Greater thank or equal to (>=)
           Less than (<)  
           Less thank or equal to (<=)
           is
           is not
           in
           not in


    """
    print(10-40*2)
    print((10-40)*2)

precedence()    


