'''
Exercise 1A: Create a string made of the first, middle and last characte

'''

str=input("Enter string=")

l=int(len(str))
print(type(l))
print(l)
mid=int(l/2)
print(mid)


s=str[0]
m=str[mid]
last=str[l-1]
print(s+m+last)