n=input("Enter your input:")
r=""
length=len(n)-1
for i in n:
    r+=n[length]
    length-=1

print("Reversed string is:",r)