'''
DATATYPES
Date: 12-Apr-24
Time: 10:30 to 12:10
MCA 2nd Sem
Lilesh Pathe
'''
'''
Data: raw facts/figures
Datatypes:
    To store data in memory and Database
    to process/operation

Number
String
Datetime

program memory
directory/ File structure/ system -> File system
Cloud/Server


    Number
        int(), float()
        0-9 digit
        immutable object
    String
        str()
        group of characters enclosed in quotes
        ' '
        " "
        ''' '''
        immutable object
        iterable object
        subscriptable object, indexing
        concatenation:
        slicing operator
            [startIndex: endIndex: steps]
    List - Dynamic Array
        list()
        []
        is an ordered collection of multiple elements, elements can be different types
        mutable object
        iterable/subscriptable/indexable

        Deep copy vs Shallow copy
    Tuple
        tuple()
        ()
        is an ordered collection of multiple elements, elements can be different types
        immutable object
        iterable/subscriptable/indexable
        index, count

    Dictionary
        dict()
        {}
        is an unordered collection of multiple elements in key value pair.
        key: any immutable object (int, str, tuple)
        value: any data types

        mutable object
        iterable but not indexable
    set
        set()
        {}
        unordered collection of multiple unique elements
        mutable
        iterable but not indexable

    frozenset
        frozenset()
        {}
        unordered collection of multiple unique elements
        immutable
        iterable but not indexable
    Boolean
'''
# a = input() # 100
# b = input() # '200'
# c = a + b #300

name = 'john'
city = "bhopal"
blog = """First line
second line."""


# name = input("Enter your Name: ") #john cena
# print(len(name))


name  = ["0103CA231387","0103CA231388","0103CA231389"]
newList = []
for i in name:
    temp = i[0:4]
    newCode = "1111"
    newList.append(i.replace(temp,newCode))
print(newList)



'''
DOCSTRING
Hello i am john
'''