'''Exercise 3: Create a new string made of the first, middle, and last characters of each input string

'''

s1=input("Enter str1:")
s2=input("Enter str2:")

l1=int(len(s1)-1)
l2=int(len(s2)-1)

m1=int(l1/2)
m2=int(l2/2)

print(s1[0]+s2[0]+s1[m1]+s2[m2]+s1[l1]+s2[l2])
