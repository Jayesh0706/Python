#using 3rd variable
a=int(input("Enter number a:"))
b=int(input("Enter number b:"))
c=a
a=b
b=c


print(f"A is {a} and B is {b}")

#Without 3rd var
x=int(input("Enter number x:"))
y=int(input("Enter number y:"))

x,y=y,x

print(f"X is {x} and Y is {y}")


