l1=[1,4,9,16,25,36,49]
for i in l1:
    print(i)


tup=(1,4,9,16,25,36,49)
x=int(input("Elememnt to search: "))
idx=0
for i in tup:
    if(i==x):
        print("Element found at index -->",idx)
        break
    else:
        print("finding...")
    idx+=1