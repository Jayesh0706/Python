'''
Exercise 6: Create a recursive function
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

A recursive function is a function that calls itself again and again.

Expected Output:

55'''

def recursive(n):
    if n==0:
        return 0
    else:
        return recursive(n-1)+n
    
print(recursive(10))