a=int(input("Enter your marks:"))

if(a>=90):
    grade="A"
elif(a>=80):
    grade="B"
elif(a>=70):
    grade="C"
elif(a>=60):
    grade="D"
else:
    grade="F"

print("Your grade is: ",grade)