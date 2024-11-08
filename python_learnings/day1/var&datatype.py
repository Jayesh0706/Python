name = "Jayesh"
age =23
price =10.23

print(name)
print(age)

print (f'my name is {name} and age is {age}')


print(type(name))


a=5
b=4
print(a+b)
a=a+10
print(a)



#logicalops
print(not True)

val=input("Enter your value: ")
print(type(val) , val)



#practice questions
#1)pgm to write 2 numbers and their sum

val1=int(input("Enter number 1: "))

val2=int(input("Enter number 2: "))

add=val1+val2
print("Addition is: ", add)


#2)pgm to print side of square and its area

val=int(input("Enter side of square:"))
print("Area of square is : ", val*val)


#3) Avg of 2 floatiing numbers
a=float(input("Enter 1st floating number: "))
b=float(input("Enter 2nd floating number: "))
print("Avg is ", (a+b)/2)


#4)enter 2 int and see if a > b
x=float(input("Enter 1st: "))
y=float(input("Enter 2nd: "))

if(x>y):
    print(True)
else:
    print(False)