import pickle
import sys
dict={}
#Function to write
def write_in_file():
    file=open ("k.bin", "ab") #a-append, b-binary 
    no=int(input("Enter number of students:"))
    for i in range (no) : 
        print ("Enter details of student ", i+1)
        dict["roll"]= input ("Enter roll number: ")
        dict["name"]=input ("enter the name: ") 
        dict["marks"]=int (input ("Enter the marks:"))
        pickle.dump (dict, file) #dump-to write in student file
    file.close()
    
    #Function to display 

def display():
#read from file and display
    file=open("k.bin", "rb") #r-read, b-binary
    try:
        while True:
            stud=pickle.load(file)
#write to the file
            print (stud)
    except EOFError:
        pass
    file.close()

#Function to display 
def search():
    file=open("k.bin", "rb") #r-read, b-binary 
    r=int(input("enter the rollno to search: ")) 
    found=0
    try:
        while True:
            data=pickle.load(file) #read from file
            if data["roll"]==r:
                print ("The rollno =",r," record found") 
                print (data)
                found=1
                break
    except EOFError:
        pass
    if found ==0:
        print ("The rollno =",r," record is not found")
    file.close()


while True:
    print ("MENU \n 1-Write in a file \n 2-display ") 
    print(" 3-search\n 4-exit \n") 
    ch=int(input ("Enter your choice = "))
    if ch==1: 
        write_in_file()
    if ch==2:
        display()
    if ch==3:
        search ()
    if ch==4:
        print("hmm")
        sys.exit()  
