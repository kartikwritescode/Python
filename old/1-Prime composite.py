# to check if a no. is prime or composite
n=int(input("Enter any no.:"))
count=0
i=1
while (i<=n):
    if (n%i==0):
        count+=1
    i+=1
if (count==2):
    print("the no. is prime")
else:
    print("The no. is composite")