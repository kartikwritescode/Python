#Library management system
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='kk',passwd='kartik007')
mycursor=mydb.cursor()
print('''
__________________________________
Welcome to Library Management System
__________________________________
''')
#creating database
mycursor.execute("create database if not exists library_3") #database tabhi banega agar exist na krta ho pehle se warna agar exist krta hoga toh mysql se error milega
mycursor.execute("use library_3") #database ko use krre hain
mycursor.execute("create table if not exists available_books(id int(11), name varchar(25),subject varchar(25),quantity int(11))") #table no
mycursor.execute("create table if not exists issued(id int,name varchar,subject varchar, s_name varchar,s_class varchar)") #primary screen ke sub parts yani second screens ke table hain yeh sab
mycursor.execute("create table if not exists login(user varchar,password varchr)")
mydb.commit() #jab bhi hum kuch progress krte hain toh usse save krne ke liye usse program me commit krna padta hai
#game saved
flag=0 #variable hai
mycursor.execute("select * from login") #sab kuch select krliya uss login wale table se (taki pta lage ki empty hai ki nahi) taki jab woh content submit kare toh ek hi baar kare
for i in mycursor: #agar yeh loop chalega hence we conclude that the table had sum value
    flag=1 #kuch value ayi yani value thi
if flag==0: #yanki koi value phle se nahi thi
    mycursor.execute("insert into login values('user','ng'")
    mydb.commit()
##################Loops#############################
    
while True:
    print("""
1.Login
2.Exit
""")
    ch=int(input("Enter your choice"))
    if ch==1:
        pas=input("Enter password:")
        mycursor.execute("select * from login")
        for i in mycursor: #(x,y) = var1(name),var2(pass)
            t_user,t_pass=i
        if pas==t_pass:
            print("Login successfully...")
        else:
            print("Wrong Password...")
            
        
            
















