'''Exercise 4: Arrange string characters such that lowercase letters should come first
'''

s1=input("Enter string:")
low=[]
up=[]
for i in s1:
    if(i.islower):
        low.append(i)
    else:
        up.append(i)

final=''.join(low+up)
print(final)