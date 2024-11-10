# str1="JAYESH's"
# str2='hell"o'
# str3="""hello wor"l'd"""

# print(str1)
# print(str2)
# print(str3)

# str4="hello world ,\t this is jayesh"  #\t tab space,\n=next line
# print(str4)



# s1="jayesh"
# s2="Nalawade"
# print(s1+s2)
# print(len(s1))

# print(s1[1:5])   #start index included , ending not included
# print(s2[:3])
# print(s2[1:len(s2)])

# print(s1[-6:-1])

s1="I am jayesh learning python"
print(s1.endswith("on"))    #checks ending with particular str

s2="jayesh nalawade"
print("only using print and not saving: ",s2.capitalize())    #capitalize 1st char , doenot change original string
print("original s2: ",s2)   #still remains same
s2=s2.capitalize()
print("Saved s2: ",s2)
 

print(s2.replace("a","o"))  #str.replace("old","new")

print(s2.find("nal"))   #finds first index of searched world , if ans -1 not found

print(s2.count("a"))    #str.count("world"/"char") 



