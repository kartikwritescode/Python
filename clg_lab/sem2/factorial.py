def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = 5
print("Factorial of", num, "is", factorial(num))



# num = 6
# # m=1
# # for i in range (1,num):
# #     m=m + m*i
# #     print(m)
    

# def factorial(num):
#     if(num ==1 or num ==0):
#         return 1
#     else:
#         return num * factorial(num-1)
    
# print(factorial(6))

# for i in range (0,10):
#     print(factorial(i))