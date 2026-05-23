file = open("k.txt","r")
lines=file.readlines()
for line in lines:
    words=line.split()
    print("#".join(words), end='')


