import mysql.connector as a
con=a.connect(host="localhost",
              user="root",
              password="Akanksha@13",
              database="library"
)

def addbook():
    bn=input("Enter Book Name :")
    c=input("Enter Book Code :")
    t=input("Total Books :")
    s=input("Enter Subject :")
    data=(bn,c,t,s)
    sql='insert into books values(%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">*****************************************<")
    print("Data entered Successfully")
    main()

def issuebook():
    n=input("Enter name :")
    r=input("Enter reg No:")
    co=input("Enter Book Code:")
    d=input("Enter Date:")
    a="insert into issue values(%s,%s,%s,%s)"
    data=(n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print(">*****************************************<")
    print("Book issued to:" ,n)
    bookup(co,-1)
    

def Subittedbook():
    n=input("Enter name :")
    r=input("Enter reg No:")
    co=input("Enter Book Code:")
    d=input("Enter Date:")
    a="insert into submit values(%s,%s,%s,%s)"
    data=(n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print(">*****************************************<")
    print("Book Submitted by :" ,n)
    bookup(co,1)

def bookup(co,u):
    a="select TOTAL from books where BCODE=%s"
    data=(co,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    t= myresult[0]+u
    sql="update books set TOTAL=%s where BCODE=%s"
    d=(t,co)
    c.execute(sql,d)
    con.commit()
    main()

def dbook():
    ac=input("Enter Book Code :")
    a="delete from books where BCODE=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    main()

def dispbook():
    a="select* from books"
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("Book Name :",i[0])
        print("Book Code :",i[1])
        print("Total :",i[2])
        print(">*****************************************<")
    main()

def main():

    print("""
                    LIBRARY MANAGER

     1.ADD BOOK
     2.ISSUE BOOK
     3.SUBMIT BOOK
     4.DELETE BOOK
     5.DISPLAY BOOKS
     """)

    choice=input("Enter Task NO :")
    print(">*****************************************<")

    if (choice=='1'):
        addbook()

    elif (choice=='2'):
        issuebook()

    elif (choice=='3'):
        Subittedbook()

    elif (choice=='4'):
        dbook()

    elif (choice=='5'):
        dispbook()

    else:
        print("Wrong Choice:")
        main()

def pswd():
    ps=input("Enter Password:")
    if ps=="1234":
        main()
    else:
        print("Wrong password")
        pswd()

pswd()
