'''
Syntax
runtime error
'''
try:
    obj = open('result.txt','a')
    num1 =  int(input("NUM 1: "))
    num2 = int(input("NUM 2: "))
    res = num1/num2
    obj.write(str(res))
    print(res)
except TypeError:
    print("TYpe ERROR")
except ZeroDivisionError:
    print("You can not divide by Zero")
finally:
    print("FINAL")
    obj.close()
    print("FINAL")

print("HELLO")




# https://quizizz.com/join?gc=89311441