# l1=[1,2,3,4]
# print(l1)
# # list are ordered
# # seperated by commas
# # muttable i.e changable 

# print(l1[0])
# l1.append(5)
# print('list after appending 5 is ', l1)

# l2=[1,2,"hello",True]
# print(l2)
# # list can store all datatypes altogether

# # list comprehension
# lst=[i for i in range(4)]
# print(lst)
# lst2=[i*i for i in range(4)]
# print(lst2)


# list manipualtion


l1=[1,2,3,4]
l1.append(5)
print(l1)
# appending value 5 to l1

l1.insert(3,6)  
print(l1)
# adds value 6 at index 3
l1.sort()
print(l1)
# sorts the list in ascending order
l1.reverse()
print(l1)
# reverses the list
l1.pop()
print(l1)
# removes the last element of the list
l1.remove(6)
print(l1)
# removes the element 6 from the list
l1.clear()
print(l1)
# clears the list
l1=[1,2,3,4]
l2=l1.copy()
print(l2)
# copies the list l1 to l2
l3=l1
print(l3)
# copies the list l1 to l3
print(l1.count(2))
# counts the number of times 2 is present in the list
print(l1.index(2))
# returns the index of 2 in the list
l1.extend([5,6,7])  
print(l1)
# adds the list [5,6,7] to l1
l1.extend( [5,6,7])
print(l1)
# adds the tuple (8,9,10) to l1
print(l1.count(5))
# counts the number of times 5 is present in the list
print(l1)

print(l1.index(5))
# returns the index of 5 in the list
print(l1.index(5,5))
# returns the index of 5 after index 2 in the list
l1.append(5)
print(l1)
print(l1.index(5,5))
# returns the index of 5 after index 5 in the list
print(l3) 
print(l1)
print(l2)
l3=l3+l1+l2
print(l3) 