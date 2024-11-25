str1=input("Enter string:")
add=0
count=0
for i in str1:
    if(i.isdigit()):
        count+=1
        add+=int(i)
avg=add/count

print(f"Sum is: {add} & avg is {avg}")