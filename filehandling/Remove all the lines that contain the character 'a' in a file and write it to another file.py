filel = open ("k.txt")
file2=  open("n.txt", "w")
for line in filel:
    if "a" in line:
        line=line.replace("a"," ")
    else:
        file2.write(line)
filel.close()
file2.close()
