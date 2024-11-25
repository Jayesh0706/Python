a=input("Enter string: ")
b=a.split()
print(b)
long=""
for i in b:
    if len(i)>len(long):
        long=i
print(long)


    