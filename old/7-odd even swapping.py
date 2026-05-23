mylist = []
print("Enter 5 elements for the list: ")
for i in range(5):
    value = int(input())
    mylist.append(value)

# printing original list
print("The original list : " + str(mylist))
# Separating odd and even index elements
odd_i = []
even_i = []
for i in range(0, len(mylist)):
    if i % 2:
        even_i.append(mylist[i])
    else :
        odd_i.append(mylist[i])

result = odd_i + even_i

# print result

print("Separated odd and even index list: " + str(result))