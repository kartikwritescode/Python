word = str(input("Enter the word:"))
occurrences = {}
for i in word:
    if i in occurrences:
        occurrences[i] += 1
    else:
        occurrences[i] = 1

print(occurrences)  