n=int(input("Enter any no.:"))
sum=0
for i in range(1,n):
    if (n%i==0):
        sum+=i
if sum==n:
    print("The no. is perfect")
else:
    print("the no. is not perfect")
# check armstrong
tmp=n
sum=0
while tmp>0:
    d=tmp%10
    sum=sum+ (d**3)
    tmp=tmp//10
if n ==sum:
    print("no. is armstrong")
else:
    print("the no. is not armstrong")