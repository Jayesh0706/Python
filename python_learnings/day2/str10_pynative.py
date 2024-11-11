'''Remove integer from a string'''
str=input("Enter str:")

final=""
for i in str:
    if(i.isdigit()):
        continue
    else:
        final+=i
print(final)