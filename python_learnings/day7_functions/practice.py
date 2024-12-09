a=10
b=15
sum=a+b
print(sum)

a=16
b=35
sum=a+b
print(sum)


def summation(a, b):
    ans=a+b
    
    return ans


s=summation(122,23)
print(s)


def avg(a,b,c):
    return (a+b+c)/3


a=int(input("give 1st number: "))
b=int(input("give 2nd number: "))
c=int(input("give 3rd number: "))

s=avg(a,b,c)
print(s)

def mult(c,a=1,b=2):
    print(a*b*c)

mult(2)    
