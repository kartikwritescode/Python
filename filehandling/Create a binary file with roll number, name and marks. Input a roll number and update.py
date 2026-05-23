import pickle 
student_data={}
#writing to the file- logic
no_of_students=int(input("Enter no of students ")) 
file=open("D:\\stud_u.dat", "ab")
for i in range (no_of_students):
    student_data["RollNo"]=int(input ("Enter roll no ")) 
    student_data["Name"]=input("Enter student Name: ") 
    student_data["Marks"]=float (input ("Enter student marks: ")) 
    pickle.dump (student_data, file) 
    student_data={}
file.close()
#reading the file- logic
file=open("D:\\stud_u.dat","rb")
try:
    while True:
        student_data=pickle.load(file) 
        print (student_data)
except EOFError:
    file.close()
#searching and updating (i.e. reading and then writing) logic
found=False
roll_no=int(input ("Enter the roll no to search: ")) 
file=open("D:\\stud_u.dat", "rb+")
try:
    while True:
        pos=file.tell()
        student_data=pickle.load(file)
        if (student_data[ "RollNo"]==roll_no):
#print (student_data["Name"])   
            student_data["Marks"]=float (input("Enter marks to be updated"))
            file.seek (pos)
            pickle.dump (student_data, file)
            found=True
except EOFError:
    if found==False:
        print("Roll no not found please try again")
    else:
        print("Student marks updated successfully. ")
    file.close()

#Displaying logic
file=open("D:\\stud_u.dat","rb")
try:
    while True:
        student_data=pickle.load(file) 
        print(student_data)
except EOFError:
    file.close()