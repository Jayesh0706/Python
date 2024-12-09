#WAF to print list length 

mylist=input("Enter your list seperated by ',' :").split(",")

print("Your list is :",mylist)

def listlen(mylist):
    
    print("Your list length is:",len(mylist))
    return len(mylist)


listlen(mylist)



def listToNormal(mylist):
    print("normal is"," ".join(mylist))
listToNormal(mylist)    

          #or
def listToNormal2(mylist):
    for i in mylist:
        print(i,end=" ")
listToNormal2(mylist)         


