# # # # # # # # # #print("Hello world")
# # # # # # # # # # Data Types
# # # # # # # # # a = 'hello'
# # # # # # # # # print(a)
# # # # # # # # # print(type(a))
# # # # # # # # # a = 12
# # # # # # # # # print(type(a))
# # # # # # # # # b=12.5
# # # # # # # # # print(type(b))
# # # # # # # # # b=True
# # # # # # # # # print(b)
# # # # # # # # # print(type(b))
# # # # # # # l1=[1,2,3,4]
# # # # # # # # print(len(l1))
# # # # # # # t1=(1,2,3,4)
# # # # # # # a=5
# # # # # # # print(l1.append(a))
# # # # # # # print(l1)

# # # # # # a= input("Enter your name:")
# # # # # # print('his name is',a)

# # # # # a=int(input('Enter your age '))
# # # # # print('your age is:',a)
# # # # nm="Harry"
# # # # print(nm[-4:-2])
# # # a='Kartik'
# # # b=a.upper()
# # # print(b)
# # # c=a.lower()
# # # print(c)
# # # print(a.rstrip())
# # # d=a.split(' ')
# # # print(d)
# # # # for i in range(0,len(d)):
# # # #     print(d[i],end='')
# # # print(a.center())
# # name='kartik'
# # age = 17
# # print(f"My name is {name} and i am {age}") #this is one way with f string
# # hehe="My name is {} and I am {}"
# # print (hehe.format(name,age))

# # docstrings and pep-8
# # docstrings are string literals that we write just after the function declaration or class declaration or anything to give a breif description


# def square(n):
#     '''takes in a no. n and returns squareof n'''
#     print(n**2)
# square(5)
# print(square.__doc__)
# #we can print docstring by this way 


# pep8(python enhancement proposal  ) is a document that provides guidelines and best practises on how to write a python code .
#it improves readability and consistency
#import this - is zen of python by tim peters - a poem - a kinda poem

# recursion
#calling a same function inside a function 

num = 5
def factorial(num):
    if (num==1) or (num==0):
        return 1
    else:
        return(num*(factorial(num-1)))
print(factorial(num))



def factorial1(num):
    n=1
    for i in range(1,num+1):
        n*=i
        return n
    print(n)
factorial1(num) 
        