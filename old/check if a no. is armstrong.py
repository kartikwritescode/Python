#to check if a no. is armstrong no.
n=int(input("Enter any no.:"))
tmp=n
sum=0
while tmp>0:
    d=tmp%10
    sum=sum+ (d**3)
    tmp=tmp//10
if n ==sum:
    print("no. is armstrong")
else:
    print("the no. is not armstrong")
