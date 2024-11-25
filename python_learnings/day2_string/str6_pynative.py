''' String characters balance Test
Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.'''



s1=input("Enter main str:")
s2=input("Enter check str:")

flag=True
for i in s2:
    if(i in s1):
        continue
    else:
        flag=False
print(flag)
