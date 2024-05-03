import mysql.connector as my
# from random import *
import random

# https://shorturl.at/aBKX5

#https://www.google.com (index/home/default -> )
# https://www.lnctu.ac.in
conn = my.connect(host="localhost",user = "root",password = "",database= "mcaapr24")
cur = conn.cursor()
# print(conn)

username = ""
logged_in = False

def main():
    print("#"*30)
    print("#"*5 + "QUIZ")
    print("""
            1. Register
            2. Login
            3. Attempt Quiz
            4. Result
            5. Exit
    """)
    choice = input("Choose an option 1/2/3/4/5 to process: ")
    print(choice)
    if choice == '1':
        register()
    elif choice  == '2':
        login()
    elif choice == '3':
        attemptQuiz()
    elif choice == '4':
        result()
    elif choice == '5':
        exitt()
    else:
        print("Please enter coorect option")
        main()

def register():
    name = input("NAME: ")
    enr = input("Enrollment: ")
    clg = input("College: ")
    psw = input("Password: ")
    con = input("contact: ")
    data = (name,enr,clg,psw,con)
    sql = "insert into register (name, enrollment, college, password, contact) values(%s,%s,%s,%s,%s)"

    cur.execute(sql,data)
    conn.commit()
    #SQL - Structure Query Language
    #MYSQL - DBMS vs RDBMS


def login():
    global username
    global logged_in
    uname = input("Enter username: ")
    # cur.execute('select password from register where enrollment = %s',(uname,))
    cur.execute('select * from register where enrollment = %s',(uname,))
    data = cur.fetchone() #fetchall
    print(data)
    if data is not None:
        try:
            pass
        except:
            pass
        pwd = input("Enter password: ")
        if data[4] == pwd:
            print(f"Welcome {data[1]}")
            username = uname
            logged_in = True
        else:
            print("Wrong password!!!")
    else:
        print("Wrong Username or you didn't registered with us!!!")
        ch = input("do you want to register!!! y/n")
        if ch=='y' or ch == 'Y':
            register()
        else:
            login()

    print("""
        Choose 1 for Attempt quiz
        Choose 2 for View result
        Choose 3 for Show profile
        Choose 4 for Update Profile
    """)
    ch = input("Enter your choice: ")
    if ch == '1':
        attemptQuiz(username)
    elif ch == '2':
        result()
    elif ch == '3':
        showProfile(data,logged_in)
    elif ch == '4':
        updateProfile(data,logged_in)

def updateProfile(log,user):
    pass

def showProfile(user,log):
    if log:
        print(f"HELLO {user[1]} Your college is {user[3]} Your contact number is {user[-1]}")
    ch = input("Do you want to update your profile: y/n")
    if ch == 'y' or ch == 'Y':
        updateProfile()

def attemptQuiz(uname):
    ch = input("Choose an option\n 1. Python\n 2. Maths\n 3. Java")
    if ch == '1':
        cat = "Python"
        sql = "select * from questions where category = 'Python'"
        cur.execute(sql)
        ques = cur.fetchall() #fetchone()
        print(ques) #[(),(),(),()]
        qu = [] #100
        for i in ques:
            qu.append(i) #[, , , , ,]
        qs = random.sample(qu,2) #14, 25, 89, 99
        n = 1
        correct = 0
        for i in qs:
            # op = [f"{i[2]}",f"{i[3]}",f"{i[4]},"f"{i[5]}"]
            # random.shuffle(op)
            print(f"HEllo {uname} you are attempting quiz of {i[-1]}")
            print(f"Q.{n}. {i[1]}\n A. {i[2]}\n B. {i[3]}\n C. {i[4]}\n D. {i[5]}\n")
            ans = input("Your Answer A/B/C/D: ").upper()
            if ans == i[-2]:
                correct += 1
            n = n+1
        
        sql_marks = "insert into result (user_id, category, marks) values(%s,%s,%s)"
        val_marks = (uname, cat, correct)
        cur.execute(sql_marks, val_marks)
        conn.commit()
        print(f"Your Result is {correct}")

    elif ch == '2':
        sql = "select * from questions where category = 'Maths'"
        cur.execute(sql)
        ques = cur.fetchall() #fetchone()
        print(ques) #[(),(),(),()]
        qu = [] #100
        for i in ques:
            qu.append(i) #[, , , , ,]
        qs = random.sample(qu,4) #14, 25, 89, 99
        n = 1
        correct = 0
        for i in qs:
            print(f"Q.{n}. {i[1]}\n A. {i[2]}\n B. {i[3]}\n C. {i[4]}\n D. {i[5]}\n")
            ans = input("Your Answer A/B/C/D: ").upper()
            if ans == i[-2]:
                correct += 1
            n = n+1
            
        print(f"Your Result is {correct}")

def result():
    pass

def exitt():
    print("Thanks foer visiting!!!")
    exit()

print("#"*30)

if __name__ == "__main__":
    main()



# WAP to Validate a password: uppercase,lowercase, digit, special char, len(8-20)