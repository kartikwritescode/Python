#program to find lcm using gcd
n1=int(input("Enter any no.:"))
n2=int(input("Enter second no.:"))
x=n1
y =n2
while (n2!=0):
    t=n2
    n2=n1%n2
    n1=t
gcd=n1
lcm=(x*y)/gcd
print("gcd=",gcd)
print("lcm=",lcm)
