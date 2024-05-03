def validPass(pwd):
    l = u = d = s = 0
    if len(pwd) >= 8 and len(pwd)<= 20:
        for i in pwd:
            if i.isupper():
                u += 1
            elif i.islower():
                l += 1
            elif i.isdigit():
                d += 1
            else:
                s += 1
    if l > 0 and u >0 and d > 0 and s>0:
        return True
    else:
        return False

pwd = input("Enter your Password: ")
res = validPass(pwd)
if res:
    print("VALID PASSWORD")
else:
    print("INVALID PASSWORD")