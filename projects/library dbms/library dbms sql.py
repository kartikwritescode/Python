#Library management system
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234')
mycursor=mydb.cursor()
print('''
__________________________________
Welcome to Library Management System
__________________________________
''')
#creating database
mycursor.execute("create database if not exists library_3") #Database will only be created if it doesn't exist.
mycursor.execute("use library_3") #Using the created database
mycursor.execute("create table if not exists available_books(id int, name varchar(25),subject varchar(25),quantity int)") #Table no         
mycursor.execute("create table if not exists issued(id int,name varchar(25),subject varchar(25), s_name varchar(25),s_class varchar(25))") #primary screen ke sub parts yani second screens ke table hain yeh sab
mycursor.execute("create table if not exists login(user varchar(25),password varchar(25))")
mydb.commit() #to save all the changes made in the database
flag=0 #variable 
mycursor.execute("select * from login") #sab kuch select krliya uss login wale table se (taki pta lage ki empty hai ki nahi) taki jab woh content submit kare toh ek hi baar kare
for i in mycursor: #agar yeh loop chalega hence we conclude that the table had sum value
    flag=1 #kuch value ayi yani value thi
if flag==0: #mtlb koi value phle se nahi thi
    mycursor.execute("insert into login values('user','sks')")
    mydb.commit()
##################Loops#############################
    
def new_func():
    else

while True:
    print("""
1.Login
2.Exit
""")
    ch=int(input("Enter your choice:"))
    if ch==1:
        pas=input("Enter password:")
        mycursor.execute("select * from login")
        for i in mycursor: #(x,y) = var1(name),var2(pass)
            t_user,t_pass=i
        if pas==t_pass:
            print("Login successfully...")
            loop1='n'#loop regarding leaving the program as for (yes/no) 
            while loop1=='n':
                print('''
______________________________
1.Add New Books
2.Remove Any Book
3.Issue Book To Student
4.Return Book
5.View Available Books
6.View Issued Books
7.Logout
_____________________________ 

''')
                
            
                ch=int(input("Enter your choice:"))
                if ch==1:
                    loop2='y'#loop regarding adding books for more than one time
                    while loop2=='y':
                        print("All information is mandatory to be filled!!")
                        idd=int(input("Enter book ID:"))
                        name=input("Enter book name:")
                        subject=input("Enter the Subject:")
                        quan=int(input("Enter Quantity:"))
                        mycursor.execute("insert into available_books values('"+str(idd)+"','"+name+"','"+subject+"','"+str(quan)+"')")
                        mydb.commit()
                        print("Data Inserted Successfully...")
                        loop2=input("Do you wish to add another book?(y/n)").lower()
                    loop1=input("Do you want to logout?(y/n)").lower()
                     
                elif ch==2: 
                    idd = int(input("Enter ID to remove the book: "))
                    mycursor.execute("select*from available_books")
                    flag=0
                    for i in mycursor:
                        t_id,t_name,t_subject,t_quann=i
                        if t_id==idd:
                            flag=1
                    if flag==1:
                        mycursor.execute("delete from available_books where id="+str(idd)+"")
                        mydb.commit()
                        print("Data removed successfully..")
                    else:
                        print("Book not found")
                    
                elif ch==3:
                        print("all information is mandatory to be filled..")
                        idd=int(input("Enter Book ID:"))
                        s_name=input("Enter Student Name:")
                        s_class=input("Enter Student Class:")
                        mycursor.execute("select * from available_books where id='"+str(idd)+"'")
                        flag=0
                        for i in mycursor:
                            t_id,t_name,t_subject,t_quan=i
                            if t_id==idd and t_name==s_name and t_class==s_class:
                                flag=1 
                        if flag==1:
                            print("This book is already issued to this student..")
                        else:
                            mycursor.execute("select * from available_books where id='"+(str(idd))+"'")
                            flag=0
                            for i in mycursor:
                                flag = 1
                                t_id,t_name,t_subject,t_quan=i
                            if flag==1:
                                quan = t_quan-1
                                if quan<0:
                                    print("Book not available.")
                                else:
                                    mycursor.execute("")
                                print("Book not available")
                        new_func():
                            print("Invalid Input")
                            loop1=input("Do you want to log out?(y/n)")
                            

                                                                 
                        pass
                elif ch==4:
                    loop2='y'
                    while loop2=='y':
                        idd=int(input("Enter book id:"))
                        s_name=input("Enter student name:")
                        s_class=input("Enter student class")
                        mycursor.execute("select * from issued")
                        flag=0
                    for i in mycursor:
                        t_id,t_name,t_subject,t_s_name,t_s_class=i
                        if t_id==idd and t_s_name==sname and t_s_class==s_class:
                            flag=1
                    if flag==1:
                        mycursor.execute("select * from available_books where id='"+str(idd)+"'")
                        for i in mycursor:
                            t_id,t_name,t_subject,t_quan=i
                        quan=t_quan+1
                        mycursor.execute('delete from issued where id='"+str(idd)+"'and s_name='"+s_name"'and s_class='"+s_class"'')
                        mycursor.execute("update available_books set quantity='"+str(quan)+"'")
                        mydb.commit()
                        print("Successfuly issued")
                        loop2=input("Do you want to issue more books?(y/n)").lower()
                        
                    else:
                        print("Book not issued yet")

                    loop1="Do you want to logout?(y/n)".lower()
                         
                                
                            
                            
                elif ch==5:
                    mycursor.execute("select * from available_books")
                    print("ID|NAME|SUBJECT|QUANTITY")
                    
                    for i in mycursor:
                        a,b,c,d=i
                        print("{a},{b},{c},{d}")
                                     
                    
                elif ch==6:
                    mycursor.execute("select from issued")
                    print("ID|NAME|S_NAME|S_CLASS")
                    for i in mycursor:
                        a2,b2,c2,d2,e2=i
                        print("{a2}|{b2}|{c2}|{d2}|{e2}")
                elif ch==7:
                    break
            
            else:
                print("Wrong Password...")