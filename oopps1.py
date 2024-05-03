ls = [1,2,3,4,5,6]

ls2 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
# 1,2,3,4,5,6,7,8,9
# 1,4,7,2,5,8,3,6,9

'''
    Class:

    Object:
    Methods: behaviour of object
    Attributes: characterstics of object

    FEatures:
        1. Inheritance
        2. Polymorphism
        3. Abstraction
        4. Encapsulation
'''
# https://github.com/lileshp/mca_apr24.git

# import show
# import show as sh
# from show import *
# from . import show

class Exercise:
    city = "BHOPAL" #Class variable
    #CONSTRUCTOR
    def __init__(self,uname,pwd):
        self.u = uname
        self.p = pwd

    def reverseNumber(ab):
        if ab.u == "abc" and ab.p == "1234":
            pass
        print(f"{ab.number}")

    def palindromNumber(self,num):
        self.number = num #instance variable
        result = 0 # local/method variable
        print("PALINDROM")

# obj = Exercise('abc','1234') 
# obj.palindromNumber(452)

#packages, modules/
# library - Numpy, jquery, reactJS
# framework - django, bootstrap, spring boot

# __init__.py

class A:
    pass
class C(A):
    pass
class D():
    pass
class B(C, D):
    pass
class E(D):
    pass

# https://quizizz.com/join?gc=77616593