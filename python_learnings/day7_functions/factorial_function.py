n=int(input("Enter a number:"))
def factorial(n):
    mult=1
    for i in range(1,n+1):
        mult=mult*i
    print("Factorial is",mult)

factorial(n)