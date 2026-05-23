s= input("Enter a string:")
# to find no. of vowels
a=s.count("a")
e=s.count("e")
i=s.count("i")
o=s.count("o")
u=s.count("u")
print ("The no. of vowels in the string are",(a+e+i+o+u))
print ("The no. of consonants in the string are",(26-(a+e+i+o+u)))
up= s.upper() 
print(up)#printing uppercase
low=s.lower()
print(low)#printing lowercase
