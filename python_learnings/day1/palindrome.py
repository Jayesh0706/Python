a=int(input("Enter a number: "))
temp=a
rev=0
while temp > 0:
    rem=temp%10
    rev=(rev*10)+rem
    temp=temp//10

if(a==rev):
    print("Number is plaindrome")
else:
    print("Number is NOT plaindrome")
