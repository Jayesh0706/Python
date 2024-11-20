n=int(input("Enter last number:"))

count=0
for i in range(1,int(n/2+1)):
    if(n%i==0):
        count+=1
    else:
        continue
if(count>2):
    print("No Not is prime")
else:
    print("No is prime")


