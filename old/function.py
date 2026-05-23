def gmeancalc(a,b):
    gmean = (a*b)/(a+b)
    return gmean
a=9
b=8
print(gmeancalc(a,b))

def average(a,b):
    print("the avg is:", (a+b)/2)
average(2,3)
# default arguements
#def average (a=3,b=2:)
# if in function def statement values are given like a-9,b=2 so it is default arguement
#keyword = to changer order like average(b=2,a=3)
#req = jo dene hi dene hai
# variable length arguement 
def average2(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        # return sum
    print("average is ",sum/len(numbers))
average2(2,4,6,8,10) 