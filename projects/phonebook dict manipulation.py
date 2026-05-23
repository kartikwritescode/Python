#dictionary manipulation
dict={}
while True:
    print("""
_________________
1. Add number
2. View phonebook
3. Remove number 
4. Exit 
_______________-""")
    ch=int(input("Enter your choice:"))
    if ch==1:
        print("ADD NUMBER:")
        service_provider=input("Enter Service provider:")
        number=int(input("Enter number:"))
        dict[service_provider]=number
    elif ch ==2:
        print("Phonebook:")
        for service_provider, number in dict.items():
            print(service_provider, ':', number)
    elif ch ==3:
        rnum=int(input("Enter number you want to remove from the phonebook:"))
        if rnum in dict.items:
            del dict[rnum]
        
    elif ch==4 :
        break 

        