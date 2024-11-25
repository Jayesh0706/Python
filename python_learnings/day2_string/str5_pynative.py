'''Exercise 5: Count all letters, digits, and special symbols from a given string
'''

str=input("Enter string: ")
alph=0
num=0
sym=0
lstalph=[]
lstnum=[]
lstsym=[]
for i in str:
    if(i.isalpha()):
        alph+=1
        lstalph.append(i)
    elif(i.isdigit()):
        num+=1
        lstnum.append(i)
    else:
        sym+=1
        lstsym.append(i)
print("numbers are:",','.join(lstnum))
print("alphabets are:",','.join(lstalph))
print("symbols are:",','.join(lstsym))

print("total numbers are: ",num)
print("total alphabets are: ",alph)
print("total symbols are: ",sym)




