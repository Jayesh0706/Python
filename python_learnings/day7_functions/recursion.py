# factorial by recursion '
n=int(input("ENter a number: "))
# def fact(n):
#     if n==0 or n==1:
#         return 1 
#     return fact(n-1)*n
# print(fact(n))


# recursive func to calculate sun od n num

def summ(n):
    if n==0:
        return 0
    return summ(n-1)+n
print(summ(n))


#to print all elements in list
mylist=["jayesh","1",2,3.4,True]

def printlist(mylist,idx=0):
    
    if idx == len(mylist):
        return
    print(mylist[idx])
    printlist(mylist,idx+1)
printlist(mylist)