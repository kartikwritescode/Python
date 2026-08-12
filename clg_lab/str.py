text = input("Enter a string: ")

freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print("\nCharacter Frequency:")
for k, v in freq.items():
    print(k, ":", v)

d = {}

while True:
    print("\nDictionary Operations")
    print("1. Add/Update")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Keys")
    print("6. Values")
    print("7. Items")
    print("8. Length")
    print("9. Clear")
    print("10. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        key = input("Key: ")
        value = input("Value: ")
        d[key] = value
    elif ch == 2:
        key = input("Key to delete: ")
        if key in d:
            del d[key]
        else:
            print("Key not found")
    elif ch == 3:
        key = input("Key to search: ")
        if key in d:
            print("Value:", d[key])
        else:
            print("Key not found")
    elif ch == 4:
        print(d)
    elif ch == 5:
        print(list(d.keys()))
    elif ch == 6:
        print(list(d.values()))
    elif ch == 7:
        print(list(d.items()))
    elif ch == 8:
        print("Length:", len(d))
    elif ch == 9:
        d.clear()
        print("Dictionary cleared")
    elif ch == 10:
        break
    else:
        print("Invalid choice")

n = int(input("\nEnter number of elements in list: "))
lst = []

for i in range(n):
    lst.append(int(input()))

lst.sort()

print("Sorted List:")
print(lst)