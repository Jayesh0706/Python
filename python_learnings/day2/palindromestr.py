a=input("Enter word/string: ")
b=(a[::-1])
print(b)
if(a==b):
    print("Its a palindrome ,",True)
else:
    print("Its Not a palindrome ,",False)
