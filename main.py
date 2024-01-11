from mysql.connector import *
import datetime
def studentry():
    n=input('enter student name =')
    c=input('enter student class =')
    stream=input('enter student stream =')
    phone=input('enter student phone no =')
    email=input('enter student email id =')
    #Create the connection object   
    myconn = connect(host = "localhost", user = "root",passwd = "root")  
    #creating the cursor object  
    cur = myconn.cursor()  
    sql = "insert into student(s_name,s_class, s_stream, s_phone, s_email) values (%s, %s, %s, %s, %s)"  
    createtable1="create table IF NOT EXISTS student(sid int(5) primary key auto_increment, s_name char(20) not null, s_class varchar(6) not null, s_stream varchar(15) not null, s_phone varchar(11), s_email varchar(20))"  
    #The row values are provided in the form of tuple   
    val = (n, c, stream, phone, email)  
  
    try:
        cur.execute('create database IF NOT EXISTS library')
        cur.execute('use library')
        #inserting the values into the table
        cur.execute(createtable1)
        #myconn.commit()
        cur.execute(sql,val)
  
        #commit the transaction   
        myconn.commit()  
      
    except:  
        myconn.rollback()  
  
    print('------',cur.rowcount,"record inserted!-------")  
    myconn.close()
    print('---------------------------------------')

def bookentry():
    bname=input('Enter book name =')
    writer=input('Enter Book Writer =')
    pubname=input('Enter Book Publisher Name =')
    edition=input('Enter Book Edition =')
    pageno=input('Enter total pages =')

    #Create the connection object   
    myconn = connect(host = "localhost", user = "root",passwd = "root",database = "library")  
    #creating the cursor object  
    cur = myconn.cursor()  
    sql = "insert into book(b_name,b_writer, b_publisher, b_edition, b_page) values (%s, %s, %s, %s, %s)"  
    createtable2="create table IF NOT EXISTS book(bid int(5) primary key auto_increment, b_name varchar(20) not null, b_writer varchar(20) not null, b_publisher varchar(20) not null, b_edition varchar(8), b_page varchar(4))" 
    #The row values are provided in the form of tuple   
    val = (bname, writer, pubname, edition, pageno)  
  
    try:
        cur.execute('create database IF NOT EXISTS library')
        cur.execute('use library')
        #inserting the values into the table
        cur.execute(createtable2)
        cur.execute(sql,val)  
        #commit the transaction   
        myconn.commit()  
      
    except:  
        myconn.rollback()  
  
    print('------',cur.rowcount,"record inserted!-------")
    print('---------------------------------------')
    myconn.close()  

def assignbooks():
    
    s_ID=int(input("enter student id ="))
    b_ID=int(input("Enter book id =")) 
    #date=(input("Enter date taken('yyyy-mm--dd')=")) #cant incorprate /
    myconn = connect(host = "localhost", user = "root",passwd = "root",database = "library")
    cur=myconn.cursor()
    
    x = datetime.datetime.now()
    #now_date=str(x.year)+'-'+str(x.month)+'-'+str(x.strftime('%d'))
    now_date=x.strftime('%Y-%m-%d')
    #print(now_date)
    d = datetime.timedelta(days = 15)
    due=x+d
    due_date=due.strftime('%Y-%m-%d')
    #print(type(due_date))
    
    
    q="insert into assign_books(sid,bid,assign_date,due_date) values (%s,%s,%s,%s)"
    createtable3="create table IF NOT EXISTS assign_books(sid int not null, bid int not null, assign_date date, due_date date)"
    #q="insert into assign_books(sid,bid) values (%s,%s)"
    val=(s_ID,b_ID,now_date,due_date)
    #val=(s_ID,b_ID)
    try:
        cur.execute('create database IF NOT EXISTS library')
        cur.execute('use library')
        cur.execute(createtable3)
        cur.execute(q,val)
        myconn.commit()
    except:
        myconn.rollback()
    print('------',cur.rowcount,"record inserted!-------")
    print('---------------------------------------')
    
def fine():
    sid=int(input('enter student id ='))
    myconn =connect(host = "localhost", user = "root",passwd = "root",database = "library")  
  
    #creating the cursor object  
    cur = myconn.cursor()  
    q="select * from assign_books where sid='%s'"%(sid)
    charges=20
    #rdate=datetime.datetime.now().strftime('%Y-%m-%d')
    rdate=datetime.date.today()
    try:  
        #Reading the Employee data      
        cur.execute(q)  
        #fetching the rows from the cursor object  
        result=cur.fetchall()  
        #printing the result
        for x in result:
            #due=x[3]
            if rdate > x[3]:
                due=x[3]
                d=(due-rdate).days
                charges= charges + (d*2)
            else:
                charges=0
    except:  
        myconn.rollback()  
    
    myconn.close()
    
    print("Your fine is=",charges)
    
print('--------------------------')
print('Library Management System')
print('--------------------------')
while True:
    print('1.Enter the Student Details')
    print('2.Enter the New Book Details')
    print('3.Assign Books to Students')
    print('4.Search the Books')
    print('5.Book Fine')
    print('6.Exit')
    choice=int(input('enter choice what u want to process ='))
    if choice==1:
        studentry()
    if choice==2:
        bookentry()
    if choice==3:
        assignbooks()
    if choice==4:
        print('A. Search by book name')
        print('B. search by book author')
        print('C. search by book publisher')
        way=input("Enter choice A/B/C=")
        if way=="A":
            name=input("Enter book name you want to search=")
            myconn =connect(host = "localhost", user = "root",passwd = "root",database = "library")  
  
            #creating the cursor object  
            cur = myconn.cursor()  
            q="select * from book where b_name='%s'"%(name)
            try:  
                #Reading the Employee data      
                cur.execute(q)  
                #print('hello')
                #fetching the rows from the cursor object  
                result=cur.fetchmany()  
                #printing the result  
      
                for x in result:  
                    print(x);  
            except:  
                myconn.rollback()  
  
            myconn.close()  
        if way=="B":
            auth=input("Enter author of the book=")
            myconn =connect(host = "localhost", user = "root",passwd = "root",database = "library")  
  
            #creating the cursor object  
            cur = myconn.cursor()  
            q="select * from book where b_writer='%s'"%(auth)
            try:  
                #Reading the Employee data      
                cur.execute(q)  
                #print('hello')
                #fetching the rows from the cursor object  
                result=cur.fetchmany()  
                #printing the result  
      
                for x in result:  
                    print(x);  
            except:  
                myconn.rollback()  
  
            myconn.close()  
        if way=="C":
            publi=input("Enter publisher of the book=")
            myconn =connect(host = "localhost", user = "root",passwd = "root",database = "library")  
  
            #creating the cursor object  
            cur = myconn.cursor()  
            q="select * from book where b_publisher='%s'"%(publi)
            try:  
                #Reading the Employee data      
                cur.execute(q)  
                #print('hello')
                #fetching the rows from the cursor object  
                result=cur.fetchmany()  
                #printing the result  
      
                for x in result:  
                    print(x);  
            except:  
                myconn.rollback()  
  
            myconn.close()  
    if choice==5:
        fine()
    if choice==6:
        print('do u want to exit from application')
        e=input('enter the Y or y for exit=')
        if e=='Y' or e=='y':
            exit()