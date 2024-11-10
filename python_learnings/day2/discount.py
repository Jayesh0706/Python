bill=int(input("Enter bill:"))
if(bill>=500):
    discount=0.2*bill
    discounted_bill=bill-discount
elif(bill<500 and bill>=100):
    discount=bill*0.1
    discounted_bill=bill-discount
else:
    discount=0
    discounted_bill=bill

print(f"You got discount of {discount} \nFinal bill is: {discounted_bill}")