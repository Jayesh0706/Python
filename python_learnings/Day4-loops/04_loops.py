'''Exercise 4: Print multiplication table of a given number'''

n=int(input("Enter number for table:"))
for i in range (1,11):
    print(f"{n} x {i} = {n*i}")