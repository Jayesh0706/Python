'''Find the last position of a given substring
Write a program to find the last position of a substring “Emma” in a given string.'''


str=input("Enter string:")
search=input("Enter search string:")

print("First found at:",str.rfind(search))

#str.find()=for first occurence
#str.rfind()=for last occurence

