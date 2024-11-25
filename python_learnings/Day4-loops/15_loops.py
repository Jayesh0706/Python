'''Exercise 11: Print all prime numbers within a range'''

start=int(input("Enter starting number:"))
End=int(input("Enter Ending number:"))

for i in range(start,End+1):
    if(i>2):
        count=0
        for n in range(2,int(i**0.5)+1):
            if(i%n==0):
                count+=1
                break

        if count==0:
            print(i,"is prime")
        

