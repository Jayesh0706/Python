'''Exercise 3: Calculate sum of all numbers from 1 to a given number
'''

n=int(input("Enter number :"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("Addition of number is: ",sum)