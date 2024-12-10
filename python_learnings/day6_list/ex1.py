#Exercise 1: Reverse each word of a string

str1=input("Enter your string:")
str2=str1.split(" ")

for i in str2:
    print("".join(i[::-1]),end=" ")
