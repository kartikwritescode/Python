# Library management system
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', passwd='1234')
mycursor = mydb.cursor()

print('''
__________________________________
Welcome to Library Management System
__________________________________
''')

# Creating database
mycursor.execute("CREATE DATABASE IF NOT EXISTS library_3") 
mycursor.execute("USE library_3") 
mycursor.execute("CREATE TABLE IF NOT EXISTS available_books(id INT PRIMARY KEY, name VARCHAR(25), subject VARCHAR(25), quantity INT)") 
mycursor.execute("CREATE TABLE IF NOT EXISTS issued(id INT, name VARCHAR(25), subject VARCHAR(25), s_name VARCHAR(25), s_class VARCHAR(25), PRIMARY KEY(id, s_name))") 
mycursor.execute("CREATE TABLE IF NOT EXISTS login(user VARCHAR(25) PRIMARY KEY, password VARCHAR(25))")

mydb.commit()

# Initialize flag
flag = 0 

# Check if login table is empty and insert default user if it is
mycursor.execute("SELECT * FROM login") 
for i in mycursor:
    flag = 1 

if flag == 0: 
    mycursor.execute("INSERT INTO login VALUES('user', 'sks')")
    mydb.commit()

##################Loops#############################

while True:
    print("""
1. Login
2. Exit
""")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        pas = input("Enter password:")
        mycursor.execute("SELECT * FROM login")
        for i in mycursor:
            t_user, t_pass = i
        if pas == t_pass:
            print("Login successfully...")
            loop1 = 'n' # Loop regarding leaving the program (yes/no)
            while loop1 == 'n':
                print("""
______________________________
1. Add New Books
2. Remove Any Book
3. Issue Book To Student
4. Return Book
5. View Available Books
6. View Issued Books
7. Logout
______________________________ 
""")
                ch = int(input("Enter your choice:"))
                
                if ch == 1:
                    loop2 = 'y' # Loop for adding books multiple times
                    while loop2 == 'y':
                        print("All information is mandatory to be filled!!")
                        idd = int(input("Enter book ID:"))
                        name = input("Enter book name:")
                        subject = input("Enter the Subject:")
                        quan = int(input("Enter Quantity:"))
                        mycursor.execute("INSERT INTO available_books VALUES(%s, %s, %s, %s)", (idd, name, subject, quan))
                        mydb.commit()
                        print("Data Inserted Successfully...")
                        loop2 = input("Do you wish to add another book? (y/n): ").lower()
                    loop1 = input("Do you want to logout? (y/n): ").lower()
                
                elif ch == 2: 
                    idd = int(input("Enter ID to remove the book: "))
                    mycursor.execute("SELECT * FROM available_books WHERE id = %s", (idd,))
                    flag = 0
                    for i in mycursor:
                        t_id, t_name, t_subject, t_quann = i
                        if t_id == idd:
                            flag = 1
                    if flag == 1:
                        mycursor.execute("DELETE FROM available_books WHERE id = %s", (idd,))
                        mydb.commit()
                        print("Data removed successfully..")
                    else:
                        print("Book not found")
                
                elif ch == 3:
                    print("All information is mandatory to be filled..")
                    idd = int(input("Enter Book ID:"))
                    s_name = input("Enter Student Name:")
                    s_class = input("Enter Student Class:")
                    
                    mycursor.execute("SELECT * FROM available_books WHERE id = %s", (idd,))
                    book_found = False
                    for i in mycursor:
                        book_found = True
                        t_id, t_name, t_subject, t_quan = i
                    if book_found:
                        mycursor.execute("SELECT * FROM issued WHERE id = %s AND s_name = %s", (idd, s_name))
                        issued_book = mycursor.fetchone()
                        if issued_book:
                            print("This book is already issued to this student..")
                        else:
                            if t_quan > 0:
                                new_quan = t_quan - 1
                                mycursor.execute("INSERT INTO issued VALUES(%s, %s, %s, %s, %s)", (idd, t_name, t_subject, s_name, s_class))
                                mycursor.execute("UPDATE available_books SET quantity = %s WHERE id = %s", (new_quan, idd))
                                mydb.commit()
                                print("Book issued successfully.")
                            else:
                                print("Book not available.")
                    else:
                        print("Invalid Book ID.")
                    loop1 = input("Do you want to logout? (y/n): ").lower()
                
                elif ch == 4:
                    loop2 = 'y'
                    while loop2 == 'y':
                        idd = int(input("Enter book id:"))
                        s_name = input("Enter student name:")
                        s_class = input("Enter student class:")
                        mycursor.execute("SELECT * FROM issued WHERE id = %s AND s_name = %s AND s_class = %s", (idd, s_name, s_class))
                        issued_book = mycursor.fetchone()
                        if issued_book:
                            mycursor.execute("SELECT * FROM available_books WHERE id = %s", (idd,))
                            for i in mycursor:
                                t_id, t_name, t_subject, t_quan = i
                            new_quan = t_quan + 1
                            mycursor.execute("DELETE FROM issued WHERE id = %s AND s_name = %s AND s_class = %s", (idd, s_name, s_class))
                            mycursor.execute("UPDATE available_books SET quantity = %s WHERE id = %s", (new_quan, idd))
                            mydb.commit()
                            print("Book returned successfully.")
                        else:
                            print("Book not issued to this student.")
                        loop2 = input("Do you want to return another book? (y/n): ").lower()
                    loop1 = input("Do you want to logout? (y/n): ").lower()
                
                elif ch == 5:
                    mycursor.execute("SELECT * FROM available_books")
                    print("ID | NAME | SUBJECT | QUANTITY")
                    for i in mycursor:
                        a, b, c, d = i
                        print(f"{a} | {b} | {c} | {d}")
                
                elif ch == 6:
                    mycursor.execute("SELECT * FROM issued")
                    print("ID | NAME | SUBJECT | S_NAME | S_CLASS")
                    for i in mycursor:
                        a2, b2, c2, d2, e2 = i
                        print(f"{a2} | {b2} | {c2} | {d2} | {e2}")
                
                elif ch == 7:
                    break
        
        else:
            print("Wrong Password...")
    
    elif ch == 2:
        print("Exiting the program...")
        break
