import mysql.connector as sqltor
con=sqltor.connect(host="localhost",user="root",passwd="root", db="railway_reservation", autocommit=True)
cur=con.cursor()
cur.execute("create table accounts(Fname varchar(30),Lname varchar(30),user_name varchar(100),passwd varchar(100),Phno varchar(20),DOB date,AGE integer,GENDER varchar(30))")
cur.execute("create table railway(NAME varchar(30),BOARDING_STN varchar(100),DESTINATION_STN varchar(100),Phno varchar(20),DOJ date,AGE integer,GENDER varchar(30))")


def menu():
    print("1. YES")
    print("2. NO")
    a=int(input(("DO YOU WANT TO CONTINUE?? : ")))
    if a==1:
        print("WELCOMEE TO ONLINE RAILWAY RESERVATION SYSREM!!")
        print("1. SIGN IN")
        print("2. SIGN UP")
        print("3. DELETE ACCOUNT")
        print("4. EXIT")
        b=int(input("ENTER YOUR CHOICE : "))
        if b==1:
            sign_in()
        elif b==2:
            sign_up()
        elif b==3:
            delete_account()
        elif b==4:
            print("THANKS FOR YOUR TIME...")
            
    elif a==2:
        print("THANKS FOR YOUR TIME!!")
        
    else:
        print("ERROR 404: PAGE NOT FOUND")


def main():
    print("1. YES")
    print("2. NO")
    c=int(input("DO YOU WANT TO CONTINUE?? : "))
    if c==1:
        print("1. TICKET BOOKING \n 2. TICKET CANCELLING \n 3. TICKET CHECKING \n 4. ACCOUNT DETAILS \n 5. LOGOUT")
        d=int(input("WHAT DO YOU WANT TO DO? : "))
        if d==1:
            ticket_booking()
        elif d==2:
            ticket_cancelling()
        elif d==3:
            ticket_checking()
        elif d==4:
            account_details()
        elif d==5:
            print("THANKS FOR YOUR TIME...")
    elif c==2:
        print("THANKS FOR YOUR TIME!!")
        
    else:
        print("ERROR 404: PAGE NOT FOUND")


def ticket_booking():
    nm=input("Enter Your Full Name : ")
    phn=int(input("Enter Your Mobile Number : "))
    age= int(input("Enter Your Age : "))
    gender=input("Enter Your Gender ('MALE', 'FEMALE', 'NOTA') : ")
    doj=(input("Enter Date Of Journey ('yyyy/mm/dd') : "))
    bds=input("Enter Your Boarding Station : ")
    dst=input("Enter Your Destination Station : ")
    s1="insert into railway values ('{}','{}','{}','{}','{}','{}','{}')".format(nm,bds,dst,phn,doj,age,gender)
    cur.execute(s1)
    cur.execute("select*from railway")
    m=cur.fetchall()
    print("TICKET BOOKED SUCESSFULLY!!")
    print("HERE IS YOUR TICKET \n ",m)
    


def ticket_cancelling():
    print("1.YES")
    print("2.NO")
    e=int(input("DO YOU WANT TO CONTINUE?"))
    if e==1:
        phn=int(input("ENTER PHONE NUMBER"))
        s2="delete from railway where Phno='{}'".format(phn)
        cur.execute(s2)
        print("TICKET CANCELLED!!")
    elif e==2:
        print("THANK YOU!!")
    
        
    
def delete_account():
    phn=input("Enter Your Mobile Number")
    s4="delete from accounts where Phno= '{}'".format(phn)
    cur.execute(s4)
    print("ACCOUNT DELETED SUCESSFULLY!!")
    
    
def sign_up():
    fn=input("Enter Your First Name : ")
    ln=input("Enter Your Last Name : ")
    phn=int(input("Enter Your Mobile Number : "))
    age= int(input("Enter Your Age : "))
    gender=input("Enter Your Gender ('MALE', 'FEMALE', 'NOTA') : ")
    dob=(input("Enter Date Of Birth('yyyy/mm/dd') : "))
    usn=input("Enter A User Name : ")
    psd=input("Make Your Password : ")
    s3="insert into accounts values ('{}','{}','{}','{}','{}','{}','{}','{}')".format(fn,ln,usn,psd,phn,dob,age,gender)
    cur.execute(s3)
    cur.execute("select*from accounts")
    p=cur.fetchall()
    if len(p)!=0:
        print("ACCOUNT CREATED!!")
        print(p)
    else:
        print("Oops...there seems to be an existing account with this username and password")
    

    
def account_details():
    usn=input("ENTER YOUR USER NAME : ")
    psd=input("ENTER YOUR PASSWORD : ")
    phn=int(input("ENTER YOUR MOBILE NUMBER : "))
    s5="select * from accounts where Phno = '{}'".format(phn)
    cur.execute(s5)
    q=cur.fetchall()
    print(q)

def sign_in():
    usn=input("ENTER YOUR USER NAME : ")
    psd=input("ENTER YOUR PASSWORD : ")
    phn=int(input("ENTER YOUR MOBILE NUMBER : "))
    s6="select Fname,Lname from accounts where Phno='{}'".format(phn)
    cur.execute(s6)
    r=cur.fetchall()
    if len(r)!=0:
        print("WELCOME",r)
    else:
        print("ACCOUNT DO NOT EXIST...")
    main()
def ticket_checking():
    usn=input("ENTER YOUR USER NAME : ")
    psd=input("ENTER YOUR PASSWORD : ")
    phn=int(input("ENTER YOUR MOBILE NUMBER : "))
    s7= "select * from railway where Phno = '{}'".format(phn)
    cur.execute(s7)
    i=cur.fetchall()
    if len(i)!=0:
        print("HERE IS YOUR TICKET \n ",i)





menu()

    
