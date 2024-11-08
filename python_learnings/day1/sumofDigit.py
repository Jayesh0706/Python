n=int(input("Enter a number: "))
temp=0
while(n>0):
    rem=n%10
    temp=temp+rem
    n=n//10

print("Addition is : ", temp)