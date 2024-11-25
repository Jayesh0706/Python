'''
Electricity Bill Calculator
Write a program to calculate electricity bills based on usage in units:
First 100 units: $0.50 per unit
Next 100 units: $0.75 per unit
Next 100 units: $1.20 per unit
Above 300 units: $1.50 per unit 

'''

a=int(input("Enter your bill units:"))


if(a<=100):
    bill=a*0.5
elif(a>100 and a<=200):
    bill=(100*0.5)+(a-100)*0.75
elif(a>200 and a<=300):
    bill=(100*0.5)+(100*0.75)+(a-200)*1.20
else:
    bill=(100*0.5)+(100*0.75)+(100*1.20)+(a-300)*1.50

print(f"Your units are {a} and bill is {bill}")