n=int(input("Enter a numer:"))
count=0
for i in range(1,n+1):
    if (n%i==0):
        count+=1

if(count==2):
    print("No is prime")
else:
    print("No is not prime")