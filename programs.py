#Q.1 Write a program to find the sum of digits of number accepted from the user.
# e.g. : 15757 output: 

num = int(input("Enter a number: ")) #124
sum = 0
rev = 0
ev = od = 0
while num > 0:
    rem = num % 10 #4 2 1
    if rem % 2 == 0:
        ev += rem
    else:
        od += rem
    rev = rev * 10 + rem #4 * 10 + 2 = 42 * 10 + 1 = 421
    sum = sum + rem #0 + 4 = 4 + 2 = 6 + 1 = 7
    num = num // 10 #0
if num == rev:
    print("PALINDROM")
else:
    print("NOt a palindrom")
#Q.2 Write a program to check that given number is palindrom or not.