list=[]
n=int(input("Amount of list:"))
for i in range(0,n):
    l=int(input("Value to be added:"))
    list.append(l)
print ("the minimum value is",min(list))
print ("the maximum value is",max(list))