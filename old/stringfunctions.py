story = "once upon a time in mumbai, there was a king named IDK"

# how to get the total length of string (by len function)
print (len(story)) #len function
print (story.endswith("named"))
print (story.endswith("IDK"))    #endswith verifier that prints true/false
print (story.count("O"))  #words/letters counter in string
print (story.capitalize()) #to make the first letter of string capital
print (story.find("once")) #to find words in string shows -1 if not and 1 if yes then sows the index no. (place) only first occurence
print (story.replace("once" , "then")) #replaces specified txt (all occurences) #doesn't save changes
# to save changes 
story = story.replace("once", "then")
print (story)

