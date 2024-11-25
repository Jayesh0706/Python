'''Exercise 7: Print the following pattern
Write a Python program to print the reverse number pattern using a for loop.

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
'''

n=int(input("Enter number: "))
for i in range (1,n+1):
    for j in range (n-i+1,0,-1):
        print(j,end=" ")
    print("")



#by gpt
n = int(input("Enter number: "))
for i in range(n, 0, -1):  # Outer loop for the rows, starting from n down to 1
    for j in range(i, 0, -1):  # Inner loop for the decreasing numbers in each row
        print(j, end=" ")
    print("") 