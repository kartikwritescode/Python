x=[1,2,9,7,63,44]
M=sum(x)
print (M)
def sum(P):
    lst=[]
    result = 0
    for z in P:
        lst.append(result)
        result=result+z
    print(lst)
    return(result)