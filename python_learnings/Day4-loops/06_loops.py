'''Write a Python program to count the total number of digits in a number using a while loop.

For example, the number is 75869, so the output should be 5.'''

n=int(input("Enter number:"))
digcount=0
while n>=1:
    digcount+=1
    n=n//10
    
print(digcount)
