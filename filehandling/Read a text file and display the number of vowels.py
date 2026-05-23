# Read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file.
def functio():
    file = open("k.txt","r")
    read=file.read()
    vowels=consonants=uppercase=lowercase=0
    
    for i in read:
        if (i=="a"or i=="e"or i=="i"or i=="o"or i=="u"or i=="A"or i=="E" or i=="I"or i=="O"or i=="U"):
            vowels+=1
        else:
            consonants+=1
        if i.isupper():
            uppercase+=1
        else:
            lowercase+=1
    print("Number of vowels are:", vowels)
    print("Number of consonants are:", consonants)
    print("Number of uppercase leeter are:", uppercase)
    print("Number of lowercase letters are:", lowercase)
functio()




