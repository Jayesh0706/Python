a=int(input("Enter side 1:"))
b=int(input("Enter side 2:"))
c=int(input("Enter side 3:"))

if(a==b==c):
    print("Eqilateral")
elif(a==b or a==c or b==c):
    print("isosceles")
else:
    print("All different")
