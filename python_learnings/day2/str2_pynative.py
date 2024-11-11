'''Exercise 2: Append new string in the middle of a given string
'''
str1=input("Enter str1:")
str2=input("Enter str2:")
l=int(len(str1))
m=int(l/2)

print(str1[:m]+str2+str1[m:])