"""to display all odd numbers bw a and b"""
l1=[]
def getNum(a,b):
    s=a+1
    for i in range(s,b):
        if(i%2==1):
            l1.append(i)
            i+=1
print(getNum(1,10))
