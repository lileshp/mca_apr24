
username = ['john','sam','mac','peter']
password = {'john':'j123','sam':'s123','mac':'m123','peter':'p123'}
def login():
    uname = input("Enter your Username: ") #john
    if uname in username:
        pwd = input("Enter your password: ")
        if pwd == password[uname]:
            print(f"WELCOME {uname}")
        else:
            print("INVALID PASSWORD")
    else:
        print("INVALID USERNAME")


#FORMAT STRING

# name = input("NAME: ")
# city = input("City: ")
# age = input("Age: ")

# print("HEllo "+name + " You are from "+ city + ", You are "+age + "Years old")
# print("Hello {} You are from {}. You are {} Years old".format(name,city,age))
# print("Hello {1} You are from {0}. You are {2} Years old".format(name,city,age))
# print(f"Hello {name} You are from {city}. You are {age} Years old")