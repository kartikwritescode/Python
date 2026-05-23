#program to find of a no. is pallindrome
n=int(input("Enter any no.:"))
tmp=n
rev=0
while(n>0):
      dig=n%10
      rev=rev*10+dig
      n=n//10
if tmp==rev:
      print("The no. is pallindrome")
else:
      print("the no. is not pallindrome")











