# from random import *
import random
# between 0-1 (15 decimal point)
print(random.random())

print(random.randint(111111,999999))

print(random.uniform(10.2,20.5))

print(random.randrange(1,100,5))
ls = [1,12,93,400,57,60]

print(random.choice(ls))
print(random.sample(ls,3))
random.shuffle(ls)
print(ls)

