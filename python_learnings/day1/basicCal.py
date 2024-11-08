#Problem 5: Basic Calculator
num1=float(input("Enter 1st number: "))
op=input("enter operator: ")
num2=float(input("Enter 2nd number: "))

if op == '+':
    print("Sum is : ",num1+num2)
elif op == '-':
    print("Substraction is: ",num1-num2)
elif op == '*':
    print("Multiplication is: ",num1*num2)
elif op == '/':
    if num2==0:
        print("Can not divide number by 0!!")
    else:
        print("Dicision is: ",num1/num2)
else:
    print("Invalid input of oprator!!!")