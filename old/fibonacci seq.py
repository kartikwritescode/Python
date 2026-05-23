numterm = int(input("Enter the no. of results u wanna see:"))
count=0
n1 = 0
n2 = 1
# 0,1,1,2,3,5,8,13,21,34,55,89,144
while numterm>count:
    print(n1)
    an = n1+n2
    n1=n2
    n2=an
    count+=1
