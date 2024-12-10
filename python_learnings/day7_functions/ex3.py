'''
Exercise 3: Return multiple values from a function
Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.'''

number1=int(input("Enter 1st number:"))
number2=int(input("Enter 2nd number:"))

def cal(n1,n2):
    print("Sum is:",n1+n2)
    print("Substraction is:",n1-n2)
cal(number1,number2)