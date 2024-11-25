passw=input("Enter your password:")
upper=0
lower=0
integer=0
length=0
for i in passw:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i==int:
        integer+=1
    elif(len(passw)>8):
        length+=1

if (upper>0 and lower>0 and integer>0 and length>0):
    print("Go ahead")
else:
    print("Change pass")


