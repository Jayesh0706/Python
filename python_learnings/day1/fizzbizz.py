'''
Write a program that prints numbers from 1 to 100, but:
For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz".
'''

end=int(input("Enter end of numbers:"))
tempfizzbizz=0
tempfizz=0
tempbizz=0
for i in range(1,end+1):
    if(i%3==0 and i%5==0):
        print("FizzBizz")
        tempfizzbizz+=1
    elif (i%3==0):
        print("Fizz")
        tempfizz+=1
    elif (i%5==0):
        print("Bizz")
        tempbizz+=1
    else:
        print(i)
print("Total fizzbizz is: ",tempfizzbizz)
print("Total fizz is: ",tempfizz)
print("Total bizz is: ",tempbizz)
